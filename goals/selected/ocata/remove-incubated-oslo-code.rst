.. -*- mode: rst -*-

======================================
 Remove Copies of Incubated Oslo Code
======================================

The Oslo team has moved all previously incubated code from the
``openstack/oslo-incubator`` repository into separate library
repositories and released those libraries to the Python Package
Index. Many of our official project teams are still using the old,
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

On 5 Aug 2016 a review of git repositories owned by official projects
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

The Chef cookbooks do not use any Python code directly, they consume
upstream packages, and thus are not affected by this goal.

Planning Artifacts:

  None

Completion Artifacts:

  None

Community App Catalog
---------------------

The Community App Catalog does not rely on oslo-incubator
or openstack/common.

Planning Artifacts:

  None

Completion Artifacts:

  None

Documentation
-------------

Planning Artifacts:

  The Documentation tools do not use anymore Oslo libraries. We had
  one references to openstack/common, cleaned up by the patch listed
  below.

Completion Artifacts:

* https://review.opendev.org/#/c/391707/

I18n
----

OpenStack I18n does not use oslo-incubator or any openstack/common modules.

Planning Artifacts:

  None

Completion Artifacts:

  None

Infrastructure
--------------

Planning Artifacts:
  - https://storyboard.openstack.org/#!/story/2000776

Completion Artifacts:
  - https://review.opendev.org/394436
  - https://review.opendev.org/394508
  - https://review.opendev.org/394509
  - https://review.opendev.org/394570
  - https://review.opendev.org/394571
  - https://review.opendev.org/395116

OpenStack Charms
----------------

Planning Artifacts:

Completion Artifacts:

OpenStack UX
------------

OpenStack UX does not use oslo-incubator or any openstack/common modules.

Planning Artifacts:

None

Completion Artifacts:

None

OpenStack client
----------------

OpenStackClient does not use oslo-incubator or any openstack/common modules.

Planning Artifacts:

None

Completion Artifacts:

None

OpenStackAnsible
----------------

Planning Artifacts:

  OpenStack-Ansible is a downstream consumer, as a result
  OpenStack-Ansible does not carry or consume Oslo Incubator code
  directly. No work required.

Completion Artifacts:

  N/A

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

The puppet modules do not rely on oslo-incubator or openstack/common.

Planning Artifacts:

  None

Completion Artifacts:

  None

Quality Assurance
-----------------

Quality Assurance does not use oslo-incubator or any openstack/common modules.

Planning Artifacts:

None

Completion Artifacts:

None

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

* https://review.opendev.org/392281
* https://review.opendev.org/391715

Security
--------

Planning Artifacts:

Completion Artifacts:

* Anchor: No incubated oslo code
* Bandit: No incubated oslo code
* Syntribos: No incubated oslo code

Stable branch maintenance
-------------------------

Planning Artifacts:

    The stable team doesn't have any code repositories and therefore has
    nothing to do.  It could be argued that the stable team is responsible for
    the stable branches of all projects but nature of the stable projects
    precludes code refactors.

Completion Artifacts:

    Not Applicable

Telemetry
---------

Planning Artifacts:

Completion Artifacts:

  https://review.opendev.org/#/c/391865/

barbican
--------

Planning Artifacts:

* https://bugs.launchpad.net/castellan/+bug/1643909

Completion Artifacts:

* https://review.opendev.org/#/c/390809/

cinder
------

Planning Artifacts:

Completion Artifacts:

cinder: NA
os-brick: NA
python-cinderclient: https://review.opendev.org/#/c/393610/
python-brick-cinderclient-ext: NA

cloudkitty
----------

Planning Artifacts:

Completion Artifacts:
cloudkitty: NA
python-cloudkittyclient: https://review.opendev.org/#/c/391885

congress
--------

Planning Artifacts:

Completion Artifacts:

* https://review.opendev.org/#/c/396501/

designate
---------

Planning Artifacts:

`Designate Planning <https://bugs.launchpad.net/designate/+bug/1637241>`_

Completion Artifacts:

`Designate Completion <https://review.opendev.org/#/c/391247/>`_

dragonflow
----------

The Dragonflow project does not use oslo-incubator or any openstack/common
modules. There was one references to openstack/common, cleaned up by
the patch listed below.

Planning Artifacts: None

Completion Artifacts:

* https://review.opendev.org/#/c/385391/

ec2-api
-------

This work is already done.

Planning Artifacts:

Completion Artifacts:

`EC2-API Completion <https://review.opendev.org/#/c/297305/>`_

freezer
-------

Freezer repos do not rely on oslo-incubator and use oslo.* libraries.

Planning Artifacts:

  None

Completion Artifacts:

  None

fuel
----

Planning Artifacts:

Completion Artifacts:

glance
------

Planning Artifacts:

* https://bugs.launchpad.net/glance/+bug/1639487

Completion Artifacts:

* https://review.opendev.org/380452

* https://review.opendev.org/394780

heat
----

Planning Artifacts:

None

Completion Artifacts:

Already removed from heat and heat-cfnclient.

python-heatclient:
https://review.opendev.org/#/q/project:openstack/python-heatclient+topic:goal-remove-incubated-oslo-code

horizon
-------

The Horizon repos does not rely on oslo-incubator and consumes
the oslo.* libraries.

Planning Artifacts: None

Completion Artifacts: None

ironic
------

This work is already done.

Planning Artifacts: None

Completion Artifacts: None

karbor
------

This work is already done.

Planning Artifacts:

   None

Completion Artifacts:

   `Karbor Client <https://review.opendev.org/#/c/378212/>`_

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

The kolla repos does not rely on oslo-incubator and consumed the oslo.*
libraries.

Planning Artifacts:

  None

Completion Artifacts:

  None

kuryr
-----

Planning Artifacts:

Completion Artifacts:

magnum
------

This work is already done.

Planning Artifacts: None

Completion Artifacts: None

manila
------

This work is already done.

mistral
-------

This work is already done.

Completion Artifacts:

python-mistralclient:
https://review.opendev.org/#/c/393076/
https://review.opendev.org/#/c/393084/
https://review.opendev.org/#/c/395055/
https://review.opendev.org/#/c/395082/

monasca
-------

Monasca no longer uses oslo-incubated code. We had a few references
to openstack/common, that were cleaned up by the patches listed below.

Planning Artifacts:

None

Completion Artifacts:

* https://review.opendev.org/#/c/395021/
* https://review.opendev.org/#/c/395014/
* https://review.opendev.org/#/c/395009/

murano
------

Planning Artifacts:

Completion Artifacts:

* https://review.opendev.org/#/c/395039/

neutron
-------

The neutron repos do not rely on oslo-incubator.
They consume the oslo.* libraries.

Planning Artifacts:

None

Completion Artifacts:

https://bugs.launchpad.net/neutron/+bug/1639103

nova
----

Planning Artifacts:

None

Completion Artifacts:

`<https://review.opendev.org/#/c/287753/>`_

octavia
-------

The octavia project does not use oslo incubator and the last references
were removed in the patch listed below.
Technically this was done while we were part of neutron, but documenting
here for clarity.

Planning Artifacts:

None

Completion Artifacts:

https://review.opendev.org/#/c/393564/

oslo
----

History:

* http://www.slideshare.net/doughellmann/taking-the-long-view-how-the-oslo-program-reduces-technical-debt

Planning Artifacts:

* https://github.com/openstack/oslo-specs/blob/master/specs/policy/incubator.rst

Completion Artifacts:

* https://github.com/openstack/oslo-specs/blob/master/specs/policy/incubator.rst#revision-history (delete
  graduating modules immediately after the library is released)
* http://lists.openstack.org/pipermail/openstack-dev/2016-June/097228.html (the
  closing/shutdown of the oslo-incubator, what's leftover is now just a set
  of tools for PTL or other community folks in oslo.tools)
* https://review.opendev.org/#/c/323706/ and
  https://review.opendev.org/#/c/320680/ (farewell reviews)

rally
-----

Planning Artifacts:

None

Completion Artifacts:

`Rally Completion <https://review.opendev.org/#/c/152847/>`_

sahara
------

Planning Artifacts: None

Completion Artifacts:

`Sahara Completion <https://review.opendev.org/#/c/351376/>`_

searchlight
-----------

Planning Artifacts:

Completion Artifacts:

`Searchlight Completion <https://review.opendev.org/#/c/396695/>`_

senlin
------

The Senlin repos don't rely on oslo-incubator and are consuming
the oslo.* libraries.

Planning Artifacts:

None

Completion Artifacts:

None

solum
-----

Solum repos do not rely on oslo-incubator and are consuming oslo.*
libraries

Planning Artifacts:

None

Completion Artifacts:

* https://review.opendev.org/#/c/391337/
* https://review.opendev.org/#/c/388675/
* https://review.opendev.org/#/c/388536/
* https://review.opendev.org/#/c/365211/
* https://review.opendev.org/#/c/365208/
* https://review.opendev.org/#/c/365024/
* https://review.opendev.org/#/c/389502/


swift
-----

The swift repos do not rely on oslo-incubator.

Planning Artifacts: None

Completion Artifacts: None

tacker
------

The Tacker repos do not rely on oslo-incubator.
They consume the oslo.* libraries.

Planning Artifacts:

None

Completion Artifacts:

None

tricircle
---------

Tricircle doesn't rely on oslo-incubator or any openstack/common modules,
it is consuming the oslo.* libraries.

Planning Artifacts:

None

Completion Artifacts:

None

tripleo
-------

Planning Artifacts: https://bugs.launchpad.net/tripleo/+bug/1636767

Completion Artifacts: https://review.opendev.org/390808

trove
-----

Planning Artifacts:

`Trove Client Planning <https://bugs.launchpad.net/python-troveclient/+bug/1638627>`_

Completion Artifacts:

`Trove Client Commit <https://review.opendev.org/#/c/396267/>`_

vitrage
-------

The Vitrage repos do not rely on oslo-incubator.
They consume the oslo.* libraries.

Planning Artifacts:

None

Completion Artifacts:

None

watcher
-------

The Watcher repos don't rely on oslo-incubator and are consuming
the oslo.* libraries.

Planning Artifacts:

None

Completion Artifacts:

None

winstackers
-----------

The Winstackers repos does not rely on oslo-incubator and consumes the oslo.*
libraries.

Planning Artifacts: None

Completion Artifacts:

* https://review.opendev.org/#/c/398760/
* https://review.opendev.org/#/c/398758/

zaqar
-----

The Zaqar repo doesn't rely on oslo-incubator and are consuming
the oslo.* libraries.

Planning Artifacts:

Completion Artifacts:

`Zaqar Client Commit <https://review.opendev.org/388638/>`_

zun
-----

The zun repos does not rely on oslo-incubator and consumed the oslo.*
libraries.

Planning Artifacts:

  None

Completion Artifacts:

  None
