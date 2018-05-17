===========================================================
 Minimal Requirements for Incubation and Integrated Status
===========================================================

.. note:: The process described here is obsolete.
  This document is retained only for historical reference. New projects seeking
  to become part of OpenStack should refer to the
  :doc:`new-projects-requirements` instead.

Incubation
==========

The TC will evaluate the project scope and its complementarity with existing
integrated projects and other official programs, look into the project
technical choices, and check a number of requirements, including (but not
limited to):

Scope
-----

* Project must have a clear and defined scope.
* Project's scope should represent a measured progression for OpenStack as a
  whole.
* Project should not inadvertently duplicate functionality present in other
  OpenStack projects. If they do, they should have a clear plan and timeframe
  to prevent long-term scope duplication.
* Project should leverage existing functionality in other OpenStack projects
  as much as possible

Maturity
--------

* Project should have an active team of contributors
* Project should not have a major architectural rewrite planned

Process
-------

* Project must be hosted under stackforge (and therefore use git as its VCS)
* Project must obey OpenStack coordinated project interface (such as tox,
  pbr, global-requirements...)
* Project should use oslo libraries or oslo-incubator where appropriate
* If project is not part of an existing program, it needs to file for a new
  program concurrently with the Incubation request, and fill the corresponding
  requirements.
* Project must have a well-defined core review team, with reviews distributed
  amongst the team (and not being primarily done by one person)
* Reviews should follow the same criteria as OpenStack projects (2 +2s
  before +A)
* Project should use the official openstack lists for discussion

API
---

* Project APIs should be reasonably stable
* Project must have a REST API with at least a JSON entity representation
* Project must have a Python client library API for its REST API
* API service is made available as a WSGI application


QA
--

* Project must have a basic devstack-gate job set up

Documentation / User support
----------------------------

* Project must have docs for developers who want to contribute to the project
* Project should have API documentation for devs who want to add to the API,
  updated when the code is updated

Legal requirements
------------------

* Project must be licensed under the Apache License v2
* Project must have no library dependencies which effectively restrict how
  the project may be distributed or deployed [1]_
* All contributors to the project must have signed the CLA
* Project must have no known trademark issues [2]_

.. [1] https://wiki.openstack.org/wiki/LegalIssuesFAQ#Licensing_of_library_dependencies
.. [2] https://wiki.openstack.org/wiki/LegalIssuesFAQ#New_Project_Names


Graduation to integrated
========================

At the end of every cycle, incubated projects go through a graduation review
to check if they are ready to be made an integral part of the next development
cycle and be included in the next OpenStack integrated release. The TC will
evaluate the technical maturity of the project and check a number of
requirements, including (but not limited to):

Scope
-----

* Project must not duplicate functionality present in other OpenStack projects,
  unless the project has intentionally done so with the intent of replacing it.
* In the case that a project has intentionally duplicated functionality of
  another project, or portion of a project, the new project must reach a level
  of functionality and maturity such that we are ready to deprecate the old
  code and remove it after a well defined deprecation cycle.  The deprecation
  plan agreed to by the PTLs of each affected project, including details for
  how users will be able to migrate from the old to the new, must be submitted
  to the TC for review as a part of the graduation review.

Maturity
--------

* Project must have a large and diverse team of contributors
* Project must have completed integration work with other integrated
  projects, as communicated by the TC when accepted into incubation (that
  includes Dashboard integration if applicable)

Process
-------

* Project must have a diverse core reviewers team (more than 4 people)
* Core reviewers must enforce a minimum of 2 +2s before accepting a change
* Project should have engaged with marketing team to check suitable official
  name
* Project must use OpenStack task, defect and design tracker(s)

QA
--

* Project must have a devstack-gate job running. This gate job should install
  the project using devstack and then run tempest tests.  This job should run
  and vote in the check and gate pipelines for the project.  It is*not* required
  that this job is running for the projects it depends on.  This demonstrates
  that it would be easy to add the project to the integrated gate after
  graduation.
* Project must have decent unit test and functional tests coverage
* Project must be compatible with all currently OpenStack-supported versions
  of Python
* Project should have a decent record of triaging incoming bugs

Documentation / User support
----------------------------

* Project must have end-user docs such as API use, CLI use, Dashboard use
* Project should have installation docs providing install/deployment in an
  integrated manner similar to other OpenStack projects, including
  configuration reference information for all options
* Project should have a proven history of providing user support (on the
  openstack@ mailing list and on Ask OpenStack)

Release management / Security
-----------------------------

* Project must have followed at least two common milestones (follow the common
  cycle at least since X-2)
* Project must have had at least one of their milestones handled by the
  release management team (at least the X-3 milestone)
* Project must provide a 2+ person team that will handle the project specific
  vulnerability process [3]_

.. [3] https://wiki.openstack.org/wiki/Vulnerability_Management


First Integrated Cycle Expectations
===================================

In the release cycle after the project has graduated, the TC expects the project
to reach a level of maturity for its first integrated release. In order for the
project to graduate, the TC will need to be confident that the project will
reach that level of maturity in the time allowed.

API
---

* The REST API must be declared stable and the project must commit to
  maintaining backwards compatibility
* If the project has resources which would make sense to provision
  via a Heat template, then the project should have Heat integration
  which enables this
* If the project has functionality which would make sense to be
  available in the Horizon dashboard, then the project should ensure
  that integration exists
* If the project has resources which could be metered, then the project
  should expose methods that would allow Ceilometer to retrieve these
  metrics
* The lifecycle of resources managed by the project should be externalized
  via notifications so that they can be consumed by other integrated
  projects

Upgrade
-------

Seamless upgradability of OpenStack components remains the most
requested feature by deployers and operators. Once a deployer of
OpenStack has installed a cloud, there is an implicit expectation that
it can be upgraded in place on the existing hardware without creating
downtime for any of the active resources that the cloud manages.

Note: at this point in time we still consider it acceptable to require
downtime of the API / control plane for upgrade, though encourage
projects to develop ways to reduce or eliminate that need.

As such, we expect projects to have a path for inplace upgrading from:

* one stable release to the next stable release (i.e. stable/havana =>
  stable/icehouse)
* from the most recent stable branch to upstream master
  (i.e. stable/icehouse => master during the Juno development cycle)
* within points in master (i.e. from a commit that merged to the
  master branch two weeks ago, to the latest commit on the master
  branch). This is for supporting deployers who wish to continuously
  deploy their OpenStack clouds.

This requirement becomes relevant after the first stable release that
a project ships in, however projects are encouraged to incorporate a
culture of upgradability early in their project lifecycle.

In place upgrade also applies when migrating functionality out of one
project into another, as in nova-volume => cinder, nova-network =>
neutron, nova-baremetal => ironic, and/or nova-scheduler -> gantt.

QA
--

* The project should prepare upgrade testing (currently grenade) during
  the first integrated cycle so that it is ready to enable upgrade testing
  jobs shortly after its first integrated release.
