..
  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-assert:supports-rolling-upgrade`:

===============================
assert:supports-rolling-upgrade
===============================

This tag is part of the assert category of tags, which are assertions
made by the project team themselves about the maturity of their deliverables. One
such assertion (or self-imposed contract) is about the rolling upgrade
features that the deliverable supports.

The "assert:supports-rolling-upgrade" tag asserts that the deliverable
will support minimal rolling upgrade capabilities.

Application to current deliverables
===================================

.. tagged-projects:: assert:supports-rolling-upgrade


Rationale
=========

OpenStack components represent code that is installed and deployed on
many distributed systems in order to provide services to
users. Operators need to know what services support a rolling upgrade
process to avoid significant downtime.

Requirements
============

* The deliverable is a software component of an OpenStack cloud
  (openstack, openstack-operations on the map) delivering a long-lived
  service with an API.
* The deliverable has already successfully asserted the supports-upgrade
  tag. All the requirements for that tag are requirements for this
  tag, and assertion of that tag is a requirement to assert this tag.
* The project has a defined plan that allows operators to roll out new
  code to subsets of services, eliminating the need to restart all
  services on new code simultaneously. This plan should clearly call
  out the supported configuration(s) that are expected to work, unless
  there are no such caveats. This does not require complete
  elimination of downtime during upgrades, but rather reducing the
  scope from "all services" to "some services at a time." In other
  words, "restarting all API services together" is a reasonable restriction.
* Full stack integration testing with services arranged in a
  mid-upgrade manner is performed on every proposed commit to validate
  that mixed-version services work together properly. This testing
  must be performed on configurations that the project considers to be
  its reference implementations. The arrangement(s) tested will depend
  on the project (i.e. should be representative of a
  meaningful-to-operators rolling upgrade scenario) and available
  testing resources. At least one representative arrangement must be
  tested full-stack in the gate.
