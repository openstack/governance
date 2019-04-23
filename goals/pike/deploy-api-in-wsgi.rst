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
#. Switch devstack jobs to deploy control-plane API services under
   uwsgi with Apache acting as a front end proxy.

uwsgi vs. mod_wsgi
------------------

When this effort was first approved, the push was to use
``mod_wsgi``. mod_wsgi has many issues when being used in devstack for
development or testing.

- services log to a very different location / format
- start/stop/restart/status of services is now very different
  depending on if they are api services or workers
- apache restarts trigger restarts of all API services, and take long
  enough that intermittent races can occur.
- API servers still need dedicated ports for certain parts of their
  config.

The effort was pushed forward because at the time no one signed up to
do the ground work for the uwsgi transition in devstack. That work was
done here -
http://lists.openstack.org/pipermail/openstack-dev/2017-April/115423.html
with the intent that the ``mod_wsgi`` support is deleted from devstack
in Queens.

References
==========

Reference documentation for the existing WSGI deployments:
* http://docs.openstack.org/developer/keystone/apache-httpd.html
* http://docs.openstack.org/developer/ceilometer/install/mod_wsgi.html

Current State / Anticipated Impact
==================================

On 12 Jan 2017 a review of git repositories owned by official projects
showed the projects that don't support their control-plane API services deployed
via WSGI:

.. (emilien) I built this list based on my research. Please comment if
   something is wrong or missing.
   This list reflects the projects where API can't be deployed via WSGI.

* cloudkitty
* congress
* designate
* glance
* kuryr-libnetwork
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
* freezer
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

* https://review.opendev.org/#/c/476996/
* https://review.opendev.org/#/c/476995/

Chef OpenStack
--------------

The Chef cookbooks do not provide any API directly, they consume
downstream packages, and thus are not directly affected by this goal.
When packages support deploying API services via WSGI, the
corresponding cookbooks use it.

Planning Artifacts: None

Completion Artifacts: None

cinder
------

Planning Artifacts:

DevStack change still needed to properly run cinder-api under Apache:

https://review.opendev.org/#/c/441266/

Completion Artifacts:

* https://review.opendev.org/#/c/207020/
* https://review.opendev.org/#/c/441266/

cloudkitty
----------

Planning Artifacts:

Completion Artifacts:

https://review.opendev.org/#/c/366043/

Community App Catalog
---------------------

Planning Artifacts:

Completion Artifacts:

congress
--------

Planning Artifacts:

* https://bugs.launchpad.net/congress/+bug/1670517

Completion Artifacts:

designate
---------

Planning Artifacts:

Completion Artifacts:

Documentation
-------------

Planning Artifacts:

* https://blueprints.launchpad.net/openstack-manuals/+spec/document-api-endpoints-wsgi

Note: Dependent on upstream projects achieving deploy-api-in-wsgi goal.

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

* Freezer has no planning documents at this time since support was
  introduced prior to Newton.

Completion Artifacts:

Freezer is already using wsgi to deploy the api service since Newton release.
Freezer supports two ways of running dsvm gate job, apache2 (with mod_wsgi) or
apache2 (with mod_proxy and uwsgi). The default way for running devstack is
apache2 with mod_proxy and uwsgi.

https://review.opendev.org/#/c/471080/


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

.. note::
   The Pike release notes for Glance state that the Glance project team does
   not recommend running Glance under the uWSGI configuration in production.
   We have renewed that statement in the Queens release notes, with the
   additional proviso that the interoperable image import functionality does
   not work when Glance is deployed as a wsgi app under uwsgi with apache.

   You can follow Bug 1742813_ for more information.

   .. _1742813: https://bugs.launchpad.net/glance/+bug/1742813

* Glance supports running as a wsgi app with this branch:
  https://review.opendev.org/#/q/status:merged+project:openstack/glance+branch:master+topic:goal-deploy-api-in-wsgi
* Devstack is now deploying glance as a wsgi app under uwsgi with apache with:
  https://review.opendev.org/459451

heat
----

Planning Artifacts:

* Heat has no planning documents at this time since the support was
  introduced and enabled by default at Ocata.

Completion Artifacts:

* `heat <https://opendev.org/openstack/heat/commit/6ef5fa9adc8886ed339132b5e5e27cee4000f762>`_

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

The Infrastructure team does not maintain any OpenStack trademark
program services, much less any with REST APIs, so has no current
need for WSGI conversion.

ironic
------

Planning Artifacts:

  RFE: https://bugs.launchpad.net/ironic/+bug/1513005

Completion Artifacts:

* ironic: PARTIAL (using mod_wsgi instead of uWSGI)
* ironic-inspector: TODO (Queens)

karbor
------

Planning Artifacts:

* https://bugs.launchpad.net/karbor/+bug/1681500

Completion Artifacts:

* https://review.opendev.org/453705/
* https://review.opendev.org/455734/
* https://review.opendev.org/467536/

keystone
--------

Planning Artifacts:

* Keystone has no planning documents at this time since support was
  introduced prior to Kilo.

Completion Artifacts:

* https://opendev.org/openstack/devstack/commit/a00e5f8810b6ca3b0b5d63cc228125e19bc91955

kolla
-----

Planning Artifacts:

Completion Artifacts:

kuryr
-----

Planning Artifacts:

* https://blueprints.launchpad.net/kuryr-libnetwork/+spec/deploy-kuryr-libnetwork-api-in-wsgi
* https://blueprints.launchpad.net/fuxi/+spec/goal-deploy-api-in-wsgi
* Only kuryr-libnetwork and fuxi includes an API server of some sort. Other projects do
  not serve APIs, so nothing to be done there.

Completion Artifacts:

magnum
------

Planning Artifacts:

Completion Artifacts:

manila
------

Planning Artifacts:

* https://blueprints.launchpad.net/manila/+spec/wsgi-web-servers-support

Completion Artifacts:

* https://review.opendev.org/#/c/448190/
* https://review.opendev.org/#/c/631338/

mistral
-------

Planning Artifacts:

Completion Artifacts:

monasca
-------

Planning Artifacts:

* https://storyboard.openstack.org/#!/story/2001464

Completion Artifacts:

* https://review.opendev.org/439577
* https://review.opendev.org/436890
* https://review.opendev.org/479447
* https://review.opendev.org/560888

murano
------

Planning Artifacts:

* `murano-api-bp <https://blueprints.launchpad.net/murano/+spec/murano-api-wsgi>`_

Completion Artifacts:

* https://review.opendev.org/#/c/442327/
* https://review.opendev.org/#/c/442936/

neutron
-------

Planning Artifacts:

* https://bugs.launchpad.net/neutron/+bug/1666779

Completion Artifacts:

* Expose neutron app as a wsgi script: https://review.opendev.org/#/c/409351/
* Enable neutron wsgi in devstack: https://review.opendev.org/#/c/439191/

nova
----

Planning Artifacts:

Nova is tracking the work in the `devstack-uwsgi etherpad`_. The placement
service already runs under mod_wsgi in devstack but that will be changed to
uwsgi. There is also a bug in nova-api that needs to be fixed before we can
deploy it under uswgi in devstack for testing.

.. _devstack-uwsgi etherpad: https://etherpad.openstack.org/p/devstack-uwsgi

Completion Artifacts:

* Enable nova wsgi in devstack: https://review.opendev.org/#/c/457715/

octavia
-------

Planning Artifacts:

The octavia API is already implemented as a wsgi application, we just need to
setup the web server integration.  This is work in progress here:
https://review.opendev.org/440934

Completion Artifacts:

* https://review.opendev.org/440934
* https://review.opendev.org/478637

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

* https://blueprints.launchpad.net/openstack-ansible/+spec/goal-deploy-api-in-wsgi

NB Individual roles are dependent on the upstream project achieving the deploy-api-in-wsgi goal.

Completion Artifacts:

OpenStackClient
---------------

Planning Artifacts:

None of the OpenStackClient deliverables have services so no work is required for this goal.

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

* The Release management team doesn't have any API services and therefore
  has nothing to do

Completion Artifacts:

* None

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
 * Enable wsgi jobs: https://review.opendev.org/#/c/454083/

searchlight
-----------

Planning Artifacts:

* https://blueprints.launchpad.net/searchlight/+spec/deploy-via-wsgi

Completion Artifacts:

* Deploy in devstack under  wsgi (reworking to move away from mod_wsgi):
  https://review.opendev.org/#/c/456627/

Security
--------

Planning Artifacts:

Completion Artifacts:

senlin
------

Planning Artifacts:

Completion Artifacts:

shade
-----

Planning Artifacts:

* The shade team does not have any API services and therefore has
  nothing to do.

Completion Artifacts:

* None

solum
-----

Planning Artifacts:

* https://blueprints.launchpad.net/solum/+spec/solum-api-under-wsgi

Completion Artifacts:

* Add wsgi script file: https://review.opendev.org/#/c/448400/
* Enable wsgi on devstack jobs: https://review.opendev.org/#/c/448410/

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

* Support tests for Apache (swift): https://review.opendev.org/#/c/23585/
* Add example Apache config files (swift):
  https://review.opendev.org/#/c/33169/
* enable apache2 server as front end for swift (devstack):
  https://review.opendev.org/#/c/33946/


tacker
------

Planning Artifacts:

Completion Artifacts:

Telemetry
---------

Planning Artifacts:

* panko: https://review.opendev.org/#/c/467796/

Completion Artifacts:

* aodh: https://review.opendev.org/#/c/292245/
* ceilometer: api is deprecated
* gnocchi: out of openstack but already has uwsgi

tricircle
---------

Planning Artifacts:

* None

Completion Artifacts:

* Tricircle Admin API: https://review.opendev.org/#/c/440175/

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

* https://bugs.launchpad.net/trove/+bug/1681478

Completion Artifacts:

* https://review.opendev.org/455477

vitrage
-------

Planning Artifacts:

* None.

Completion Artifacts:

* https://review.opendev.org/#/c/478518/

watcher
-------

Planning Artifacts:

Completion Artifacts:

Watcher API may now works with mod-wsgi.
Patchset https://review.opendev.org/#/c/450740/ provided the following
changes:

* wsgi app script files, to run watcher-api under Apache HTTPd.
* updated devstack plugin to run watcher-api default with mod-wsgi.
* document to deploy watcher-api behind wsgi.

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

* https://blueprints.launchpad.net/zun/+spec/deploy-zun-api-in-wsgi

Completion Artifacts:

* Add wsgi script file: https://review.opendev.org/#/c/437190/
* Enable wsgi on devstack jobs: https://review.opendev.org/#/c/438774/
