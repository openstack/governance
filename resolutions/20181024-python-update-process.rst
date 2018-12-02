==================================
 2018-10-24 Python Update Process
==================================

For many years OpenStack has effectively run on Python 2.7. However, with the
:doc:`upcoming deprecation of Python 2 support
<20180529-python2-deprecation-timeline>`, future releases of OpenStack will run
on the rapidly evolving Python 3. Already many Linux distributions have
completed the switch to Python 3-only by default, and are seeking to package
OpenStack for versions of Python 3 that we haven't necessarily tested upstream.

The resolution defines the process by which we will ensure that upstream
testing occurs, to the extent possible, on the versions of Python needed to
support downstream Linux distributions. There are different considerations for
jobs that test code by importing it directly into the testing process (unit
tests) and jobs that test code in a running process from the outside
(integration tests).

Unit Tests
----------

Prior to the beginning of each release cycle, the TC will designate the minor
versions of Python 3 that will be tested in that release using the following
criteria:

* The latest released version of Python 3 that is available in *any*
  distribution we can feasibly use for testing. It need not be a
  long-term-supported release, but could be a non-LTS version of Ubuntu,
  Fedora, openSUSE Leap, or even a rolling release distribution (such as Debian
  Testing or openSUSE Tumbleweed) if necessary.
* Each Python 3 version that is the default in any of the :ref:`Linux
  distributions specifically identified in the Project Testing Interface
  <pti-linux-distros>` at the beginning of the development cycle.
* Each Python 3 version that was still used in any integration tests at the
  beginning of the development cycle. (This category is necessary to ensure
  that projects don't break other projects' integration tests before those
  tests have completely migrated to newer distributions.) Testing for these
  versions can be dropped once all integration tests have migrated.

Where the tested versions are not contiguous, any intermediate minor
versions may be tested if the TC judges it likely that they may need to be
tested in a future release. However only periodic jobs (not check or gate
jobs) are needed for these versions.

This decision will be encoded in a Zuul template for unit tests named
``openstack-python3-<releasename>-jobs``, containing:

* Voting check and gate jobs for each of the selected minor versions of py3
* A periodic job for each intermediate minor version of py3 that may need to be
  fully tested in a future release, if any exist

The TC will set an :doc:`OpenStack-wide goal <../goals/index>` for the cycle
that project teams update each repo to:

* change its Zuul config to the template for that release;
* declare support for the tested versions in its PyPI package; and
* configure tox's default environment list to match.

If the new Zuul template contains test jobs that were not in the previous one,
the goal champion(s) may choose to update the *previous* template to add a
non-voting check job (or jobs) to match the gating jobs in the new template.
This means that all repositories that have not yet converted to the template
for the upcoming release will see a non-voting preview of the new job(s) that
will be added once they update. If this option is chosen, the non-voting job
should be limited to the ``master`` branch so that it does not run on the
preceding release's stable branch.

Integration Tests
-----------------

Prior to the beginning of each release cycle, the TC will determine whether
there have been any new releases of any of the :ref:`Linux distributions
specifically identified in the Project Testing Interface <pti-linux-distros>`.
If there have, it will set an :doc:`OpenStack-wide goal <../goals/index>` to
update any integration tests running on an older version of that distribution
to run on the new release.

The goal champion(s) may choose to make a hard cut-over (i.e. a
non-self-testing change to the Zuul job/template definitions that may break any
jobs that have not had incompatibilities fixed) of any unconverted test jobs at
some point during the release cycle, to ensure that all OpenStack components
are usable on a single version of a distribution prior to the OpenStack
release. The schedule for any such cut-over must be publicised in advance as
part of the goal definition.
