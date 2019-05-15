..
  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-assert:supports-zero-downtime-upgrade`:

=====================================
assert:supports-zero-downtime-upgrade
=====================================

This tag is part of the assert category of tags, which are assertions made by
the project team themselves about the maturity of their deliverables.

The ``assert:supports-zero-downtime-upgrade`` tag asserts that in addition to a
deliverable supporting `minimal rolling upgrade capabilities
<https://governance.openstack.org/tc/reference/tags/assert_supports-rolling-upgrade.html>`_,
it does so *without incurring any disruption to API availability*.

Application to current deliverables
===================================

.. tagged-projects:: assert:supports-zero-downtime-upgrade


Rationale
=========

OpenStack components represent code that is installed and deployed on many
distributed systems in order to provide services to users. Operators need to
know what services support an upgrade process that eliminates downtime of the
control plane entirely.

Requirements
============

* The deliverable is a software component of an OpenStack cloud
  (openstack, openstack-operations on the map) delivering a long-lived
  service with an API.

* The deliverable has already successfully asserted both the
  :ref:`tag-assert:supports-upgrade` and
  :ref:`tag-assert:supports-rolling-upgrade` tags. All the requirements for
  those tags are requirements for this tag, and assertion of both those tags
  are requirements to assert this tag.

* In addition to the plan required by the
  :ref:`tag-assert:supports-rolling-upgrade` tag which allows for minimal
  downtime, this tag requires services to completely eliminate API downtime of
  the control plane during the upgrade. In other words, requiring operators to
  "restart all API services together" is not reasonable under this tag.
  Additionally, it is not reasonable for services to respond to requests with
  HTTP 5xx codes when they otherwise would have returned successful responses,
  even intermittently.

* While all requests to the control plane must be eventually processed,
  performance degradation during the upgrade is acceptable. This may include
  slow HTTP responses and delayed request handling (such as messages queuing up
  on the message bus).

* In addition to the full stack integration testing required by the
  :ref:`tag-assert:supports-rolling-upgrade` tag, services should be capable of
  receiving and handling requests throughout the rolling upgrade process with a
  normal success rate. In order to assert this tag, services should prevent
  regression by implementing a zero-downtime gate job wherein both a new
  version of the service and an old version of the service are run
  concurrently.
