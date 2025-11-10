===============================================
 OpenStack Testing and Collaboration Tools SIG
===============================================

The Testing and Collaboration Tools (TaCT) SIG maintains, in
cooperation with the OpenDev project, the tooling and infrastructure
needed to support the development process and testing of the
OpenStack project.

Contact
-------

* #openstack-infra channel on the OFTC IRC network
  (`logs <http://eavesdrop.openstack.org/irclogs/%23openstack-infra/>`_)
* openstack-discuss@lists.openstack.org mailing list with ``[tact-sig]``
  in the subject line
  (`subscribe <http://lists.openstack.org/cgi-bin/mailman/listinfo/openstack-discuss>`_,
  `archives <http://lists.openstack.org/pipermail/openstack-discuss/>`_)

Participants
------------

The TaCT SIG consists of many former Infra team collaborators:
people who review OpenStack job configuration changes, people who
dig into problems with test frameworks to unblock the integrated
gate queue, people who figure out strange Python packaging related
issues, people who help work out lapsed control of Launchpad admin
groups... also, the person selected by the TC to serve as
OpenStack's representative on the OpenDev Advisory Council is
expected to be heavily involved. Many of these activities are
closely related to work the Quality Assurance team is doing, so
folks who are active in QA participate in this SIG as well.

History
-------

The OpenStack Infrastructure team, and the CI team before it,
traditionally existed to care for the continuous integration and
collaboration infrastructure on which the OpenStack community
relies. With the rise of the `OpenDev Collaboratory
<https://opendev.org/>`_ as a distinct effort outside of (but still
primarily in service of) OpenStack, the majority of the team's
former systems administration activities were no longer occurring
under the authority of OpenStack. Most of the software and
configuration management repositories previously in the care of the
Infra team were also no longer official OpenStack deliverables, as
they became part of OpenDev as well (and their biggest development
effort, `Zuul+Nodepool <https://zuul-ci.org/>`_, was already spun
out as an independent Open Infrastructure Project even earlier
still).

With these responsibilities moved elsewhere, the existence of a
formal team was less of a necessity. What remained was a need to
support OpenStack's project-specific testing and collaboration
tooling and services, primarily job configuration and other things
which shouldn't currently be generalized into components of the
OpenDev Collaboratory. To this end, a Testing and Collaboration
Tools (TaCT) SIG was created to serve the role previously occupied
by the OpenStack Infrastructure team.

Naming
------

The choice to rename was, in large part, because the term
"infrastructure" perpetually confused newcomers to the community,
and the SIG's formation was an opportunity to use something less
overloaded.

OpenSearch
----------

This service collects CI job results in one place, so the developer
will be able to filter them by time or other criteria, see simple
visualization for most common errors etc.

To check the OpenSearch service, you need to login with credentials
that are described below:

* url: https://opensearch.logs.openstack.org/_dashboards/app/discover?security_tenant=global
* username: `openstack`
* password: `openstack`
* tenant: `global` (if prompted)
