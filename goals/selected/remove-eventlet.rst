==============================
Remove Eventlet from OpenStack
==============================

OpenStack is built on the top of asynchronous mechanisms.
Many Openstack deliverables use the Eventlet library to obtain asynchronous
those asynchronous mechanisms. The problem is that Eventlet lacks of active
maintainers and that has led the library to a point where Eventlet is broken
with each new CPython version.

Asyncio based solutions (awaitlet, aiohttp, etc) offer flexible, perennial,
and modern alteratives to Eventlet. Since the Eventlet Asyncio hub was
released, allowing Eventlet and Asyncio to be run within the same process, the
Eventlet community has encouraged the usage of those alternatives and the
deprecation of any existing code still using Eventlet.

Champion
========

- Hervé Beraud <hberaud@redhat.com> (hberaud)

Gerrit Topic
============

To facilitate tracking, commits related to this goal should use the
gerrit topic::

  eventlet-removal

An etherpad has been created to track milestone and any related advancement by
deliverable:

* https://etherpad.opendev.org/p/epoxy-eventlet-tracking

Completion Criteria
===================

#. (2025.1 or 2025.2) (if applicable) Get the oslo deliverables doing
   networkIO providing drivers and backends that do not require Eventlet.
   Indeed many oslo libraries provides alternative executors like threading,
   if one library is only based on Eventlet executor, then this library should
   provide alternative executor. The following libraries might be impacted by
   that:
   - oslo.cache;
   - oslo.messaging;
   - oslo.db;
   - etcd3gw;
   - oslo.metrics;
#. (2025.1) Get libraries like OpenStackSDK migrated;
#. (2025.2) Get an OpenStack deliverable as reference user project selected to
   test Oslo changes related to new Asyncio based drivers;
#. (2025.2) Get non actively maintained OpenStack deliverables retired;
#. (2026.2) Ensure all other OpenStack deliverables relying on Eventlet gained
   support for running without Eventlet.
#. (2027.1) Deprecate the Eventlet support. To have a SLURP target release
   supporting both the old Eventlet and any new concurrency mode, this release
   keeps the Eventlet support.
#. (2027.2) Get usage of Eventlet in all OpenStack (including oslo
   deliverables) removed;


.. note:: Any project finishing the work before 2026.2 can do the step
   mentioned in 2027.1 early but make sure you have a one SLURP cycle to
   support both mode and deprecation phase.

References
==========

The main reference guide could be found in [1]_. This guide provides
information about how to migrate from Eventlet to the available alternatives.

From this same link, there is also a reference to identify alternatives for
an existing snippet of code. This identification is based on table of
correspondences [2]_ which aim to put solution in the front of the main
Eventlet patterns [3]_.

This guide will be updated in the coming weeks to provide some migration
examples for those patterns:

* the server pattern;
* the client pattern;
* the dispatch pattern.

Replacing Eventlet usage requires more than just a drop-in replacement. The
available alternatives are different and will require rethinking the way each
module is designed in a way that precludes a blind or programmatic
substitution.

As commented in the OpenStack mailing list [4]_, the migration is based on the
freedom of decision-making. Some Openstack deliverables represent thousand of
line code. Asyncio is by nature invasive. Using Asyncio everywhere would
require to rewrite the deliverables entirely. For this reason we created
Awaitlet [5]_ which could be used to introduce usage of Asyncio while
limiting its impact on the existing code.

Current State / Anticipated Impact
==================================

History of this goal can be found here [6]_.

Official wiki page can be found here [7]_.

A dedicated IRC channel (``#openstack-eventlet-removal``) has been created.
IRC meetings are scheduled every two weeks (on odd weeks).
Schedule details are available in the official wiki page [7]_.

Links
=====

.. [1] https://eventlet.readthedocs.io/en/latest/asyncio/migration.html
.. [2] https://github.com/eventlet/eventlet/pull/982
.. [3] https://eventlet.readthedocs.io/en/latest/design_patterns.html
.. [4] https://lists.openstack.org/archives/list/openstack-discuss@lists.openstack.org/thread/4KOGIDNM2SWJDBBFCTCJC3ZSITLMVMDL/#4KOGIDNM2SWJDBBFCTCJC3ZSITLMVMDL
.. [5] https://github.com/sqlalchemy/awaitlet
.. [6] https://review.opendev.org/c/openstack/governance/+/902585
.. [7] https://wiki.openstack.org/wiki/Eventlet-removal
