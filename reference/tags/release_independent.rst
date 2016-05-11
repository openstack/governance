::

  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-release:independent`:

===================
release:independent
===================

This tag is part of the release category of tags, describing the release
model for a given deliverable. Development in OpenStack is generally organized
around 6-month cycles (like "kilo"), which involves releasing a "final"
version at the very end of the development cycle. However, some projects opt
to completely bypass the 6-month cycle and release independently. That is
for example the case of projects that support the development infrastructure.

The "release:independent" tag describes such projects.


Application to current projects
===============================

.. tagged-projects:: release:independent


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

   By adopting this tag, projects indicate that they **are not part of
   any OpenStack release** and will therefore **not be listed** on the
   release series-specific pages on the `releases website`_. Projects
   that want to be listed along with other parts of the OpenStack
   release are encouraged to adopt a model such as
   :ref:`tag-release:cycle-with-intermediary` and follow the release
   schedule.

.. _releases website: http://releases.openstack.org


Requirements
============

* "release:independent" projects produce releases from time to time.
* Release tags for deliverables using this tag are managed without
  oversight from the Release Management team.


Tag application process
=======================

The release management team (ultimately represented by the release management
PTL) is responsible for maintaining tags in the "release" category, so that
they match the current release model followed by each code repository.

There is no need to apply for addition/removal. Changes externally proposed
will be reviewed and approved by the release management team, ultimately
represented by the release management PTL.
