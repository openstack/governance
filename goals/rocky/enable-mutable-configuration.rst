.. -*- mode: rst -*-

============================
Enable mutable configuration
============================

There is a strong desire from operators to be able to change configuration
options without a service restart. For example, to selectively enable DEBUG
logging in response to observed issues. As of OpenStack Newton, config
options can be marked as 'mutable'. This means they can be reloaded (usually
via SIGHUP) at runtime, without a service restart. However, each project has
to be enabled before this will work and some care needs to be taken over how
each option is used before it can safely be marked mutable. For more details
please refer to `Enabling your project for mutable config`_

Champion
========

Goals need a main driver to project-manage them to completion. Project teams
need assistance, reminders and sometimes direct help in order for them to
complete the goals.

ChangBo Guo (gcb) has volunteered to drive this goal.

Gerrit Topic
============

To facilitate tracking, commits related to this goal should use the
gerrit topic::

  mutable-config

Storyboard
==========

Progress on this goal is tracked via
https://storyboard.openstack.org/#!/story/2001545

Completion Criteria
===================

Each project service could be turned on/off debug logging without restart

#. Support reloading configuration options at runtime, without a service
   restart
#. Toggle the debug option for each service at runtime

References
==========

* `Original Discussion`_
* `Enabling your project for mutable config`_
* `Example of enabling projects`_

.. _Original Discussion: https://etherpad.openstack.org/p/mitaka-cross-project-dynamic-config-services
.. _Enabling your project for mutable config: https://docs.openstack.org/oslo.config/latest/reference/mutable.html
.. _Example of enabling projects: https://review.opendev.org/#/q/topic:bp/mutable-config+(status:open+OR+status:merged)

Current State / Anticipated Impact
==================================

oslo.config and oslo.service have implemented basic functions and we have
enabled Nova to support mutable configuration and mark some configuration
option like CONF.libvirt.live_migration_progress_timeout as 'mutable'.
