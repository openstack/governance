==============================
Distributed Project Leadership
==============================

The default leadership model for an OpenStack project team is for a single
elected :doc:`Project Team Lead (PTL) <project-leadership>` to serve as the
team's point of accountability. As an alternative, project teams may opt in to
a "distributed leadership" model where there is no PTL and the responsibilities
normally held by the PTL are instead distributed to various named liaisons,
which may be held by one or multiple contributors.

This document describes the DPL model and how to opt in to it. Project teams
that use the default PTL-based model should refer to the
:doc:`Project Leadership <project-leadership>` document instead.

What the DPL Model Is
---------------------

The day-to-day responsibilities of the PTL are broken down into a set of named
liaison roles, which are distributed amongst one or more individuals. The
responsibilities not addressed by those roles (driving the team's goals,
resolving technical disputes) are trusted to the team as a whole. If
necessary, project teams can still contact the TC to resolve deadlocks.

.. _dpl-required-roles:

Required roles
~~~~~~~~~~~~~~

The project teams are expected to have at least the following required liaison
roles:

* **Release Liaison**: The release liaison is responsible for requesting
  releases for deliverables produced by the project team. In addition, release
  liaisons generally review requests for Feature Freeze Exception (FFE).

* **TaCT SIG Liaison**: Historically named the "infra Liaison", the Tact SIG
  liaison is responsible for the health of the CI jobs run in the OpenStack
  Zuul CI. In the event that there is an issue with those jobs, this liaison
  will be a point of contact for the `TaCT SIG`_. Also, a +1 from at least one
  TaCT Sig liaison will be required for changes in the :repo:`project-config
  repo <openstack/project-config>`.

* **Security Liaison**: The security liaison is the contact person to help
  assessing the impact of any security reported issues in the project team
  deliverables, coordinate the development of patches, review proposed patches,
  and propose any eventual backport(s).

* **TC Liaison**: The TC liaison is a TC members who will follow the project
  activities at regular intervals and make sure the DPL model is reset every
  cycle. A project team that is planning to adopt the DPL model can reach out
  to the TC to find the TC liaison for their project.

.. _dpl-additional-roles:

Additional recommended roles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Any other responsibilities of the PTL that are not addressed above are optional,
and are left to the project teams to determine.  The TC recommends project teams
opting in for distributed project leadership to assign people into the following
optional roles, to each project team's discretion:

* **Events Liaison**: An events liaison ensures that a project team has space
  reserved at a PTG or Summit that will be sufficient for the project team's
  meeting needs. The events liaison puts out an agenda for any of the team
  meetings, makes sure those meetings are organized and facilitated, and that
  the results are documented. This is a temporary role, lasting only during
  the preparation time for the event and it's duration. Due to the temporary
  aspect of this role, the liaison will not be recorded in governance, else it
  might quickly get outdated.

  At the beginning of the organisation of an event, the OpenStack Events teams
  will query on our openstack-discuss ML for participants ready to liaise for
  the event, for all the teams with distributed leadership. The project teams
  interested in being represented at the event can then opt-in to the event by
  assigning a liaison. The project teams are free to decide how and who will be
  assigned as the event liaison. The project teams not answering on the ML or
  not assigning a liaison on time will not have representation in the event.

* **Project Update/Onboarding Liaisons**: The project update liaison is
  responsible for giving the project update showcasing team's achievements for
  the cycle to the community. The "Project Onboarding" liaison is responsible
  for giving/facilitating onboarding sessions during events for its projects'
  community.  Similarly to the events liaison, those two roles are opt ins.

* **Meeting Facilitator**: The meeting facilitator chairs the project team's
  regular periodic meetings and maintains their agenda.

* **Bug Deputy**: The bug deputy ensures all incoming bugs are triaged.

* **RFE Coordinator**: The RFE coordinator makes sure that blueprint status
  and milestone targets are up to date, that RFEs are triaged and discussed
  before acceptance, and that the tracking LaunchPad or Storyboard items for
  RFEs are properly managed.

Liaison selection
~~~~~~~~~~~~~~~~~

The process by which each project team chooses these liaisons is left to the
discretion of the project teams, as long as it is public, open, and respectful
of the current TC guidelines.  The TC advocates the use of consensus decisions,
with polls or elections when consensus can not be reached.

DPL model & liaison duration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DPL liaisons are assigned for a single release cycle. The assigned TC liaison
will follow the project activities at regular intervals. Before the next cycle
PTL election nominations start, the TC liaison will reset the project team
leadership model to PTL. A project team needs to opt-in to the DPL model
again, explicitly before the next cycle PTL election nominations start. This
can be done by either of the following options:

* All current liaisons are recording their -1 vote against the change to reset
  the leadership model. Once all liaisons have recorded -1 vote, the TC will
  not reset the DPL model and will consider continuing the DPL model for the
  next cycle as well.
* If the DPL model has already been reset, a new change to readopt the DPL
  model needs to be proposed. This change requires +1 from all the people
  volunteering as liaisons.

Points of Concern
-----------------

There are a few places where the project teams that choose the distributed
leadership model will need to innovate and solve problems:

* Discoverability: It will make harder to know whom to contact for a project team.
* Distributed Consensus: With an increased number of people accountable for
  aspects of the project team, the potential for miscommunications increases.
* Unclear responsibilities: As a project team moves to the distributed leadership
  model, it will lose the single point of contact (SPoC). This SPoC was useful
  for coordination on community topics, like the follow up/implementation of
  community goals or an official answer on project teams's questions on the
  mailing lists, to name a few.
  As mentioned in the distributed consensus above, an increased number of people
  accountable for the project team leads to consensus challenges, and also
  to unclear responsibilities for the liaisons.
  This could lead to a blurry situation where no one is actually doing the work
  for the community, as they might have expected "someone else" to do it.
  The TC expects and trusts the project teams to continue working on their
  community duties, and encourage projects teams to actively communicate on the
  mailing lists on community efforts, to remove any eventual misunderstandings
  and misconceptions.
* Inclusion: Since some of the liaisons will not be explicitly written in code -
  like the events liaisons - the project team members will need to actively
  contact the OpenStack events team. This is different than our usual opt out,
  and is less inclusive than before.
* Minimum Viable: This document is intended to assert the minimum set of roles
  the TC would require to consider the project team to be active and
  functioning.  It is not an exhaustive list of possible roles.  For example, a
  project team might assign someone at the end of each cycle to write the cycle
  highlights.  These responsibilities could also be collectively handled by the
  project team, as needed or rotated at intervals.  Teams have the freedom to
  choose what works best for them.

Process for Opting In to Distributed Leadership
-----------------------------------------------

Project teams that would like to opt in to a distributed leadership role should
make sure this change has a relative degree of consensus within the project
team.  To make the request, a change should be pushed to ``projects.yaml`` in
the ``openstack/governance`` repository to change the ``leadership_type`` to
``distributed`` in the team's definition.  The minimum required liaisons will
also need to be filled-in, in the appropriate fields in the ``liaisons`` section
of the team.

This change to move to a distributed leadership model can only be accepted by
the TC when it will receive at least a +1 from the current PTL, and the future
liaisons.

Technical notes:

* The releases liaison will continue to be listed in the ``releases`` repository,
  to not impact the current delivery of the releases.

Once a project team has moved to the distributed leadership model, they can
revert to the PTL model by creating a change to ``projects.yaml`` to change
``leadership_type`` to ``ptl`` in the team's configuration. This change
should have at least a +1 from all the people currently serving as liaisons,
including the :repo:`openstack/governance/src/branch/master/reference/projects.yaml`
for the project team, which might not be in the ``governance`` repo.
It must also get a +1 from the future PTL, listed in the same change.

.. note::

   In every release cycle, The TC liaison will reset the DPL model & liaison (see
   `DPL model & liaison duration`_).

A project team may change their opt-in status only once a release cycle, to
ensure that the elections officials have clarity on which project teams need PTL
elections. All requests should be merged before the election nominations start
otherwise request will be postponed to the next cycle.

The distributed leadership model is only requested explicitly.  If a project
team has no candidate for PTL, the TC will still evaluate the future of the
team and its deliverables, with now an extra option
(on top of stopping the project or appointing a PTL):
convert the project to a distributed leadership with the help of the project
team members.

.. _TaCT SIG: https://governance.openstack.org/sigs/tact-sig.html
