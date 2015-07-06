::

  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-release:none`:

============
release:none
============

This tag is part of the release category of tags, describing the release
model for a given deliverable. Most repositories in OpenStack publish
releases, by tagging a specific point in development using a version number.
However, some projects (or some repositories) are not meant to be "released"
and can opt to never publish such releases. This is for example the case of
of specs repositories which track incoming feature design.

The "release:none" tag allows to clearly describe such repositories.


Application to current projects
===============================

.. tagged-projects:: release:none


Rationale
=========

Some repositories will never produce a release and are supposed to be directly
consumed as git repositories. Describing which repositories follow this
model is therefore a useful piece of information to provide to our users.
"release:none" is different from having no release tag specified at all: it
specifically expresses that the repository will not result in any release. Not
having any release model tag just means the project hasn't clearly picked a
model yet.

A given deliverable can't have more than one model: it therefore must choose
between the :ref:`tag-release:cycle-with-milestones`,
:ref:`tag-release:cycle-with-intermediary`, :ref:`tag-release:independent`
and :ref:`tag-release:none` models.


Requirements
============

* "release:none" repositories can't have a release.


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
