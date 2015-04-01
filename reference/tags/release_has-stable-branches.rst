::

  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-release:has-stable-branches`:

===========================
release:has-stable-branches
===========================

This tag is part of the release category of tags, describing the release
model for a given code repository. Development in OpenStack is organized
around 6-month cycles (like "kilo"). Some projects opt to specifically
release a "final" version at the end of the cycle, while some others just
release as-needed.

Stable branches are maintained for OpenStack software and related
libraries. They are cut from the last release in the cycle for a given code
repository.


Rationale
=========

Stable branches are designed to be a safe source of backward-compatible
updates and bugfixes. The existence of a stable branches for a given project
is therefore useful information for our downstream users in their assessment
of OpenStack projects.

This information is distinct from whether or not the project produces a
coordinated release at the end of the 6-month cycle (which is a property
described by the "release:at-6mo-cycle-end" tag).


Requirements
============

* "release:has-stable-branches" projects cut a stable branch from their last
  release in a given development cycle.
* "release:has-stable-branches" projects commit to help maintain the stable
  branches by proposing backports for critical issues and reviewing those.


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


Application to current projects
===============================

.. tagged-projects: release:has-stable-branches
