==========================================
Migrate CI/CD jobs to new Ubuntu LTS Focal
==========================================

At the start of the Victoria development cycle, the current
:ref:`LTS or stable distribution <pti-linux-distros>` versions
include Ubuntu 20.04 (Focal). Our CI/CD testing use Ubuntu 18.04 (Bionic)
version. We need to migrate the testing to the new Ubuntu Focal.

Current CI/CD jobs are mixed with zuulv3 native and legacy jobs. During Ubuntu
Xenial to Bionic migration we did comparable work (especially legacy
job migration was painful).

Zuulv3 native jobs community goal of Victoria cycle will make this
migration easy.

In this goal, we will only migrate the zuulv3 native jobs to Ubuntu Focal
which includes the devstack base job migration also. So that all the legacy
jobs will be migrated to Ubuntu Focal automatically during zuulv3 migration
work.

If any failures related to the new distro (Focal) block the zuulv3 migration, then
such jobs can use Bionic nodeset temporarily and later migrate to Focal.

Stable branches will keep using their original distro version, and that will
be handled with job branches variant.

* `Storyboard stories <https://storyboard.openstack.org/#!/story/2007865>`__

Champion
========

Ghanshyam Mann (gmann)

Gerrit Topic
============

To facilitate tracking, commits related to this goal should use the
gerrit topic::

  migrate-to-focal

Completion Criteria
===================

#. All CI testing jobs for official OpenStack projects should run
   on Ubuntu Focal.

References
==========

Xenial to Bionic migration: http://lists.openstack.org/pipermail/openstack-discuss/2018-November/000168.html

Current State / Anticipated Impact
==================================

All CI/CD jobs run on Bionic. First, we will provide the devstack base job
on Focal with WIP, and all projects will test it before merging.
