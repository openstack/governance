.. -*- mode: rst -*-

================================================
 Control Plane API endpoints deployment via WSGI
================================================

In some projects, API services can be run:

#. As a Python command that runs a web server (e.g. wsgiref or werkzeug).
#. As a WSGI application hosted by performant web servers (e.g. Apache with
   mod_wsgi or Nginx with uWSGI).

When a project provides a WSGI application the API service gains flexibility
in terms of deployment, performance, configuration and scaling.

Gerrit Topic
============

To facilitate tracking, commits related to this goal should use the
gerrit topic::

  goal-deploy-api-in-wsgi

Completion Criteria
===================

For all projects:

#. Provide WSGI application script file(s) (e.g. to be used by web server).
   There shouldn't be any web server restriction and the application could be
   deploying to any web server that support WSGI applications.
#. Switch devstack jobs to deploy control-plane API services in WSGI with Apache.
   Usage of Apache is already the default in Devstack, let's keep using it
   for consistency unless there is some efforts to support another web server but
   this is not the case at this time.

References
==========

Reference documentation for the existing WSGI deployments:
* http://docs.openstack.org/developer/keystone/apache-httpd.html
* http://docs.openstack.org/developer/ceilometer/install/mod_wsgi.html

Current State / Anticipated Impact
==================================

On 12 Jan 2017 a review of git repositories owned by big tent project
showed the projects that don't support their control-plane API services deployed
via WSGI:

.. (emilien) I built this list based on my research. Please comment if
   something is wrong or missing.
   This list reflects the projects where API can't be deployed via WSGI.

* cloudkitty
* congress
* designate
* freezer
* glance
* kuryr
* magnum
* murano
* neutron
* octavia
* searchlight
* solum
* tacker
* trove
* vitrage
* watcher
* zun

.. (emilien) TODO

These projects already deploy devstack with API service via WSGI:

* aodh
* ceilometer
* cinder
* gnocchi
* ironic
* keystone
* mistral
* nova
* panko
* swift
* zaqar
* (...)

Project Teams
=============

barbican
--------

Planning Artifacts:

* https://blueprints.launchpad.net/barbican/+spec/goal-deploy-api-in-wsgi

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

* `Glance Spec Lite
  <http://specs.openstack.org/openstack/glance-specs/specs/pike/approved/glance/lite-specs.html>`_

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

* The I18n team does not have any API services and therefore has
  nothing to do

Completion Artifacts:

* None

Infrastructure
--------------

Planning Artifacts:

Completion Artifacts:

ironic
------

Planning Artifacts:

  RFE: https://bugs.launchpad.net/ironic/+bug/1513005

Completion Artifacts:

karbor
------

Planning Artifacts:

Completion Artifacts:

keystone
--------

Planning Artifacts:

* Keystone has no planning documents at this time since support was
  introduced prior to Kilo.

Completion Artifacts:

* http://git.openstack.org/cgit/openstack-dev/devstack/commit/?id=a00e5f8810b6ca3b0b5d63cc228125e19bc91955

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

Nova is tracking the work in the `devstack-uwsgi etherpad`_. The placement
service already runs under mod_wsgi in devstack but that will be changed to
uwsgi. There is also a bug in nova-api that needs to be fixed before we can
deploy it under uswgi in devstack for testing.

.. _devstack-uwsgi etherpad: https://etherpad.openstack.org/p/devstack-uwsgi

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

Projects where we plan to add support:

* puppet-zaqar

Completion Artifacts:

Projects that already support WSGI deployments for API:

* puppet-aodh
* puppet-barbican
* puppet-ceilometer
* puppet-cinder
* puppet-gnocchi
* puppet-heat
* puppet-ironic
* puppet-keystone
* puppet-mistral
* puppet-nova
* puppet-panko
* puppet-vitrage

Quality Assurance
-----------------

Planning Artifacts:

* The only project that includes a python web application is the API part
  of OpenStack Health, which is not an OpenStack control plane service.
  OpenStack Health API is deployed as a WSGI application as part of OpenStack
  infra. Further details in https://etherpad.openstack.org/p/pike-qa-goals-wsgi.

Completion Artifacts:

* None

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

* The requirements team do not have any API services and therefore has
  nothing to do.

Completion Artifacts:

* None

sahara
------

Planning Artifacts:

* Update devstack plugin to deploy in WSGI with Apache
* Launchpad bug: https://bugs.launchpad.net/sahara/+bug/1673198

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

* The stable team doesn't have any code repositories and therefore has
  nothing to do.

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

Completion Artifacts:

tripleo
-------

Planning Artifacts:

During Pike, we plan to migrate some services under WSGI with Apache:

* Heat APIs
* Ironic API when https://bugs.launchpad.net/ironic/+bug/1608252 will
  be fixed.
* Mistral API when https://bugs.launchpad.net/mistral/+bug/1663368 will
  be fixed.
* Nova API when it will be officially supported by Nova team.

Completion Artifacts:

TripleO already deploy some services under WSGI with Apache:

* Aodh API
* Barbican
* Ceilometer API
* Cinder API
* Gnocchi API
* Keystone
* Nova Placement
* Panko API

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

