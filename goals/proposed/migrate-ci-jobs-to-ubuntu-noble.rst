=================================================
Migrate CI/CD jobs to Ubuntu 24.04 (Noble Numbat)
=================================================

For the Epoxy development cycle :doc:`current tested runtime </reference/runtimes/2025.1>`
was defined to support Ubuntu 24.04 (Noble). This means that our jobs should
be compatible with this distribution and using it by default. We should
identify and migrate jobs that are currently using Ubuntu 22.04 (Jammy)
to use Ubuntu 24.04 (Noble) instead.

If any failures related to the new distro (Noble) block project development
progress, then we can help project to either with fixing code to support
Ubuntu 24.04 or override nodeset for their jobs and add Noble jobs as
non-voting, so that projects can continue using Jammy nodeset until codebase
is fully compatible with Noble.
Custom project jobs that define nodeset explicitly may remain intact and
allow projects to manage such jobs on their own.

Stable branches will keep using their original distro version, and that will
be handled with job branches variant.

Champion
========

Ghanshyam Mann (gmann)

Gerrit Topic
============

To facilitate tracking, commits related to this goal should use the
gerrit topic::

  migrate-to-noble

Completion Criteria
===================

#. All official OpenStack projects should test their codebase against
   Ubuntu 24.04 (Noble Numbat).


Current State / Anticipated Impact
==================================

A big amount of jobs, like openstack-python3-jobs, docs or devstack, currently
use Ubuntu 22.04 (Jammy) but we have a passing devstack platform job on Noble.
First, we will provide the devstack base job on Noble with WIP, and majority of
projects will test it before merging.
