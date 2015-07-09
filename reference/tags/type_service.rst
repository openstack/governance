::

  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-type:service`:

==============
 type:service
==============

This tag is part of the type-classification system for projects
managed by the release team. ``type:service`` indicates that a project
provides a long-running service, usually with a REST API.


Application to current projects
===============================

.. tagged-projects:: type:service


Rationale
=========

The release team is building some tools for automating common release
processes. Some of these tools will look at the type of the repository
to make choices, including skipping or including the repository or
applying different criteria or process steps. For example, most of the
service projects use pre-versioning rather than post-versioning, and
so some of the release tools need to take different steps when
processing a service project.


Requirements
============

* The repository contains software that meets the description of
  "service" above.


Tag application process
=======================

Anyone may propose adding or removing this tag to a set of projects by
proposing a change to the openstack/governance repository. The change
is reviewed by the Release Team and Technical Committee and approved
using standard resolution approval rules, including discussion at at
least one Technical Committee public IRC meeting.

Deprecation
===========

There is no deprecation process for tags in the ``type`` namespace. If
we need to change the type of a project, we can just do that.
