==========================================
Migrate from oslo.rootwrap to oslo.privsep
==========================================

The oslo.rootwrap library is a precursor of oslo.privsep that allows code to
run commands under "sudo" if it matches a predefined filter. Beyond the bad
performance of calling full commands in order to accomplish simple tasks,
oslo.rootwrap also led to bad security; it was difficult to filter commands in
a way that would not easily allow privilege escalation.

oslo.privsep offers a superior security model, faster and more secure. Since
oslo.privsep was released, the community has encouraged the usage of
oslo.privsep and the deprecation of any existing code still using
oslo.rootwrap.


Champion
========

Rodolfo Alonso Hernandez <ralonsoh@redhat.com> (ralonsoh)


Gerrit Topic
============

To facilitate tracking, commits related to this goal should use the
gerrit topic::

  privsep-migration

A new Story in https://storyboard.openstack.org/ will be created to track any
related patch.


Completion Criteria
===================

#. A migrated project should not import oslo.rootwrap, the rootwrap filters
should be deleted and the library should not be required anymore during the
project installation.

#. The migration will be considered complete when no project inherits
oslo.rootwrap and this import is added to hacking [1]_.


References
==========

The main reference guide could be found in [2]_. This guide provides
information about how to create a privsep context, assign privileges and use it
as a decorator for a function. As commented in the first section, this context
should contain the minimum set of needed capabilities to execute the decorated
function. For example:

.. code-block:: python

   default = priv_context.PrivContext(
      __name__,
      cfg_section='privsep',
      pypath=__name__ + '.default',
      capabilities=[caps.CAP_SYS_ADMIN,
                    caps.CAP_NET_ADMIN,
                    caps.CAP_DAC_OVERRIDE,
                    caps.CAP_DAC_READ_SEARCH,
                    caps.CAP_SYS_PTRACE],
   )


The function “entrypoint” [3]_ of this instance can be used as a decorator for
another function:

.. code-block:: python

   @privileged.default.entrypoint
   def delete_interface(ifname, namespace, **kwargs):
       _run_iproute_link("del", ifname, namespace, **kwargs)


From this same link, there is also a reference to convert from oslo.rootwrap to
oslo.privsep. These are some migration examples:

* Nova: [4]_
* Neutron: [5]_
* os-vif: [6]_


Replacing instances of oslo.rootwrap usage requires more than just a drop-in
replacement. The oslo.privsep approach is different and will require rethinking
the way each privileged operation is conducted in a way that precludes a blind
or programmatic substitution. As commented in the OpenStack mailing list [7]_,
the security idea is based on the principle of least privilege. That means any
command executed inside a privsep context [8]_ should gain the minimum needed
privileges to execute the task and exit. Unfortunately some projects have
implemented all privileged commands under a single privsep context, containing
all needed capabilities [9]_ to execute all those commands. This is an
incorrect implementation of oslo.privsep and should be considered during the
migration.


Current State / Anticipated Impact
==================================

These are the projects still using oslo.rootwrap that should migrate:

* ceilometer
* cinder
* cinderlib
* designate
* freezer
* glance_store
* ironic
* ironic-inspector
* ironic-lib
* kolla
* magnum
* manila
* monasca-agent
* networking-bagpipe
* neutron
* neutron-vpnaas
* os-brick
* sahara
* solum
* tacker
* tripleo-common


Links
=====

.. [1] https://opendev.org/openstack/hacking/src/branch/master/hacking/checks/imports.py
.. [2] https://docs.openstack.org/oslo.privsep/latest/user/index.html
.. [3] https://opendev.org/openstack/oslo.privsep/src/tag/2.1.1/oslo_privsep/priv_context.py#L216
.. [4] https://review.opendev.org/#/q/project:openstack/nova+branch:master+topic:my-own-personal-alternative-universe
.. [5] https://review.opendev.org/#/q/status:merged+project:openstack/neutron+branch:master+topic:bug/1492714
.. [6] https://review.opendev.org/#/c/287725/
.. [7] http://lists.openstack.org/pipermail/openstack-discuss/2019-March/004358.html
.. [8] https://docs.openstack.org/oslo.privsep/latest/user/index.html#defining-a-context
.. [9] http://man7.org/linux/man-pages/man7/capabilities.7.html
