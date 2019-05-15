..
  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-assert:follows-standard-deprecation`:

===================================
assert:follows-standard-deprecation
===================================

This tag is part of the assert category of tags, which are assertions
made by the project team themselves about their maturity. One such assertion
(or self-imposed contract) is about under which conditions APIs and features
of a given service may be deprecated in the future.

The "assert:follows-standard-deprecation" tag asserts that the project will
follow standard feature deprecation rules as described here.


Application to current deliverables
===================================

.. tagged-projects:: assert:follows-standard-deprecation


Rationale
=========

End users of a given service need to know if a feature or an API they are
using and rely on will still be supported by the software tomorrow.
Operators and deployers of a given service want to be able to roll out code
and configuration changes asynchronously, and therefore rely on new code
working correctly with the existing config files.

At the early stages of development it's important to be agile, experiment,
and fail fast. At that point it's not reasonable to commit to support those
early mistakes forever. But as the project matures and gets more users that
rely on existing features, knowing under which conditions the project can
remove features, APIs or alter configuration options in the future becomes
important. It can be a factor in deciding if the project is stable and mature
enough for a specific use case.


Requirements
============

Project teams can apply this tag to services that they produce to assert that
they will follow the following process for end-user-visible or operator-visible
features deprecation:

#. Features, APIs or configuration options are marked deprecated in the code.
   Appropriate warnings will be sent to the end user, operator or library user.
   Code will be frozen and only receive minimal maintenance (just so that it
   continues to work as-is).

#. A migration path will be documented for current users of the feature. An
   email thread will be started on openstack-operators to determine how many
   people are using the deprecated API or feature, and how costly the migration
   plan is to implement. A migration path may be "stop using that feature":
   the cost is then very related to the number of people using the feature
   and how dependent they are to that feature.

#. If the deliverable is part of an Interop Working Group Guideline, the
   project will check if the deprecated feature is part of the exposed
   capabilities. If it is, the obsolescence date (see below) additionally
   needs to take into account Interop WG capabilities deprecation schedule.

#. Based on that data, an obsolescence date will be set. At the very minimum
   the feature (or API, or configuration option) should be marked deprecated
   (and still be supported) in the next stable release branch, *and* for at
   least three months linear time.
   For example, a feature deprecated in November 2015 should still appear
   in the Mitaka release and stable/mitaka stable branch and cannot be
   removed before the beginning of the N development cycle in April 2016.
   A feature deprecated in March 2016 should still appear in the Mitaka
   release and stable/mitaka stable branch, and cannot be removed before
   June 2016.
   Features included in an intermediate release but not a coordinated release
   may be deprecated in the next release of any type and must stay in place at
   least 3 months after being deprecated before being removed in a release of
   any type.

Note that this delay is a required minimum. For significant features, it is
recommended that the deprecated feature appears at least in the next *two*
stable release branches.

In addition, projects assert that:

* It uses an automated test to verify that configuration files are
  forward-compatible from release to release and that this policy is not
  accidentally broken (for example, a gating grenade test).

* No existing config options will have their meaning changed in such a way
  that it would alter the software behavior or otherwise render an existing
  config file broken.

Note: this tag can currently only be applied to services (type:service
deliverables). The tag definition may evolve in the future to include library
feature deprecation policy and be applicable to libraries as a result.
