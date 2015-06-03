::

  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-release:independent`:

===================
release:independent
===================

This tag is part of the release category of tags, describing the release
model for a given code repository. Projects with the "release:independent"
tag produce releases as-needed. Those are generally not coordinated with
any other project. Releasing in this fashion doesn't prevent projects from
also releasing a "final" release at the end of a development cycle.


Application to current projects
===============================

.. tagged-projects:: release:independent


Rationale
=========

Some projects opt to ship features to users more often than every 6 months.
These out-of-cycle releases are generally not supported by teams like the
stable branch maintenance team or the vulnerability management team. Knowing
which projects follow that model is therefore significant for our downstream
users, especially operators and packagers.


Requirements
============

* "release:independent" projects produce releases from time to time.


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
