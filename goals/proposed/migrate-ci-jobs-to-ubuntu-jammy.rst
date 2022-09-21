====================================================
Migrate CI/CD jobs to Ubuntu 22.04 (Jammy Jellyfish)
====================================================

For the Antelope development cycle :doc:`current tested runtime </reference/runtimes/2023.1>`
was defined to support Ubuntu 22.04 (Jammy). This means that our jobs should
be compatible with this distribution and using it by default. We should
identify and migrate jobs that are currently using Ubuntu 20.04 (Focal)
to use Ubuntu 22.04 (Jammy) instead.

Last time :doc:`we switched distro </goals/completed/victoria/migrate-ci-cd-jobs-to-ubuntu-focal>`
for CI/CD jobs during Victoria development cycle.

Since goal of :doc:`migrating CI/CD jobs to zuulv3 native </goals/completed/victoria/native-zuulv3-jobs>`
ones has been accomplished, migration to the new distro should be relatively
easy.
If any failures related to the new distro (Jammy) block project development
progress, then we can help project out either with fixing code to support
Ubuntu 22.04 or override nodeset for their jobs and add Jammy jobs as
non-voting, so that projects can continue using Focal nodeset until codebase
is fully compatible with Jammy.
Custom project jobs that define nodeset explicitly may remain intact and
allow projects to manage such jobs on their own.

Stable branches will keep using their original distro version, and that will
be handled with job branches variant.

Champion
========

Dmitriy Rabotyagov (noonedeadpunk)
Ghanshyam Mann (gmann)

Gerrit Topic
============

To facilitate tracking, commits related to this goal should use the
gerrit topic::

  migrate-to-jammy

Completion Criteria
===================

#. All official OpenStack projects should test their codebase against
   Ubuntu 22.04 (Jammy Jellyfish).


Current State / Anticipated Impact
==================================

A big amount of jobs, like openstack-python3-jobs, docs or devstack, currently
use Ubuntu 20.04 (Focal).
First, we will provide the devstack base job on Jammy with WIP, and majority of
projects will test it before merging.
