===========================
 TC Chair Responsibilities
===========================

.. note::

   This document is maintained as a simple text file, outside of the
   published governance document, because it is meant to be used for
   shared notes rather than as an official "guide to being TC chair".

General
=======

* Keep the Board informed of important decisions

  * email the board chair and secretary with brief summaries of
    decisions, linking to the public discussion (e.g., resuming
    meetings, election outcome, etc.)

* Keep the TC informed of important Board actions

  * attend board meetings when possible
  * follow board discussions on the mailing list(s)
  * report useful information back to the TC

* Manage formal TC meetings

  * maintain the agenda in the wiki
    https://wiki.openstack.org/wiki/Meetings/TechnicalCommittee

* Manage the initiative tracker

  * https://wiki.openstack.org/wiki/Technical_Committee_Tracker

* Review proposals to the openstack/governance repo (see below)
* Coordinate the agenda for joint leadership meetings with the board (see below)
* Send weekly update emails to openstack-dev (see below)

Each Cycle
==========

* See "Around TC elections"
* Ensure that the TC has a representative on the meta SIG team, to
  work with the UC to manage SIGs.
* Ensure that 2 TC members are signed up to manage the goal selection
  process for the next cycle.
* Ensure the next release naming is started
* Ensure PTI update is done

Around TC elections
===================

During the election period all current TC members continue to serve,
even if their term is up and they are not running again. Committee
membership changes when the election results are published.

When the election results are available, the outgoing chair should:

* welcome new and returning members
* update the tech-committee group in gerrit:
  https://review.opendev.org/#/admin/groups/205,members to remove
  members who should no longer be included and add new members
* encourage all TC members to vote on the patch prepared by the
  election officials with the new roster
* encourage all TC members to include the "[tc]" topic in their filter
  list for the openstack-discuss mailing list
* propose a patch to remove current chair and vice chair
* propose a patch to remove liaisons assigned to previous members
  (``python ./tools/assign_liaisons.py --remove-all``)

After the election results are confirmed, the outgoing chair should:

* start the chair selection process by encouraging TC members to
  consider serving as chair by proposing a patch to the member list to
  add "chair" status next to their name
* monitor and coordinate the discussion and selection of the new
  chair, including establishing a CIVS poll if there are multiple
  candidates
* after a chair is selected, ensure they appear in the
  tech-committee-chair group in gerrit:
  https://review.opendev.org/#/admin/groups/206,members
* the outgoing chair should notify the board chair and secretary of
  the new TC membership and chair
* the outgoing chair should notify the community of the new chair

After the chair status is confirmed, the incoming chair should:

* start the liaison assignment process (see below)
* propose a patch to appoint a vice chair

Project Team Liaisons
=====================

Each term of the TC we designate 2 members to be liaisons to each
project team


* encourage TC members to volunteer to act as liaisons for the project
  teams they want (set a deadline, ~1 week)
* Run ``python ./tools/assign_liaisons.py`` to randomly assign the remaining
  members.

Governance Repo Patches
=======================

Different changes to openstack/governance use different voting
rules. The chair is responsible for setting the topic for each change
to the right value, and monitoring reviews so we know when it is OK to
approve them or when they need to be rejected.

https://governance.openstack.org/tc/reference/charter.html#motions and
https://governance.openstack.org/tc/reference/house-rules.html cover
the voting rules

Running "tox -e check-review-status" builds a report to show the
current status of each patch.

Keep in mind that even patches that are technically ready for approval
may need to be held if there is strong minority dissent or someone key
to the discussion hasn't had a chance to participate.

Remind TC members to review patches that are lingering without review.

Joint Leadership Meetings
=========================

The TC, User Committee, Board of Directors, and leaders of other
Foundation projects meet at the Summit to discuss topics of interest
to the entire group.

Work with the Chair of the Board to build the agenda for the meeting,
using input from the TC about topics that we want/need to discuss.

Weekly Update Emails
====================

We use weekly email summaries of TC activity as a way to communicate
with the rest of the community more easily. These are especially
important for folks who do not have time to follow all of the
discussions directly.

The summary should include:

* updates about ongoing discussions, including links to mailing list
  threads, IRC logs, and reviews
* a list of the top 1-2 of things TC members should be focusing on for
  the next week, such as reviews or mailing list threads

Foundation Annual Report
========================

Near the end of each calendar year the OpenStack Foundation prepares
an annual report. The TC and UC are responsible for contributing a
status update for the OpenStack project and community. The Foundation
staff will contact the TC chair, who should either write the report or
ensure that it is written.

See
https://www.openstack.org/assets/reports/OpenStack-AnnualReport2017.pdf
for one example report and
https://etherpad.openstack.org/p/openstack-2018-annual-report for the
working notes for the 2018 report.

Upstream Investment Opportunities
=================================

https://governance.openstack.org/tc/reference/upstream-investment-opportunities/index.html

Toward the end of each calendar year, invite sponsors of the current year's
Upstream Investement Opportunities to repropose any relevant ones for the
following year. Solicit new entries on the mailing list.

At the beginning of the new year, switch the index to point at the directory
for the new year. (If no business cases have been approved yet, seed it with a
symlink to the template - this can be removed once there are entries in the
list.)
