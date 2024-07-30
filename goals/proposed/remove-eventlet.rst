==============================
Remove Eventlet from OpenStack
==============================

Giving to all the OpenStack teams, themselves responsible of a collection
of deliverables who constitutes the OpenStack components, a solution
to securely remove their dependence to Eventlet, usable by everyone,
regardless of their resources, while by ensuring the enjoyment of
decision-making autonomy for each team. Combine the parts of this proposal
in such a way that the general will takes precedence over the individual
will, allows the sovereignty of teams over their environment to exist in
their full extent, and equality of chance between teams, and the exercise
of freedom individual, this is the problem we had to solve.

Problem
=======

OpenStack is built on the top of asynchronous mechanisms.

All the OpenStack components heavily rely on the Eventlet library to
obtain asynchronous features and greenlet coroutines, however, the OpenStack
community currently suffer from many aspects of the usage of that library.

Indeed this library currently does not support Python 3.12 and face many
issues with Python 3.11 (those are described below).

This new python version will be part of the supported runtime in the coming
OpenStack series. At least Python 3.12 should be a supported runtime of the
"Dalmatian" series. 2024.1/Caracal currently `support Python 3.11 <https://governance.openstack.org/tc/reference/runtimes/2024.1.html>`_.

Many distros already started to transition to Python 3.12. That's the
case for Debian, Fedora `includes all Python versions <https://developer.fedoraproject.org/tech/languages/python/multiple-pythons.html>`_
which are `supported upstream <https://devguide.python.org/versions/#versions>`_,
and Ubuntu 24.04 `also introduced support to this version <https://launchpad.net/ubuntu/noble/+package/python3-all>`_.

It is urgent to solve this compatibility problem and it could be the right
moment to move to a more sustainable solution in replacement of Eventlet.
Without rapid actions the community will soon face more pressure.

Here is a purged list of the main pain points in Eventlet that led to this
situation:

#. **The lack of maintenance:** the lib is not actively maintained. No reviews
   were made during several months. Only one person could be still considered
   as an active core member. The consequences of this inactivity are legion.
   Tests don't pass, locally or in CI. CI doesn't run at all for Python 3.11.
   The github pull requests and issues backlogs of Eventlet are growing
   indefinitely. Legit bugs are not fixed. Python 3.12 is not supported in
   runtime.

#. **The technological dead-end:** The premise of Eventlet is drop-in
   compatibility via monkey patching. Unfortunately that quite possibly hasn't
   been true for a long time, and it's becoming increasingly more difficult
   over time and over new Python version.

   *Example #1: Compliance suite*

   Per `the docs <https://github.com/eventlet/eventlet/blob/master/doc/testing.rst#standard-li>`_,
   "Eventlet provides the ability to test itself with the
   standard Python networking tests. This verifies that the libraries it wraps
   work at least as well as the standard ones do."

   That is, Eventlet will run the Python standard library's test suite against
   Eventlet to make sure it's compatible.

   Unfortunately, this testing mechanism was never updated for Python 3.

   As such, it's basically designed for Python 2.7, and there has been 13
   major releases of Python since then. Is Eventlet still compatible with the
   standard library? It's hard to say, but quite likely not.

   *Example #2: RLock*

   When Eventlet was originally written, ``threading.RLock`` was written in
   Python. This has a bug, e.g. it didn't actually work in the face of
   signals: https://bugs.python.org/issue13697 (there's a bunch of comments in
   the ticket from people encountering this in the real world, logging being a
   common situation.)

   The problem doesn't occur in the version of RLock which is written in C,
   which is the current default and was introduced in Python 3.2.

   However, the C version of RLock doesn't work with Eventlet, so Eventlet has
   been monkey patching ``threading.RLock``, replacing it with the (buggy and
   unfixable) version written in Python (``threading._PyRLock_``).

   In 3.11 this gets worse, as the RLock version written in Python has become
   subtly incompatible with eventlet's expectations. To get the Eventlet test
   suite passing on 3.11 maintainers had to copy/paste the Python RLock code
   and `tweak
   it <https://github.com/eventlet/eventlet/pull/823/files#diff-029df1ae9b7431e9cdd>`_.

   So now Eventlet has to use a forked version of a broken implementation of
   RLock. It's possible there's another solution, but Eventlet basically
   relies on monkey patching a whole bunch of functions and on implementation
   details of Python standard library using those functions in particular ways,
   which are not always stable over time.

   This problem will continue to get worse as Python evolves. E.g. it would
   not surprise if the GIL removal makes things even more difficult for
   Eventlet.

Root Cause
==========

One could think that the root cause of the OpenStack issue described above
lives in the recent lack of maintenance of the Eventlet library, yet this is
not the case. Even if Eventlet simplified the life of the community developers
for years, one can't ignore the fact that by its inherent philosophy and
nature it has only widened the gap between the OpenStack code base and the
CPython stdlib implementation.

Now, because of the usage of Eventlet, 13 major releases of CPython implicitly
separate OpenStack and CPython.

Thinking that the recent lack of maintenance in Eventlet explain our current
issue and hoping that simply fixing two or three things will unlock our
problem is just hypothetical. When the `GIL removal (for now just optional) <https://peps.python.org/pep-0703/>`_
will become a reality we will surely live in a nightmare.

Indeed, considering that Eventlet is fully based on volunteers, and
considering the current available resources of this project - 3 people -, it
would be feasible to fix urgent things, but considering the gap between
Eventlet and the recent CPython releases, it would be really hard to catch up
and it would surely require several development years.

So, for these reasons, thinking that way will sooner lead us toward deeper
moats which are impossible to cross. Thinking that way already led us to stick
to EOLed design of CPython.

One could think that the Eventlet case is an isolated case. Unfortunately not.
`Resources are scarce <https://www.sonatype.com/hubfs/9th-Annual-SSSC-Report.pdf>`_.
The same observation is true have the vast majority of other third parties
libraries. Almost all these libraries rest on the shoulders of one or two
people. It's the harsh law of the open source ecosystem. **Scarcity lead the
world**. Only mainstream projects like CPython or OpenStack has decent
resources. **Winners take all**.

The root cause of the problems described here is due to the fact of using
a library without resources. A library that did not have the means to adapt
to its environment. A library designed to solve Python design issues from
another time. A time when python was not provided with an internal
asynchronous backend.

All the problems described above inherit from choices made in Eventlet,
several years ago, to improve older versions of Python, 2.7 at least. All the
current issues are related to Eventlet design implementations made for Python
EOL versions. Design choices and implementation made at a time where the
Python stdlib was not designed to support async. That mean that OpenStack is
now really far from the concurrency approach chosen by our main runtime,
Python. An approach that is the future of the main technology on which rest
all OpenStack, Python.

Even if Python 2.7 is now EOL and even if its support have been dropped from
OpenStack years ago, today we are still impacted by previous design choices
made for it.

One major argument initially brandished to defend usage of Eventlet inside
OpenStack was one of those was to avoid explicit concurrency in our code base.
Monkey patching. We use Eventlet as an optional, pluggable, backend that
allows swapping out blocking APIs for an event loop, transparently, without
changing any code. However, with time, this affirmation has become false. Now,
`numerous are the examples <https://codesearch.openstack.org/?q=is_monkey_patched&i=nope&literal=nope&files=&excludeFiles=&repos=>`_
where OpenStack source code now has a whole bunch of patches necessary for
Eventlet to work properly.  `Locks are heavily used in sync designed OpenStack
code <https://codesearch.openstack.org/?q=self.lock%3A&i=nope&literal=nope&files=&excludeFiles=&repos=>`_
, where, apparently, no explicit concurrency is expected. Eventlet has
infected synchronous code. Even our initial arguments have evaporated with
time.

Is all this Eventlet problem are solvable? Is the gap recoverable?
Yes, but at a significant cost.

Investing money, time, and engineering skills in a solution that will continue
to diverge from the main runtime pillar of OpenStack, Python, isn't something
conceivable.

Investing energy in a solution that is made to improve dead version of Python
is not something rational.

Investing OpenStack's precious - decreasing - resources in a migration toward
one an other library likes Eventlet, without it having good and long term
maintenance capabilities is not something desirable neither. We would face the
same situation again, sooner than we think.

The current situation, trigger a signal to the community. The community should
catch this event to decide actions to lead OpenStack toward a solution.
A realistic solution. A pragmatic solution. A deterministic solution.

We should design a solution, that once is applied, must ensure that the
current inputs always provides the same outputs. No regressions.

Sustainability should be the main priority of the OpenStack community.
Our sustainability should be based on the future of Python, not on its past.

Eventlet is not a sustainable solution for a project like OpenStack. Eventlet
struggles to remain compatible with CPython. Using Eventlet introduce
a gap between us and the CPython stdlib. We should adopt a solution that
remove that gap.

But... Our challenge is to find a solution which leaves no one behind.
Our challenge is to find a solution that every OpenStack team can adopt.
Our challenge is to find a solution that respect freedom of choice of every
OpenStack team.
Our challenge is to find a solution which take account of the evolution
of the Python ecosystem.

.. _on-eventlet:

On Eventlet
===========

The purpose of Eventlet is to manage asynchronism. To achieve that goal
Eventlet relies on concepts, `monkey patching
<https://eventlet.readthedocs.io/en/latest/patching.html#greening-the-world>`_,
and `greenthread <https://eventlet.readthedocs.io/en/latest/modules/greenthread.html>`.

Eventlet is based on `greenlet <https://greenlet.readthedocs.io/en/latest/>`.

Eventlet is designed around `3 essential design patterns
<https://eventlet.readthedocs.io/en/latest/design_patterns.html>`_:

* *the client pattern*: allow clients to communicate with third parties in
  an asynchronous way. By example a web crawler. A list of urls are crawled
  asynchronously to retrieve their bodies for later processing.
* *the server pattern*: non-blocking server who wait for requests on a socket.
  By example an HTTP server.
* *the dispatch pattern*: this pattern represent a server which is also
  a client of some other services. By example a proxy, an aggregator, a job
  worker.

These 3 Eventlet design patterns allow non-blocking and rely on
greenthreads to implement them.

There are two main use cases for Eventlet:

#. As a required networking framework, much like one would use AsyncIO, trio,
   or older frameworks like Twisted and tornado;
#. As an optional, pluggable backend that allows swapping out blocking APIs
   for an event loop, transparently, without changing any code. This is how
   Celery and Gunicorn use eventlet.

Greenthreads, are inherited from the greenlet library. They are lightweight
coroutines for in-process sequential concurrent programming. Greenlets can
be used on their own but they are also a fundamental piece of the voodoo
behind the monkey patching mechanisms from Eventlet. They are designed to be
cooperative and sequential. This means that when one greenlet is running, no
other greenlet can be running.

OpenStack use greenthreads pools and greenlet as executor. Those can be used
among other examples, to launch cooperative threads, to run workers, and to
launch periodic tasks. A concrete example of greenlet usage in OpenStack is
the thread launched to manage the RADOS Block Device (RDB) calls. Those calls
are executed in Eventlet tpool while the current coroutine/greenthread is
blocking until the method completes.

Disclaimers
===========

On the Perspective of the Proposed Solution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**The solution proposed below focus exclusively on OpenStack components that
currently rely on Eventlet. OpenStack components which are not relying on
Eventlet can safely ignore this proposal. The proposed solution is a by
default solution. Like with all governance goals, OpenStack teams are free to
design their own solution.**

We should notice that many teams do not have time and resources to follow
their own path. For many of these teams, the threading model they have
inherited through the usage of Eventlet is blackbox. These teams are afraid to
touch this model.

This proposal aim to provide a default solution that can be adopted by any
teams who wants it.

Our goal is to get rid of Eventlet, and without default solution these teams
will remains dependent of Eventlet, and, hence, Eventlet will continue to
threaten the coming OpenStack releases.

`OpenStack leaders are expected to put the needs of OpenStack first in their
decision making, before the needs of any individual project team
<https://governance.openstack.org/tc/reference/principles.html#openstack-first-project-team-second-company-third>`_.
For this reason, readers should appreciate this proposal with a global
perspective and not only with a team based perspective.

.. _on-the-standards-of-the-industry:

On the Standards of the Industry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The raise of parallelism and of concurrency are trends which are carried by
the constant evolution of our industry. Hardware is now naturally
parallel. Decades of works in computer architecture have focused on
maintaining the illusion of serial execution.

Python wasn’t written with parallelism in mind. Many Python developers,
since decades, lives in a sequential world. Indeed, *Parallelism* is when
tasks literally run at the same time, e.g., on a multi-core processor.
On the paper `Threads are made for parallelism
<https://docs.python.org/3/library/threading.html#module-threading>`_,
not for concurrency, but, in CPython, the GIL affect threading.
`One thread runs Python, while N others sleep or await I/O <https://wiki.python.org/moin/GlobalInterpreterLock>`_.
When do threads switch? Whenever a thread begins sleeping or awaiting network
I/O, there is a chance for another thread to take the GIL and execute Python
code, not really such a parallelism. The GIL prohibits parallelism with
threads. Only multiple processes (forks) would allow real parallelism with
CPython.

During almost 20 years, CPython suffered from the absence of concurrency.
*Concurrency* is when two or more tasks can start, run, and complete in
overlapping time periods. It doesn't necessarily mean they'll ever both be
running at the same instant.

Today, in 2024, the CPython stdlib, includes the concurrency concept.
The CPython community, through the addition of AsyncIO, introduced coroutines
and async features. AsyncIO is not affected by the GIL, but it cannot
benefit from multiple CPU either. In AsyncIO each task decide to when get back
control to the main event loop. AsyncIO coroutines avoid context switching.
AsyncIO save system resources.

The absence of these 2 concepts, *parallelism* and *concurrency* certainly
played on important role in the creation of Eventlet and in its adoption
by the CPython community, OpenStack included.

The fact is now the Python community wanted these 2 concepts, parallelism
and concurrency. The utility of a creation cannot be decreed, it
is discovered. The original utility of Python can't fight.

We recently discovered native concurrency with the addition of AsyncIO in the
stdlib. We are now in the face of discovering multiprocessing. It is
inevitable.

Starting from `Python 3.13 <https://docs.python.org/3.13/whatsnew/3.13.html>`_
the `PEP 703 <https://peps.python.org/pep-0703/>`_ will become a reality and
disabling the GIL will be permitted, therefore, giving access to
parallelism in the Python ecosystem, and introducing all the consequence that
such a paradigm shift bring with him.

Indeed, the option-ability of the GIL raise a concern that we cannot
ignore.

Many third party libraries in use in OpenStack are binding of *C*
libraries, or rely on *C* libraries. Greenlet is the perfect example of
that. The GIL option-ability will allow these binding to don't shy away
from using parallelism. That was not possible before, but the door ajar.

We cannot really predict which are the libraries that we use which
will follow that transition, and we can't guarantee that they will remains
backward compatible with the sequential paradigm.

We can't ignore that point, else the following scenarios await us:

* we could simply loose the capacity of using those libraries;
* we won't be able to properly control their uses;
* we may have to stick to older and outdated versions of these libraries
  and so which could represent a significant security problem for us.

Abruptly using parallelism in OpenStack may lead to unexpected problems.
Depending on the evolution of our ecosystem, keeping the GIL enabled could
block us in an unsupported world. Again, the utility of a creation cannot be
decreed, it is discovered.

We should not ignore that emerging trends and, if possible, think in ways to
adapt to the evolution of the industry.

We are at a crossroads.  Option-ability of the GIL will shift our world.
Parallelism is at some kind a new paradigm for our ecosystem.

Solution
========

**Here are the facts: Stop using Eventlet is not an option it is an
obligation. Eventlet can't be removed abruptly. We need a way to keep our
affairs running. We need alternatives to replace Eventlet. We need a plan to
implement these alternatives.**

This proposal aim to make Eventlet work again on the short run.
Then incrementally abandon Eventlet in favor of alternatives to keep OpenStack
healthy on the long run.

The solution described here propose to smoothly migrate from a broken
Eventlet that threaten new OpenStack releases, to an healthy OpenStack free
from Eventlet. All of that would be possible by keeping Eventlet healthy in
the short run.

The solution proposed here is composed of the following elements:

#. an identification of the possible alternatives to replace the common
   `Eventlet patterns <https://eventlet.readthedocs.io/en/latest/design_patterns.html>`_.
   In other words, which modules are at our disposal to replace Eventlet;
   One alternative can't fit all the Eventlet usages. By example, for many
   deliverables replacing Eventlet by AsyncIO would almost mean a complete
   rewriting of these deliverables.

   **Identifying a couple of alternatives would give us more freedom and will
   simplify the removal of Eventlet**.

#. a guide to help to select the alternatives that fits the identified
   Eventlet pattern. Teams can rely on this guide during the migration of
   their deliverables. Many alternatives may fits one identified pattern.

   This guide is based on a hierarchy of specifications which aim to produce
   one to one replacement solutions. For one Eventlet use case this guide may
   produce several alternatives and patterns that can be chosen by
   developers according to their needs and to the complexity that they are
   ready to accept;

#. a schedule of steps required during the migration of a single
   deliverable. OpenStack's Python deliverables can be seen of two types,
   common libraries, or services.

   This solution propose a specific schedule for both types of deliverables.
   Teams know their deliverables types, hence, they will be autonomous
   on the execution of these schedules.

#. a global schedule of the whole steps required to remove Eventlet from
   OpenStack. This global schedule is composed of 3 global milestones, short,
   medium, and long term. Each milestone is ordered in terms of priority
   and of dependency. This section aim to define how to move from A to Z;

Removing our dependency to Eventlet is a real challenge, and, we can't
take such challenge without strategy and tactics. Each items which compose
this solution is a tactics and the whole is the strategy.

The global duration of this goal could be at least five to six years and
would requires several series to be fully applied.

Removing Eventlet is not an option. That's a vital need.
Lets see how to do that removal.

The Available Alternatives to Eventlet
======================================

We need alternatives to replace Eventlet. One Alternative one choice, many
alternatives many choices. Variety is the key of decision-making autonomy.

This section propose to define a couple of identified alternatives. Defining
is limiting. Without limits no assistance is possible. Without limits lots of
misunderstanding lies in wait for us.

The first objective of this community goal is to help and to assist. If
teams have no assistance, Eventlet, as a blackbox, will remains here. If
teams decide to follow an other path, unfortunately, we won't be able to
assist them.

The second objective of this community goal is to avoid misunderstanding.
Misunderstanding lead to blackboxes. Bots are roots of traps. We want to
prevent us from taking the wrong path.

The list of the selected alternatives proposed below is not fully exhaustive.
Some other options may be added during our discussions, provided that we are
able to provide a minimal understanding and expertise.

How using the following alternatives is defined into the guide proposed
later in this document. These selected alternatives and their definition will
be stored in guide. :ref:`migration-guide`.

Greenlet
~~~~~~~~

Is it still necessary to present `Greenlet <https://greenlet.readthedocs.io/en/latest/>`_?

Greenlets are lightweight coroutines for in-process sequential concurrent
programming.

Even if eventlet is ill, Greenlet is healthy. Eventlet depends on Greenlet.
Greenlet is totally independent from Eventlet.

In several case we could use greenlets and its coroutines. Greenlet can be
used to run workers or specific tasks who needs to be detached from the main
thread.

Unlike with Eventlet the code ran into these coroutines would become blocking.

Greenlet are frequently defined by analogy to threads. For many purposes, you
can usually think of greenlets as cooperatively scheduled threads. The major
differences are that since these greenlets are cooperatively scheduled, you
are in control of when they execute, and since they are coroutines, many
greenlets can exist in a single native thread.

Threads (in theory) are preemptive and parallel [1], meaning that multiple
threads can be processing work at the same time, and it’s impossible to say
in what order different threads will proceed or see the effects of other
threads.

AsyncIO
~~~~~~~

As with Greenlet, we don't think it is necessary to present `AsyncIO
<https://docs.python.org/3/library/asyncio.html>`_.

AsyncIO is Python’s built-in coroutines. AsyncIO is designed around concepts
like generators and async def functions. AsyncIO is a module made to write
concurrent code.

Unlike Eventlet, AsyncIO bring explicit asynchronous features. But explicit is
explicitly explicit... AsyncIO is by nature invasive. This invasive nature
have a cost. This nature increase the cost of the adoption of AsyncIO on a
code base like the OpenStack one. We can't neglect that point.

Most of our parallel things made in OpenStack are network calls. Network
calls who are blocking IO.

AsyncIO is not affected by the GIL, but it cannot benefit from multiple CPU
either. In AsyncIO each task decide to when get back control to the main event
loop. AsyncIO coroutines avoid context switching. AsyncIO save system
resources.

In short, AsyncIO offers:

* a safer alternative to preemptive multitasking.
* a simple way to support many thousand of simultaneous socket connections.

Awaitlet
~~~~~~~~

`Awaitlet <https://github.com/sqlalchemy/awaitlet>`_ allows existing programs
written to use threads and blocking APIs to be ported to AsyncIO, by replacing
front-end and backend code with AsyncIO compatible approaches, but allowing
intermediary code to remain completely unchanged. Its primary use is to
support code that is cross-compatible with AsyncIO and non-AsyncIO runtime
environments.

Internally Awaitlet rely on AsyncIO and Greenlet in the same time. Awaitlet
bringing together the best of both worlds.

Awaitlet is a concepts that found its roots in SQLAlchemy. Awaitlet is
a standalone implementation of this concept. An extract. The Awaitlet
initiative is born from the comments made by Mike Bayer earlier in this
proposal, and is born from the different discussions who followed these
comments.

Awaitlet allow using AsyncIO and its derived libraries (aiohttp, etc...)
without requiring a complete rewrite of all our applications.

Awaitlet is a good deal between modern concurrency, and simplicity of
implementation.

Aiohttp
~~~~~~~

`Aiohttp <https://github.com/aio-libs/aiohttp>`_ is Asynchronous HTTP
Client/Server library for AsyncIO and Python.

We think that Aiohttp is a credible alternative to many use cases
provided by Eventlet's patterns.

Using aiohttp de facto lead us to use AsyncIO. Rewriting a server module
with aiohttp may require a significant amounts of works. Fortunately for us
Aiohttp can now be used through the mechanisms offered by Awaitlet.

Eventlet's AsyncIO Hub
~~~~~~~~~~~~~~~~~~~~~~

Eventlet's `AsyncIO Hub
<https://eventlet.readthedocs.io/en/latest/asyncio/compatibility.html#asyncio-compatibility>`_
is a compatibility layer between AsyncIO and
Eventlet. This hub has been recently introduced. Like Awaitlet, the creation
of this hub find its roots in the discussions related this community goal
proposal.

This hub is not strictly speaking an alternative to Eventlet. This hub is
Eventlet. But this hub is a like a proxy which allow using the other
Alternatives presented here.

This hub would allow us to use AsyncIO, Aiohttp, Awaitlet etc in the same
time that Eventlet. This hub is a the key of a smooth migration.

Threading
~~~~~~~~~

To finish, threading and native threads could be used to run tasks in a
parallel fashion.

As Eventlet rely on green threads and greenlet, in many aspects, it would be
surely easier to migrate our Eventlet existing code to native threads.
On the other hand, using Awaitlet could provide a credible alternative to
threads, depending on the context.

Before using threads, the reader should consider some aspects of using
threads.

*Threading* - as a programming model - is best suited to certain
kinds of computational tasks that are best executed with multiple CPUs and
shared memory for efficient communication between the threads. In such tasks,
the use of multicore processing with shared memory is a necessary evil because
the problem domain require it. Network programming is not one of those
domains. The key insight is that network programming involves a great deal of
*"waiting for things to happen"* and because of this, we don't need the
operating system to efficiently distribute our tasks over multiple CPUs.
Furthermore, we don't need the risks that preemptive multitasking brings, such
as race conditions when working with shared memory.

Threads consume a lot of preallocated virtual memory per thread (8Mb stack
space per thread). Threads requires context switching even when threads are
waiting from an IO. At very high concurrency levels, there can also be an
impact on throughput due to `context switching costs
<https://blog.tsunanet.net/2010/11/how-long-does-it-take-to-make-context.html>`_.

Threads are resources intensive and not particularly designed for non blocking
IO.

In Python, threads are impacted by the GIL in many aspects. We won't repeat
the problem with *parallelism* in Python in this section, rather we invite the
reader to go to :ref:`on-the-standards-of-the-industry`.

Other alternatives
~~~~~~~~~~~~~~~~~~

Depending on specific needs, other alternatives could find their place here,
like Futurist or Cotyledon. But as they are really related to specific aspects
not related to the Eventlet patterns we won't list them here, but we will
speak about them later in this document. Especially because oslo.service is
impacted by the removal of Eventlet. But Cotyledon and Futurist are more
related to features of oslo.service rather than to Eventlet itself.

.. _migration-guide:

Migration Guide
===============

The migration guide rests on 3 pillars:

#. The guide would define the official alternatives where we would be
   able to provide assistance. ;

#. The guide must provide a glossary to ensure that everyone has the same
   understanding of the used terms;

#. the guide aims to provide a table of correspondences that developers
   can use to migrate their code and hence remove their Eventlet usages.

**This section simply aim to offer an overview of what this guide could look
like**.

The guide proposal made in this document doesn't aim to give all the possible
details that can find their place in this guide. This proposal simply opens
this referential. The details of the different section of this guide should
be defined in a parallel spec/blueprint/review.

As new usages of Eventlet are discouraged, and as migrating off of Eventlet
is encouraged, we think that this guide will benefit to a more broader
audience if it is hosted into the Eventlet documentation itself. The whole
Python community would benefit from this guide and from our works.

Lets now observe the details and concepts of each pillar.

The Storage of the Alternatives
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

That's just the storage of the elements, the alternatives, from the previous
section. Alternatives may be seen as something alive, so the guide needs to
remains up-to-date in accordance with the possible additions.

we may think the selected alternatives as a shelf of raw materials.
Elementary bricks. Building house requires bricks, but it also require
architectural plan. The table of correspondences below is the architectural
plan.

The Glossary
~~~~~~~~~~~~

The goal of the glossary is to ensure that everyone is on the same page,
and that everyone have the same understanding of used terms.

The glossary aim to define terms like:

* concurrency;
* parallelism;
* preemptive;
* cooperative;
* coroutine;
* task;
* thread;
* etc...

The Tables of Correspondences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The goal of the tables of correspondences is to bind the common use cases of
Eventlet to turnkey alternatives. We propose to define two tables. Each
table is a representation that can help developers to identify alternatives
that they can use to remove their Eventlet usages depending on a given
context.

The tables provided by the guide should help developers to identify the
complexity of adopting a replacement solution or an other. By example, if
moving to an AsyncIO based solution, the guide should indicate that all the
calling code would also became async/await based, or that it should be ran
into an executor (``asyncio.run``).

This guide should be the result of a collegial work to gather all the specific
use cases and to oppose them alternatives based on asyncio, Awaitlet, queue,
future, etc.

The tables given below are not full list of alternatives. This section do not
aim to provide a detailed and finished extract of the alternatives. The tables
as the guide who contains them, again, should be designed by their own.
Tables are the keys of the freedom of decision-making.

The first table of correspondences would be based on the main Eventlet
design patterns, server, client, dispatch (see :ref:`on-eventlet`).

This table invites the persons in charge of the migration to think in terms
of common patterns. Most people using Eventlet can identify themselves into
one of these three categories.

+---------------------+--------------------------------+--------------------------------+
| Eventlet Patterns   | Eventlet features              | Available alternatives         |
+=====================+================================+================================+
| 1. **Server**       | eventlet.GreenPool,            | aiohttp.web.Application,       |
|                     | eventlet.listen,               | async (for|with), await        |
|                     | eventlet.green.socket,         | http.server.HTTPServer,        |
|                     | eventlet.green.http.server,    | http.server.TreadingHTTPServer |
|                     | eventlet.green.*Server,        | asyncio.start_server()         |
|                     | eventlet.websocket,            | StreamReader, StreamWriter,    |
|                     | eventlet.wsgi                  | asyncio.open_connection(),     |
|                     |                                | awaitlet*                      |
+---------------------+--------------------------------+--------------------------------+
| 2. **Client**       | eventlet.green.urllib*,        | asyncio.run(),                 |
|                     | eventlet.greenpool             | aiohttp.ClientSession,         |
|                     |                                | http.client                    |
|                     |                                | urllib.request                 |
|                     |                                | async (for|with), await,       |
|                     |                                | awaitlet*                      |
+---------------------+--------------------------------+--------------------------------+
| 3. **Dispatch**     | eventlet.listen,               | asyncio.Future,                |
|                     | eventlet.GreenPile             | futurist.Future,               |
|                     |                                | concurrent.futures.Executor    |
|                     |                                | aiohttp.web.Application,       |
|                     |                                | async (for|with), await        |
|                     |                                | http.server.HTTPServer,        |
|                     |                                | http.server.TreadingHTTPServer |
|                     |                                | asyncio.start_server()         |
|                     |                                | StreamReader, StreamWriter,    |
|                     |                                | asyncio.open_connection(),     |
|                     |                                | asyncio.run(),                 |
|                     |                                | aiohttp.ClientSession,         |
|                     |                                | http.client                    |
|                     |                                | urllib.request                 |
|                     |                                | async (for|with), await,       |
|                     |                                | awaitlet*                      |
+---------------------+--------------------------------+--------------------------------+

The second table of correspondences invites the reader to think in terms of
task and coroutine. This table is based on a hierarchy of tiers.
Each tier is built on the specification of the previous level.

To provide replacement to existing features of Eventlet, we think it is much
more useful to think about the use cases being arranged in a hierarchy, rather
than a flat list.

This way of representing the correspondences is inspired from the book
`Using Asyncio in Python <https://www.oreilly.com/library/view/using-asyncio-in/9781492075325/>`_.

Each tier is related to a level of abstraction. The first tiers are
the most abstract layers. The last tiers reflect low level mechanisms.

For most people Eventlet and its threading model is a blackbox. By reasoning
in term of tiers developers will have a better understanding of the
mechanisms currently in use in their code, hence, it will simplify their
removal.

Some tiers may have many solutions to the same Eventlet usage. In other
words some solutions may overlaps. Often, overlapping solutions are async and
non async alternatives. Solutions should indicate if they are
asynchronous or not. By example code using ``eventlet.tpool`` can be replaced
by blocking code (native thread who will blocks the calling thread).
Developers will be free to decide which solution best fit their needs.

Asyncio target two main audiences:
    * end-users developers who want to make applications using asyncio -
      Some may consider OpenStack services (neutron, nova, etc);
    * framework developers who want to make frameworks and libraries that
      end-users developers can use in their applications -
      Some may consider OpenStack shared libraries (oslo, etc).

But the OpenStack world is not so waterproof, and it is common to see teams
who implement services to also implement API related to these services, so
even services may be seen as a framework developers audience.

This hierarchy is so strongly coupled to Asyncio concept, but other third
party libraries and stdlib modules may find their places somewhere in this
hierarchical organisation.

By example, Cotyledon and Futurist aim to provide ways to create workers and
periodic tasks. Both concepts are strongly coupled to tiers 3 and 5 of the
hierarchy.

Another example is the CPython stdlib. CPython provide modules like
``threading``, ``http.server`` etc, that could be used to replace some
Eventlet based logic.

+---------------------+--------------------------------+--------------------------------+
| Hierarchy of tiers  | Eventlet features              | Available alternatives         |
+=====================+================================+================================+
| 1. **coroutines**   | eventlet.GreenPool,            | async def, async with,         |
|                     | eventlet.tpool,                | async for, await, awaitlet*    |
|                     | eventlet.spawn,                |                                |
|                     | eventlet.spawn_n,              |                                |
|                     | eventlet.spawn_after           |                                |
+---------------------+--------------------------------+--------------------------------+
| 2. **event loop**   | eventlet.greenthread.spawn*    | asyncio.run(),                 |
|                     |                                | BaseEventLoop                  |
+---------------------+--------------------------------+--------------------------------+
| 3. **Futures**      |                                | asyncio.Future,                |
|                     |                                | futurist.Future,               |
|                     |                                | concurrent.futures.Executor    |
+---------------------+--------------------------------+--------------------------------+
| 4. **Tasks**        | eventlet.GreenPool.spawn,      | asyncio.Task,                  |
|                     | eventlet.pools                 | asyncio.create_task()          |
+---------------------+--------------------------------+--------------------------------+
| 5. **Subprocess &** | eventlet.GreenPool.spawn,      | run_in_executor(),             |
|    **threads:**     | eventlet.greenthread.spawn*    | asyncio.subprocess,            |
|                     | eventlet.tpool,                | cotyledon.Service,             |
|                     | eventlet.spawn,                | futurist.Future,               |
|                     | eventlet.spawn_n,              | concurrent.futures.Executor    |
|                     | eventlet.spawn_after           | threading.Thread,              |
|                     |                                | futurist.ThreadPoolExecutor    |
+---------------------+--------------------------------+--------------------------------+
| 6. **Tools**        | eventlet.green.Queue           | asyncio.Queue, queue.Queue,    |
|                     | eventlet.lock                  | asyncio.Lock, threading.Lock   |
|                     | eventlet.timeout               | asyncio.timeout, threading..., |
|                     | eventlet.semaphore             | asyncio.Semaphore,             |
|                     |                                | threading.Semaphore            |
+---------------------+--------------------------------+--------------------------------+
| 7. **_Network**     |                                | BaseTransport                  |
| **(transport)**     |                                |                                |
+---------------------+--------------------------------+--------------------------------+
| 8. **Network**      | eventlet.green.SocketServer    | Protocol                       |
| **(TCP & UDP):**    |                                |                                |
+---------------------+--------------------------------+--------------------------------+
| 9. **Network**      | eventlet.green.BaseHTTPServer, | StreamReader, StreamWriter,    |
| **(streams):**      | eventlet.green.httplib         | asyncio.open_connection(),     |
|                     | eventlet.websocket             | asyncio.start_server(),        |
|                     | eventlet.wsgi                  | http.server.HTTPServer,        |
|                     | eventlet.support.greendns      | http.server.TreadingHTTPServer |
|                     |                                | dnspython                      |
+---------------------+--------------------------------+--------------------------------+

The previous table voluntarily ignores some Eventlet concepts like
``eventlet.patcher``, ``eventlet.hubs``, who have no meaning outside of the
Eventlet context. The previous table also voluntarily ignores green
representations of third party modules like ``eventlet.zmq``.

We should notice that finally many subsets of Eventlet features may match
many tiers, depending on their usages. By example the ``eventlet.tpool``
which is present in tiers 1 and 5. That's due to the fact that Eventlet only
reason in terms of greenlet.

This table of correspondences can be completed with additional
solutions like the web server of the ``aiohttp`` lib that can be a solution
to replace the WSGI features of Eventlet.

We may think these tables as a architectural plan. Where are the rooms, the
plumbing, the electricity. Where each team is able to choose its own design.

But, building house requires a schedule. In addition of the plans, a kind of
Gantt's diagram is now necessary. Lets see how to schedule the building of a
single house.

.. _how-to-migrate-our-deliverables:

How to migrate a single deliverable
===================================

Here is a proposal to define the different required steps to migrate an
OpenStack deliverable.

The OpenStack Python code base is mostly composed of libraries and services.
The migration plan may differ depending the kind of deliverable.

We should notice that an incremental migration really increase the complexity
to get a big picture of the advancement of this goal. Almost all deliverables
relying on Eventlet could remains in a transient state without being fully
migrated. Migrating this way could lead us to a blur state.

How to migrate a library
~~~~~~~~~~~~~~~~~~~~~~~~

Consider the migration of a single one OpenStack library (e.g oslo.messaging,
OpenStackSDK, ...). Lets call this OpenStack library example ``oslo.demo``.
Lets consider that the ``oslo.demo`` library provide existing drivers to
communicate with backends.

Migrating a library, in our example oslo.demo, would mean:

#. if not already done previously, starting by moving requirements of the
   oslo.demo, to a minimum version of Eventlet that support Asyncio (0.35.0 at
   least).

   Many libraries are requesting Eventlet in their ``test-requirements.txt``
   file. These requirements should be updated first to avoid pip resolver
   issues.

#. Developers of the oslo.demo should identify which python packages could be
   good candidates for the implementation of their Asyncio based driver.

   Example, in an oslo.messaging context, the existing rabbitmq driver relies
   on `py-amqp <https://github.com/celery/py-amqp>`_ library, the new Asyncio
   based driver could rely on `aioamqp <https://github.com/Polyconseil/aioamqp>`_.
   Both drivers will be available for end users.

   There exists good candidates for almost all our third parties
   libraries. `Here is curated list <https://github.com/timofurrer/awesome-asyncio>`_
   that can help us which package we want to use for depending on our needs.

   Identified candidates could be now added to the requirements of oslo.demo.

#. start migrating the code base of oslo.demo. This step would simply
   translate by the implementation of the new driver. At some points some
   depending on the underlying libraries chosen, config options of oslo.demo
   may be modified or added.

#. Libraries may have specific features who are strongly related to Eventlet,
   like the ``heartbeat_in_pthread`` feature in oslo.messaging. Removing
   Eventlet would make these feature obsolete. As this kind of feature
   exposes configuration endpoints we would have to deprecate them to allow
   lib users (services) to update their config files accordingly. However, the
   deprecation process would take several months or even series before hoping
   to see these features removed. Hence blocking the migration.

   The proposed solution is to mock these features with empty entry-points
   who will only raise deprecation warnings to inform users that they have
   to update their config files. After 1 or 2 series these empty mocks could
   be safely removed without impacting anybody.

   In other words, these feature will remain in the code, but they will do
   nothing. They will be empty feature allowing us to migrate properly.

   Example with the ``heartbeat_in_pthread`` feature, by removing Eventlet
   wouldn't have to run heartbeats in a separated threads. This feature,
   the RabbitMQ heartbeat, would be run in a coroutine. The config option
   will remain available but it will only show a deprecation warning like the
   following one.

   .. code::

       __main__:1: DeprecationWarning: Using heartbeat_in_pthread is
       deprecated and will be removed in {SERIES}. Enabling that feature
       have no functional effects due to recent changes applied in the
       networking model used by oslo.messaging. Please plan an update of your
       configuration.

#. oslo.demo would be considered as fully ready once it will provide Asyncio
   based drivers for all its functionalities.

How to migrate a service
~~~~~~~~~~~~~~~~~~~~~~~~

As with libraries, the migration of services could be incremental.
As long as the OpenStack deliverables start releasing migrated sub modules
operators would be able to start using them.

As for the oslo.demo example, let's consider an hypothetical OpenStack service
named ``supernova``. Migrating a service like ``supernova`` would mean:

#. Upgrade the minimal version of Eventlet in ``requirements.txt`` file.
   Deliverables eager to use Asyncio based drivers/backends from the common
   libraries, we would have to always use Eventlet in a compatible version
   (at least `0.35.0 <https://github.com/eventlet/eventlet/releases/tag/v0.35.0>`_).
   Else Asyncio won't be supported by Eventlet.

#. Without some configuration, Eventlet and `Asyncio are not compatible and
   can't live together in the same process <https://github.com/eventlet/eventlet/issues/673#issuecomment-740429872>`_.
   Allowing running Eventlet and Asyncio in the same process will allow using
   a wide range of the solutions proposed in the guide.

   Deliverables eager to use AsyncIO must `activate the new Eventlet AsyncIO
   hub <https://eventlet.readthedocs.io/en/latest/migration.html#step-1-switch-to-the-asyncio-hub>`_
   After that it will be possible to run Eventlet and AsyncIO code in the
   same process. From this point, we will be able to start refactor our own
   code to migrate async features toward Asyncio or to use AsyncIO based
   driver/backends from the common libraries.
   As `the Asyncio hub was added within Eventlet 0.35.0 <https://github.com/eventlet/eventlet/releases/tag/v0.35.0>`_,
   this will require Eventlet in a version equal or higher to version 0.35.0.

   If maintainers prefer a thread based solution, then, the Eventlet hub
   do not really matter, and could remains as it is. In this case, AsyncIO
   based alternatives (AioHttp, Awaitlet, etc) would not been available while
   the removal of Eventlet is not fully finished on this deliverable.

#. As a service migration could represent an heavy workload, and as OpenStack
   resources are more decreasing than increasing, we recommend to split
   the transition into subtopics. Firstly we would recommend to identify
   if teams want to use the Asyncio based facade of the OpenStack libraries.
   Else, teams should decide of the execution model of these libraries that
   best fits their needs. They can use the migration guide to compare
   alternatives.

   For more details about the migration guide please see
   :ref:`migration-guide`.

   In a supernova context, splitting topics would translate, by example, by,
   starting migrating oslo.messaging first, once done, start migrate
   oslo.cache, and so on. Then, once all OpenStack library
   usages are transitioned then, start migrating third parties libraries calls
   directly made into supernova. And then replace all occurrence of Eventlet
   coroutines by something else, by example native threads.
   The oslo.messaging migration is a subtopic. The oslo.cache migration is a
   subtopic. The migration of requests usages by aiohttp is a subtopic.
   The migration of Eventlet coroutines is an other one. And so on...

   requirements versions could be used to identify which subtopics remains
   an active topic or not - a transition to be made.

   We could maintain a requirements matrix helping to identify which
   versions of OpenStack libraries are already migrated or not and maybe
   what is their level of migration completeness.

#. As for libraries we want to migrate the unit tests of supernova lastly, so
   the migration must start by migrating the code base loaded at
   runtime, tests would be migrated in a second time.

   Again the migration guide would suggest alternatives to the majority
   of the use cases that deliverables may face.

#. Services may face the same problem that libraries with features who expose
   configuration options and who are strongly coupled to Eventlet, hence,
   leading to delay the migration of the service due to deprecation period.

   We suggest to handle this kind of blocking point the same way that we
   proposed for libraries, i.e by mocking these features with empty endpoints.

   The config option will remains available but won't do nothing if used.
   Please refer to the ``heartbeat_in_pthread`` use case above for more
   details about how to manage blocking deprecations.

#. Migrate unit tests. As said previously we want to
   avoid regression, so the latter we migrate unit tests the better.

#. Releasing the refactors. Subtopics must be addressed incrementally. We
   would suggest to try addressing a subtopic in its entirety to simplify
   progress tracking, however, if not possible, it would be feasible to
   release partially migrated sub modules.

#. If new bugs are opened during the migration, and if these bugs are related
   to Eventlet and/or to possible race conditions triggered by using Eventlet,
   then, we would suggest refactoring the impacted code to drop the related
   Eventlet usage, and, hence, avoid wasting time by fixing something that
   will be removed soon.

Now that we are able to construct a single house, lets see how to design
different districts which would represent at the end an entire city.
Again we are close in meaning of something like a Gantt's diagram.

.. _the-global-strategy:

The global Strategy
===================

This global strategy, the global schedule, is composed of 3 global milestones.
A short term milestone, a medium term milestone, and long term milestone.
Each milestone is ordered in terms of priority and of dependency.

.. _short-terms-solution:

Short terms solutions (done)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*The short term milestone is where we were 6 months ago. Even if this
milestone is now done, we preferred to keep this milestone under this document
to provide a full and unified context.*

As Python 3.12 will be a supported runtime in the next coming
OpenStack series, the support issue should be quickly fixed.

So, In short term, Eventlet itself should be fixed first.

This milestone should be done before the beginning the next series
("2024.2/Dalmatian").

Here is a plan proposal to see this milestone succeed:

#. Start the discussion with current maintainers (*done*).
   https://github.com/eventlet/eventlet/issues/824

#. gain write access to the current repo (*done*).
   https://github.com/eventlet/eventlet/issues/824#issuecomment-1853128741

#. draft future announcements early in the process to ensure we have achieved
   our goals when the time comes to publish our announcements. Could be
   a good benchmark for us to measure our advancements and to validate them.

#. Merge the CI patches. (*done*)

   * https://github.com/eventlet/eventlet/pull/827
   * https://github.com/eventlet/eventlet/pull/831
   * https://github.com/eventlet/eventlet/pull/832

#. Merge the fix for introduce the support of CPython 3.12. (*done*)

   * https://github.com/eventlet/eventlet/pull/817
   * https://github.com/eventlet/eventlet/pull/847
   * https://github.com/eventlet/eventlet/pull/854

#. Release the latest changes by creating a new version. (*done*)

   * https://github.com/eventlet/eventlet/issues/842
   * https://github.com/eventlet/eventlet/issues/861
   * https://pypi.org/project/eventlet/0.34.1/
   * https://pypi.org/project/eventlet/0.34.2/

#. Upgrade the OpenStack requirements to match this new version. (*done*)

   * https://review.opendev.org/c/openstack/requirements/+/904147
   * https://review.opendev.org/c/openstack/requirements/+/907048

#. Validate that the main issues are now fixed. (*done*)

.. _medium-terms-solution:

Medium terms solutions
~~~~~~~~~~~~~~~~~~~~~~

Now Eventlet can be considered as healthy and OpenStack secured for the coming
series (2024.2/Dalmatian).

As our goal is to remove Eventlet and as Eventlet occupies an important place
in OpenStack, we would have to consider the following points:

#. Asyncio in some aspects may be a credible alternatives to many Eventlet
   use cases. If some deliverables are eager to use some Asyncio based
   solutions they would surely also aim to use our common libraries in an
   Asyncio based fashion.

   For this reason, if common libraries from OpenStack have the opportunity
   to offer drivers, backends, or facades based on Asyncio, in addition of
   the already existing drivers, backends, and facades, then they must
   provide these opportunity to not closing the door of the Asyncio based
   alternatives.

   These new drivers, backends, facades, may be based on third parties
   libraries like aiohttp etc...

   If common libraries close the door to Asyncio, then that will close the
   door of using Asyncio in the majority of the OpenStack deliverables.

   For more details about the migration guide and the proposed alternatives
   please see :ref:`migration-guide`.

#. Asyncio in versions of Eventlet lower than 0.35.0, is not supported.
   Both technologies cannot run in the same process.

This milestone would surely require at least two series. One series
(*2024.2/Dalmatian*) to design and implement the transitive engine that
will allow us to start the migration and two series (*2025.2/F*) to migrate
the first bricks. Here are items for milestone 2:

#. design specs of the new Eventlet's Asyncio hub or similar that has an
   Asyncio backed eventloop that we can enable instead of the default Eventlet
   one. (*done*)

   * https://github.com/eventlet/eventlet/issues/868

#. implementing the new hub. (*done*)

   * https://github.com/eventlet/eventlet/issues/869
   * https://eventlet.readthedocs.io/en/latest/asyncio/migration.html#migration-guide

#. Creating the Awaitlet library. (*done*)

   Following the `comments related to the previous patch set of this proposal
   <https://review.opendev.org/c/openstack/governance/+/902585/comment/289922c2_42aaa933/>`_
   the AsyncIO-greenlet pattern created by Mike Bayer has been identified as a
   possible solution, in some circumstances, to some OpenStack scenarios,
   for this reason we think that providing a standalone implementation
   of this pattern would translate into a good opportunity for us to
   solve this challenge.

   This pattern is internal to SQLAlchemy, the objective of this item is to
   provide a standalone deliverable that host this pattern.

#. Identify and add replacement third parties libraries into
   ``openstack/requirements``. It exists good candidates replacement for
   almost all our third parties libraries. `Here is curated list
   <https://github.com/timofurrer/awesome-asyncio>`_
   that can help us which package we want to use for depending on our needs.

   Once selected these packages should be added, one by one, to
   ``openstack/requirements``, `by following our usual process
   <https://docs.openstack.org/project-team-guide/dependency-management.html#for-new-requirements>`_.

#. deprecating oslo.service.

   Oslo.service was originally designed to provide a framework for
   defining long-running services, and performing periodic operations. To
   implement this logic oslo.service is strongly coupled to Eventlet, so an
   Eventlet removal would mean either an oslo.service total rewrite or an
   oslo.service removal. We have several options to replace oslo.service so
   a total rewrite of oslo.service would a lost of time. Instead we propose
   to replace oslo.service use cases by other libraries specifically tailored
   for.

   The first option would be to use `cotyledon <ihttps://cotyledon.readthedocs.io/en/latest/index.html>`_.
   Cotyledon provides a framework
   for defining long-running services. It provides handling of Unix signals,
   spawning of workers, supervision of children processes, daemon reloading,
   sd-notify, rate limiting for worker spawning, and more. This library is
   mainly used in OpenStack Telemetry project, so we have concrete internal
   examples of working usages. We can use cotyledon to define the way we run
   our long-running services, and to manage our needs of workers.

   The second option to replace oslo.service and to manage periodic tasks
   would be to generalize the adoption of `Futurist <https://docs.openstack.org/futurist/latest/index.html>`_
   in place of Eventlet. By example the RBD executor of Nova could be
   rewritten by using the ``ThreadPoolExecutor`` of Futurist.

   So, in a first time will have to deprecate oslo.service, and to provide
   migration paths toward Cotyledon and Futurist.

   Once oslo.service won't be used anymore in OpenStack, we will be free to
   abandon it.

#. Introduce Asyncio in the first OpenStack bricks (a couple of identified
   libraries):
   * oslo.messaging;
   * oslo.db
   * oslo.concurrency;
   * oslo.cache;
   * OpenStackSDK (SDK is blocking and do not support async, it should be also
   migrated to Asyncio to avoid wrapping rest calls made to other services)

   The solution described here proposes to adapt common libraries with a
   collection new drivers and backends based on Asyncio in addition of
   the already existing drivers and backends. Teams maintaining services will
   be free to decide which can of backend they want to use, and which kind of
   migration path they want to follow for their deliverables.

   Moving these libraries first would be a first significant step toward a
   successful migration.

   By example, for oslo.db that would translate by the implementation of
   an Asyncio based enginefacade. For oslo.messaging, that would mean the
   implementation of a new AMQP driver based on the `aioamqp <https://github.com/Polyconseil/aioamqp>`_
   third party library based on Asyncio.

   For more details about how to conduct a migration for a single deliverable
   please see :ref:`how-to-migrate-our-deliverables`.

#. choose a service that will serve as reference user. Glance-api have been
   proposed because it seems relatively small and typical.

#. migrate this reference user deliverable (glance-api for now).

#. prepare a migration guide based on the observations made during the
   migration of the previous deliverables. The goal of this guide would be
   to help during the migration of the services and of the libraries that
   remains not transitioned. This guide should accelerate the way teams are
   able to migrate their deliverables.

   For more details about the migration guide please see
   :ref:`migration-guide`.

#. cross testing the previously migrated deliverables. It would surely
   need the help of the QA team and of the requirements and infra team to
   design these cross tests and to make them running jobs.

#. identifying the low hanging fruits that could be easily migrated by
   involving cross team expertness to inspect their deliverables. That would
   help making a list of migration priority and give a big picture of the
   remaining workload.

.. _long-terms-solutions:

Long terms solutions
~~~~~~~~~~~~~~~~~~~~

This milestone would surely require at least four or five series. 2027.2
would surely be our deadline.

Deliverables like nova or swift could be the hard ones to migrate.
Also we could face difficulty with non active deliverables. They could slow
down our progress.

To migrate the remaining deliverables we should consider the following
points:

Here are the main steps to conduct this long terms migration:

#. Identify deliverables who are not actively maintained and decide with the
   TC to retire them. This is a crucial point to avoid falling in an infinite
   loop of projects still relying on Eventlet and that could stuck this goal.

   This kind of deliverable could force us to rollbacks all our previous
   efforts as we did with the recent `oslo.db/sqlalchemy upgrade
   <https://lists.openstack.org/archives/list/openstack-discuss@lists.openstack.org/thread/Y4U2EHQYHB7DN5JSV2I7SJLXXVLW2QFF/#FMEIONXDKUKF3PXDULPFAVZ7WAGSTJIF>`_.
   We don't want to repeat this situation, especially with the inherent
   complexity of the Eventlet migration topic.

   Identifying them could be done with the help of release team and
   requirements team by defining some criteria like the absence of
   patches merged (excluding automated patches related to series upgrade) and
   the absence of new releases since more than 5 months from the beginning
   of the current series at this time.

#. Migrate all the OpenStack remaining deliverables not yet migrated:

   * Remaining libraries should be migrated first.
   * Easily one should be migrated as soon as possible to allow harvesting
     feedback and experience easily acquired. The previously reference user
     (glance-api) could be used as an example.
   * Easily one should be migrated as soon as possible to free the maximum of
     available resources to focus efforts on the hardest deliverables to
     migrate.
   * Easily one should be migrated as soon as possible to allow cross
     integration testing to be run early during the migration of the
     hardest one.

   For more details about how to conduct a migration for a single deliverable
   please see :ref:`how-to-migrate-our-deliverables`.

#. Once all the deliverables are migrated, we should be able remove Eventlet
   requirements from all our deliverables.

#. Abandoning oslo.service and retiring it from our global requirements.

#. Retiring third parties libraries from our global requirements. If a third
   party library is not used anymore (even in a non async/Eventlet model),
   then it could be removed from our global requirements. If all deliverables
   are already migrated, then all useless third parties requirements could
   be removed.

#. Once all the OpenStack migration would be done we would have to Plan the
   retirement of Eventlet, or, at least, we would have to socialize the fact
   that we don't have anymore interest in continuing maintaining this library,
   so if the OpenStack maintainers involved in Eventlet want to retire, then
   they would to socialize their departure. If someone else, outside of
   OpenStack, volunteer to continue the Eventlet adventure, then, we would
   have to bequeath this project to him.

Limitations of the proposed solution
====================================

The reader should be aware that proposed solution do not provide any
guarantee if the GIL is disabled, especially if teams decide to prefer the
usage of native threads to replace existing code based on Eventlet.

We cannot predict the impacts of such change, this is why this
solution cannot give guarantees in this context
(:ref:`on-the-standards-of-the-industry`).

We encourage, if possible, to prefer the usage of a cooperative paradigm over
the usage of a preemptive paradigm. Many of our alternatives are based on
a cooperative paradigm. Greenlet, Awaitlet, AsyncIO, Eventlet AsyncIO hub,
etc... Cooperative would leave less room for uncertainties.

We invite the reader to carefully consider this point.

Conclusion
==========

| A community goal does not shape a new and personal vision of OpenStack.
| A Community goal collects this vision from the scattered hopes and
  intentions of our community's past.

This goal is a plan proposal to implement our community vision.

| A plan designed for our own perennity.
| A plan in accordance with previous decisions of our community.
| A plan based on the right technologies and on their capabilities.
| A plan taking account of resources scarcity.

| Removing Eventlet is not an option, that's an obligation.
| Without action we will soon face a brutal discontinuation.
| Adopting a goal is a logical continuation.
| A goal which consider team predisposition.

| A solution proposing a smooth migration.
| A solution offering visible gains to our customers.
| A solution That bring an engineering apprehensible by our expert developers.
| A cost saving solution that would optimize resource consumption.

| The TC is elected to provides technical leadership.
| The TC is responsible in providing an ultimate appeals board for technical decisions.
| If TC members simply reject this proposal without proposing anything else,
  they will have made a technical decision, but they will not be showing
  leadership.

We ask TC to provide leadership!

Champion
========

- Hervé Beraud <hberaud@redhat.com> (hberaud)

Credits
=======

A challenge such removing Eventlet from Openstack cannot be taken alone.
Since the beginning of this topic the collaboration is the keystone of
solving this problem. All the elements presented in this document are the
fruits of numerous collaborations.

Communities are the common denominators of success. Openstack is the result
of our community. Our community is the demonstration of numerous successful
collaborations. We cannot divide our success of our collaborations.

For this reason, we want to thank all the persons who participated to this
topic. We want to specially thank the following people and credit their
contributions:

- Jay Faulkner for originally raising this issue and for all the efforts made,
  the support provided, and for all the help given during previous months;
- Julia Kreger for advocating for a community initiative to address the
  Eventlet problem;
- Itamar Turner-Trauring for his help on maintaining and on improving
  Eventlet, which ultimately moved the subject forward significantly;
- Mike Bayer for his suggestions and for his works on various aspect of this
  topic, especially Awaitlet;
- Sean Mooney and Dan Smith for their numerous reviews and their
  suggestions who significantly helped to reach a credible and feasible
  solution;
- Tobias Urdin for his previous works on the NATS driver which led us to
  a better understanding of the Eventlet side effects on AsyncIO.

These persons embodies the greatness of our community!
These persons, taken together, are the equation to solve this problem!
These persons are the formula of our success!
They are our champions!

Gerrit Topic
============

To facilitate tracking, commits related to this goal should use the
gerrit topic::

  eventlet-removal


Completion Criteria
===================

#. (done) Get an healthy new version of Eventlet;
#. (done) Be able to support Python 3.12 and higher version as an OpenStack runtime;
#. (done) Get Asyncio supported by Eventlet and vice versa;
#. Get the oslo world fully migrated;
#. Get libraries like OpenStackSDK migrated;
#. Get a reference user project elected;
#. Get non actively maintained deliverables retired;
#. Get all other OpenStack deliverables relying on Eventlet migrated;
#. Get Eventlet retired from OpenStack;
#. Get Eventlet abandoned or bequeath to someone else.

References
==========

- Using Asyncio in Python; Caleb Hattingh - ISBN: 978-1-492-07533-2
- The hacker's guide to scaling python; Julien Danjou - ISBN: 978-1-387-37932-3
- Structured Parallel Programming - Patterns for Efficient Computation; Michael McCool, Arch D. Robison, James Reinders - ISBN: 978-0-12-415993-8


Previous similar attempts and discussions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `Replace Eventlet by asyncio, by Victor Stinner <https://review.openstack.org/#/c/153298/>`_
- `Replace eventlet + monkey-patching with threads, by Joshua Harlow <https://review.openstack.org/#/c/156711/>`_
- `Use an asyncio event loop, by Victor Stinner <https://wiki.openstack.org/wiki/Oslo/blueprints/asyncio>`_
- `The oslo.messaging NATS driver <https://lists.openstack.org/archives/list/openstack-discuss@lists.openstack.org/thread/TOZU6ONOSOD6BBHTCBVHWG6HPOOLOW6N/#U4F4I4OURQMIP6PVKARG6UT2JB6XU2PM>`_
- `Specs to add the NATS transport driver to oslo.messaging <https://review.opendev.org/c/openstack/oslo-specs/+/692784>`_

A brief Eventlet history in OpenStack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- https://wiki.openstack.org/wiki/Obsolete:UnifiedServiceArchitecture
- https://lists.openstack.org/pipermail/openstack/2012-March/027583.html
- https://code.launchpad.net/~termie/nova/eventlet_merge/+merge/43383
- https://lists.openstack.org/archives/list/openstack-discuss@lists.openstack.org/message/WCCJULVHRZUI7EUVLOUEMCTSPE5YIJGV/

Identified Blocking Points
==========================

Epolls Multiple Readers
~~~~~~~~~~~~~~~~~~~~~~~

OpenStack rely on hacks which allow to disable the Eventlet protection
against race condition. Indeed, by default Eventlet's hub prevent multiple
readers (greenlets) reading from a socket. However, Eventlet also come
with a **debug** convenience which allow to disable this protection. Hence,
using this convenience mean allowing readers to read from the same socket and
hence introducing several risks of race conditions and of unexpected
behaviors.

More details about this convenience can be found there:

* https://eventlet.readthedocs.io/en/latest/modules/debug.html#eventlet.debug.hub_prevent_multiple_readers

Swift contains this kind of hack based on this **debug** convenience:

* https://opendev.org/openstack/swift/src/branch/master/swift/common/utils/__init__.py#L6102-L6116

The Asyncio hub doesn't support that multiple readers notion. Hence, this debug
convenience can't be used with the Asyncio hub. This multiple readers notion
is a bad practice. We already have several discussions concerning that notion:

* https://github.com/eventlet/eventlet/issues/874
* https://github.com/eventlet/eventlet/issues/432

Risks are too high. It would be too easy to introduce bugs and unexpected
behaviors. Benefits are too low and we should consider that alternatives
exists through using design patterns and by using native system features.

Eventlet users should handle things differently. User should manage that's
need as a design topic of their application and not as buggy convenience
in a low maintained library.

Users are encouraged to use the right concepts to correctly handle that kind
of needs. By example may use the chain of responsibility patterns in their
application design or why not using dup file descriptors or feeder threads if
they want to accomplish such kind of mechanisms without risks.

* https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern
* https://www.man7.org/linux/man-pages/man2/dup.2.html
* https://docs.python.org/3/library/os.html#os.dup
* https://docs.python.org/3/library/socket.html#socket.socket.dup

Each solutions may present advantages disadvantages, but they can't be worst
than disabling all protections against race conditions through using
a debug convenience.

Each deliverable that contains this hack is a deliverable which cannot
Eventlet and Asyncio in the same time. Each deliverable that contains this
hack is a deliverable where the removal of Eventlet will be complex.

Current State / Anticipated Impact
==================================

* Progress is maintained on the below wiki page:
  https://wiki.openstack.org/wiki/Modernize_OpenStack_Networking_Programming_Model
* aihub discussions and pre-specs are currently hosted on the below wiki page:
  https://wiki.openstack.org/wiki/Aiohub-Discussion
* Identification of Eventlet based deliverables that can be easily migrated to
  asyncio is hosted on the below wiki page:
  https://wiki.openstack.org/wiki/Eventlet-Based-Deliverables-Easily-Migrated

Related links:

- https://github.com/eventlet/eventlet/issues/824
- https://github.com/eventlet/eventlet/issues/824#issuecomment-1853128741
- https://github.com/eventlet/eventlet/pull/827
- https://github.com/eventlet/eventlet/pull/831
- https://github.com/eventlet/eventlet/pull/832
- https://github.com/eventlet/eventlet/pull/817
- https://github.com/eventlet/eventlet/pull/847
- https://github.com/eventlet/eventlet/pull/854
- https://github.com/eventlet/eventlet/issues/842
- https://github.com/eventlet/eventlet/issues/861
- https://pypi.org/project/eventlet/0.34.1/
- https://pypi.org/project/eventlet/0.34.2/
- https://review.opendev.org/c/openstack/requirements/+/904147?usp=search
