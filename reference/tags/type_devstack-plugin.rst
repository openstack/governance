::

  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-type:devstack-plugin`:

======================
 type:devstack-plugin
======================

This tag is part of the type-classification system for projects
managed by the release team. ``type:devstack-plugin`` indicates that a
deliverable is meant to be consumed by :ref:`project-devstack` as a
plug-in, to provide an integrated devtest environment for a given project.


Application to current projects
===============================

.. tagged-projects:: type:devstack-plugin


Rationale
=========

We have a growing number of projects that are Devstack plugins, and it would be
useful to have them easily grouped together. Using this tag will help both
users and automated tooling identify which deliverables provide companion
functionality for Devstack.


Requirements
============

* The repository contains code meant to be dynamically loaded by
  Devstack to provide installation and configuration for specific projects in
  devtest environments.


Tag application process
=======================

Anyone may propose adding or removing this tag to a set of projects by
proposing a change to the openstack/governance repository. The change
is reviewed by the Release Team and the QA PTL, and the Technical
Committee finally approves it using its lazy consensus approval rule.


Deprecation
===========

There is no deprecation process for tags in the ``type`` namespace. If
we need to change the type of a project, we can just do that.

.. _releases.openstack.org: http://releases.openstack.org/
