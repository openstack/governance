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

Completion Artifacts:

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

