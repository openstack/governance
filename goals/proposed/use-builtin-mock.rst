=========================================
Migrate from mock to bultin unittest.mock
=========================================

The external mock library was necessary in python versions less than 3.3.  The
built in unittest.mock provides the functionality of the old mock library and
also provides a more stable interface vs the constantly updating external mock
library.


Champion
========

* Matthew Thode <mthode@mthode.org> (prometheanfire)
* Sean McGinnis <sean.mcginnis@gmail.com> (smcginnis)


Gerrit Topic
============

To facilitate tracking, commits related to this goal should use the
gerrit topic::

  unittest.mock

A new Story in https://storyboard.openstack.org/ will be created to track any
related patch.


Completion Criteria
===================

#. All projects with managed constraints do not use the mock library but use
   the built in unittest.mock.


References
==========

The main refrence is upstream documentation located at [1]_
An example review can be found in [2]_
Current progress is tracked in [3]_

Current State / Anticipated Impact
==================================

There are over 100 repositories needing this change, a short selection is
listed below.

* openstack/ironic
* openstack/ironic
* openstack/ironic-ui
* openstack/karbor-dashboard
* openstack/keystoneauth
* openstack/keystoneauth
* openstack/keystoneauth
* openstack/keystonemiddleware
* openstack/keystonemiddleware
* openstack/kuryr-tempest-plugin
* openstack/magnum
* openstack/manila
* openstack/mistral-dashboard
* openstack/mistral-tempest-plugin
* openstack/monasca-analytics
* openstack/monasca-analytics
* openstack/monasca-ceilometer
* openstack/monasca-events-api
* openstack/monasca-log-api
* openstack/monasca-statsd
* openstack/monasca-tempest-plugin
* openstack/monasca-transform
* openstack/monasca-transform
* openstack/monasca-ui
* openstack/networking-l2gw
* openstack/networking-l2gw-tempest-plugin
* openstack/networking-midonet
* openstack/networking-powervm
* openstack/networking-sfc
* openstack/neutron
* openstack/neutron-dynamic-routing
* openstack/neutron-fwaas
* openstack/neutron-fwaas-dashboard
* openstack/neutron-vpnaas-dashboard
* openstack/nova
* openstack/nova-powervm
* openstack/openstack-ansible
* openstack/openstack-doc-tools
* openstack/openstack-doc-tools
* openstack/openstack-health
* openstack/openstacksdk
* openstack/os-brick
* openstack/os-collect-config


Links
=====

.. [1] https://docs.python.org/3/library/unittest.mock.html
.. [2] https://review.opendev.org/#/c/720914/
.. [3] https://review.opendev.org/#/q/branch:master+topic:unittest.mock
