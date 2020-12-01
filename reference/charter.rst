=======================================
 OpenStack Technical Committee Charter
=======================================

Mission
=======

The Technical Committee ("TC") is tasked with providing the technical
leadership for OpenStack as a whole (all official projects, as defined below).
It enforces OpenStack ideals (Openness, Transparency, Commonality, Integration,
Quality...), decides on issues affecting multiple projects, forms an ultimate
appeals board for technical decisions, and generally has technical oversight
over all of OpenStack.

OpenStack Project Teams
=======================

OpenStack "Project Teams" are groups of people dedicated to the completion of
the OpenStack project mission, which is ''to produce a ubiquitous Open Source
Cloud Computing platform that is easy to use, simple to implement,
interoperable between deployments, works well at all scales, and meets
the needs of users and operators of both public and private clouds.''
Project Teams may create any code repository and produce any deliverable they
deem necessary to achieve their goals.

The work of project teams is performed under the oversight of the TC.
Contributing to one of their associated code repositories grants you ATC status
(see below). The TC has ultimate authority over which project teams are
designated as official OpenStack projects. The projects are listed in
:ref:`projects`.

Project Team Leads
==================

Project Team Leads ("PTLs") manage day-to-day operations, drive the team goals
and resolve technical disputes within their team. Each team
should be self-managing by the contributors, and all disputes should be
resolved through active debate and discussion by the community itself. However
if a given debate cannot be clearly resolved, the PTL can decide the outcome.
Although the TC is generally not involved in team-internal decisions, it
still has oversight over team decisions, especially when they
affect other teams or go contrary to general OpenStack goals.

TC Members
==========

The TC is composed of directly-elected members. It is partially renewed
using elections every 6 months. All TC members must be OpenStack Foundation
individual members. You can cumulate any other role, including Foundation
Director, with a TC seat.

TC Chair
========

After each election, the TC proposes one of its members to act as the TC chair.
In case of multiple candidates, it may use a single-winner election method to
decide the result (see below). The Board of Directors has the authority to
approve the TC chair and shall approve the proposition, unless otherwise
justified by its bylaws. The TC chair is responsible for making sure meetings
are held according to the rules described below, and for communicating the
decisions taken during those meetings to the Board of Directors and the
OpenStack community at large. It may be revoked under the conditions described
in the Foundation bylaws.

The elected TC chair will seek another TC member to volunteer to serve
as vice chair until the next chair election is held. The chair may delegate some regular
duties to the vice chair. In addition to any delegated tasks, the vice
chair is responsible for being ready to step in and fulfill the
responsibilities of the TC chair when the elected chair is not
available.

The current TC chair is in charge of the next TC chair election, and
stays in charge of TC chair duties until the next TC chair is elected.

Meeting
=======

The community should not wait for a formal meeting to raise issues or
bring questions to the Technical Committee (see
:doc:`/resolutions/superseded/20170425-drop-tc-weekly-meetings`). In most cases,
asynchronous communication via email or gerrit is preferred over
meetings. If a topic will require significant discussion or to need
input from members of the community other than the committee, start a
mailing list discussion on ``openstack-dev at lists.openstack.org``
and use the subject tag ``[tc]`` to bring it to the attention of
Technical Committee members.

`TC status meetings <http://eavesdrop.openstack.org/#Technical_Committee_Meeting>`__
are public and held monthly in the
``#openstack-tc`` channel on the freenode IRC network. The meeting
time is decided among TC members after each election. The TC maintains
an open list of candidate topics for the agenda on `the wiki
<https://wiki.openstack.org/wiki/Meetings/TechnicalCommittee>`__. Anyone
may add items to the list, and the chair or vice chair will set and
publicize the agenda before each meeting.

For a meeting to be actually held, at least half of the members need
to be present (rounded up: in a 13-member committee that means a
minimum of 7 people present). Non-members affected by a given
discussion are strongly encouraged to participate in the meeting and
voice their opinion, though only TC members can ultimately cast a
vote.

.. _charter-motions-section:

Motions
=======

Motions presented before the TC should be discussed publicly to give a chance to
the wider community to express their opinion. Motions should therefore be
announced on the development mailing list and posted to Gerrit for review for a
minimum of 7 calendar days.

TC members can vote positively, negatively, or abstain (using the
"RollCall-Vote" in Gerrit). Decisions need more positive votes than negative
votes (ties mean the motion is rejected), and a minimum of positive votes of at
least one third of the total number of TC members (rounded up: in a 13-member
committee that means a minimum of 5 approvers).

Patches with motions should use the gerrit topic tag ``formal-vote``.

Election for PTL seats
======================

PTL seats are completely renewed every development cycle. A separate election
is run for each project team. These elections are collectively held no later
than 3 weeks prior to each cycle final release date (on or before 'R-3' week)
and should be held open for no less than four business days.

If a PTL seat is vacated before the end of the cycle for which the individual
was elected, the TC will appoint a new PTL, in consultation with the outgoing
PTL and any interested candidates, following the process for leaderless project
teams (see
:doc:`/resolutions/20141128-elections-process-for-leaderless-programs`). An
email must be sent to the ``openstack-discuss at lists.openstack.org`` mailing
list announcing the change in leadership. A patch must also be submitted to the
:repo:`openstack/governance` repository updating the project's
PTL information in ``projects.yaml``, which must be approved by the TC in order
for the appointed candidate to officially assume PTL responsibilities.

Any exception to PTL election schedule needs to be recorded in
:doc:`Election Exceptions </reference/election-exceptions>`

Voters for PTL seats ("APC")
============================

Voters for a given project's PTL election are the Active Project Contributors
("APC"), which are a subset of the Foundation Individual Members. Individual
Members who committed a change to a repository of a project over the last two
6-month release cycles are considered APC for that project team.

Candidates for PTL seats
========================

Any APC can propose their candidacy for the corresponding project PTL election.
Sitting PTLs are eligible to run for re-election each cycle, provided they
continue to meet the criteria.

Election for TC seats
=====================

The TC seats are partially renewed twice a year using staggered elections.
Members are elected for a term that expires at the conclusion of the second
scheduled election after the start of their term or after 14 months, whichever
is shorter. For this election we'll use a multiple-winner election system
see below). The election is held no earlier than 6 weeks and no later
than 4 weeks prior to each cycle final release date (between 'R-6' and 'R-4'
week), with elections held open for no less than four business days.

If required, TC and PTL elections can be held as combined election.

If a seat on the TC is vacated before the end of the term for which
the member was elected, the TC will select a replacement to serve out
the remainder of the term. The mechanism for selecting the replacement
depends on when the seat is vacated relative to the beginning of the
candidacy period for the next scheduled TC election. Selected
candidates must meet all other constraints for membership in the TC.

* If the vacancy opens less than four weeks before the candidacy
  period for the next scheduled TC election begins, and the seat
  vacated would have been contested in the upcoming election anyway,
  then the seat will remain open until the election and filled by the
  normal election process.
* If the vacancy opens less than four weeks before the candidacy
  period for the next scheduled TC election begins and the seat would
  not have been contested in the upcoming election, the candidates who
  do not win seats in the election will be consulted in the order they
  appear in the results until a candidate who is capable of serving
  agrees to serve out the partial term.
* If the vacancy opens with more than four weeks until the candidacy
  period for the next scheduled TC election begins, regardless of
  whether the vacated seat would have been contested in the next
  election, the candidates who did not win seats in the most recent
  previous TC election will be consulted in the order they appear in
  the results until a candidate who is capable of serving agrees to
  serve out the partial term.
* If there is no candidate available to fill the vacancy as per above
  mentioned criteria (either no extra candidate from election results
  or none of the candidates who do not win in previous elections accept
  the vacant TC partial term), then special election is held to fill the
  vacancy.

Any exception to TC election schedule needs to be recorded in
:doc:`Election Exceptions </reference/election-exceptions>`

.. _atc:

Voters for TC seats ("ATC")
===========================

The TC seats are elected by the Active Technical Contributors ("ATC"), which
are a subset of the Foundation Individual Members. Individual Members who
committed a change to a repository under any of the official OpenStack
Project Teams (as defined in :ref:`projects`) over the last two
6-month release cycles are automatically considered ATC. Specific contributors
who did not have a change recently accepted in one of the OpenStack projects
but nevertheless feel their contribution to the OpenStack project is technical
in nature (bug triaging not tracked in Gerrit, for example) can exceptionally
apply for ATC either by sending an email to the TC chair or by being nominated
by an existing ATC via email to the TC chair. Final approval on the exception is
decided by the TC itself, and is valid one year (two elections).

Candidates for TC seats
=======================

Any Foundation individual member can propose their candidacy for an
available, directly-elected TC seat. `Appendix 4 of the Foundation
Bylaws
<http://www.openstack.org/legal/technical-committee-member-policy/>`__
describe eligibility requirements and membership constraints for the
Technical Committee.

Number of seats to elect
========================

The Q3 2019 elections elected 6 seats, for a total of 13 members for the
Q3-Q4 2019 TC membership. Over 2020 the number of TC seats will be
gradually reduced to 9 members, with the following number of seats to elect:

- Q1 2020 elections: 5 seats (out of 7 incumbents): 11 members total
- Q3 2020 elections: 4 seats (out of 6 incumbents): 9 members total

Each year after 2020, the Q1 election should renew 5 seats, and the Q3 election
should renew 4 seats.

Election systems
================

For single-winner elections, a Condorcet system shall be used.

For multiple-winner elections, a Condorcet or a STV system should be used.

.. _charter-amendment-section:

Amendment
=========

Amendments to this Technical Committee charter shall be proposed in a special
motion, which needs to be approved by the affirmative vote of at least
two-thirds of the total number of TC members (rounded up: in a 13-member
committee that means a minimum of 9 approvers).

Patches with charter amendments should use the gerrit topic tag
``charter-change``.
