=======================
Drop Python 2.7 Support
=======================

Ussuri cycle is the time to drop the python2 support from OpenStack.
All the projects have completed all of the work of updating all of
their CI jobs to work under Python 3. This goal accomplishes the drop
of support for python2 by removing testing python2, as well as
configuration required for that testing.  The only changes to the code
a project would run in production are those required to fix py3
compatibility, in the event that a job is converted to py3 that was
not already.

Along with py2.7 drop, we will use this goal to update the Python 3
test runtimes for Ussuri :doc:`../../../reference/runtimes/ussuri`.

* Storyboard stories TODO

Champion
========

Ghanshyam Mann(gmann) <gmann@ghanshyammann.com> has volunteered to drive this goal.

Gerrit Topic
============

To facilitate tracking, commits related to this goal should use the
gerrit topic::

  drop-py27-support

Completion Criteria
===================

In order for a project to call this goal complete it must:

#. Drop the python 2.7 unit, functional & integration testing.

   This will be done by updating the python testing template from Train to Ussuri template
   and drop the ``openstack-python-jobs`` job template.

#. Migrate any python 2.7 job if no corresponding py3 job yet.

#. Update tox.ini and setup.cfg to remove the py2 reference.

#. Update requirements file to drop py2.7 specific dependency.

#. Add release notes saying dropping py2.7 explicitly in upgrade section.

   Python 2.7 support has been dropped. Last release of <project> to support
   python 2.7 is OpenStack Train. The minimum version of Python now
   supported by <project> is Python 3.6.

All these updates will go in a single patch.

Projects keeping py2.7 support
------------------------------

#. Swift

   * Swift is still fixing py3 bugs, want more than a single OpenStack release with both py2 and py3
     support, and want to continue to support xenial.

#. Storlets

   * Storlets is very close to Swift in term of source code and use case. Storlets will keep
     python 2.7 support along with python3.

Projects keeping py3.5 support
------------------------------

#. OpenStackSDK

   * As an end-user facing library, OpenStackSDK has to take a slightly more conservative approach.
     In particular, some large users of OpenStackSDK, such as Zuul, still support 3.5 as a minimum.
     In fact, OpenDev's Zuul currently runs in production on Ubuntu Xenial on python3.5.

#. Keystoneauth

   * Keystoneauth is a fundamental part of OpenStackSDK, so if it doesn't support 3.5 neither does
     OpenStackSDK.

#. QA branchless tools

   Many QA tools are branchless and few of them do not release tag also. Those are used as its
   master version on all stable branches including the stable/rocky which runs with py3.5 env.
   We are keeping the py3.5 support for below listed QA projects until stable/rocky is EOL.

   * hacking

   * stackviz

   * openstack-health

   * os-performance-tools

   * bashate

Schedule
--------

This will be divided into three phases. 3rd phase will be to audit the completion criteria.

#. Phase-1: Now -> Ussuri-1 milestone (deadline R-22 )

   * OpenStack Services to start dropping the py2.7 support and finish by milestone-1.
     Project needs to coordinate with third party CI or any backend drivers.
     Example: Nova - http://lists.openstack.org/pipermail/openstack-discuss/2019-October/010109.html

   * If there is any cross project dependency and removing the py2.7 support causing other projects
     py27 jobs then failing job can be dropped immediately to unblock the gate and proceed on complete
     cleanup in another patch.

   * This includes horizon and its plugins.

#. Phase-2: milestone-1 -> milestone-2 (deadline R-13 )

   * Common libraries and testing tooling.

   * This includes Oslo, QA tools (including Tempest plugins or any other testing tools), common lib
     used among projects (os-brick), Client libraries. Tempest will drop the support during Feb as
     discussed with TripleO.

   * By milestone 1 which is phase-1 all the projects using those lib and testing tools should have
     completed the removal of py2.7 support.

#. Phase-3: at milestone-2

   * openstack/requirements has to be the last one and will drop the support in phase-3.

   * Final audit on Phase-1 and Phase-2 plan and make sure everything is done without breaking anything.
     This is enough time to measure any break or anything extra to do before Ussuri final release.

Details discussion:  https://etherpad.openstack.org/p/drop-python2-support

References
==========

* https://etherpad.openstack.org/p/drop-python2-support

* http://lists.openstack.org/pipermail/openstack-discuss/2019-October/010142.html

Current State / Anticipated Impact
==================================

Few projects started dropping the py2.7 support.
