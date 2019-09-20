===================================================
What's next? After the Technical Committee Election
===================================================

Once the most recent TC election results are in, it is time to
start organizing the committee for the next cycle.

The first step for the pre-existing TC members is to approve the
patch prepared by the election officials to update the TC roster.
This looks something like this: https://review.opendev.org/#/c/680356/

After the patch is merged, the TC is officially seated and we need to select
a chair. If you are interested in being chair (see also ``CHAIR.rst`` in the
governance repository) and propose a patch on ``reference/members.yaml`` to
change your ``role:`` to ``chair``.

After the chair is designated, contact the chair if you're interested at being vice-chair.
The chair proposes a patch to add a vice-chair in
``reference/members.yaml`` about one week after being selected for chair.

Tips for new members
~~~~~~~~~~~~~~~~~~~~

Joining the TC can seem a little daunting, especially when you may already have
responsibilities in a project team, SIG, or group. A large part of being on the TC is
active communication to ensure each member is up-to-date on what's being
discussed, issues that may have arisen, and what's coming up.

As a TC member, we have two primary ways of communicating. Take a moment to
ensure that your email filters are configured to ensure you see any messages on
the `mailing list
<http://lists.openstack.org/cgi-bin/mailman/listinfo/openstack-discuss>`_ with
the '[tc]' topic tag. Please also join the '#openstack-tc' channel on IRC, and
set a notification for the string 'tc-members'. There is no requirement to do
this, but we recommend also setting a notification for a string with your name.
This is helpful for mentions in other channels if you are the tc-liaison to a
specific project.

Each project under OpenStack governance is assigned two TC members to act as
liaisons.  These liaisons should act as a bridge between that project and the
TC, helping the project with governance concerns.  You will be assigned a list
of projects based on random selection.  It is best to introduce yourself to the
project members either in person at a Forum or PTG or at their regular IRC
meetings.  This mechanical assignment looks something like this:
https://review.opendev.org/#/c/680386/

Once you have been assigned your projects, the first work item for new and recurring
members is to talk to the projects you are liaison of. We recommend introducing yourself
to the PTL, a greeting to the project team to ensure they know someone to talk to,
making sure the TC is an accessible community.

The TC has meetings on the first Thursday of each month in #openstack-tc; `check
Eavesdrop for the current schedule
<http://eavesdrop.openstack.org/#Technical_Committee_Meeting>`_.  We hold office
hours at various times during the week on the #openstack-tc IRC channel, `see
Eavesdrop for the schedule of those as well
<http://eavesdrop.openstack.org/#Technical_Committee_Office_hours>`_.  For more
information, see our `wiki page
<https://wiki.openstack.org/wiki/Meetings/TechnicalCommittee>`_.

Familiarize yourself with the governance changes currently being discussed in
the `openstack/governance project
<https://review.opendev.org/#/q/status:open+project:openstack/governance>`_.
Make sure you are familiar with the `house rules
<https://governance.openstack.org/tc/reference/house-rules.html>`_ that govern
voting on governance changes.  The `TC review dashboard
<https://review.opendev.org/#/dashboard/?title=Technical+Committee+Inbox&foreach=project%3Aopenstack%2Fgovernance+is%3Aopen&My+proposals=owner%3Aself&Formal+Vote+Items+I+have+not+voted+on+yet=topic%3Aformal-vote+NOT+(+label%3ARollCall-Vote%2B1%2Cself+OR+label%3ARollCall-Vote-1%2Cself+)&Has+at+Least+One+Objection=(+label%3ARollCall-Vote%3C%3D-1+OR+label%3ACode-Review%3C%3D-1+)&Quickies=(+topic%3Atypo-fix+OR+topic%3Acode-change+OR+topic%3Adocumentation-change+OR+topic%3Aproject-update+)&Formal+Vote+Items=topic%3Aformal-vote&Goal+Items+I+Haven't+Voted+On=path%3A^goals%2F.*+NOT+(+label%3ARollCall-Vote%2B1%2Cself+OR+label%3ARollCall-Vote-1%2Cself+)&I+Haven't+Voted+on+this+Draft=NOT+(+label%3ARollCall-Vote%2B1%2Cself+OR+label%3ARollCall-Vote-1%2Cself+)&Everything=>`_
can help you stay on top of what changes need your vote.

If you have any questions about getting started with the TC, ping any of the existing
team members in the #openstack-tc channel.
