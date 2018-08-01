.. _python2-deprecation-timeline:

=========================================
 2018-05-29 Python2 Deprecation Timeline
=========================================

The Jan. 1, 2020 deadline for upstream support of Python 2 is
approaching. Now that most of our projects can claim at least basic
support for Python 3, we can consider dropping Python 2 support.

We need to coordinate the timing of that change, and take the step
together as a community, rather than going one project at a time, to
avoid doubling the work of downstream consumers such as distributions
and independent deployers. We do not want to require them to package
all (or even a large number) of the dependencies of OpenStack twice
because they have to install some services running under Python 2 and
others under Python 3. Ideally they would be able to upgrade all of
the services on a node together as part of their transition to the new
version, without ending up with a Python 2 version of a dependency
along side a Python 3 version of the same package.

In various online and in-person discussions, we have previously
settled on the end of the T cycle as the point at which we would have
all of the prerequisite tests running to allow us to be confident of
our Python 3 support, to be followed by dropping Python 2 during the
beginning of the U cycle, in late 2019 and before the 2020 cut-off
point when upstream Python 2 support will be dropped.

This resolution is the formal documentation of the time line, and
includes three points:

1. Projects should continue to work to expand Python 3 support as
   quickly as possible, by ensuring that all unit, functional, and
   integration tests, as well as other ancillary jobs for building
   documentation, packaging, etc., run properly under Python 3.

2. All projects must complete the work for Python 3 support by the end
   of the T cycle, unless they are blocked for technical reasons by
   dependencies they rely on.

3. Projects should complete all of the work of updating all of their
   CI jobs to work under Python 3 before dropping Python 2 support.

4. Existing projects under TC governance at the time this resolution
   is accepted must not drop support for Python 2 before the beginning
   of the U development cycle (currently anticipated for late 2019).

Resources
=========

* `Rocky Forum Session Etherpad
  <https://etherpad.openstack.org/p/YVR-python-2-deprecation-timeline>`__
* Mailing list discussion threads from `April 2018
  <http://lists.openstack.org/pipermail/openstack-dev/2018-April/129866.html>`__
  and `May 2018
  <http://lists.openstack.org/pipermail/openstack-dev/2018-May/130824.html>`__
