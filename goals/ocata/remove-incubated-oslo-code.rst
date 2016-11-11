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

Reference documentation for the existing Oslo libraries:
http://docs.openstack.org/developer/openstack-projects.html

Links to the Oslo specs covering graduation for various modules
(useful for identifying which library a module moved to, and for
finding "porting notes" written at the time of graduation):
http://specs.openstack.org/openstack/oslo-specs/

Current State / Anticipated Impact
==================================

On 5 Aug 2016 a review of git repositories owned by big tent project
showed:

::

   $ for r in $(list-repos ); do
     [ -d ~/repos/$r ] &&
     (cd ~/repos/$r; [ -d */openstack/common ] &&
         (echo $r; ls */openstack/common; echo )
     ); done

   openstack-dev/heat-cfnclient
   exception.py
   gettextutils.py
   importutils.py
   __init__.py
   jsonutils.py
   local.py
   log.py
   timeutils.py

   openstack-infra/python-storyboardclient
   apiclient
   _i18n.py
   __init__.py
   local.py
   log.py
   uuidutils.py

   openstack-infra/storyboard
   fileutils.py
   fixture
   gettextutils.py
   __init__.py
   jsonutils.py
   local.py
   lockutils.py
   processutils.py
   py3kcompat

   openstack/castellan
   fileutils.py
   _i18n.py
   __init__.py
   local.py

   openstack/designate
   __init__.py
   memorycache.py

   openstack/heat
   crypto
   _i18n.py
   __init__.py
   README

   openstack/python-ceilometerclient
   apiclient
   _i18n.py
   __init__.py

   openstack/python-cinderclient
   apiclient
   __init__.py

   openstack/python-cloudkittyclient
   apiclient
   cliutils.py
   __init__.py

   openstack/python-congressclient
   apiclient
   gettextutils.py
   __init__.py

   openstack/python-glanceclient
   apiclient
   _i18n.py
   __init__.py

   openstack/python-heatclient
   apiclient
   cliutils.py
   _i18n.py
   __init__.py

   openstack/python-manilaclient
   apiclient
   cliutils.py
   _i18n.py
   __init__.py
   uuidutils.py

   openstack/python-mistralclient
   apiclient
   cliutils.py
   gettextutils.py
   importutils.py
   __init__.py
   strutils.py
   uuidutils.py

   openstack/python-monascaclient
   apiclient
   gettextutils.py
   __init__.py
   py3kcompat

   openstack/python-muranoclient
   apiclient
   __init__.py

   openstack/python-saharaclient
   apiclient
   cliutils.py
   _i18n.py
   __init__.py

   openstack/python-searchlightclient
   apiclient
   cliutils.py
   _i18n.py
   __init__.py

   openstack/python-smaugclient
   apiclient
   __init__.py

   openstack/python-solumclient
   apiclient
   cliutils.py
   gettextutils.py
   importutils.py
   __init__.py
   strutils.py
   uuidutils.py

   openstack/python-troveclient
   apiclient
   __init__.py

   openstack/solum
   excutils.py
   fileutils.py
   fixture
   gettextutils.py
   importutils.py
   __init__.py
   local.py
   lockutils.py
   log.py
   strutils.py
   uuidutils.py

   openstack/solum-infra-guestagent
   config
   gettextutils.py
   importutils.py
   __init__.py
   jsonutils.py
   local.py
   log.py
   strutils.py
   timeutils.py

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
  - https://storyboard.openstack.org/#!/story/2000776

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

  The release tools do not use Oslo libraries. We have a few
  references to openstack/common, cleaned up by the patches listed
  below.

Completion Artifacts:

* https://review.openstack.org/392281
* https://review.openstack.org/391715

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

`Designate Planning <https://bugs.launchpad.net/designate/+bug/1637241>`_

Completion Artifacts:

`Designate Completion <https://review.openstack.org/#/c/391247/>`_

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

This work is already done.

Planning Artifacts: None

Completion Artifacts: None

keystone
--------

The keystone repos does not rely on oslo-incubator and consumed
the oslo.* libraries.

Planning Artifacts:

  None

Completion Artifacts:

  None

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

This work is already done.

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

Planning Artifacts: https://bugs.launchpad.net/tripleo/+bug/1636767

Completion Artifacts: https://review.openstack.org/390808

trove
-----

Planning Artifacts:

`Trove Client Planning <https://bugs.launchpad.net/python-troveclient/+bug/1638627>`_

Completion Artifacts:

`Trove Client Commit <https://review.openstack.org/#/c/296667/>`_

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
