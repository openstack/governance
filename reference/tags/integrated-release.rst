::

  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

==================
integrated-release
==================

The integrated-release tag describes projects that were "integrated"
in the previous project structure.


Rationale
=========

Until the tag taxonomy is sufficiently developed to accurately describe
OpenStack projects, we need to hold on to what we currently have. Therefore,
to ensure a seamless transition between the previous project structure and
the new one, the "integrated release" concept is first imported in the
new tag-based project taxonomy as an initial, frozen tag. When we'll complete
the deconstruction of the single "integrated release" concept into a more
precise set of tags, the integrated-release tag will be discontinued.

For more information on this transition plan, see http://governance.openstack.org/resolutions/20141202-project-structure-reform-spec.html


Requirements
============

* Project must be an "integrated" project in the Kilo development cycle
  (under the old project structure rules)


Tag application process
=======================

This tag is frozen: only projects that were "integrated" at the beginning of
the Kilo development cycle are and will be granted the "integrated-release"
tag. There is therefore no need for an addition or removal process.


Deprecation
===========

This tag doesn't have a deprecation period. It is expected to simply be
removed when the deconstruction of the "integrated release" concept will
have been completed.


Application to current projects
===============================

The following code repositories would get the proposed tag. Those match the
contents of the Kilo release as decided at the end of the Juno cycle, and
take into account the recent Neutron advanced services code split:

* openstack/nova
* openstack/swift
* openstack/glance
* openstack/keystone
* openstack/horizon
* openstack/neutron
* openstack/neutron-fwaas
* openstack/neutron-lbaas
* openstack/neutron-vpnaas
* openstack/cinder
* openstack/ceilometer
* openstack/heat
* openstack/trove
* openstack/ironic
* openstack/sahara
