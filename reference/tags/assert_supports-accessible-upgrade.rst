..
  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-assert:supports-accessible-upgrade`:

==================================
assert:supports-accessible-upgrade
==================================

This tag is part of the assert category of tags, which are assertions made by
the project team themselves about the maturity of their deliverables.

The ``assert:supports-accessible-upgrade`` tag asserts that in addition to a
deliverable supporting basic :ref:`upgrade capabilities
<tag-assert:supports-upgrade>`, it does so *without disrupting the
accessibility of controlled resources.*.

Application to current deliverables
===================================

.. tagged-projects:: assert:supports-accessible-upgrade


Rationale
=========

Many OpenStack services control and manage compute, networking and data storage
resources for end users. Operators need to know which services support an
upgrade process that maintains end user accessibility to controlled resources
during the upgrade process.

Requirements
============

* The deliverable is a software component of an OpenStack cloud
  (openstack, openstack-operations on the map) delivering a long-lived
  service with an API.

* The deliverable has already successfully asserted the
  :ref:`tag-assert:supports-upgrade` tag. All the requirements for that tag are
  requirements for this tag, and assertion that tag is a requirement to assert
  this tag.

* In addition to the plan required by the :ref:`tag-assert:supports-upgrade`
  tag, which allows for upgrades to disrupt end user accessibility of
  controlled resources, this tag requires services to eliminate any abnormal
  disruption of accessibility to controlled resources during the upgrade
  process when using at least one documented configuration. For example,
  upgrades should not take managed resources offline or otherwise make them
  inaccessible. Conversely, configurations that may result in
  abnormal disruption, and any limitations of the upgrade process that may
  affect accessibility, must be explicitly documented as such.

* In addition to the full stack integration testing required by the
  :ref:`tag-assert:supports-upgrade` tag, the accessibility of controlled
  resources should be maintained throughout the upgrade process. In order to
  assert this tag, services should prevent regression by implementing a gate
  job wherein accessibility of a controlled resource is validated throughout
  the upgrade process.
