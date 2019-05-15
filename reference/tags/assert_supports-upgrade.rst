..
  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-assert:supports-upgrade`:

=======================
assert:supports-upgrade
=======================

This tag is part of the assert category of tags, which are assertions
made by the project team themselves about the maturity of their deliverables. One
such assertion (or self-imposed contract) is about the cold-upgrade
features that the deliverable supports.

The "assert:supports-upgrade" tag asserts that the deliverable will
support minimal cold (offline) upgrade capabilities.

Application to current deliverables
===================================

.. tagged-projects:: assert:supports-upgrade


Rationale
=========

OpenStack components represent code that is installed and deployed on
many distributed systems in order to provide services to
users. Operators need to know what services support a controlled and
planned upgrade process from release to release in order to make good
decisions about what to expose to users. Utilizing an OpenStack
project in a deployment where smooth upgrades are not provided is a
danger that operators should be aware of.

Requirements
============

* The deliverable is a software component of an OpenStack cloud
  (openstack, openstack-operations on the map) delivering a long-lived
  service with an API.
* Configuration from release N-1 is supported in release N. Sane
  defaults for new configuration variables are provided in such a way
  that deployed code from N can be expected to run without operator
  intervention.
* Database schema updates are stable and ordered such that moving a
  database (with actual data in it) from release N-1 to N is possible
  without data loss. This must be actively tested full-stack on every
  proposed commit in the gate, with resources present and working
  before and after the upgrade step.
* A procedure for general upgrades of the deliverable is defined and does
  not change substantially from cycle to cycle.
* The project provides an upgrade impact section on the release notes
  page that highlights anything that must be done by operators for
  each cycle outside the normal upgrade procedures.
* The upgrade procedure does not result in any state changes to
  controlled resources, but may disrupt their accessibility. This
  allowance is eliminated by the
  :ref:`tag-assert:supports-accessible-upgrade` tag.
* Full stack integration testing is performed on every proposed commit
  to validate that cold upgrades from the previous stable release are
  not broken. Any upgrade tasks that would be documented as above are
  codified in the testing to demonstrate correctness.
