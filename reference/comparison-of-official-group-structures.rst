=======================================
Comparison of Official Group Structures
=======================================
This document aims to explain and compare the difference between a community
goal, project team, SIG (special interest group), working group, and a pop-up
team. The intention of this document is to provide a clear view between these
different groups and OpenStack-wide goal. We hope to answer questions such as,
what is the timing to create a SIG? and do I need a SIG or pop-up team to
drive my plan?

The OpenStack community is working to provide multiple different groups and
goal formats to help drive the community forward. To ensure you're able to
achieve your goals, it's important to know which format you need to drive your
mission.

If you are still unsure, even after you read through this document, please
raise your question on `Mailing List`_ or on IRC: #openstack-tc so
people might be able to help you.

.. image:: ./team-formats.png
   :width: 100%


Mission oriented: Long-term missions
====================================

There are currently three types of group for long-term missions: a SIG (special
interest group), a working group, and a project team.
Long-term mission has no time limitation.
The life cycle should be considered by whether or not the mission of the group
is completed. A long-term mission can be widely scoped. For example, the aim of
a long-term mission group can be to produce software, share use cases, build
documentations, to build cross-project test jobs, or overall communications.

The specific interest can be well-defined, well maintained, and easier to adopt
across OpenStack. For example, self-healing SIG is working on help with
general self-healing use cases, so whoever wishes to start using self-healing
functionality has the confidence to adopt it in their own environment.

Produces the software: Project teams
------------------------------------
:doc:`Project teams </reference/projects/index>` are responsible for producing
the OpenStack software up to release. They are either producing a specific set
of deliverables (like Compute service deliverables), or provide functions that
are integral to the production of the software (Release management, QA...).
Project teams are governed by TC and lead by individual project PTL (project
team leader). Project team is required when planning for release a deliverable
service. These projects maintain service repository, make sure on time release
for service, manage bug reports, and control the code quality (like
consistency review) are all part of the jobs for the project team.

OpenStack has a large number of existing project teams. if you would like to
create a new project team, you can reference
:doc:`new projects requirements </reference/new-projects-requirements>`
documentations for more details.

Special Interest Group (SIG)
----------------------------
`SIGs`_ (and `SIG wiki page`_) are governed by both TC and UC and lead by SIG
chairs, their function being to gather people (A user, developer, or operator)
who are interested in a specific mission to join discussion and driving actions
across community. You can also consider SIG as a bridge between developers,
operators and users.

SIGs are teams within the community where we collaborate to bring unified
discussions for all community members who share a common interest.
As examples, SIGs can be but are not limited to being a first stage
in the development of new projects, feature requests, standards
adoption, policy implementation, adjacent community work, and just
general discussions.

You can check for `process to create a SIG`_ for creat a new SIG.

Meta SIG
~~~~~~~~
This is just a SIG for `SIGs`_ so to speak. A SIG to discuss OpenStack SIGs
themselves, to encourage workgroups to become SIGs, accompany them along the
way, give them tools and processes to be efficient. More generally, this SIG
will discuss how to best close the loop between users and developers of
OpenStack. The SIG chair is assigned by both TC and UC.

Working Group (WG)
------------------
Working Group (WG) is governed by UC and lead by group leaders to help
users represent and achieve their needs through collaboration in the upstream
community. It's recommended to build a SIG instead of WG if you wish to make
sure the group is under governance of both UC and TC.

If your mission required deliverable services, you can either consider ask
project teams to help host those services or libraries, or you should consider
create a project team if that's more appropriate.

Mission oriented: Short-term missions
=====================================

Mission oriented means the group or goal is build up to serve a specific
mission. Once mission is completed, the group or goal should be consider as no
longer needed anymore.

There are two short-term mission formats, a pop-up team and a
:doc:`community goal </goals/index>`. These both require collaborative
work from multiple teams.

Pop-up team
-----------
Pop-up teams are lightweight structures aiming to provide quick start for short
term (time-limited) cross-project mission. A pop-up team can be supported by
the Technical Committee, and should be lead by (at least) two co-leads.

Mission of a pop-up team could transfer to a OpenStack-wide cycle goal.
For example, TC members can accept mission of a pop-up team as particular
cycle goal (at which point former members of the proposing pop-up team could
go on to become its goal champions).

You can reference create process of popup team in
:doc:`popup team guideline </reference/popup-teams>`
if you consider to create one.

.. note::
    All pop-up teams, SIGs and WGs shouldn't maintain any releasable
    deliverable. If deliverable repo is required, it should be maintained
    under a project team (please also note that SIGs/WGs/pop-up teams still
    can create and maintain their own code repositories). Like pop-up team
    `Image encryption`, requiring multiple project teams (Nova, Cinder, and
    Glance) to maintain and release their implementation in project
    repositories.

OpenStack-wide goal champion
----------------------------
A :doc:`community goal </goals/index>` (OpenStack-wide goal) is lead by goal
champions. It is used to achieve visible common changes, push for basic levels
of consistency and user experience, and efficiently improve certain areas where
technical debt payments have become too high across all OpenStack projects.
These are usually scoped by cycle.

If you have a time-limited mission to push to multiple teams but not to entire
community, you can consider for build a pop-up team to drive it. And if it's a
OpenStack-wide goal material but not yet mature enough to announce as a
OpenStack-wide goal for current or following cycle, to form a pop-up team and
drive it before it can be a community goal might be another way you can
consider.

If you have a mission which affects projects OpenStack-wide, then you're
free to propose it as a community goal. The Technical Committee will be
responsible for selecting :doc:`community goal </goals/index>` for each cycle.
The goal is not necessarily a cross-project feature or bug, it can also be any
OpenStack-wide mission (like :doc:`/goals/selected/train/pdf-doc-generation`
goal). Community goals are defined for a specific development cycle, because
we need to be specific on what we need each team to complete that mission and
how they can do it. That's why it's a short-term mission. But the follow up
mission might still be another goal for another cycle (like
:doc:`/goals/selected/stein/python3-first` goal can be consider as follow up
action from other python3 goals).

.. note::
    All OpenStack-wide goal shouldn't maintain any releasable
    deliverable. If deliverable repo is required, it should be maintained
    under a project team.

Governance
==========

Committees exist to help `govern`_ the community and provide leadership.
You can self-nominate for the below committees and become a committee member,
or provide feedback to committee. If you find it's hard or confusing to push
your mission into community, or you find the current structure can't fulfill
your goal, we encourage you to encounter with these committees that might be
able to help:

* Technical Committee (TC)
* User Committee (UC)
* Board of Directors (BoD)

OpenStack Foundation or Board-level committees and working groups
=================================================================

We have another level of `committees and working groups`_ like
`Edge Computing Group`_ which are directly driven by OpenStack Foundation
(OSF) or Board of directors.

Others
======
We have some other formate of team like `Election officials`_ helps on multiple
community functionality.

.. _Mailing List: http://lists.openstack.org/cgi-bin/mailman/listinfo/openstack-discuss
.. _govern: https://governance.openstack.org/
.. _SIGs: https://governance.openstack.org/sigs/
.. _committees and working groups: https://wiki.openstack.org/wiki/Governance/Foundation#Committees_.26_Working_Groups
.. _Edge Computing Group: https://wiki.openstack.org/wiki/Edge_Computing_Group
.. _Election officials: https://wiki.openstack.org/wiki/Election_Officiating_Guidelines
.. _SIG wiki page: https://wiki.openstack.org/wiki/OpenStack_SIGs
.. _process to create a SIG: https://governance.openstack.org/sigs/#process-to-create-a-sig
