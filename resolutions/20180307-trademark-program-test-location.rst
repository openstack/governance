.. _201180307_interop_test_location:

=======================================================================
 2018-03-07 Location of tempest tests for OpenStack Trademark Programs
=======================================================================

Introduction
============

When :ref:`20160504_defcore_test_location` was proposed, the trademark program
was simpler, involving only a small subset of the projects available in
OpenStack.

With the proposed "add on" and "vertical" trademark programs, more projects are
involved. This growth introduces some scaling problems into the management of
tests for the trademark programs. These issues were discussed at the Rocky PTG.
The outcome of those discussions are reported here.

This resolution supersedes :ref:`20160504_defcore_test_location`.

Updated Resolution
==================

Whereas the Trademark Program has made it clear that they have the tooling and
willingness to support trademark tests located in any of

* The `Tempest repository`_
* Project specific tempest plugins (e.g., `image-trademark-tempest-plugin`)
* Vertical specific tempest plugins (e.g.,
  `nfv-vertical-trademark-tempest-plugin`)
* A global Trademark tempest plugin (e.g.,
  `openstack-trademark-tempest-plugin`)

as long as they are tests that can be run by tempest.

And the QA Team, Trademark Program and individual projects have shared
responsibility for the management of trademark tests, with varying degrees of
bandwidth for review attention.

And trademark tests are expected to be changed rarely.

It is resolved that trademark tests (and candidates thereof) for individual
projects should live in one, and only one, of four possible locations, each
with differing strategies for review and repository ownership (status in
:ref:`projects`):

* The `Tempest repository`_, with approval reviews performed by the QA Team,
  repository ownership via the QA Team (already true).
* A vertical specific tempest plugin, with approval reviews performed by the QA
  Team and the Trademark Program, repository ownership via the Trademark
  Program.
* A global Trademark tempest plugin, with approval reviews performed by the QA
  Team and the Trademark Program, repository ownership via the Trademark
  Program.
* A project specific tempest plugin, specifically limited to trademark-oriented
  tests, with approval reviews performed by the project, the QA Team, and the
  Trademark Program, repository ownership via the Trademark Program if they
  accept, otherwise the project team.

The choice is up to the individual projects, in consultation with the QA Team
and the Trademark Program.

.. note:: No overarching direction is provided here on what tooling must be
          used in the tests but it is generally expected that the tooling
          should be agreed by the people who are reviewing the code. If a
          project wants to use tooling other than the core tempest libraries
          (e.g., gabbi_) they should prefer a project specific plugin and be
          aware that their choice of tooling may limit the ability for
          non-project parties to review tests. Any tooling chosen must be able
          to produce tests that are run by tempest.

.. _gabbi: https://gabbi.readthedocs.io/
.. _Tempest repository: https://opendev.org/openstack/tempest
