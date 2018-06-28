.. _release-cycle-goals:

======================
 OpenStack-wide Goals
======================

The pages in this part of the governance documentation describe
OpenStack-wide goals for each release series.

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
addressing these concerns. This community input enables the TC to
select specific community-wide goals for all projects to achieve
during a development cycle. We need to consider the timing, cycle
length, priority, and feasibility of the goals selected.

We will brainstorm goals before and at each summit, using feedback
received from deployers, users, contributors, and PTLs. Those goals
will be discussed on the mailing list to collect feedback about
whether each goal is achievable and described completely. The TC will
use that input to come to consensus and make the final decisions for
OpenStack-wide goals for each cycle in time to allow planning and
other discussion at the PTG event at the start of the cycle.

Defining Goals
--------------

Goals are defined here in the governance documentation to ensure that
we establish a common understanding of the expectations being set.
Goal definitions should use the provided template so they are all
formatted consistently.  The goal definition does not take the place
of any blueprints, spec documents, or other planning tools used within
a project to track its work, but can be referenced from those
documents.

To define goals for a release cycle, a TC member should set up the
series directory in one patch, and then in follow-up patches TC
members can propose specific goals. This separates the discussion for
each goal onto its own review.

The actual goals shouldn't be completely new proposals (things no one
else in the community has seen before) because there will have been
discussion in the course of reaching consensus.

Tracking Goal Progress
----------------------

After goals are approved, the goal champions will create one story per
goal and one task per project per goal to track progress on
completion.

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

Each PTL is responsible for updating the storyboard task used to track the
goal progress for their project to set the status to "Progress" and to
include planning artifact links before the first milestone
deadline. The planning artifact is likely to be a link to a spec or
bug, and the completion artifact is likely to be a link to one or more
committed patches.

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
storyboard task used to track the goal progress for their project to
set the status to "Merged" and to add links to all completion
artifacts, before the final release date for the cycle.

If a goal is not completed, that information should be added, along
with any references needed to track when that work will be completed.

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

Release Cycles
==============

.. toctree::
   :glob:
   :maxdepth: 2

   */index
