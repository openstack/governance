.. _20160119_stackforge_resolution:

============================================
 2016-01-19 Stackforge Namespace Retirement
============================================

Introduction
============

When the :ref:`20150615_stackforge_resolution` was originally adopted,
the TC felt that the term "Stackforge" was still useful as a sort of
shorthand for "the area where unofficial projects can develop before
they became official".  In keeping with that, we have continued to
refer to the hosting space for unofficial projects as "Stackforge".
This has certainly resulted in people thinking our documentation was
out of date, and has also likely resulted in missed opportunities to
communicate that projects within openstack/ but not approved by the TC
are unofficial, rather than official OpenStack projects.

This updated resolution reflects the TC's revised intention to retire
not only the "stackforge" namespace but also the term itself in favor
of "unofficial project".

Updated Resolution
==================

The Stackforge project provides an environment for projects to share
the OpenStack project's development resources and methodology, and
otherwise participate in the OpenStack community.  It enables projects
to deeply interact with OpenStack in development and testing, whether
they seek to become "core" OpenStack projects or not.

This is an extremely valuable service that benefits our entire
community, including new as well as established projects.

With recent changes in project governance, the OpenStack project has
opened itself to including a much wider range of projects under its
umbrella.  Because of this, projects are moving between Stackforge and
OpenStack at a much higher frequency than previously.

The names of projects hosted in the OpenStack project infrastructure
have prefixes that have been used for distinguishing Stackforge
("stackforge/") and OpenStack ("openstack/") projects.  Because these
prefixes form part of the full name of the project's source code
repository, organizational changes entail renaming the project.  This
is complex for the Infrastructure team and very disruptive to
developers, operators, and users.

In order to simplify software development lifecycle transitions of
Unofficial and Official OpenStack projects, all projects developed
within the OpenStack project infrastructure will be permitted to use
the "openstack/" namespace.  The use of the term "Stackforge" to
describe unofficial projects should be considered deprecated.

The "openstack/" namespace is intended to convey that projects
contained within it are hosted on OpenStack infrastructure.  Only some
of the projects within will be official OpenStack projects
themselves. As such, there should not be any new requirements such as
CLA signing. This resolution should not alter the workflow of any of
the projects.
