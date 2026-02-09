=================================
FIPS Compatibility and Compliance
=================================

FIPS Compliance is often a requirement not just for organizations conducting
business with the US Federal Government, but also for other highly regulated
industries seeking to meet security compliance targets.  The Foundation has,
in fact, been approached by cloud vendors attempting to run refstack on
FIPS enabled systems.

There are two distinct goals for FIPS: FIPS Compatibility and FIPS Compliance.

FIPS Compatibility
==================

The main effect of turning on FIPS mode in the kernel is to set the kernel
cryptographic modules to disallow certain cryptographic operations, ciphers
and algorithms, or to only allow their use within certain contexts.  More
precise details can be obtained from the FIPS spec. [1]

The goal of FIPS Compatibility is ensure that OpenStack functions correctly
when the control plane nodes are running with FIPS mode enabled.

A lot of work has already been done to advance the FIPS compatibility goal.
Making this a community goal would raise awareness of this effort and would
ensure that all projects, as well as third party vendors, test their
functionality under FIPS.

We would also be able to identify dependencies that need to be updated to work
under FIPS. [2]

Moreover, there are problems that are common to many projects, which could
be better solved with a standard approach.

FIPS Compliance
===============

The goal of FIPS Compliance is to ensure that any crypto operations that are
performed are done using crypto libraries that are FIPS certified. To complete
this goal, we will need to:

* Audit the cryptographic libraries used within OpenStack.
* Replace if possible, or document as a limitiation, libraries which are
  not FIPS certified.

Goal Checklist
==============

Is design finalized?
Status: YES

The plan is simply to create voting CI jobs with FIPS enaled in all the
OpenStack projects, and fix or document any issues that arise.  This work
has been underway for some time, and you can see the status (and the work
that has been completed) in the "Current Status" section below.

Some design work will be needed when deciding how to replace/fix paramiko,
but this work is explicitly called out to be completed by the end of the
Zed release.

Is implementation finalized?
Status: YES

The jobs that have been completed or are in progress are listed in [10].

Is there any dependency or blocker?
Status: YES

Having voting CI jobs depends on either centOS-9-stream jobs becoming
stable or being able to use FIPS-enabled Ubuntu images.

Achieving FIPS compliance will necessarily require an audit to determine
which external software implements cryptography, and whether it is FIPS
compliant.  An initial audit was conducted in [14]. So far, only a few
software modules are of concern.

Part of this goal is to identify any issues with external software and
address it by BB.

Champion
========

#. Ade Lee <alee@redhat.com> (alee)

Gerrit Topic
============

To facilitate tracking, commits related to this goal should use the
gerrit topic::

  fips-compatibility or fips-compliance

Completion Criteria
===================

Milestone 1: Zed-cycle release:

#. Projects that curently have FIPS CI jobs in-flight should have these
   jobs merged. These jobs should be sufficient to test base functionality
   and in particular those areas expected to be affected by FIPS. The
   tests should pass. Any limitations uncovered should be documented.

#. The current role to enable FIPS mode should be enhanced to allow FIPS to
   be enabled on Ubuntu environments. Jobs using Ubuntu will need to be
   tested using Python 3.9, as this is the earliest release that supports the
   usedforsecurity parameter on hashlib.md5().

#. The ultimate goal is to have the FIPS CI jobs running as voting in the
   check/gate pipelines.  At this point, though, the FIPS jobs are only
   available on CentOS-9-stream, which has not been stable.  Until the
   centos-9-stream jobs become stable or the FIPS jobs are moved to Ubuntu,
   it is acceptable to have the jobs running in the periodic pipeline.

#. These jobs should run from Zed onwards.  There have been requests to add
   these jobs to the stable branches - as far back as wallaby.  This would be
   considered a good-to-have.

#. A review of crypto used within OpenStack should be completed. This review
   should identify crypto that is not FIPS certified and propose alternatives.
   Depending on which libraries are identified and the projected impact, a
   schedule for replacement can be decided at that time.  An initial review of
   crypto in OpenStack is documented here. [14]

#. A plan should be formulated to provide a FIPS compliant replacement option
   to paramiko across OpenStack projects.

Milestone 2: AA-cycle release:

#. All OpenStack projects should have at least one job to test functionality
   when FIPS is enabled. These tests should pass with limitations documented.
   This job should be in the check/gate pipelines as a voting job.

#. Run the relevant integrated tempest tests in FIPS mode. These tests should pass.
   It is expected that some FIPS specific configuration may be required [3], or that
   some tests/features would be invalid under FIPS [4]. These configurations and
   limitations should be well documented.

#. A FIPS compliant replacement for paramiko should be implemented as an option
   across the major OpenStack projects.  See details under "Current Issues" below.

Milestone 3: BB-cycle-release:

#. A FIPS compliant replacement for paramiko should be implemented as an option
   across all OpenStack projects.

Current Status
==============

A lot of work has already been done to advance the FIPS compatibility goal.
Making this a community goal will ensure that all projects as well as third
party vendors test their functionality under FIPS, as well as providing an
opportunity to solve common problems with a standard approach.

FIPS biggest effect on OpenStack services so far has been in disallowing the
use of MD5.  Under FIPS, hashlib.md5() will fail unless it is annotated as
not being used in a security context using a special annotation
(usedforsecurity) that was introduced in python 3.9 [5].  This annotation
has been backported by some distributions.

To take advantage of this annotation, an adapter for hashlib.md5() was added
to oslo.utils() [6], and patches were added to Keystone, Barbican, Nova,
Glance, Octavia, Neutron and other projects to take advantage of this
annotation. [7]  A similar wrapping was added to swift [8].

An ansible role has been added to zuul-jobs to enable FIPS mode in CI jobs
[9].  Right now, this role only works for RHEL/Fedora/Centos systems.

Using this role, a whole slew of CI FIPS jobs have been proposed. [10]
The vast majority of the tempest tests in these jobs currently pass.

Current Issues
==============

* Tempest currently uses paramiko to ssh to instances. This currently fails
  because of a call to md5() to generate fingerprints that are written to log
  files. This use of md5() is valid under FIPS and so we can patch paramiko
  to either allow the usage [11] or to use a different algorithm [12].

* Paramiko also uses md5() in generating a key from a password while reading an
  encrypted PEM file that is not in the newer OpenSSH format. We can get around
  that by simply making sure that relevant encrypted key files are generated by
  OpenSSH.

* Paramiko is not FIPS compliant and so will ultimately need to be replaced
  across OpenStack for compliance. This should be co-ordinated across projects
  so it can be done consistently. Ideally, a library could be found that can
  be configured to FIPS compliant and also support algorithms like  ed25519.
  Alternatively, projects should be changed to allow the selection of either
  paramiko (as default) or a FIPS certified library at run-time.

* A patch has been proposed to replace paramiko with libssh instead as this
  library uses FIPS certified crypto [13]. Ultimately, a different library
  may need to be selected.

References
==========

#. FIPS Spec:
   https://csrc.nist.gov/publications/detail/fips/140/3/final
#. So far, packages that we have found to require FIPS updates include django, certmonger
   paramiko and sphinx.
   https://github.com/django/django/pull/14763
#. Some required setting include:
   iscsi chap algorithms: https://review.opendev.org/c/openstack/puppet-tripleo/+/778081
   snmp_auth_type: https://review.opendev.org/c/openstack/tripleo-heat-templates/+/813089
#. Features and tests that come to mind include:
   volume encryption using plain encryptor:
   https://review.opendev.org/c/openstack/barbican-tempest-plugin/+/810782
#. hashlib.MD5() issue in Python 3.9:
   https://bugs.python.org/issue9216
#. Change to oslo.utils to use usedforsecurity:
   https://review.opendev.org/c/openstack/oslo.utils/+/750031
#. Patches to various projects to use oslo.utils adapter for hashlib.md5
   (as examples):
   glance: https://review.opendev.org/c/openstack/glance/+/756158
   nova: https://review.opendev.org/c/openstack/nova/+/756434
   nova: https://review.opendev.org/c/openstack/nova/+/777686
   os-brick: https://review.opendev.org/c/openstack/os-brick/+/756151
   oslo: https://review.opendev.org/c/openstack/oslo.versionedobjects/+/756153
   tooz: https://review.opendev.org/c/openstack/tooz/+/756432
   opensdk: https://review.opendev.org/c/openstack/openstacksdk/+/767411
   octavia: https://review.opendev.org/c/openstack/octavia/+/798146
   designate: https://review.opendev.org/c/openstack/designate/+/798157
   glance_store: https://review.opendev.org/c/openstack/glance_store/+/756157

#. Swift patch to handle hashlib.md5
   https://review.opendev.org/c/openstack/swift/+/751966
#. Ansible role in zuul-jobs
   https://review.opendev.org/c/zuul/zuul-jobs/+/788778
   https://etherpad.opendev.org/p/state-of-fips-in-openstack-ci-yoga#L23
#. Current proposed and merged CI jobs
   https://etherpad.opendev.org/p/qa-zed-ptg-fips (as of zed)
   https://etherpad.opendev.org/p/state-of-fips-in-openstack-ci-yoga#L53 (as of yoga)
#. https://github.com/paramiko/paramiko/pull/1928
   This change is relatively small.  Until it passes, we have added a monkey-patch
   for paramiko in https://review.opendev.org/c/openstack/tempest/+/822560
#. https://github.com/vakwetu/paramiko/commit/b4beb535d7293447f25afd12051dbc45bb1e6ddc
#. https://github.com/paramiko/paramiko/pull/1103
#. Tempest patches:
   https://etherpad.opendev.org/p/state-of-fips-in-openstack-ci-yoga#L33
#. Initial audit of crypto libraries in OpenStack:
   https://etherpad.opendev.org/p/zed-ptg-fips-goal-compliance-audit
   The audit indicates that very few libraries are of concern, the most
   prominent being paramiko.
