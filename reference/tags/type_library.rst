::

  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-type:library`:

==============
 type:library
==============

This tag is part of the type-classification system for projects
managed by the release team. ``type:library`` indicates that a project
is a library, middleware, client, or other piece of software that is
used to build another project and does not, by itself, provide a
long-running service or stand-alone tool.


Application to current projects
===============================

.. tagged-projects:: type:library


Rationale
=========

The release team is building some tools for automating common release
processes. Some of these tools will look at the type of the repository
to make choices, including skipping or including the repository or
applying different criteria or process steps. For example, changes in
library projects are not available to server projects until the
libraries are released. We want to provide an easy way to find all
unreleased changes in all libraries to ensure that they are released
in a timely manner, and that requires having a way to identify all of
the library projects and their repositories.


Requirements
============

* The repository contains software used as a library for the loose and
  commonly-understood definition of "library".


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
