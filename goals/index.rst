.. _release-cycle-goals:

======================
 OpenStack-wide Goals
======================

The pages in this part of the governance documentation describe
OpenStack-wide goals.

We use these OpenStack-wide goals to achieve visible common changes,
push for basic levels of consistency and user experience, and efficiently
improve certain areas where technical debt payments have become too high
-- across all OpenStack projects. From a contributor perspective, the goals
help unify the community's work as a whole, with some shared objectives. We
know this work is worthwhile, because these goals are how we achieve the
OpenStack mission together. We will build these goals based on our shared
values.

We know this process is working when:

* Users and operators see OpenStack working well as a platform, rather
  than a collection of loosely-related, different projects.
* We make progress on solving long-standing issues that would
  otherwise have lingered indefinitely at different stages of
  implementation in various projects.
* All contributors and projects know they are valued members of the
  successful and thriving OpenStack community.
* We facilitate marketing communication around release time due to
  successful completion of community-wide goals during the cycle.

Process Details
===============

Identifying Goals
-----------------

The goal process enables the community of OpenStack projects to
surface common concerns and work out specific technical strategies for
addressing these concerns.

The first step in the process is to build a `backlog of potential goals`_.
This helps us coalesce feedback received from deployers, users, contributors,
and PTLs. It is the reference used as a base for goal discussion during
Forum events. Finally, it serves as inspiration for prospective goal
champions.

.. _`backlog of potential goals`: https://etherpad.openstack.org/p/community-goals

Defining Goals
--------------

Goals are defined here in the governance documentation to ensure that
we establish a common understanding of the expectations being set.

Once champions have volunteered to propose and drive a specific goal, they
should iterate through goal definition in the ``/goals/proposed/`` directory.
This allows to keep the goal selection process separate from the goal
definition process.  Goal proposals should have the ``goal-proposal`` gerrit
topic, whose voting rules are specified in the `house rules`_.

.. _`house rules`: https://governance.openstack.org/tc/reference/house-rules.html

Goal definitions should use the provided template so they are all
formatted consistently.  The goal definition does not take the place
of any blueprints, spec documents, or other planning tools used within
a project to track its work, but can be referenced from those
documents.

This separates the discussion for each goal, and allows authors to gradually
refine and improve their proposal through multiple incremental changes.
Goals should be discussed on the mailing list to collect feedback on their
feasibility, and consensus on whether they have been completely and clearly
described.

Selecting goals
---------------

The TC will consider proposed goals from the ``/goals/proposed/`` directory
and select a set of OpenStack-wide goals to allow planning and other
discussion at the PTG event at the start of each cycle.

OpenStack-wide goals are not tied to any release, and they can have target
dates which can be a particular cycle release date or multi-cycle or even
in between a release cycle. Goal completion target dates will be selected by
considering the amount of work needed and the community (project and
champions) bandwidth. If a goal requires a large amount of work, it can be
divided into different milestones, with each milestone targetting a set of
things to complete. For example, if goal 'A' needs two big things to do, it
can be divided into two milestones, say Milestone 1: Yoga cycle release,
Milestone 2: Z cycle release.

There is no minimum or maximum limit on the number of goals to be selected at
a time. It can be zero or more depends on the complexity and work required per
goal. For example, if three groups of contributors would like to start
three different goals and projects are also ok with that, then it is fine to
select all three goals at a time and implement those in parallel. Also, it is
completely fine to have no goal for a particular time with a valid reason,
for example, if any previous OpenStack-wide goal is still pending and needs
more time to complete, or project team has less bandwidth and working on
other priority items like popup team work etc.

To select a goal, a TC member can pick one or more goals from the
``/goals/proposed/`` directory and move them to the ``/goals/selected/``
directory.

This allows to consider the proposed series goals as a group, and take
into account how feasible they are together, considering the timing and
amount of work required. Champions for selected goals should +1 this patch to
confirm they are ready to work on their goal.


Tracking Goal Progress
----------------------

After goals are approved, the goal champions can create one story per
goal and one task per project per goal or setup an etherpad to track progress
on completion.

.. note::

   It is expected that some projects may not always be able to complete a goal
   within the targeted cycle. If this is the case, existing projects are
   encouraged to continue to track their progress once they are able to further
   work on the goals.

   New projects do not need to retroactively track past goals as part of the
   created stories or in pre-StoryBoard documentation, whether the goals were
   completed before or after becoming an official project.

Team Acknowledgment of Goals
----------------------------

Each PTL is responsible for updating the progress on their tracking item
(etherpad, story, or blueprint). A status indicating progress is being made
should include a link to a planning artifact (such as a spec). The planning
artifact is likely to be a link to a spec or bug, and the completion artifact
is likely to be a link to one or more committed patches.

This step is also the indication that a project team is signing up as
agreeing to the goal and committing to do the work to complete the
goal, within their project. That commitment may mean doing it
themselves or may mean simply prioritizing reviews submitted by
others. Either way, the commitment is to have the goal completed, and
all teams are expected to commit the necessary resources to ensure
that it is finished.

All project teams are expected to prioritize these goals above other
work.

If the project has already met the goal, skip to the "Completing
Goals" step.

If the goal does not apply to a project, the PTL should explain why
that is the case, instead of linking to planning artifacts.

Completing Goals
----------------

After a goal is completed, each PTL is responsible for updating the
storyboard task or etherpad used to track the goal progress for their project
to set the status to "Merged" and to add links to all completion artifacts,
before the final deadline of the goal.

If a goal is not completed, that information should be added, along
with any references needed to track when that work will be completed.

Champion or TC member needs to move the completed goal from
``/goals/selected/`` directory to ``/goals/completed/`` directory.

Goal Champion Responsibilities
------------------------------

The "goal champion" is responsible for guiding teams to implement a
goal, but is not responsible for doing the work themselves.

The champion is typically somewhat familiar with the technical issues
involved in a goal, at least enough to help teams find the information
they need. The champion does not need to be an expert with the tools
or libraries used for the goal, but some experience does help.

The champion is responsible for configuring StoryBoard to track
progress on their goal, and then ensuring that it is kept up to date
as work progresses.

The champion should check in with project teams regularly to ensure
they are able to make progress on the work and have not become stuck.

At the end of the release, there may be open tasks and these can remain open
in case someone comes along later and completes the task. As goal champion you
are not responsible for completing any incomplete tasks for which you are not
assigned, i.e. the project assigned to the task is responsible for completing
it. It is also encouraged to send a retrospective email to the
openstack-discuss mailing list with a summary of the goal including things
such as how many projects completed the goal, reasons behind some projects
that did not complete the goal, anything notable that came up during the goal
implementation phase, and next steps if there are any.

Goal Selection Schedule
=======================

To give enough time to projects and champion to implement each cycle
community-wide goals, TC has to make sure goals are selected before
the development cycle start.

Below schedule is for the next (say N+1) cycle goals preparation
during the current (say N) cycle timeframe.

+-------------------+-------------------------------------+-------------------------------------------------------+
| Time              |   Phase                             | Tasks                                                 |
+===================+=====================================+=======================================================+
|                   |                                     |                                                       |
|Before Summit &    | TC volunteer & `Identifying Goals`_ |- Identify the two TC volunteers to drive the process. |
|PTG of N release   |                                     |- Kick off the process to collect the goal ideas over  |
|                   |                                     |  ML etc.                                              |
|                   |                                     |                                                       |
+-------------------+-------------------------------------+-------------------------------------------------------+
|                   |                                     |                                                       |
|                   |                                     |- Find potential candidates for N+1 goals.             |
|At Summit & PTG    |                                     |- This can be new ideas or from backlog of potential   |
|of N release       | Find potential goals & Champion     |  goals.                                               |
|                   |                                     |- Call for Champions for goal candidates (mutiple      |
|                   |                                     |  champions are acceptable)                            |
|                   |                                     |- This can be done via ML, Forum and PTG sessions.     |
+-------------------+-------------------------------------+-------------------------------------------------------+
|                   |                                     |                                                       |
|                   |                                     |                                                       |
|                   |                                     |- TC volunteer to Report on required pre-work for all  |
|                   |                                     |  identified potentials goal candidates.               |
|Until Milestone-1  | Discussion                          |- Find volunteers for action taker on required         |
|of N release       |                                     |  pre-works                                            |
|                   |                                     |- TC need to review the report and the                 |
|                   |                                     |  vote for the readiness of goal.                      |
|                   |                                     |                                                       |
+-------------------+-------------------------------------+-------------------------------------------------------+
|Until Milestone-2  |                                     |                                                       |
|of N release       | `Defining Goals`_                   |                                                       |
|                   |                                     |                                                       |
+-------------------+-------------------------------------+-------------------------------------------------------+
|Until Milestone-3  |                                     |                                                       |
|of N release       | `Selecting goals`_                  |                                                       |
|                   |                                     |                                                       |
+-------------------+-------------------------------------+-------------------------------------------------------+
|Until N+1          |                                     |                                                       |
|development cycle  | Goal Implementation                 |- Champion & projects to start the goal implementation |
|start              |                                     |                                                       |
+-------------------+-------------------------------------+-------------------------------------------------------+

Community goals
===============

It's not required to define community goals every time. The TC can
decide to not set any actionable community-wide goal for a specific
release/time, leaving the projects to focus on whatever is most important
in their scope.

.. toctree::
   :maxdepth: 2

   selected/index
   proposed/index

.. toctree::
   :maxdepth: 3

   completed/index
