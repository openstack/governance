.. -*- mode: rst -*-

============================
Enable mutable configuration
============================

There is a strong desire from operators to be able to change configuration
options without a service restart. For example, to selectively enable DEBUG
logging in response to observed issues. As of OpenStack Newton, config
options can be marked as 'mutable'. This means they can be reloaded (usually
via SIGHUP) at runtime, without a service restart. However, each project has
to be enabled before this will work and some care needs to be taken over how
each option is used before it can safely be marked mutable. For more details
please refer to `Enabling your project for mutable config`_

Champion
========

Goals need a main driver to project-manage them to completion. Project teams
need assistance, reminders and sometimes direct help in order for them to
complete the goals.

ChangBo Guo (gcb) has volunteered to drive this goal.

Gerrit Topic
============

To facilitate tracking, commits related to this goal should use the
gerrit topic::

  mutable-config

Completion Criteria
===================

Each project service could be turned on/off debug logging without restart

#. Support reloading configuration options at runtime, without a service
   restart
#. Toggle the debug option for each service at runtime

References
==========

* `Original Discussion`_
* `Enabling your project for mutable config`_
* `Example of enabling projects`_

.. _Original Discussion: https://etherpad.openstack.org/p/mitaka-cross-project-dynamic-config-services
.. _Enabling your project for mutable config: https://docs.openstack.org/oslo.config/latest/reference/mutable.html
.. _Example of enabling projects: https://review.openstack.org/#/q/topic:bp/mutable-config+(status:open+OR+status:merged)

Current State / Anticipated Impact
==================================

oslo.config and oslo.service have implemented basic functions and we have
enabled Nova to support mutable configuration and mark some configuration
option like CONF.libvirt.live_migration_progress_timeout as 'mutable'.

Project Teams
=============

barbican
--------

Planning Artifacts:

Completion Artifacts:

blazar
------

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

congress
--------

Planning Artifacts:

Completion Artifacts:

cyborg
------

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

loci
----

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

masakari
--------

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

OpenStack-Helm
--------------

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

OpenStackSDK
------------

Planning Artifacts:

Completion Artifacts:

oslo
----

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

Completion Artifacts:

storlets
--------

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
