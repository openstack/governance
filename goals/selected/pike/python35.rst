.. -*- mode: rst -*-

.. _goal-support-python-3.5:

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
as part of our Project Testing Interface for Python (:ref:`pti-python`).

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
* ceilometer
* cinder
* cliff
* congress
* cue
* designate
* fuxi
* glance
* gnocchi
* heat
* horizon
* ironic
* keystone
* keystoneauth
* keystonemiddleware
* kolla
* kuryr
* kuryr-kubernetes
* kuryr-libnetwork
* magnum
* manila
* mistral
* murano
* murano-agent
* murano-dashboard
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
* python-muranoclient
* python-neutronclient
* python-novaclient
* python-openstackclient
* python-saharaclient
* python-senlinclient
* python-solumclient
* python-swiftclient
* python-troveclient
* python-tuskarclient
* python-watcherclient
* rally
* sahara
* searchlight
* senlin
* shade
* solum
* solum-dashboard
* stevedore
* taskflow
* tripleo
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
are used in a voting gate job. 66 unit tests remain as of 2017-07-26.

There is a known issue with a race condition that trips up mox-based
tests. A large number of tests need to be rewritten to use mock
instead, and so that part of the work is likely to be deferred beyond
Pike and treated as a longer-term ongoing effort.

``gate-tempest-dsvm-py35-ubuntu-xenial`` is gating on Nova changes.

All nova functional tests are also passing with py35 and gating on nova.

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

* https://blueprints.launchpad.net/barbican/+spec/goal-py3

Completion Artifacts:

Chef OpenStack
--------------

The Chef cookbooks do not provide any Python code directly, they consume
downstream packages, and thus are not directly affected by this goal. Once
a package is available in a python3 variant, deployers can use variables
in order to select these packages instead of python2.

Planning Artifacts: None

Completion Artifacts: None

cinder
------

Planning Artifacts:

Completion Artifacts:

cloudkitty
----------

Planning Artifacts:

* Cloudkitty has no planning documentation at this time since Python 3
  support has already been implemented.

Completion Artifacts:

* https://opendev.org/openstack/cloudkitty/src/branch/master/setup.cfg#L19

Community App Catalog
---------------------

Planning Artifacts:

Completion Artifacts:

congress
--------

Planning Artifacts:

* https://blueprints.launchpad.net/congress/+spec/support-python3
* https://bugs.launchpad.net/congress/+bug/1681577

Completion Artifacts:

* https://review.opendev.org/#/c/525349/
* https://review.opendev.org/#/c/525423/

designate
---------

Planning Artifacts:

Completion Artifacts:

Documentation
-------------

Planning Artifacts:

* https://blueprints.launchpad.net/openstack-doc-tools/+spec/support-python3.5

Note: This applies to the doc-tools and openstackdoctheme repos.

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

* All freezer unit tests are passing with py35 and gating on different freezer
  components.
* https://review.opendev.org/#/c/466807/
* https://review.opendev.org/#/c/466811/
* https://review.opendev.org/#/c/466813/
* https://review.opendev.org/#/c/466816/

Completion Artifacts:

fuel
----

Planning Artifacts:

Completion Artifacts:

glance
------

Planning Artifacts:

* `Glance Spec Lite
  <http://specs.openstack.org/openstack/glance-specs/specs/pike/approved/glance/lite-specs.html>`_
* `Glance Store Spec Lite
  <http://specs.openstack.org/openstack/glance-specs/specs/pike/approved/glance_store/lite-specs.html>`_
* `Glance Client Spec Lite
  <http://specs.openstack.org/openstack/glance-specs/specs/pike/approved/python-glanceclient/lite-specs.html>`_

Completion Artifacts:

* glance_store library: completed.  (For details, see the
  `glance project py35 tracking etherpad
  <https://etherpad.openstack.org/p/glance-pike-python35-goal>`_.)
* python-glanceclient: completed.  (For details, see the
  `glance project py35 tracking etherpad
  <https://etherpad.openstack.org/p/glance-pike-python35-goal>`_.)
* glance: not completed.

  - Glance is affected by the eventlet ssl-handshake-drop problem in py35
    (see `Bug #1482633 <https://bugs.launchpad.net/glance/+bug/1482633>`_)
  - Fix will have to occur in eventlet (not sure that will actually happen)
  - We've reconfigured the functional tests that were being skipped when
    run under py35 and will run them as their own non-voting gate job
    named 'glance-eventlet-ssl-handshake-broken-py35' so that it's obvious
    that this issue exists (and, more optimistically, we can easily detect
    when it's fixed).  (See https://review.opendev.org/#/c/571040/)
  - There is a workaround, namely, use something like HAProxy to do SSL
    termination before calls are forwarded to Glance.

heat
----

Planning Artifacts:

* Heat will enable python35 gates for voting.
* heat-agents repo support for python35
* heat-templates repo support for python35
* heat-cfntools repo support for python35

Completion Artifacts:

* `heat <https://opendev.org/openstack/heat/src/branch/master/setup.cfg#n19>`_
* `python-heatclient <https://opendev.org/openstack/python-heatclient/src/branch/master/setup.cfg#n21>`_
* `heat-translator <https://opendev.org/openstack/heat-translator/src/branch/master/setup.cfg#L20>`_

horizon
-------

Planning Artifacts:

Completion Artifacts:

I18n
----

Planning Artifacts:

    * https://blueprints.launchpad.net/openstack-i18n/+spec/python35-support

Completion Artifacts:

Infrastructure
--------------

The Infrastructure team actively avoids maintaining deliverables
which are Python dependencies of deliverables within the TC Approved
Release or of other official teams, so our needs for Python 3
support differ somewhat. While we do actively test most of our
Python-based tools and utilities against Python 3, our
responsibility to this community goal is that we have ensured our CI
system provides sufficient Python 3 support to allow other teams to
adequately test their deliverables. To the extent that this goal was
predicated on that work, it is already complete for Infra.

ironic
------

Planning Artifacts:

  RFE: https://bugs.launchpad.net/ironic/+bug/1673768

Completion Artifacts:

* ironic: DONE

  Patch making the CI job voting: https://review.opendev.org/#/c/531398/

* ironic-python-agent: TODO

* ironic-inspector: DONE

  Patch making the CI job voting: https://review.opendev.org/#/c/531400/

karbor
------

Planning Artifacts:

* https://bugs.launchpad.net/karbor/+bug/1681622

Completion Artifacts:
* `karbor classifier <https://opendev.org/openstack/karbor/src/branch/master/setup.cfg#L19>`_
* `karbor-dashboard classifier <https://opendev.org/openstack/karbor-dashboard/src/branch/master/setup.cfg#L19>`_
* `python-karborclient classifier <https://opendev.org/openstack/python-karborclient/src/branch/master/setup.cfg#L19>`_
* `python 3 jobs <https://review.opendev.org/302072/>`_

keystone
--------

Planning Artifacts:

* Keystone has no planning documentation at this time since Python 3 support
  has already been implemented.

Completion Artifacts:

* `keystone <https://opendev.org/openstack/keystone/src/branch/master/setup.cfg#L19>`_
* `keystonemiddleware <https://opendev.org/openstack/keystonemiddleware/src/branch/master/setup.cfg#L19>`_
* `python-keystoneclient <https://opendev.org/openstack/python-keystoneclient/src/branch/master/setup.cfg#L19>`_
* `keystoneauth <https://opendev.org/openstack/keystoneauth/src/branch/master/setup.cfg#L19>`_

kolla
-----

Planning Artifacts:

* https://blueprints.launchpad.net/kolla/+spec/support-python-35

Completion Artifacts:

* https://review.opendev.org/#/c/414813/
* https://review.opendev.org/#/c/341068/

kuryr
-----

Planning Artifacts:

* https://blueprints.launchpad.net/kuryr-kubernetes/+spec/goal-python35
* https://blueprints.launchpad.net/kuryr-libnetwork/+spec/goal-python35
* https://blueprints.launchpad.net/fuxi/+spec/goal-python35

Completion Artifacts:

* `kuryr <https://opendev.org/openstack/kuryr/src/branch/master/setup.cfg#L19>`_

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

* https://storyboard.openstack.org/#!/story/2000975

Completion Artifacts:

* https://review.opendev.org/480160
* https://review.opendev.org/479165

murano
------

Planning Artifacts:

* Murano has no planning documentation at this time since Python 3 support
  has already been implemented and all major murano projects have py3.5 gates
  voting.

Completion Artifacts:

* `murano <https://opendev.org/openstack/murano/src/branch/master/setup.cfg#L36>`_
* `murano-dashboard <https://opendev.org/openstack/murano-dashboard/src/branch/master/setup.cfg#L41>`_
* `murano-agent <https://opendev.org/openstack/murano-agent/src/branch/master/setup.cfg#L21>`_
* `python-muranoclient <https://opendev.org/openstack/python-muranoclient/src/branch/master/setup.cfg#L23>`_

neutron
-------

Planning Artifacts:

* Bug to track broad effort of enabling jobs:
  https://bugs.launchpad.net/neutron/+bug/1683301

Completion Artifacts:

nova
----

Planning Artifacts:

* https://blueprints.launchpad.net/nova/+spec/goal-python35

Completion Artifacts:

* https://review.opendev.org/#/c/436540/

octavia
-------

Planning Artifacts:

All python 3.5 unit, functional, and tempest tests are in place.
Unit and functional tests are voting, scenario tests are blocked pending
diskimage-builder patches for python 3.5. Specifically this patch:
https://review.opendev.org/#/c/449721/

Completion Artifacts:

* setup.cfg: https://review.opendev.org/#/c/341070/
* Unit tests are voting: https://review.opendev.org/#/c/337946
* Functional tests voting: https://review.opendev.org/446148
* Scenario tests voting: https://review.opendev.org/#/c/458311/
                         https://review.opendev.org/#/c/477689/

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

* https://blueprints.launchpad.net/openstack-ansible/+spec/goal-python35

NB Dependent on upstream projects achieving python35 goal.

Completion Artifacts:

OpenStackClient
---------------

Planning Artifacts:

* https://blueprints.launchpad.net/python-openstackclient/+spec/pike-goal-python35

Completion Artifacts:

* `cliff <https://opendev.org/openstack/cliff/src/branch/master/setup.cfg#L15>`_
* `openstackclient <https://opendev.org/openstack/openstackclient/src/branch/master/setup.cfg#L20>`_
* `os-client-config <https://opendev.org/openstack/os-client-config/src/branch/master/setup.cfg#L19>`_
* `osc-lib <https://opendev.org/openstack/osc-lib/src/branch/master/setup.cfg#L19>`_
* `python-openstackclient <https://opendev.org/openstack/python-openstackclient/src/branch/master/setup.cfg#L19>`_

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

* Nothing is planned since Puppet OpenStack doesn't contain Python code

Completion Artifacts:

* None

Quality Assurance
-----------------

Planning Artifacts:

QA projects already mostly support python 3.5.
The little left to be done to is tracked in this etherpad:
https://etherpad.openstack.org/p/pike-qa-goals-py35

Completion Artifacts:

https://review.opendev.org/#/q/branch:master+topic:qa_py35_ack

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

* https://etherpad.openstack.org/p/pike-relmgt-plan

Completion Artifacts:

* Port the releases repository jobs to use python 3.5: https://review.opendev.org/#/q/project:openstack/releases+topic:goal-python35
* Switch the releases repo to gate on python 3.5: https://review.opendev.org/#/c/441459/

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

* Searchlight has no planning documentation at this time since Python 3 support
  has already been implemented.

Completion Artifacts:

* https://opendev.org/openstack/searchlight/src/branch/master/setup.cfg#L19

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

* Solum has no planning documentation at this time since Python 3 support
  has already been implemented.

Completion Artifacts:

* `solum <https://opendev.org/openstack/solum/src/branch/master/setup.cfg#L20>`_
* `python-solumclient <https://opendev.org/openstack/python-solumclient/src/branch/master/setup.cfg#L19>`_
* `solum-dashboard <https://opendev.org/openstack/solum-dashboard/src/branch/master/setup.cfg#L13>`_

Stable branch maintenance
-------------------------

Planning Artifacts:

* The stable team doesn't have any code repositories and therefore has
  nothing to do

Completion Artifacts:

* None

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

* None

Completion Artifacts:

* Support Python35 in Tricircle: https://review.opendev.org/#/c/417553/
* Add Python35 job for Tricircle: https://review.opendev.org/#/c/418655/

tripleo
-------

TripleO only has two types of tests, unit and integration (the tripleo-ci
jobs).  The unit tests are already running and voting on the TripleO
Python projects, but there is a problem with using Python 3 in the integration
tests.  These tests are dependent on downstream packaging, and downstream does
not currently package Python 3 versions of all the OpenStack dependencies.  As
of the Atlanta PTG they were not planning to start that work in the near
future either.

It may be possible to get Python 3 dependencies from other sources, but then
TripleO would lose the insulation against broken dependencies that RDO
provides through its promotion system.  This is similar to the upper
constraints system in OpenStack proper.

Basically TripleO has a circular dependency on the "allowing downstream
packaging to catch up" part of the goal.  Given that, the team's plan was to
focus on ensuring every Python project in TripleO is gating on py35 and to
improve unit test coverage of the projects so there is a better chance of
TripleO working on Python 3 once that becomes possible from a packaging
perspective.

* dib-utils

This repository doesn't contain Python code (only bash).

* instack

  - Planning Artifacts: none.

  - Completion Artifacts: py35 unit tests are passing and gating.

* instack-undercloud

  - Planning Artifacts: none.

  - Completion Artifacts: py35 unit tests are passing and gating.

* os-apply-config

  - Planning Artifacts: none.

  - Completion Artifacts: py35 unit tests are passing and gating.

* os-collect-config

  - Planning Artifacts: none.

  - Completion Artifacts: py35 unit tests are passing and gating.

* os-net-config

  - Planning Artifacts: none.

  - Completion Artifacts: py35 unit tests are passing and gating.

* os-refresh-config

  - Planning Artifacts: none.

  - Completion Artifacts: py35 unit tests are passing and gating.

* puppet-tripleo

  - Planning Artifacts: none, this project is written in Puppet and Ruby.

  - Completion Artifacts: none, this project is written in Puppet and Ruby.

* python-tripleoclient

  - Planning Artifacts: none.

  - Completion Artifacts: py35 unit tests are passing and gating.

* tripleo-common

  - Planning Artifacts: none.

  - Completion Artifacts: py35 unit tests are passing and gating.

* tripleo-docs

  - Planning Artifacts: none, this project is written in RST.

  - Completion Artifacts: none, this project is written in RST.

* tripleo-heat-templates

  - Planning Artifacts: https://blueprints.launchpad.net/tripleo/+spec/support-python-35

  - Completion Artifacts: None.

* tripleo-image-elements

This repository doesn't contain Python code (only bash).

* tripleo-incubator

This project is deprecated and will be removed soon if not in Pike.

* tripleo-puppet-elements

This repository doesn't contain Python code (only bash).

* tripleo-quickstart

  - Planning Artifacts: None, these are Ansible playbooks.

  - Completion Artifacts: None

* tripleo-quickstart-extras

  - Planning Artifacts: None, these are Ansible playbooks.

  - Completion Artifacts: none

* tripleo-repos

  - Planning Artifacts: make Python jobs working (WIP).

  - Completion Artifacts: none

* tripleo-specs

  - Planning Artifacts: none, this project is written in RST.

  - Completion Artifacts: none, this project is written in RST.

* tripleo-ui

  - Planning Artifacts: none, this project is written in Javascript and CSS.

  - Completion Artifacts: none, this project is written in Javascript and CSS.

* tripleo-validations

  - Planning Artifacts: None, these are Ansible playbooks.

  - Completion Artifacts: none


trove
-----

Planning Artifacts:

Trove already has voting python35 gate jobs. The classifier has been
added to setup.cfg. There are no specific planning artifacts for this
project.

Completion Artifacts:

* https://review.opendev.org/#/c/454699/
* https://review.opendev.org/#/c/454697/

vitrage
-------

Planning Artifacts:

* https://blueprints.launchpad.net/vitrage/+spec/support-python-35

Completion Artifacts:

* https://review.opendev.org/491488
* https://review.opendev.org/493758
* https://review.opendev.org/526908

watcher
-------

Planning Artifacts:

* Functional tests should be run in a py35 environment.

Completion Artifacts:

* Watcher has gates for testing py27 and py35 unit tests. Functional tests are
  passing with a py27 and py34.

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

* https://blueprints.launchpad.net/zun/+spec/support-python-35

Completion Artifacts:

* Classifier: https://opendev.org/openstack/zun/src/branch/master/setup.cfg
* Unit tests: All unit tests are passed in python 3.5. There is a voting check and gate job setup called 'gate-zun-python35'.
* Functional tests: Zun doesn't have functional tests.
* Integration tests: All integration tests are passed in python 3.5. There is a voting check and gate job setup: https://review.opendev.org/#/c/491623/

