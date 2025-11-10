=======================================================
Guidelines for OpenStack SIGs (Special Interest Groups)
=======================================================

Before we dive into more details, it is important to learn what a SIG is and
what the differences are to other work groups in OpenStack. Please check
`Comparison of Official Group Structures`_ for more detail.


SIGs lifecycle
==============

Before creating a SIG
---------------------

Before creating a SIG, you should check out the existing `SIGs`_ and see if
your goals could not be shared with an existing group.

If not, you should raise a thread on the openstack-discuss mailing-list about
creating a new SIG. That should allow you to raise visibility of the SIG,
get more feedback, refine the SIG scope, and recruit more volunteers.

Creating a SIG
--------------

To formally propose a SIG you'll need to propose a change to the
`SIG Governance`_ file. That change will be reviewed and approved by the
`OpenStack Technical Committee`_.

The change should include the chosen name for the SIG (a combination of
ASCII letters, `-` and space), the proposed SIG scope, the initial status
(usually "forming") and the name of the SIG chair(s). It's strongly
encouraged to have more than one chair in order to spread the load.

Particular attention should be paid to the SIG scope. Documenting down the
very reason for this SIG will help others who have similar interests to join
this group. It's important to learn why we need to form a SIG, where we need
this SIG, and what's the goal and responsibility of this SIG.

Here is an `example of a SIG creation request`_.

Keeping SIG status up to date
-----------------------------

Once the SIG is approved, it is important to keep its filing in
`SIG Governance`_  up to date. In particular, keeping the status, chairs,
and scope up to date.

SIG status may be:

forming
~~~~~~~

The SIG is still setting up. This status also applied to SIG which needs to
regroup.

active
~~~~~~

The SIG reaches out for discussion, have plans for current
cycle, host meetings or send messages about status out to the mailing-list
regularly.

advisory
~~~~~~~~

The SIG is not actively meeting or driving specific goals every cycle. SIG
members stay around for help, make sure everything stays working and
provide advice when needed.

The SIG will keep the owned repository or documents up to date and will accept
updates on-demand.

unknown
~~~~~~~

SIG status is unknown, the TC is currently working to update its status.

completed
~~~~~~~~~

This SIG's mission is considered completed and the SIG itself is retired.

archived
~~~~~~~~

This SIG is considered retired but didn't complete its mission.

Retiring a SIG
--------------

Inactive SIGs can be made "advisory" if SIG members are still available for
answering questions, or they can be retired.

Before retiring
~~~~~~~~~~~~~~~

Before considering to retire a SIG, you need to first provide discussion
in community to make sure it's common agreement to retire it. This should at
least include a mailing list. You can also consider to host an offical meeting
to make sure opinions are received and noted.
The next step is to take care of SIG resources. You need to make sure resources
maintained by this SIG can find new maintainer group. Resources mean
documentation, etherpads, Wiki pages, repositories, etc. Make sure these
resources can be found even after SIG is retired.
For repositories, you can consider to retire them (see
`Repository retirement`_ process) or move it under other group's maintenance.

For resources which are no longer needed (resources like IRC channels, meeting
schedule, etc.), you need to delete them at this stage.

Retire a mission completed SIG
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To retire a SIG which is considered mission completed. You need to propose a
change that moves its definition from `SIG Governance`_ to the
`Completed SIGs`_ file, changes the `status` field to `completed`, and changes
the `reason` field to provide explanation why the SIG is considered completed
and where we can found documentations or references (if any).


Retire an archived SIG
~~~~~~~~~~~~~~~~~~~~~~

Be careful when you consider retiring a SIG which didn't finish its mission.
You need to make sure discussions are made with clear agreement on retiring the
SIG, and resources are well maintained (See `Before retiring`_).
To retire a SIG which didn't finish it's mission, You need to propose a
change that moves its definition from `SIG Governance`_ to the
`Archived SIGs`_ file, changes the `status` field to `archived`, and changes
the `reason` field to provide proper explanation why we archive the SIG as not
completed and where we can find documentations or references (if any).

Best practices for running a SIG
================================

SIG chairs role
---------------

A chair is encouraged as a moderator for the following work:

* Organize meeting agenda and host meetings
* Organize polling
* Coordinate with SIG members to generate a schedule for possible upcoming
  events (Summit, PTG, etc.) if needed.
* Moderate SIG tasks and help to find and encourage action takers for each
  task.
* Welcome new members to join the SIG.

SIG communications
------------------

Due to SIG differences, each SIG might have its own way to communicate. The
only requirement is that the SIG communications are well documented, so that
interested parties can easily join. Here are a few suggestions:

Mailing List
~~~~~~~~~~~~

Asynchronous communication between SIG members happens on the
`OpenStack-discuss mailing-list`_, prefixing the subject with [$signame-sig]
where $signame matches the SIG’s name. SIG work output can, of course, be
posted to other mailing-lists as needed to reach other groups.

IRC
~~~

IRC is the preferred method of communication as it aligns with OpenStack
community best practices for inclusive, synchronous messaging.

If your SIG uses a specific IRC channel, Opendev provides a number of IRC bots
to assist with logging. You can read more about `IRC services`_ and see an
`example for adding status/meeting bot to channel`_.

IRC meetings
~~~~~~~~~~~~

If you run regular SIG meetings, you should consider to post the meeting
schedule for SIG. SIG members can decide the meeting schedule (frequency
and location) and make sure there will be moderator for each meeting.
Here's an `example for adding meeting schedule`_ to `meeting list`_.

.. note::
   Meeting location can be at SIG's IRC channel or other public places if
   more desired (Like K8s SIG uses Slack channel in K8s community for
   meeting). Make sure meeting location allows public access so everyone can
   join.

Post SIG news regularly
~~~~~~~~~~~~~~~~~~~~~~~

It's encouraged to provide updates for all who might be interested in
learning. This can be done through the mailing list, or instant messaging
channels. Keeping everyone informed of the SIG progress helps to attract new
members, and to make sure others know about the new changes.

Attend events
~~~~~~~~~~~~~

We encourage every SIG to participate to the Summit and PTG events if possible.
SIGs can have:

* PTG rooms for SIG in-person group discussions

* Forum sessions to get wider community feedback on issues within the SIG
  scope.

* Speaking slots are reserved for SIG update presentations at Summits. This
  is a great way to spread the word about a SIG and recruit new members.


SIG resources
-------------

Git repositories
~~~~~~~~~~~~~~~~

While SIGs do not produce software that is included in the regular OpenStack
release, SIGs can own git repositories, for example for documentation or add-on
software.

You can read more about `how to create a new git repository`_. In particular,
you will need to register this new repository in the `sigs-repos.yaml`_ file
(like in this `example for register a repository under SIG`_),
`add Gerrit permission`_ and `ask Infra team to create core team`_ for
Gerrit.

Doc repository
~~~~~~~~~~~~~~

A classic use case for a git repository in a SIG is to publish peer-reviewed
documentation. Using `Sphinx`_ and `Zuul jobs`_ it is easy to publish
documentation under `docs.openstack.org`_.

A good example of such a repository is `openstack/auto-scaling-sig`_, which
includes `Sphinx`_ configuration and `Zuul jobs`_ to publish the
`Auto-scaling SIG docs`_.

StoryBoard task tracker
~~~~~~~~~~~~~~~~~~~~~~~

If you use a git repository, you can use `StoryBoard`_ to track tasks in the
SIG. Adding `use_storyboard: true` to the repository definition in
`gerrit/projects.yaml`_ will automatically generate a corresponding project
in StoryBoard. Here is an `example for add config in gerrit/projects`_.


.. _Comparison of Official Group Structures: https://governance.openstack.org/tc/reference/comparison-of-official-group-structures.html
.. _SIGs: https://governance.openstack.org/sigs/
.. _SIG Governance: https://opendev.org/openstack/governance/src/branch/master/reference/sigs/sigs.yaml
.. _OpenStack Technical Committee: https://governance.openstack.org/tc/
.. _example of a SIG creation request: https://review.opendev.org/#/c/632252/
.. _OpenStack-discuss mailing-list: http://lists.openstack.org/cgi-bin/mailman/listinfo/openstack-discuss
.. _Repository retirement: ` https://docs.openstack.org/project-team-guide/repository.html#retiring-a-repository
.. _Completed SIGs: https://opendev.org/openstack/governance/src/branch/master/reference/sigs/completed-sigs.yaml
.. _Archived SIGs: https://opendev.org/openstack/governance/src/branch/master/reference/sigs/archived-sigs.yaml
.. _IRC services: https://docs.openstack.org/infra/system-config/irc.html
.. _example for adding status/meeting bot to channel: https://review.opendev.org/#/c/656796
.. _example for adding meeting schedule: https://review.opendev.org/#/c/656810/
.. _meeting list: http://eavesdrop.openstack.org/
.. _how to create a new git repository: https://docs.openstack.org/infra/manual/creators.html
.. _sigs-repos.yaml: https://opendev.org/openstack/governance/src/branch/master/reference/sigs-repos.yaml
.. _example for register a repository under SIG: https://review.opendev.org/#/c/637126
.. _add Gerrit permission: https://docs.openstack.org/infra/manual/creators.html#add-gerrit-permissions
.. _ask Infra team to create core team: https://docs.openstack.org/infra/manual/creators.html#update-the-gerrit-group-members
.. _Sphinx: https://www.sphinx-doc.org/
.. _Zuul jobs: https://zuul-ci.org/docs/zuul/index.html
.. _docs.openstack.org: https://docs.openstack.org/
.. _openstack/auto-scaling-sig: https://opendev.org/openstack/auto-scaling-sig/
.. _Auto-scaling SIG docs: https://docs.openstack.org/auto-scaling-sig/
.. _StoryBoard: https://storyboard.openstack.org/
.. _gerrit/projects.yaml: https://github.com/openstack/project-config/blob/master/gerrit/projects.yaml
.. _example for add config in gerrit/projects: https://review.opendev.org/#/c/637125/7/gerrit/projects.yaml
