::

  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-assert:supports-rolling-upgrade`:

===============================
assert:supports-rolling-upgrade
===============================

This tag is part of the assert category of tags, which are assertions
made by the project team themselves about their maturity. One such
assertion (or self-imposed contract) is about the rolling upgrade
features that the project supports.

The "assert:supports-rolling-upgrade" tag asserts that the project
will support minimal rolling upgrade capabilities.

Application to current projects
===============================

.. tagged-projects:: assert:supports-rolling-upgrade


Rationale
=========

OpenStack projects represent code that is installed and deployed on
many distributed systems in order to provide services to
users. Operators need to know what projects support a rolling upgrade
process to avoid significant downtime.

Requirements
============

* The project is already tagged as type:service.
* The project has already successfully asserted the supports-upgrade
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

Tag application process
=======================

Assertion tags are set by the project team PTL or suitable designee
based on meeting the above criteria. The Technical Committee may
exceptionally remove the tag if they find that the project doesn't
actually follow the requirements for the assertion.

The project asserting this tag should do so when the above
requirements are met for the reference implementation(s) or
configuration(s) officially adopted by that project.
