::

  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-type:horizon-plugin`:

=====================
 type:horizon-plugin
=====================

This tag is part of the type-classification system for projects
managed by the release team. ``type:horizon-plugin`` indicates that a
deliverable is meant to be consumed by :ref:`project-horizon` as a
plug-in, to provide an integrated web UI for a given project.


Application to current projects
===============================

.. tagged-projects:: type:horizon-plugin


Rationale
=========

On `releases.openstack.org`_ we group deliverables by their type. We have a
growing number of projects that are Horizon plugins, and it would be useful
to have them all appear together on the site. Using this tag will help users
of both this site and the releases site identify which deliverables provide
companion functionality for Horizon.


Requirements
============

* The repository contains code meant to be dynamically loaded by
  OpenStack Horizon to provide UI to specific projects.


Tag application process
=======================

Anyone may propose adding or removing this tag to a set of projects by
proposing a change to the openstack/governance repository. The change
is reviewed by the Release Team and the Horizon PTL, and the Technical
Committee finally approves it using its lazy consensus approval rule.


Deprecation
===========

There is no deprecation process for tags in the ``type`` namespace. If
we need to change the type of a project, we can just do that.

.. _releases.openstack.org: http://releases.openstack.org/
