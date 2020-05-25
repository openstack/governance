=============================================
 House rules for governance changes approval
=============================================

While most of the governance changes follow the rules described in the
:ref:`charter-motions-section` section (or :ref:`charter-amendment-section`
section) of the Charter and call for a formal discussion and vote by the
Technical Committee membership, we also have a number of exceptions to that
general rule, in order to speed up the processing of smaller changes. This
document lists those "house rules" for reference.

The goal of the TC is always to operate by consensus where possible. The best
decisions are always the ones where all TC members can commit to the outcome,
even if they voted against it. These guidelines and the ones in the charter are
designed to provide the chair with an objective standard for when they may
consider consensus to have been achieved. However, if it is clear to the chair
from other factors that consensus has not been achieved (for example because
there are multiple incompatible proposals with sufficient votes to merge), the
chair should use their discretion to keep debate open and seek rough consensus
by other means.

Typo fixes
----------

:Gerrit topic: ``typo-fix``

When the change fixes content that is obviously wrong (updates a PTL email
address, fixes a typo...) then any TC member (who is not the proposer) can
directly approve them.

Community-wide goal proposals
-----------------------------

:Gerrit topic: ``goal-proposal``

The `process for choosing community goals`_ has two stages relevant to Gerrit
changes: defining goal proposals and selecting goals for a cycle.  For changes
that propose a new goal, or that iterate on an existing proposal, apply the
normal code review rules (with RollCall votes being considered +-2): change will
be approved once 2 `RollCall+1` (other than the change owner) are posted (and no
`RollCall-1`). Any TC member (who is not the proposer) can approve them at this
point.

Selecting community wide goals for a cycle should be proposed as a single change
that moves selected goals from `goals/proposed/` to `goals/selected/`.  This way
the collective feasibility of the goals can be clearly evaluated.  Such a change
requires a formal-vote.

.. _`process for choosing community goals`: https://governance.openstack.org/tc/goals/index.html#process-details

Code changes
------------

:Gerrit topic: ``code-change``

The `openstack/governance` repository also contains code to build and publish
pages on the governance.openstack.org website. For those we apply the normal
code review rules (with RollCall votes being considered +-2): change will be
approved once 2 `RollCall+1` (other than the change owner) are posted (and no
`RollCall-1`). Any TC member (who is not the proposer) can approve them at this
point.

Documentation changes
---------------------

:Gerrit topic: ``documentation-change``

The `openstack/governance` repository also contains documentation
related to internal operations of the TC but that does not represent
formal policy. Changes to these documents, as well as minor updates to
policies to improve the document without changing the policy itself
(formatting, extra headings, wording changes that are not substantive,
etc.), follow the normal code review rules (with RollCall votes being
considered +-2): change will be approved once 2 `RollCall+1` (other
than the change owner) are posted (and no `RollCall-1`).

Election Results
----------------

:Gerrit topic: ``election-results``

The results of elections are documented in the `openstack/governance`
repository, but are not subject to "review" or "approval" by the TC,
other than to confirm that they accurately reflect the outcome of the
election. Patches to update those results for TC and PTL elections
should be reviewed and confirmed by the election officials, and then
approved and merged following the normal code review rules (with
RollCall votes being considered +-2): change will be approved once 2
`RollCall+1` (other than the change owner) are posted (and no
`RollCall-1`).

Delegated tags
--------------

:Gerrit topic: the name of the tag being applied (``stable:follows-policy``,
               ``vulnerability:managed``)

Some tags are delegated to a specific team, like
:ref:`tag-stable:follows-policy`
or :ref:`tag-vulnerability:managed`. Those need to get approved by the
corresponding team PTL, and can be directly approved by the chair once this
approval is given.

Delegated metadata
------------------

:Gerrit topic: ``release-management``

The ``release-management`` setting for a deliverable is delegated to
the PTL of the Release Management team. When proposed or approved by
the PTL, changes can be directly approved by the chair.

Other project team updates
--------------------------

:Gerrit topic: ``project-update``

This topic is used for other changes within an existing project team, like
addition of a new git repository, retirement or self-assertion of a tag.

If there is no objection posted after the addition or retirement of a project
is proposed (assuming the correct retirement process has been followed), then
the change can be approved by the chair if it has at least two 2 roll call
votes (which can include the vote of the chair and excludes the change owner)
and a code review vote from the PTL of the project (or their delegate).
If the change is from the PTL or their delegate, this will count as an
acknowledgment code review vote.

One exception to this would be significant team mission statement changes,
which should be approved by a formal vote after discussion on the mailing list
or the gerrit change.

If a technical committee member disagrees with the addition or retirement of a
project, they can propose a revert which would then be discussed by our usual
``formal-vote`` rules.

Goal Updates from PTLs
----------------------

:Gerrit topic: ``goal-update``

PTLs will acknowledge community-wide goals at the start of each cycle
by providing links to artifacts for tracking the work, or an
explanation of why work is not going to be done. They will also
provide references to completion artifacts at the end of each cycle
for goals where work was needed. These patches should be reviewed by
TC members for completeness and clarity (is enough information
provided for interested parties to track the work, or is the
justification for not doing work clear enough).

The patches to add team acknowledgments, planning artifacts, and
completion artifacts to the goal document do not need to go through
the formal vote process, and so lazy consensus rules will be used. If
there is no objection posted one week after the most recent version of
a change is proposed, then the change can be approved by the chair.

If a TC member feels that one of these responses needs to be discussed
by the entire TC, they should bring it up on the mailing list and the change
should not be approved until after the discussion is completed.

Appointing PTLs
---------------

In a resolution regarding :ref:`leaderless programs`, the TC was granted
authority to appoint a Project Team Lead to any official project where the
`election`_ process failed to produce a leader. When this happens,
``reference/projects.yaml`` in the ``governance`` repository should be updated
to indicate the new PTL and their appointment by adding their name and contact
details and updating an ``appointed`` key with the cycle during which they will
be the PTL. If the ``appointed`` key is already present, add the cycle to the
list. If the key is not present, add it and set the cycle as a single member of
a list. This format is used for two reasons: to track all the cycles for which
there has been an appointment and to require a comprehensible change for review
by the TC. The ``appointed`` key should only be changed when the PTL was not
chosen by the election process.

These changes are subject to the standard review and approval guidelines.

Rolling back fast-tracked changes
---------------------------------

As a safety net, if any member disagrees with any change that was fast-tracked
under one of those house rules, that member can propose a revert of the
change. Such revert should be directly approved by any TC member (who is not
the proposer) and the change be discussed on the mailing list or on the
re-proposed change in gerrit.

Voting on Changes in openstack/governance
-----------------------------------------

TC member should use their RollCall-Vote permissions on all
patches. Code-Review votes are ignored for the purposes of tallying
votes, regardless of the content of the patch.

In the course of evaluating alternatives for complex proposals, we
often ask one TC member to write several patches that might be
mutually exclusive so that the committee can compare them and select
one by voting on them independently. Because of this, we need to
ensure that it is clear which patch the author of the patches prefers,
and so we usually ask all TC members to cast a vote on all patches,
even those they write.

.. _election: https://docs.openstack.org/project-team-guide/open-community.html#technical-committee-and-ptl-elections
