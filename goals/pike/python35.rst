.. -*- mode: rst -*-

====================
 Support Python 3.5
====================

The OpenStack community has been working on porting to Python 3 since
the Havana summit, following a long-term and multi-phase approach.
Python 2.7 is scheduled for end-of-life in 2020, and is currently only
receiving security updates, so there is a firm deadline for finishing
the transition.  We need to finish enabling Python 3 support so we can
move on to future phases of handling upgrades, allowing downstream
packaging to catch up, and eventually dropping Python 2 support
entirely -- ideally all before we reach that end-of-life date for
Python 2.

This goal describes the "done" state for the next major step in the
plan, which is to establish test jobs showing that the services work
properly under Python 3 beyond their unit tests.  Given the amount of
work left to do on the long-term plan, it is important to take this
step as soon as possible.

.. note::

   We will defer any discussion of those future steps, and especially
   dropping Python 2 support, until after all projects are
   successfully running on Python 3, as defined below.

Our primary deployment platforms, Ubuntu LTS and Red Hat Enterprise
Linux, include Python 3.5 support in their most recent releases,
either fully or via add-ons for supporting OpenStack. The primary test
platform in CI is now Ubuntu Xenial, which includes Python 3.5. There
are release candidates for Python 3.6 available upstream, but it is
not clear yet whether distributors will adopt it immediately. Given
the support for 3.5, that is the target, for now. Porting to 3.6 or
later should be easier once 3.5 support is in place, and can be
handled as a separate step from the items described in this goal.

Gerrit Topic
============

To facilitate tracking, commits related to this goal should use the
gerrit topic::

  goal-python35

Completion Criteria
===================

For projects with functional tests in any form:

#. All of the functional tests must pass when a service is running
   under python 3.5.
#. Voting check and gate jobs are present to run all of the project's
   functional tests under python 3.5 to avoid regressions.

For projects with integration tests in any form:

#. All of the integration tests must pass when a service is running
   under python 3.5.
#. Voting check and gate jobs are present to run all of the project's
   integration tests under python 3.5 to avoid regressions.

For all projects:

#. The setup.cfg for the project includes the "trove classifier" for
   PyPI projects "``Programming Language :: Python :: 3.5``".

Optionally, for projects with unit tests:

#. All unit tests should pass under python 3.5, or have explicit skips
   added if the test does not apply to python 3 for some reason.
#. Check and gate jobs are present to run the unit tests under python
   3.5 to avoid regressions.

References
==========

Existing work is being tracked using the wiki at
https://wiki.openstack.org/wiki/Python3

Refer to the wiki for links to the history of the porting work as well
as documents and tools that will help with the port.

Refer to the wiki page for instructions to enabling Python 3 for a
project in devstack and for setting up the functional and integration
tests.

Assistance is available from community members on IRC in the
``#openstack-python3`` channel on freenode and on the openstack-dev
mailing list using the subject tag ``[python3]``.

Current State / Anticipated Impact
==================================

Python 3.5 will be available in all of the long-term-support versions
of the operating systems on which we support deployment, and is listed
as part of our Python testing interface (:ref:`cti-python`).

Our CI infrastructure supports Python 3.

All of our major external dependencies now support Python 3.

All of our own libraries support Python 3.

It is possible to enable Python 3 in devstack for functional and
integration testing.

The project status information below was collected from
https://wiki.openstack.org/wiki/Python3 and is presented here for
background information. Unit test support is **not** a requirement for
this goal.

Projects with Unit Tests Voting
-------------------------------

* aodh
* barbican
* ceilomter
* cinder
* cliff
* congress
* cue
* designate
* glance
* gnocchi
* heat
* horizon
* ironic
* keystone
* keystoneauth
* keystonemiddleware
* magnum
* manila
* mistral
* murano
* murano-agent
* neutron
* neutron-fwaas
* neutron-lbaas
* neutron-vpnaas
* octavia
* oslo.concurrency
* oslo.config
* oslo.context
* oslo.db
* oslo.i18n
* oslo.log
* oslo.messaging
* oslo.messaging
* oslo.middleware
* oslo.rootwrap
* oslo.serialization
* oslo.utils
* oslo.versionedobjects
* oslo.vmware
* oslotest
* pylockfile
* python-barbicanclient
* python-ceilometerclient
* python-cinderclient
* python-designateclient
* python-fuelclient
* python-glanceclient
* python-heatclient
* python-ironicclient
* python-keystoneclient
* python-manilaclient
* python-marconiclient
* python-neutronclient
* python-novaclient
* python-openstackclient
* python-saharaclient
* python-senlinclient
* python-swiftclient
* python-troveclient
* python-tuskarclient
* python-watcherclient
* rally
* sahara
* searchlight
* senlin
* solum
* stevedore
* taskflow
* trove
* watcher
* zaqar

Projects with Remaining Work on Unit Tests
------------------------------------------

networking-l2gw
~~~~~~~~~~~~~~~

Work has not begun on unit tests.

nova
~~~~

Unit test porting is in progress, and the tests that have been ported
are used in a voting gate job. 3077 tests remain as of 2016-09-22.

There is a known issue with a race condition that trips up mox-based
tests. A large number of tests need to be rewritten to use mock
instead, and so that part of the work is likely to be deferred beyond
Pike and treated as a longer-term ongoing effort.

swift
~~~~~

Unit test porting is in progress, and the tests that have been ported
are used in a voting gate job. 4495 tests remaining as of 2016-06-27.

More reviews needed.

Project Teams
=============

barbican
--------

Planning Artifacts:

Completion Artifacts:

Chef OpenStack
--------------

Planning Artifacts:

Completion Artifacts:

cinder
------

Planning Artifacts:

Completion Artifacts:

cloudkitty
----------

Planning Artifacts:

Completion Artifacts:

Community App Catalog
---------------------

Planning Artifacts:

Completion Artifacts:

congress
--------

Planning Artifacts:

Completion Artifacts:

designate
---------

Planning Artifacts:

Completion Artifacts:

Documentation
-------------

Planning Artifacts:

Completion Artifacts:

dragonflow
----------

Planning Artifacts:

Completion Artifacts:

ec2-api
-------

Planning Artifacts:

Completion Artifacts:

freezer
-------

Planning Artifacts:

Completion Artifacts:

fuel
----

Planning Artifacts:

Completion Artifacts:

glance
------

Planning Artifacts:

Completion Artifacts:

heat
----

Planning Artifacts:

Completion Artifacts:

horizon
-------

Planning Artifacts:

Completion Artifacts:

I18n
----

Planning Artifacts:

Completion Artifacts:

Infrastructure
--------------

Planning Artifacts:

Completion Artifacts:

ironic
------

Planning Artifacts:

Completion Artifacts:

karbor
------

Planning Artifacts:

Completion Artifacts:

keystone
--------

Planning Artifacts:

Completion Artifacts:

kolla
-----

Planning Artifacts:

Completion Artifacts:

kuryr
-----

Planning Artifacts:

Completion Artifacts:

magnum
------

Planning Artifacts:

Completion Artifacts:

manila
------

Planning Artifacts:

Completion Artifacts:

mistral
-------

Planning Artifacts:

Completion Artifacts:

monasca
-------

Planning Artifacts:

Completion Artifacts:

murano
------

Planning Artifacts:

Completion Artifacts:

neutron
-------

Planning Artifacts:

Completion Artifacts:

nova
----

Planning Artifacts:

Completion Artifacts:

octavia
-------

Planning Artifacts:

Completion Artifacts:

OpenStack Charms
----------------

Planning Artifacts:

Completion Artifacts:

OpenStack UX
------------

Planning Artifacts:

Completion Artifacts:

OpenStackAnsible
----------------

Planning Artifacts:

Completion Artifacts:

OpenStackClient
---------------

Planning Artifacts:

Completion Artifacts:

oslo
----

Planning Artifacts:

Completion Artifacts:

Packaging-deb
-------------

Planning Artifacts:

Completion Artifacts:

Packaging-rpm
-------------

Planning Artifacts:

Completion Artifacts:

Puppet OpenStack
----------------

Planning Artifacts:

Completion Artifacts:

Quality Assurance
-----------------

Planning Artifacts:

Completion Artifacts:

rally
-----

Planning Artifacts:

Completion Artifacts:

RefStack
--------

Planning Artifacts:

Completion Artifacts:

Release Management
------------------

Planning Artifacts:

Completion Artifacts:

requirements
------------

Planning Artifacts:

Completion Artifacts:

sahara
------

Planning Artifacts:

Completion Artifacts:

searchlight
-----------

Planning Artifacts:

Completion Artifacts:

Security
--------

Planning Artifacts:

Completion Artifacts:

senlin
------

Planning Artifacts:

Completion Artifacts:

solum
-----

Planning Artifacts:

Completion Artifacts:

Stable branch maintenance
-------------------------

Planning Artifacts:

    The stable team doesn't have any code repositories and therefore has
    nothing to do.

Completion Artifacts:

    Not Applicable

swift
-----

Planning Artifacts:

Completion Artifacts:

tacker
------

Planning Artifacts:

Completion Artifacts:

Telemetry
---------

Planning Artifacts:

Completion Artifacts:

tricircle
---------

Planning Artifacts:

Completion Artifacts:

tripleo
-------

Planning Artifacts:

Completion Artifacts:

trove
-----

Planning Artifacts:

Completion Artifacts:

vitrage
-------

Planning Artifacts:

Completion Artifacts:

watcher
-------

Planning Artifacts:

Completion Artifacts:

winstackers
-----------

Planning Artifacts:

Completion Artifacts:

zaqar
-----

Planning Artifacts:

Completion Artifacts:

zun
---

Planning Artifacts:

Completion Artifacts:

