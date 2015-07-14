::

  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-release:managed`:

===============
release:managed
===============

This tag is part of the release category of tags, describing the release
model for a given code repository. Projects tagged with "release:managed" tag
are those who are directly managed by the Release Management team.


Application to current projects
===============================

.. tagged-projects:: release:managed


Rationale
=========

The OpenStack `Release Management team`_ defines release models and applies
a number of strict release processes to ensure that a satisfying release
will be produced for all the projects it manages. The team has a track
record with the handling of all "integrated releases" up to the Kilo cycle.

Communicating the information of which code repositories are actually still
directly handled by that team is therefore useful to downstream stakeholders,
especially packagers.

.. _Release Management Team: https://wiki.openstack.org/wiki/Release_Cycle_Management

Requirements
============

* "release:managed" projects commit to follow a predefined release model.
* Where appropriate, "release:managed" projects accept to submit to release
  management team oversight starting at Feature Freeze and up to final release.
* "release:managed" projects delegate their tagging rights to the release
  management team.
* "release:managed" projects commit to having their release team liaison
  available on milestone and release weeks, to ensure proper coordination.
* The release management team needs to accept to handle release process for
  those projects.


Tag application process
=======================

The release management team (ultimately represented by the release management
PTL) is responsible for maintaining tags in the "release" category, so that
they match the current release model followed by each code repository.

There is no need to apply for addition/removal. Changes externally proposed
will be reviewed and approved by the release management team, ultimately
represented by the release management PTL.


Attributes
==========

Tags in the "release" category do not use attributes.
