::

  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-release:cycle-with-intermediary`:

===============================
release:cycle-with-intermediary
===============================

This tag is part of the release category of tags, describing the release
model for a given deliverable. Development in OpenStack is organized
around 6-month cycles (like "kilo"), generally with a "final" version at
the very end of the development cycle. Some projects will publish a single
release at the end of the cycle (and publish development milestones at
predetermined times in the cycle schedule), while some others will release
intermediary releases.

The "release:cycle-with-intermediary" tag describes which projects follow the
second option: multiple releases during the development cycle, with a final
release to match the end of the cycle.


Application to current projects
===============================

.. tagged-projects:: release:cycle-with-intermediary


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


Requirements
============

* "release:cycle-with-intermediary" projects commit to produce a release to
  match the end of the 6-month development cycle.
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
