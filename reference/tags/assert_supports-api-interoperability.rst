..
  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-assert:supports-api-interoperability`:

====================================
assert:supports-api-interoperability
====================================

This tag is part of the assert category of tags, which are assertions
made by the project team themselves about their maturity. One such assertion
(or self-imposed contract) is about the interoperability of the API. In this
context interoperability is a combination of an API that's both stable and compatible.

The "assert:supports-api-interoperability" tag asserts that the project will
follow the API interoperability guidelines and that they will not change (or
remove) an API in a way that will break existing users of an API.

Application to current deliverables
===================================

.. tagged-projects:: assert:supports-api-interoperability

Rationale
=========

End users of a given service need to have confidence that the API they are
using and relying on won't break when they upgrade a cloud or start using their
code on a new OpenStack cloud. This tag asserts that a service adheres to this
principle and follows the requirements to ensure this.

Requirements
============

Project teams can apply this tag to services that they produce to assert the
service will follow the following process for end-user-visibile API stability:

#. The project follows the `API interoperability guidelines`_ when making
   changes to the REST API
#. The projects API uses a versioning scheme (like `microversions`_) or a
   discoverablity mechanism  to ensure that any new features or other changes
   to the API are both explicit and discoverable.
#. There are branchless API tests run on every commit to ensure that the API
   doesn't change between release boundaries.

Tag application process
=======================

Anyone may propose adding or removing this tag to a set of projects by
proposing a change to the openstack/governance repository. The change is
reviewed by the Technical Committee and approved using standard resolution
approval rules. As this is an assert tag, it is up to the project itself to
judge if they are currently meeting the requirements (above) and intend to
continue doing so.

Deprecation
===========

This tag has no deprecation period, as that would rather violate the point of
the tag. If a project chooses to assert the tag then they are making a
commitment to maintain API interoperability henceforth. If the project chooses
to no longer maintain that commitment they should remove the tag. If a member
of the community wishes to claim the project is not meeting the commitment a
proposal should be made removing the tag from the project whereupon the
Technical Committee will review the situation using standard processes.

.. _API interoperability guidelines: http://specs.openstack.org/openstack/api-wg/guidelines/api_interoperability.html
.. _microversions: http://specs.openstack.org/openstack/api-wg/guidelines/microversion_specification.html
