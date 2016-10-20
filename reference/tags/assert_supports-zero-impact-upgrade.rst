::

  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-assert:supports-zero-impact-upgrade`:

===================================
assert:supports-zero-impact-upgrade
===================================

This tag is part of the assert category of tags, which are assertions made by
the project team themselves about their maturity.

The ``assert:supports-zero-impact-upgrade`` tag asserts that in addition to a
project supporting `zero-downtime, rolling upgrade capabilities
<https://governance.openstack.org/reference/tags/assert_supports-zero-downtime-upgrade.html>`_,
it does so *without incurring any perceivable performance penalty*.

Application to current projects
===============================

.. tagged-projects:: assert:supports-zero-impact-upgrade


Rationale
=========

OpenStack projects represent code that is installed and deployed on many
distributed systems in order to provide services to users. Operators need to
know what projects support a seamless upgrade process that does not impact the
performance of the cloud.

Requirements
============

* The project is already tagged as ``type:service``.

* The project has already successfully asserted the
  :ref:`tag-assert:supports-upgrade`,
  :ref:`tag-assert:supports-rolling-upgrade`, and
  :ref:`tag-assert:supports-zero-downtime-upgrade` tags. All the requirements
  for those tags are requirements for this tag, and assertion of both those
  tags are requirements to assert this tag.

* In addition to the plan required by the
  :ref:`tag-assert:supports-zero-downtime-upgrade` tag which allows for
  performance degradation during the upgrade process, this tag requires
  services to completely eliminate any perceivable performance penalty during
  the upgrade process. In other words, operators should not expect any portion
  of the upgrade or migration process to place abnormally high load on any part
  of the cloud, or to cause delays in the handling of API requests, even
  intermittently.

* In addition to the gate testing required by the
  :ref:`tag-assert:supports-zero-downtime-upgrade` tag, services should be
  capable of receiving and handling requests throughout the rolling upgrade
  process within normal performance parameters. In order to assert this tag,
  services should prevent regression by implementing a zero-impact gate job
  wherein both a new version of the service and an old version of the service
  are run concurrently under load. *A measurement of API response times must
  show that there are no statistically significant outliers during the upgrade
  process when compared to normal operations.*

Tag application process
=======================

Assertion tags are set by the project team PTL or suitable designee based on
meeting the above criteria. The Technical Committee may exceptionally remove
the tag if they find that the project doesn't actually follow the requirements
for the assertion.

The project asserting this tag should do so when the above requirements are met
for the reference implementation(s) or configuration(s) officially adopted by
that project.
