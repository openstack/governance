::

  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-release:at-6mo-cycle-end`:

========================
release:at-6mo-cycle-end
========================

This tag is part of the release category of tags, describing the release
model for a given code repository. Development in OpenStack is organized
around 6-month cycles (like "kilo"), and some projects opt to specifically
release a "final" version at the very end of the development cycles.

The "release:at-6mo-cycle-end" tag describes which projects specifically
commit to producing a coordinated release at the end of the 6-month cycle.
Note that it doesn't prevent those projects from also producing intermediary
releases in the middle of a development cycle.


Application to current projects
===============================

.. tagged-projects:: release:at-6mo-cycle-end


Rationale
=========

At the end of every 6-month cycle a number of projects release at the same
time, providing a convenient reference point for downstream teams (stable
branch maintenance, vulnerability management) and downstream users (in
particular packagers of OpenStack distributions).

Describing which projects commit to follow that model is therefore a useful
piece of information to provide to our users.

Note that it is slightly different from projects which maintain stable
branches (described using the "release:has-stable-branches" tag). Stable
branches are cut from the last release in the cycle, whether the project
releases at the very end of the cycle or not.

Requirements
============

* "release:at-6mo-cycle-end" projects commit to produce a release to match
  the end of the 6-month development cycle.


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
