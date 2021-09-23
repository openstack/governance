======================================
 2021-09-23 Stable Core Team Process
======================================

During the past Shanghai PTG, the TC discussed the Stable Core team process,
there were some concerns which include:

* Projects can't get things done because of the stable policy
* The stable core team is overworked as it is.
* The OpenStack community isn't getting enough stable reviewers on teams.

The idea of removing or changing the stable policy was raised since most
consumers of OpenStack assume that releases will be stable and the stable tag
is barely used anymore.

Also, a much more conservative group of people are working on OpenStack;
hence, they have experience and are less likely to break things now.

Recently, during the TC Xena PTG, this issue was brought up again because the
Stable Maintenance Core Team is not as active as it used to be, so we are
wondering if  we still need a Stable Maintenance Core Team or if it should
become more of an advisory team.

Current Challenges
------------------
* A few of the team members still pop in and out.
* We still have Stable Core members in each project.
* There may be some teams that don't have any stable core team members.

Proposed Solution
-----------------
The proposed solution has two changes: 1) Enabling project teams to
manage their own stable core teams and 2) renaming the 'Extended Maintenance'
SIG to 'Stable Maintenance'.

The first change is required due to the Stable Support Team no longer
being active.  Without that team in place, the individual project teams
need to be enabled to manage their own stable core team and policies.
The stable core teams will be managed in the same way that the regular
core team is managed.  Project teams will also be empowered to
create/enforce polices that best meet the needs of that project.
The policies must continue to be consistent with the existing
stable polices and must also be documented for reference by the
project team.

The second change, renaming the 'Extended Maintenance' SIG to the
'Stable Maintenance' SIG is being done to make it clear that this
team is able to provide guidance on stable maintenance issues.
Previously, the team was named the 'Stable Support Team' so
making this name change is sensible and clarifies the fact that
the team is able to provide guidance on stable branch issues
when necessary.
