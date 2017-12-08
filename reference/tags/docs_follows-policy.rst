::

  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-docs:follows-policy`:

===================
docs:follows-policy
===================

This tag indicates that a deliverable’s documentation set is prepared in
coordination with the OpenStack Documentation team, and follows their defined
practices and policies for review and verification. It does not indicate that
the documentation team has taken ownership of producing the documentation for
the deliverable.

Application to current deliverables
===================================

.. tagged-projects:: docs:follows-policy

Rationale
=========

At present, the documentation team is responsible for all documentation in the
openstack/openstack-manuals repo. Maintaining this documentation requires basic
knowledge of all of the projects covered by the guides. However, being able to
successfully maintain some of the more in-depth knowledge that is written in the
guides is out of scope for the technical writers to handle on their own.
Previously, the documentation team has worked alongside project
teams to collaborate and share knowledge to ensure that the manuals document
all necessary major bug fixes and enhancements. This approach no longer
ensures that the documentation is sufficiently verified by the teams each
release.

The "docs:follows-policy" tag indicates that project teams are
coordinating with the documentation team, so that contributions, bug reports,
and timely reviews happen over the course of each release cycle. Detailed
expectations are described in the doc-tag section of the Documentation
Contributors' Guide: https://review.openstack.org/453642 .

The documentation team recommends that project teams who maintain
project-specific guides inside of the openstack-manuals repository (such as,
nova, neutron, cinder, horizon, glance, and keystone), including teams
maintaining projects outside of the starter-kit set, and deployment projects,
apply for this tag. Having the tag indicates that the project teams commit
to provide accurate documentation every release. In these cases, the
documentation team will review the project team's guides, but won't
necessarily contribute significantly to ongoing maintenance.

Requirements
============

The structure outlined by the doc team in their policy
(https://review.openstack.org/453642) is to be loosely followed, dependent on
project circumstance.

For all teams:

1. The team must `designate a liaison <https://wiki.openstack.org/wiki/CrossProjectLiaisons#Documentation>`_
   to the documentation team.

For project teams with deliverables covered by guides that are maintained by the
documentation team:

1. The project team must provide summaries of new features, configuration changes,
   etc. that need to be reflected in the documentation.
2. The documentation liaison must follow the published review schedule, read the
   documentation, and open bugs appropriately, either providing information
   to the docs team on how to document these issues or submitting patches to fix them.

For project teams with deliverables covered by documentation that is not maintained
by the documentation team:

1. The project team must prepare their documentation using the standard tool set
   provided by the documentation team, and ensure the guides are published to
   docs.openstack.org.
2. The project team must prepare and update their documentation following
   the published review schedule, and coordinate with the documentation team
   to ensure that a review is performed.
3. The project team must actively manage their documentation, handling bug reports
   and publishing corrections as needed.
4. The project team must make the documentation team aware of any major changes to the guides
   that will impact the way the guides are published.

Tag application process
=======================

The tag will be applied for the first time for the Pike release.

Members of project teams who want the tag associated with their deliverables
should apply for it by adding it to the deliverables they want to cover.

The documentation team PTL must approve the tag to show that the documentation
team agrees that the relevant guides have been reviewed appropriately by the
review deadline for each cycle as indicated by this tag.

The tag is applied to deliverables in the governance repository. Each manual
for a deliverable covered by the tag will be annotated to indicate the level
of input or review from the documentation team so that users can easily
discover who is responsible for maintining the content.

Deprecation
===========

This tag will be removed from deliverables when the required coordination
and reviews are not performed for a cycle. Any existing documents annotated
as having been reviewed will not be affected. A project team can re-apply
to have the tag for the following cycle, after the relevant reviews are
performed.
