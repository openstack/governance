==============================
Emerging and inactive projects
==============================

As a community we want to be inclusive for new projects under the OpenStack
umbrella. This, however, isn't that easy as each project needs to fit many
requirements (see :doc:`new-projects-requirements` for more details) and that can
be sometimes hard for new projects.

In order to grow a new project team within OpenStack, we want to accept them
into the OpenStack space when they have code that's functional enough to
indicate what it is they want to accomplish, but at the same time we need to be
clear to OpenStack consumers that such a project is not yet ready to be run in
production due to factors such as the code repository not structured according
to OpenStack standards, functionality is missing, etc.

It may also happen for already existing official OpenStack projects that they
may not be so active anymore, they may not be able to do release on time or have
broken testing or not merge incoming patches for long time.

In order to solve the above problems, there is ``Emerging technology`` state for
such new projects and ``inactive`` state for existing projects that are not so
active anymore. TC will keep working on such projects to make them consistent
with OpenStack or try to transition inactive projects to active. TC might not be
able to solve these problems but we will try to keep eyes on such projects and
give our best effort to make them active.

``Emerging technology`` is a state which can be set for new OpenStack projects.
The state of ``inactive`` can be set for existing projects that aren't well
maintained due to lack of maintainers or active contribution.

Entry criteria
==============

If a new project wants to become an official OpenStack project, but it does not
fit all requirements for new official projects (see
:doc:`new-projects-requirements` for details) TC can consider to add such
project to the OpenStack projects as ``Emerging technology``.

For existing projects which became inactive due to lack of maintainers and are
not able to do the mandatory activities, such as release, fix testing, review
incoming code, etc., TC can consider marking such projects as ``inactive``,
try to solve the problem if we can but keep it in the official
OpenStack projects list instead of deprecating and removing it immediately (see
:doc:`dropping-projects` for more details).


Exit criteria
=============

A project can exit the ``Emerging technology`` or ``inactive`` state by either
becoming an active OpenStack project or by becoming a retired project.

An ``Emerging technology`` project can be considered active when it meets all
the requirements to be an OpenStack official project, which are described in
:doc:`new-projects-requirements`.  In particular, there must be a sufficient
number of active maintainers to perform all the basic activities of OpenStack
official projects.

Any existing project which became ``inactive`` and did not turn back to the
``active`` state before milestone-2 of the same cycle (see `Timeline`_) will
usually stay in the ``inactive`` state for at least one full cycle in which it
meets all of the :doc:`new-projects-requirements`.
If it meets all those requirements for one full cycle, and continues to
be in the good shape in the next one, then it can be considered by the TC to
exit an ``inactive`` state and become an active OpenStack project again.
If a project becomes active very early in a cycle after it was deemed
"inactive", project members can approach the TC to waive the two-cycle wait
period mentioned above. This proposal must be made to the TC before Milestone-2
of the release.

A project may be retired by the TC if it does not complete the work required to
become an active project within the timeline defined below.

Timeline
========

A new project must become an active OpenStack project before the third OpenStack
coordinated release after the project has entered ``Emerging Technology``
status. For example, a project became OpenStack ``Emerging technology`` project
in Yoga cycle then timeline for them is BB (after two releases, Zed and AA). In
BB development cycle such project should meet all requirements for a new project
listed in :doc:`new-projects-requirements` to stay as an official OpenStack
project.
If project is not able to become an official OpenStack project within that
timeframe, TC will discuss with the team if more time is required for the
project to meet the :doc:`new-projects-requirements` or will retire the project.

The TC will monitor the existing projects at different stages of the development
cycle and if any project becomes inactive due to lack of maintainers and is not
able to do the mandatory activities then the project will be marked as inactive.
We will try to detect and mark a project inactive in the early stage of the
development cycle but it can happen at any phase of development cycle.

An existing project should be reinstated as an active OpenStack project before
the release milestone-2 of the cycle they entered or extended the ``inactive``
state to become ``active`` again and to be released in that cycle.  In the case
where an ``inactive`` project does not become ``active`` before the release
milestone-2, there will be no release of it proposed by the release team in that
cycle.  In such a case, it is up to the project itself to get CI working and
propose a release if that is needed. It may be required in some cases for
example, when there will be security fixes or compatibility fixes merged in the
project. In the case where an ``inactive`` project still does not meet
requirements for an official OpenStack project during the next cycle after the
cycle they entered or extended the ``inactive`` state, the TC will discuss with
the team if project will be retired before the release milestone-2 of the cycle.
In such a case there will be no new releases of that project.

If TC detects inactive project or project becomes inactive after the release
milestone-2 of the cycle, TC needs to take decision based on the severity and
risk to continue the project release.

Tracking
========

At the end of each cycle, TC will evaluate this list of the ``Emerging
technology`` and ``inactive`` projects and based on the timeline checks if any
of them can become active or if it maybe should be retired. Any addition or
removal of projects in this list will require a formal-vote.

Current Emerging Technology Projects
------------------------------------

No emerging projects at this moment

Current Inactive Projects
-------------------------
* Monasca

  * Inactive since 2024.1 cycle
  * Extension in 2024.2 cycle

* Freezer

  * Inactive since 2024.1 cycle
  * Extension in 2024.2 cycle
