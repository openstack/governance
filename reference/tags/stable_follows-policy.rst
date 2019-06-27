..
  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-stable:follows-policy`:

=======================
 stable:follows-policy
=======================

Downstream users of OpenStack (users, but also packagers and lifecycle
management tools) need to know whether they can count on a source
of reliable bugfixes for a given component.

This tag indicates that a project team maintains stable branches for a given
deliverable, and that those stable branches are maintained following the common
`Stable branch policy`_, as defined by the Stable branch maintenance team.


Application to current deliverables
===================================

.. tagged-projects:: stable:follows-policy


Rationale
=========

All OpenStack project teams can create stable branches, with the
name of their choice. However, some of those branches do not follow the
`Stable branch policy`_: some approve backports that modify the behavior
of the software, some backport new features, some do not actively backport
significant bugfixes, some don't monitor proposed backports, or monitor
the CI system on their stable branches...

That creates confusion for packagers and deployers of our software, which
no longer know what to expect from a stable branch. Having stable branches
is no longer a guarantee of an up-to-date source of safe fixes.

To replace it, this tag is granted by the stable branch maintenance team only
to deliverables which have stable branches maintained following the common
`Stable branch policy`_. This lets downstream users easily determine which
projects adhere to the common rules, and expose what the common rules are to
a wider audience. As a side-effect, it encourages more project teams to
follow the policy.


Requirements
============

The tag can only be applied to software components of an OpenStack cloud
(openstack, openstack-operations on the map) and associated libraries
(openstack-libs). It is not meant be applied to SDKs (openstack-user)
or deployment tools (openstack-lifecyclemanagement).

Deliverables must follow the `Stable branch policy`_ in all currently active
stable branches.


.. _application-process:

Tag application process
=======================

Proposals to add or remove this tag must be reviewed by the
`Stable Branch Maintenance team`_ prior to final approval by
the Technical Committee.


Deprecation
===========

The ``stable:follows-policy`` tag may be removed from deliverables at any
time, when the Stable Branch Maintenance team considers that the deliverable
repeatedly violated the `Stable branch policy`_.

The ``stable:follows-policy`` tag is applicable to all currently active stable
branches. The removing the tag will also be applicable for all currently active
stable branches, meaning that projects that have removed the tag no longer
needs to follow `Stable branch policy`_ for any of the active stable branches.

Once the tag is removed, it can be re-obtained as per the
:ref:`reobtaining-tag` process.


.. _reobtaining-tag:

Re-obtaining the Tag
====================

Re-obtaining the ``stable:follows-policy`` tag back is always possible and can
be proposed with the agreement of `Stable Branch Maintenance team`_. Because
this tag is applicable per repository not per branch, any project not having
this tag can backports the unstable changes to any of the currently active
stable branches.
Re-obtaining the tag will follow the same process as obtaining tag from fresh,
meaning that all active stable branches follow `Stable branch policy`_. If the
branch that the tag was removed is still in active stable branches it means
project is not following the `Stable branch policy`_ in all active stable
branches.

As summary, the project can be applicable to re-obtain the tag once the branch
that the tag was removed from is EOL.

The tag re-obtain application process is the same as described in
:ref:`application-process`.

.. _Stable branch policy: https://docs.openstack.org/project-team-guide/stable-branches.html
.. _Stable Branch Maintenance team: https://review.opendev.org/#/admin/groups/530,members
