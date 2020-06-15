=================================================================
 Guidelines for dropping project teams from OpenStack governance
=================================================================

Dropping project teams is hard. There is no reason to remove low-activity
but functional teams. And there are teams that cannot be dropped, even if
dysfunctional. Here is a set of guidelines to help with that process.

Triggers
========

Triggers are events which may trigger an inquiry on the opportunity of
dropping a specific project team. They are generally a sign that the team
is struggling to continue to be part of the OpenStack release cycle
requirements.

- No PTL candidate during a PTL renewal

  This is generally a signal that there aren't enough people maintaining
  the project, or at least nobody willing to engage to be the default
  contact point and ambassador for a project. Alternatively, it may signal
  that the team is out of touch with the mailing-list and the release cycle
  and misses the window for self-nomination.

- Missing RC1 signoff or triggering forced releases

  The release management team expects some confirmation from the PTL or
  their release liaison at critical points in the release cycle. In case
  such signoffs are not provided, the release management team forces
  releases, at the risk of producing non-functional deliverables. This is
  obviously not sustainable and a good sign of a dysfunctional project team.

- Failure to communicate with community goal champions

  We set common goals at each cycle that bring more value if all project
  teams and OpenStack deliverables complete them. In some corner cases,
  teams are unable to complete the goal, and should communicate why to
  the goal champion(s). It is also expected that changes pushed by the
  goal champion(s) in support of the goal get reviewed in a reasonable
  timeframe. Failure to communicate at all with the goal champion(s)
  signals a dysfunctional team.

Criteria
========

Triggers alone are not a reason for removal. They just trigger an inquiry,
which may result in proposing their removal, or actively looking for new
volunteers to take over the project and/or adding the team to the
:doc:`upstream-investment-opportunities/index`.

The criteria to evaluate how "critical" a project is is based on:

- Usage

  If the user survey shows that the project is used in more than 5% of the
  deployments, it is necessary to continue the project to support those
  existing users that have invested in that technology, or at least provide
  a clear migration path to some alternative solution.

- Dependency

  If the project is a dependency of other projects, it should also be
  continued in order to support that other project team. For example, we
  could not ever consider dropping Glance, as Nova depends on it.
  Dependencies are documented in the OpenStack Map (osf/openstack-map
  repository).

Process
=======

Whenever a project generates one of the triggers, TC members may raise an
inquiry. If the project is deemed critical, the TC should raise a public
call for help and report to the Board to encourage more engagement in this
area. However if the project is not deemed critical, calling for help can
be counter-productive: it is very likely that a volunteer will step up to
"save" the project, when that volunteer's energy could be better spent on
more critical things. Therefore the TC should just start a thread about
removing that project team from governance and future releases of OpenStack.

If project's existing or new team shows interest to continue the development under:

- OpenStack governance then they need to update the TC on ML thread or IRC channel
  before retirement is approved.

- OpenDev, please refer to the `Continue Development`_ section.

Once retirement is approved, the Technical Committee's decision overrides any objections
of the project's contributors, so may involve deleting blocking votes on retirement changes.
Any interested team members may continue the development as non-official OpenStack project.

Continue Development
====================

With the OpenDev model, it is possible for the project to continue the development
under different namespace than `openstack/`. Refer to the resolution
:doc:`../resolutions/20190322-namespace-unofficial-projects`. for OpenStack namespace criteria.

Refer to `this document <https://docs.opendev.org/opendev/infra-manual/latest/creators.html>`_
for the complete process to create the project under OpenDev.

Re-becoming Official OpenStack Project
======================================

Becoming an official OpenStack project again requires following the same criteria
as :doc:`new-projects-requirements`.
