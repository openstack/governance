::

  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-release:cycle-trailing`:

========================
 release:cycle-trailing
========================

This tag is part of the release category of tags, describing the release
model for a given deliverable. Development in OpenStack is organized
around 6-month cycles (like "kilo"), generally with a "final" version at
the very end of the development cycle. Some projects will publish a single
release at the end of the cycle (and publish development milestones at
predetermined times in the cycle schedule), while some others will release
intermediary releases.

The "release:cycle-trailing" tag describes projects that follow the
release cycle, but because they rely on the other projects being
completed may not always publish their final release at the same time
as those projects. For example, projects related to packaging or
deploying OpenStack components need the final releases of those
components to be available before they can run their own final tests.

Application to current projects
===============================

.. tagged-projects:: release:cycle-trailing


Rationale
=========

At the end of every 6-month cycle a number of projects release at the same
time, providing a convenient reference point for downstream teams (stable
branch maintenance, vulnerability management) and downstream users (in
particular packagers of OpenStack distributions).

This "final" release may be the only release of the development cycle,
in which case the project publishes intermediary "development
milestones" on a time-based schedule during the cycle. Or the project
may release more often and make intermediary releases in the middle of
the cycle. Other projects trail the main release deadline, waiting for
the final releases of components on which they rely.

Describing which projects commit to follow which model is therefore a useful
piece of information to provide to our users.

A given deliverable can't have more than one model: it therefore must
choose between the :ref:`tag-release:cycle-with-milestones`,
:ref:`tag-release:cycle-with-intermediary`,
:ref:`tag-release:independent`, :ref:`tag-release:cycle-trailing`, and
:ref:`tag-release:none` models.

.. warning::

   This release model is not intended for use by components that have
   programmatic dependencies on each other, such as one service that
   calls another or a library used by multiple services. It is
   intended for use by projects that truly cannot complete their work
   without "final" versions of their dependencies.

Requirements
============

* "release:cycle-trailing" projects commit to produce a release no
  later than 2 weeks after the end of the 6-month development cycle.
* Within the cycle, projects using this release model will produce
  intermediate or milestone releases (adhering to the same regular
  deadlines) leading up to their final release.
* Release tags for deliverables using this tag are reviewed and
  applied by the Release Management team.

Tag application process
=======================

The release management team (ultimately represented by the release management
PTL) is responsible for maintaining tags in the "release" category, so that
they match the current release model followed by each code repository.

There is no need to apply for addition/removal. Changes externally proposed
will be reviewed and approved by the release management team, ultimately
represented by the release management PTL.
