..
  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-assert:supports-standalone`:

==========================
assert:supports-standalone
==========================

This tag is part of the assert category of tags, which are assertions
made by the project team themselves about the maturity of their deliverables.

The "assert:supports-standalone" tag asserts that the service can be
operated without requiring other OpenStack services, if the operator
so chooses.

Application to current deliverables
===================================

.. tagged-projects:: supports-standalone


Rationale
=========

While OpenStack services are designed to work well together to manage
the datacenter as a whole, some services can be operated independently of
each other for specific use cases and requirements. Operators need to know
which services these are in order to consider their adoption.

Requirements
============

* The core functionality of the service is not affected by being operated
  without other OpenStack services and limitations are clearly documented.
* The service either supports another form of authentication separate
  from Keystone, or no authentication in the case of a single tenant
  environment.
* The project tests and gates this deployment strategy.
