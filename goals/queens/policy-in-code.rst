.. -*- mode: rst -*-

====================================
Register and Document Policy in Code
====================================

OpenStack services typically have a file that describes and enforces policy or
Role Based Access Control for the APIs of that service. The file is usually
maintained in the project source and documents the default policy values. The
goal here would be to move default policy definitions from file-based
maintenance to registering them in code. This is very similar to how we treat
default configuration values.

By registering and documenting default policy in code, we see the following
benefits for operators and developers:

#. The policy file can be removed for deployments that don't modify any default
   policies. This continues to move configuration out of `/etc/$PROJECT/`
   directories and into code, which naturally enables easier upgrades.
#. Operators can remove default checks from policy files. The result is that
   their policy file only contains the overridden policies they need for their
   deployment. This makes auditing and policy maintenance easier.
#. Tooling can be used to generate sample policy files.
#. Tooling can be used to generate complete policy files that include overrides
   from a specific policy file.
#. Documentation describing each policy is `generated and available
   <https://docs.openstack.org/developer/nova/sample_policy.html>`_ to assist
   operators.
#. Project developers have a way to communicate changing defaults to operators
   through a library. Think of this like marking configuration values for
   deprecation or removal. The important bit is that we have a programmatic way
   to signal those changes for operators.
#. Project developers use the process of moving defaults into code and
   documenting them as an exercise for understanding the default policies
   within the project and how they might be improved.

By doing this, it becomes easier for developers and operators to move towards a
more flexible set of roles by introducing better, or more granular, defaults.
The change is backwards compatible and allows operators to continue overriding
policies their deployment relies on.


Gerrit Topic
============

To facilitate tracking, commits related to this goal should use the
gerrit topic::

  policy-and-docs-in-code

Completion Criteria
===================

Enumerate the items that must be true in order to call the goal
"completed" for a given project.

For all projects:

#. Use `oslo.policy` to register default policies in code that map to the
   defaults described in policy files.
#. Each policy must contain a `description` that describes the API the policy
   is intended to protect.
#. Ensure default policies that are registered in code can be overridden by
   operators.
#. Ensure `oslo.policy` endpoints can be used to leverage tooling for
   generating default policy files, or producing custom policy files that
   consist of defaults in addition to overrides specified by operators in
   existing policy files. This mainly consists of exposing `oslo.policy`
   endpoints in each project's `setup.cfg` file. An example can be found in
   some of the existing `services
   <https://github.com/openstack/nova/blob/15.0.0/setup.cfg#L42>`_.

References
==========

This effort was discussed during the Newton design summit and has been
completed by a few projects already. The `etherpad
<https://etherpad.openstack.org/p/newton-oslo-policy-default-embedded>`_
capturing the original discussion describes the approach.

The following specifications detail the work done already by specific projects:

* `Nova policy-in-code specification <http://specs.openstack.org/openstack/nova-specs/specs/newton/implemented/policy-in-code.html>`_
* `Nova policy-docs specification <http://specs.openstack.org/openstack/nova-specs/specs/pike/approved/policy-docs.html>`_
* `Keystone policy-in-code specification <http://specs.openstack.org/openstack/keystone-specs/specs/keystone/pike/policy-in-code.html>`_
* `Keystone policy-docs specification <http://specs.openstack.org/openstack/keystone-specs/specs/keystone/pike/policy-docs.html>`_

Current State / Anticipated Impact
==================================

Note that this goal does not require the changing of default policies and only
specifies moving the defaults into code and documenting them. If at a later
time the community comes together and agrees upon a direction using specific
defaults, we can leverage this work to make that transition easier.

As noted in the section above, the nova and keystone projects have already
completed these items as of the Pike release. The patterns used to implement
policy and policy documentation in code by these projects can serve as a
reference for other projects looking to complete the aforementioned goals.

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

shade
-----

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
