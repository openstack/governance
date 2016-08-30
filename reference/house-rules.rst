=============================================
 House rules for governance changes approval
=============================================

While most of the governance changes call for a formal discussion and
vote by the Technical Committee membership, we also have a number of
exceptions to that general rule, in order to speed up the processing
of smaller changes. This document lists those "house rules" for reference.

Typo fixes
----------

When the change fixes content that is obviously wrong (updates a PTL email
address, fixes a typo...) then the chair is allowed to directly approve them.

Code changes
------------

The `openstack/governance` repository also contains code to build and publish
pages on the governance.openstack.org website. For those we apply the normal
code review rules (with RollCall votes being considered +-2): change will be
approved once 2 `RollCall+1` (other than the change owner) are posted (and no
`RollCall-1`).

Delegated tags
--------------

Some tags are delegated to a specific team, like
:ref:`tag-stable:follows-policy`, :ref:`tag-release:cycle-with-intermediary`
or :ref:`tag-vulnerability:managed`. Those need to get approved by the
corresponding team PTL, and can be directly approved by the chair once this
approval is given.

Other project team updates
--------------------------

For other changes within an existing project team, like addition of a new git
repository or self-assertion of a tag, we use lazy consensus. If there is no
objection posted one week after the change is proposed (or a significant new
revision of the change is posted), then the change can be approved by the
chair.

One exception to this would be significant team mission statement changes,
which should be approved by a formal vote after an in-meeting discussion.

In corner cases where the change is time-sensitive (like a deliverable
reorganization which blocks a release request), the chair may fast-track the
change, but should report on that exception at the next TC meeting.

Goal Updates from PTLs
----------------------

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
by the entire TC, they should place it on the agenda for an upcoming
meeting and the change should not be approved until after the
discussion is completed.

Rolling back fast-tracked changes
---------------------------------

As a safety net, if any member disagrees with any change that was fast-tracked
under one of those house rules, that member can propose a revert of the
change. Such revert should be directly approved by the chair and the change
be put on the agenda of the next TC meeting for further discussion.
