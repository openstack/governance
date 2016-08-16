.. -*- mode: rst -*-

======================================
 Remove Copies of Incubated Oslo Code
======================================

The Oslo team has moved all previously incubated code from the
``openstack/oslo-incubator`` repository into separate library
repositories and released those libraries to the Python Package
Index. Many of our big tent project teams are still using the old,
unsupported, incubated versions of the code. The Oslo team has been
working to remove that incubated code from projects, and the time has
come to finish that work.

Gerrit Topic
============

To facilitate tracking, commits related to this goal should use the
gerrit topic::

  goal-remove-incubated-oslo-code

Completion Criteria
===================

For all projects:

#. The project correctly declares dependencies for all Oslo libraries
   replacing the incubated version of older Oslo code.
#. The project no longer contains copies of the graduated code.
#. Any ``openstack/common`` directories are removed.

For projects using the ``apiclient`` module, which was deprecated by
the Oslo team:

#. The copy of ``apiclient`` from the ``openstack/common`` module has
   been moved to a new location within the code base so that
   ``openstack/common`` can be deleted.

References
==========

An estimated list of repositories owned by big tent teams with
incubated Oslo code as of 5 August 2016:
http://paste.openstack.org/show/550418/

Reference documentation for the existing Oslo libraries:
http://docs.openstack.org/developer/openstack-projects.html

Links to the Oslo specs covering graduation for various modules
(useful for identifying which library a module moved to, and for
finding "porting notes" written at the time of graduation):
http://specs.openstack.org/openstack/oslo-specs/

Project Teams
=============

Chef OpenStack
--------------

Planning Artifacts:

Completion Artifacts:

Community App Catalog
---------------------

Planning Artifacts:

Completion Artifacts:

Documentation
-------------

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

OpenStack Charms
----------------

Planning Artifacts:

Completion Artifacts:

OpenStack UX
------------

Planning Artifacts:

Completion Artifacts:

OpenStack client
----------------

Planning Artifacts:

Completion Artifacts:

OpenStackAnsible
----------------

Planning Artifacts:

Completion Artifacts:

OpenStackSalt
-------------

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

RefStack
--------

Planning Artifacts:

Completion Artifacts:

Release Management
------------------

Planning Artifacts:

Completion Artifacts:

Security
--------

Planning Artifacts:

Completion Artifacts:

Stable branch maintenance
-------------------------

Planning Artifacts:

Completion Artifacts:

Telemetry
---------

Planning Artifacts:

Completion Artifacts:

astara
------

Planning Artifacts:

Completion Artifacts:

barbican
--------

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

designate
---------

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

ironic
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

oslo
----

Planning Artifacts:

Completion Artifacts:

rally
-----

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

senlin
------

Planning Artifacts:

Completion Artifacts:

smaug
-----

Planning Artifacts:

Completion Artifacts:

solum
-----

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
