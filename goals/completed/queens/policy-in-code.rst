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
   <https://docs.openstack.org/nova/queens/configuration/sample-policy.html>`_
   to assist operators.
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

Champion
========

Goals need a main driver to project-manage them to completion. Project teams
need assistance, reminders and sometimes direct help in order for them to
complete the goals.

Lance Bragstad (lbragstad) has volunteered to drive this goal.


Gerrit Topic
============

To facilitate tracking, commits related to this goal should use the
gerrit topic::

  policy-and-docs-in-code

Completion Criteria
===================

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

* `barbican implementation <https://review.opendev.org/#/q/topic:policy-and-docs-in-code+project:openstack/barbican>`_

Chef OpenStack
--------------

Goal not applicable.

cinder
------

Planning Artifacts:

* `cinder policy-in-code blueprint <https://blueprints.launchpad.net/cinder/+spec/policy-in-code>`_

Completion Artifacts:

* `cinder policy-in-code implementation <https://review.opendev.org/#/q/topic:policy-and-docs-in-code+project:openstack/cinder>`_
* `cinder documentation update <https://review.opendev.org/#/c/512187/>`_

cloudkitty
----------

Planning Artifacts:

Cloudkitty used this document as the planning artifact for this goal.

Completion Artifacts:

* `cloudkitty implementation <https://review.opendev.org/#/q/topic:policy-and-docs-in-code+(status:open+OR+status:merged)+project:openstack/cloudkitty>`_

congress
--------

Planning Artifacts:

* `congress planning <https://bugs.launchpad.net/congress/+bug/1724714>`_

Completion Artifacts:

* `congress implementation <https://review.opendev.org/#/q/topic:policy-and-docs-in-code+(status:open+OR+status:merged)+project:openstack/congress>`_

designate
---------

Planning Artifacts:

* `designate policy-in-code blueprint <https://blueprints.launchpad.net/designate/+spec/policy-in-code>`_

Completion Artifacts:

* `designate documented policy-in-code implementation <https://review.opendev.org/#/q/status:merged+project:openstack/designate+branch:master+topic:policy-and-docs-in-code>`_
* `designate policy documentation <https://docs.openstack.org/designate/latest/admin/policy.html>`_

Documentation
-------------

Goal not applicable.

dragonflow
----------

Goal not applicable.

ec2-api
-------

Planning Artifacts:

Completion Artifacts:

freezer
-------

Planning Artifacts:

Completion Artifacts:

* `Freezer API implementation <https://review.opendev.org/#/q/topic:policy-and-docs-in-code+(status:open+OR+status:merged)+project:openstack/freezer-api>`_

fuel
----

Planning Artifacts:

Completion Artifacts:

glance
------

Planning Artifacts:

* `Spec Lite: Community Goal: Register and Document Policy in Code
  <http://specs.openstack.org/openstack/glance-specs/specs/queens/approved/glance/spec-lite-policy-and-docs-in-code.html>`_

Completion Artifacts:

* Glance did not complete this goal during the Queens cycle.  We will be
  discussing refactoring the way Glance handles policies at the Rocky PTG.
  In light of that (and in light of the fact that the development team is
  currently under-powered), we felt that it did not make sense to work on
  this goal during Queens.

  The `implementation <https://review.opendev.org/#/c/693129/>`_ for moving
  policy into code was completed in Ussuri. Work remains to document each
  policy.

heat
----

Planning Artifacts:

* `heat specification <https://specs.openstack.org/openstack/heat-specs/specs/queens/policy-in-code.html>`_

Completion Artifacts:

* `heat implementation <https://review.opendev.org/#/q/(status:open+OR+status:merged)+project:openstack/heat++%22policy+in+code%22>`_

horizon
-------

Goal not appliable.

I18n
----

Goal not applicable.

Infrastructure
--------------

Planning Artifacts:

Completion Artifacts:

ironic
------

The ironic project moved default policies into code during the Newton release.
The Queens release will focus on documenting policies and using the new
``DocumentedRuleDefault`` object.

Planning Artifacts:

* `ironic policy-in-code bug <https://bugs.launchpad.net/ironic/+bug/1526752>`_
* `ironic documenting policy bug <https://bugs.launchpad.net/ironic/+bug/1716772>`_

Completion Artifacts:

* `ironic documented policy-in-code implementation <https://review.opendev.org/#/c/502519/>`_
* `ironic policy documentation <https://docs.openstack.org/ironic/latest/configuration/policy.html>`_

ironic-inspector
----------------

Until Queens, ironic-inspector project had no configurable API access policies.
They were implemented in Queens, with documented policies in code
from the start.

Planning Artifacts:

* `inspector policy-in-code bug <https://bugs.launchpad.net/ironic-inspector/+bug/1719812>`_

Completion Artifacts:

* `inspector policies implementation <https://review.opendev.org/#/c/507826/>`_
* `inspector policies documentation <https://docs.openstack.org/ironic-inspector/latest/configuration/policy.html>`_

karbor
------

Planning Artifacts:

Completion Artifacts:

keystone
--------

The keystone project completed this work in the Pike release.

Planning Artifacts:

* `keystone policy-in-code specification <http://specs.openstack.org/openstack/keystone-specs/specs/keystone/pike/policy-in-code.html>`_
* `keystone policy-docs specification <http://specs.openstack.org/openstack/keystone-specs/specs/keystone/pike/policy-docs.html>`_

Completion Artifacts:

* `keystone policy-in-code implementation <https://review.opendev.org/#/q/status:merged+project:openstack/keystone+branch:master+topic:bp/policy-in-code>`_
* `keystone policy-docs implementation <https://review.opendev.org/#/q/status:merged+project:openstack/keystone+branch:master+topic:bp/policy-docs>`_

kolla
-----

Goal not applicable.

kuryr
-----

Goal not applicable.

magnum
------

Planning Artifacts:

* `magnum blueprint <https://blueprints.launchpad.net/magnum/+spec/policy-in-code>`_

Completion Artifacts:

* `magnum implementation <https://review.opendev.org/#/q/topic:policy-and-docs-in-code+status:merged+project:openstack/magnum>`_

manila
------

Planning Artifacts:

* `manila blueprint <https://blueprints.launchpad.net/manila/+spec/policy-in-code>`_

Completion Artifacts:

* `manila implementation <https://review.opendev.org/#/q/status:merged+project:openstack/manila+branch:master+topic:policy-and-docs-in-code>`_

mistral
-------

Planning Artifacts:

* mistral used this document as the planning artifact

Completion Artifacts:

* `mistral policy-in-code implementation <https://review.opendev.org/#/q/project:openstack/mistral++topic:policy-and-docs-in-code+status:merged>`_
* `mistral policy documentation <https://docs.openstack.org/mistral/latest/configuration/policy-guide.html>`_

monasca
-------

Planning Artifacts:

Completion Artifacts:

murano
------

Planning Artifacts:

Murano implemented this toward the end of Pike-2 milestone.

The blueprint used was:
https://blueprints.launchpad.net/murano/+spec/policy-in-code

Completion Artifacts:

The final RBAC patch in the chain was:
https://review.opendev.org/#/c/473562/

The policy documentation is available here:
https://docs.openstack.org/murano/latest/admin/murano_policies.html

neutron
-------

Neutron implemented this towards the end of the Stein-2 milestone.

Planning Artifacts:

* `neutron policy-in-code specification <https://blueprints.launchpad.net/neutron/+spec/neutron-policy-in-code>`_

Completion Artifacts:

* `neutron policy-in-code implementation <https://review.opendev.org/#/c/585037/>`_

nova
----

Note that nova moved policy into code during the Newton release and formally
documented it in Pike.

Planning Artifacts:

* `nova policy-in-code specification <http://specs.openstack.org/openstack/nova-specs/specs/newton/implemented/policy-in-code.html>`_
* `nova policy-docs specification <http://specs.openstack.org/openstack/nova-specs/specs/pike/approved/policy-docs.html>`_

Completion Artifacts:

* `nova policy-in-code implementation <https://review.opendev.org/#/q/topic:bp/policy-in-code+project:openstack/nova+status:merged>`_
* `nova policy-docs implementation <https://review.opendev.org/#/q/topic:bp/policy-docs+project:openstack/nova+status:merged>`_

octavia
-------

Planning Artifacts:

Octavia implemented this as part of our new endpoint in Pike.

The tracking bug was:
https://bugs.launchpad.net/octavia/+bug/1690481

Completion Artifacts:

The final RBAC patch in the chain merged while Pike was still in development:
https://review.opendev.org/#/c/475980/

The policy documentation is available here:
https://docs.openstack.org/octavia/latest/configuration/policy.html

OpenStack Charms
----------------

Goal not applicable.

OpenStackAnsible
----------------

Planning Artifacts:

We'll have to adapt on the other project's completion artifacts, and everything
will be analysed case by case.

Completion Artifacts:

We already have a mechanism to adapt to policy in code (see our Keystone Role).

OpenStackClient
---------------

Goal not applicable.

oslo
----

Goal not applicable.

Packaging-deb
-------------

Goal not applicable.

Packaging-rpm
-------------

Goal not applicable.

Puppet OpenStack
----------------

Goal not applicable.

Quality Assurance
-----------------

Goal not applicable.

rally
-----

Goal not applicable.

RefStack
--------

Goal not applicable.

Release Management
------------------

Goal not applicable.

requirements
------------

Goal not applicable.

sahara
------

Planning Artifacts:

We used the community goal document found in
https://governance.openstack.org/tc/goals/queens/policy-in-code.html as
planning artifact.

Completion Artifacts:

The goal was implemented in https://review.opendev.org/#/c/503221/ and can be
marked as done.

searchlight
-----------

Planning Artifacts:

* Work was done without the need for a bug / blueprint

Completion Artifacts:

* `searchlight policy-in-code implementation <https://review.opendev.org/#/q/status:merged+project:openstack/searchlight+branch:master+topic:policy-and-docs-in-code>`_
* `searchlight policy documentation <https://docs.openstack.org/searchlight/latest/configuration/policy.html>`_


Security
--------

Goal not applicable.

senlin
------

Planning Artifacts:

Completion Artifacts:

* `senlin implementation <https://review.opendev.org/#/q/topic:policy-and-docs-in-code+project:openstack/senlin+status:merged>`_

shade
-----

Goal not applicable.

solum
-----

Planning Artifacts:

* `solum blueprint <https://blueprints.launchpad.net/solum/+spec/policy-in-code>`_

Completion Artifacts:

* `solum implementation <https://review.opendev.org/#/q/status:merged+project:openstack/solum+branch:master+topic:bp/policy-in-code>`_

Stable branch maintenance
-------------------------

Goal not applicable.

storlets
--------

Goal not applicable.

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

This document was used as the planning document for the Telemetry project.

Completion Artifacts:

* `panko implementation <https://review.opendev.org/#/q/topic:policy-and-docs-in-code+status:merged+project:openstack/panko>`_

* `aodh implementation <https://review.opendev.org/#/q/topic:policy-and-docs-in-code+status:merged+project:openstack/aodh>`_

tricircle
---------

Planning Artifacts:

This document was used as the planning artifact for tricircle.

Completion Artifacts:

* `policy-in-code implementation <https://review.opendev.org/#/q/topic:policy-and-docs-in-code+status:merged+project:openstack/tricircle>`_

tripleo
-------

Goal not applicable.

trove
-----

Planning Artifacts:

We used the community goal document found in
https://governance.openstack.org/tc/goals/queens/policy-in-code.html as
planning artifact.

Completion Artifacts:

* `trove policy-in-code implementation <https://review.opendev.org/#/q/project:openstack/trove+topic:policy-and-docs-in-code+status:merged>`_

vitrage
-------

Planning Artifacts:

Completion Artifacts:

* https://review.opendev.org/#/c/509217/

watcher
-------

Planning Artifacts:

* `watcher policy-in-code blueprint <https://blueprints.launchpad.net/watcher/+spec/policy-and-docs-in-code>`_

Completion Artifacts:

* `watcher policy-in-code implementation <https://review.opendev.org/#/q/project:+openstack/watcher+topic:policy-and-docs-in-code+status:merged>`_

winstackers
-----------

Goal not applicable.

zaqar
-----

Planning Artifacts:

Completion Artifacts:

zun
---

Planning Artifacts:

TBD, checking with the Zun team to see if they want a specification for this or
if this can serve as the planning artifact.

Completion Artifacts:

* `zun implementation <https://review.opendev.org/#/q/topic:policy-and-docs-in-code+status:merged+project:openstack/zun>`_
