====================================
Technical Committee Onboarding Guide
====================================

You're either here because you are interested in being on the TC one
day or because you were recently elected, either way: Thank You! We
appreciate the interest and your desire to volunteer to help
steer this big wonderful project!

Below is an outline of what you need to know about the duties of a
Technical Committee member.

After the Election
-------------------

Once the most recent TC election results are in, it is time to
start organizing the committee for the next cycle.

The first step for the pre-existing TC members is to approve the
patch prepared by the election officials to update the TC roster.
This looks something like this: https://review.opendev.org/#/c/680356/

After the patch is merged, the TC is officially seated and we need to select
a chair. If you are interested in being chair (see also ``CHAIR.rst`` in the
governance repository) and propose a patch on ``reference/members.yaml`` to
change your ``role:`` to ``chair``. These chair nomination patches should be
proposed within two weeks of the new members being seated.

After the chair is designated, candidates for vice chair should propose their
candidacies within the week after the chair is seated. The candidate needs to
propose a patch to add a vice-chair in ``reference/members.yaml``.

General Info
------------

Joining the TC can seem a little daunting, especially when you may already have
responsibilities in a project team, SIG, or group. A large part of being on the
TC is active communication to ensure each member is up-to-date on what's being
discussed, issues that may have arisen, and what's coming up.

Other Documents
~~~~~~~~~~~~~~~

In addition to this document, there are three others you should read as a new
TC member and reference throughout your term on the TC.

#. :doc:`Technical Committee Charter </reference/charter>`

#. :doc:`House Rules for openstack/governance repo </reference/house-rules>`

#. :doc:`Role of the TC </reference/role-of-the-tc>`

Communication
~~~~~~~~~~~~~

As a TC member, we have two primary ways of communicating.

#. Email:
   Take a moment to ensure that your email filters are configured
   to ensure you see any messages on the `mailing list
   <http://lists.openstack.org/cgi-bin/mailman/listinfo/openstack-discuss>`_
   with the '[tc]' topic tag.

#. IRC channel:
   Please also join the ``#openstack-tc`` channel on IRC, and set a notification
   for the string ``tc-members``. There is no requirement to do this, but we
   recommend also setting a notification for a string with your name. This
   is also helpful for mentions in other channels if you are the ``tc-liaison``
   to a specific project.

TC Project Liasions
~~~~~~~~~~~~~~~~~~~~

Each project under OpenStack governance is assigned two TC members to act as
liaisons.  These liaisons should act as a bridge between that project and the
TC, helping the project with governance concerns.  You will be assigned a list
of projects based on random selection if you don't set them yourself. You can
pick your preferred projects yourself after you are seated by submitting a
patch. This mechanical assignment of tc members as liaisons looks something
like this: https://review.opendev.org/#/c/680386/.

Once you have been assigned your projects, the first work item for new and returning
members is to talk to the projects for which you are a liaison. We recommend
introducing yourself to the PTL in an email or during a team meeting if you're
able to attend them, a greeting to the project team to ensure they know someone
to talk to, making sure the TC is an accessible community.

You can see the assigned list of projects per TC member in
:doc:`TC Liaisons </reference/tc-liaisons>`

TC Repos
~~~~~~~~~

While your main focus as a TC member is the governance repo, the complete list
of repos that are under the governance of the TC is listed below:

* :repo:`openstack/governance/raw/branch/master/reference/technical-committee-repos.yaml`.

* :repo:`openstack/governance/raw/branch/master/reference/user-committee-repos.yaml`.

The `TC review dashboard
<https://review.opendev.org/#/dashboard/?title=Technical+Committee+Inbox&foreach=project%3Aopenstack%2Fgovernance+is%3Aopen&My+proposals=owner%3Aself&Formal+Vote+Items+I+have+not+voted+on+yet=topic%3Aformal-vote+NOT+(+label%3ARollCall-Vote%2B1%2Cself+OR+label%3ARollCall-Vote-1%2Cself+)&Has+at+Least+One+Objection=(+label%3ARollCall-Vote%3C%3D-1+OR+label%3ACode-Review%3C%3D-1+)&Quickies=(+topic%3Atypo-fix+OR+topic%3Acode-change+OR+topic%3Adocumentation-change+OR+topic%3Aproject-update+)&Formal+Vote+Items=topic%3Aformal-vote&Goal+Items+I+Haven't+Voted+On=path%3A^goals%2F.*+NOT+(+label%3ARollCall-Vote%2B1%2Cself+OR+label%3ARollCall-Vote-1%2Cself+)&I+Haven't+Voted+on+this+Draft=NOT+(+label%3ARollCall-Vote%2B1%2Cself+OR+label%3ARollCall-Vote-1%2Cself+)&Everything=>`_
can help you stay on top of what changes need your vote.

Duties
-------

In general, being a member of the Technical Committee is as much work as you are
willing to dedicate time to it. That said, there are some 'bare-minimums' you
should be meeting.

Be Present on ML and IRC
~~~~~~~~~~~~~~~~~~~~~~~~

As discussed above, communication is incredibly important. As a team, you want
to make sure questions from the community in IRC and on the ML don't go
unanswered.

Meetings
~~~~~~~~

Attend the Technical Committee meetings (assuming your timezone allows). The
TC has meetings every Thursday in #openstack-tc; `check
Eavesdrop.
<http://eavesdrop.openstack.org/#Technical_Committee_Meeting>`_
To hold the meeting we must meet quorum, so it's important that you attend
as many as possible. If you have topics that should be discussed at the
meeting, they should be sent to the chair or vice-chair to be included
in the agenda. The agenda should also be publicized to the openstack-discuss
list to encourage community involvement.

Governance Core Duties
~~~~~~~~~~~~~~~~~~~~~~

Book time on your calendar for reviewing open patches in the TC Repos.
As a TC member, you are a primary maintainer (a core member in OpenStack terms)
of all the TC repos. Even if you have already done a review of the patch,
there might have been other progress that you should familiarize yourself
with and stay up to date on.

If you are interested, there are other repositories it might be good to keep
an eye on as well that are related to TC duties, like openstack/elections.


TC Interactions with Other Governing Bodies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Its encouraged that you attend Board of Directors meetings wherever possible.
There are a variety of topics that often come up that the TC should be weighing
in on. Sometimes there are face to face meetings as well where your attendance
is encouraged.

