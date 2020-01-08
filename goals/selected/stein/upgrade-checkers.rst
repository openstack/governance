==========================
Support Pre Upgrade Checks
==========================

Providing assurances and useful feedback to deployers preparing to upgrade
services vastly improves the upgrade experience. One basic step that we can
make consistent across OpenStack projects is to provide "upgrade checks" that
can be run prior to upgrade that will help identify any known issues that would
result in that upgrade failing.

Each project would provide their specific checks for things like missing or
changed configuration options, incompatible object states, or other conditions
that could lead to failures upgrading that project. In general, anything that
should be documented today in the upgrade release notes would be a good
candidate for an upgrade checker to validate.

These checks should perform any upgrade validation that can be automated. There
may always be some things that need some subjective evaluation, but for those
things that can be automated to determine if there is an issue that could
impact upgrade success, a validation check should be created to automate it.

:Storyboard Board: https://storyboard.openstack.org/#!/board/107
:Storyboard Story: https://storyboard.openstack.org/#!/story/2003657

Champion
========

Matt Riedemann <mriedem.os@gmail.com> has volunteered to drive this goal.

Gerrit Topic
============

To facilitate tracking, commits related to this goal should use the
gerrit topic::

  upgrade-checkers

Completion Criteria
===================

In order for a project to call this goal complete it must provide a command in
the format::

    $PROJECT-status upgrade check

The command must:

#. Iterate through all defined checks
#. Provide a :ref:`summary list output<summary_list>` showing:

   * Check name
   * Result (Success or Failure)
   * Details

#. Return the following codes based on check results:

   * 0 - All checks passed
   * 1 - Warning that one or issues were found that require investigation
   * 2 - One or more checks found an issue that will cause upgrade to fail

#. Projects with the :ref:`tag-assert:supports-upgrade` tag must integrate
   their upgrade check command into their upgrade CI testing.

.. note:: This goal is primarily focused on the traditional stateful service
   projects like keystone, cinder, glance, etc. However, deployment projects
   would clearly benefit from integrating these checks into their install and
   upgrade routines but that is not part of this goal in Stein since some of
   the service project checks might not even be complete until the end of
   Stein and thus not consumable to deployment projects until the "T" release
   at the earliest.

.. _summary_list:

Summary List Output
-------------------

The ``$PROJECT-status upgrade check`` command output should be similar to the
following format::

    +----------------------------------------------------+
    | Upgrade Check Results                              |
    +----------------------------------------------------+
    | Check: Cells v2                                    |
    | Result: Success                                    |
    | Details: None                                      |
    +----------------------------------------------------+
    | Check: Placement API                               |
    | Result: Failure                                    |
    | Details: There is no placement-api endpoint in the |
    |          service catalog.                          |
    +----------------------------------------------------+

References
==========

The Nova project has already implemented a ``nova-status upgrade check``
command along with several checkers. The `command source
<https://opendev.org/openstack/nova/src/commit/a1f3a5946ab703225a74f8e85a068cb4fb20e2ff/nova/cmd/status.py>`__
may be useful as a reference.

The `original commit
<https://opendev.org/openstack/nova/commit/a1f3a5946ab703225a74f8e85a068cb4fb20e2ff>`__
adding the checker framework may also be useful.

The `Command Line Reference
<https://docs.openstack.org/nova/latest/cli/nova-status.html>`__ for the
``nova-status`` command provides a good description with some details on
the checks that are performed.

The command line is also used in the `grenade upgrade checks
<https://github.com/openstack-dev/grenade/blob/dc7f4a4ba5697d5a73a1e656d4a1717964324eab/projects/60_nova/upgrade.sh#L96>`__
for Nova.

Nova contributor reference for ``nova-status upgrade check``:
https://review.opendev.org/#/c/596902/

Current State / Anticipated Impact
==================================

Most projects today either have their own checklists or tools for checking for
upgrade issues, or more commonly, nothing at all. By providing a consistent
mechanism to discover known issues we can improve the upgrade process and the
deployers confidence and allow for further upgrade tooling to be created.
