========================
IPv6 Support and Testing
========================

IPv6 has been around over 10 years and most of the OpenStack projects do
have IPv6 supports in general or at some extent depends on
various scenarios and use cases. There are multiple levels of IPv6 support.
For example, the two primary IPv6 use cases are:

* OpenStack services listen and communicate with each other on IPv6.
* OpenStack resources, for example Compute VM are assigned an IPv6
  address and able to ssh and communicate with each other over IPv6.

All these scenarios are good to target in OpenStack as complete software and
most of them might have been working. But we do not have concrete testing for
any of IPv6 scenario or use cases which means we do not know what all scenarios
work properly or not regressed or never worked at all.

It is always difficult to guarantee that all the use cases of IPv6 work and
have been tested in the upstream gate. We can target to test and fix that one
by one.

This community wide goal cover the below scenarios:

#. OpenStack services (include mysql, rabbitmq etc) listen and communicate with
   each other on IPv6.

#. OpenStack booted VMs can communicate (to other VMs or OpenStack service
   endpoint) over IPv6. This scenario is much needed when OpenStack services
   like Octavia and Sahara need to communicate to other services from compute
   VM.

In most of the cases, above two scenarios might work fine but there is not
enough testing of IPv6. The purpose of this goal is to add the integration
testing of IPv6-only support setting for all the projects and adding the
IPv6 support for inter-service communication where it doesn't exist.
This way we can at least make sure that OpenStack services work fine on
IPv6-only environment.

.. note::

    Covering all the possible IPv6 scenarios and testing all projects
    resources, backend vendors driver or hardware is out of the scope of this
    goal. That might need more work and a large number of testing across all
    projects with various drivers. Each project team should encourage their
    vendors and partners to head in the direction of ipv6 native operation.

Once we have integration jobs running as voting on gate to test the
OpenStack services listen on IPv6 address and VM connectivity over
IPv6, below are the next steps for respective team to extend the
IPv6 testing scope or documentation:

#. Encourage vendors/backends to extend the IPv6-only testing as per
   their specific scenarios and use cases. Corresponding Project team
   can choose to document the same if any limitation over their supported
   backends.

#. OpenStack Deployment projects, can target to deploy the OpenStack using
   IPv6-only environment.

.. note::

   The above listed work is specific to few projects and not applicable for all
   the OpenStack projects so these are  out of scope if this goal and good
   to extend as per project requirement and scope.

* `Storyboard stories <https://storyboard.openstack.org/#!/story/2005477>`__
* `Storyboard dashboard <https://storyboard.openstack.org/#!/board/138>`__

Champion
========

Ghanshyam Mann(gmann) <gmann@ghanshyammann.com> has volunteered to drive this goal.

Gerrit Topic
============

To facilitate tracking commits related to this goal should use the
gerrit topic::

  IPv6-support-and-testing

Completion Criteria
===================

In order for a project to call this goal complete it must:

#. All Devstack plugins should use the standard variable like
   ``SERVICE_HOST``, ``SERVICE_LISTEN_ADDRESS`` to create the service
   endpoint or service listen address. Devstack plugins should not use
   any hard-coded value or any other variables not adjusted by
   devstack when it is configured for IPv6.

#. Run the voting integration job with IPv6-only setting in check and gate
   pipeline. This job will be suffixed as -IPv6-only. This integration job does
   not need to run all the tests present (or running in other integration
   jobs) in that project. The set of tests to run on these jobs will be
   decided on runtime based on each project requirement and considering the
   two scenarios listed above under the scope of this goal.
   For example:

   * New IPv6-only Tempest job can install devstack with
     default services with IPv6-only mode and run the IPv6 related tests
     only.

   * Or have a single integrated tempest job install devstack with all
     services enabled and tests their endpoints etc.

IPv6 setting on Devstack and Devstack plugins
---------------------------------------------

Devstack already has IPv6 setting support. Setting the
``SERVICE_IP_VERSION=6`` and not setting the ``SERVICE_HOST``
in local.conf will make projects to configure their services to listen
and create keystone endpoint on IPv6.

DevStack workflow:

#. If ``SERVICE_IP_VERSION`` == '6' then, devstack sets the ``SERVICE_HOST``
   to ``HOST_IPv6`` (if ``SERVICE_HOST`` is not set explicitly) and
   ``SERVICE_LISTEN_ADDRESS`` to ``[::]`` and other settings too.

#. Each project will use the ``SERVICE_HOST`` to create their service
   endpoint with this address.


The above setting make sure each service listen and communicate over IPv6. These
settings are confirmed for all six services which are configured by devstack.
We hope all the devstack-plugins also follow the same setting which means use
``SERVICE_HOST`` to create the endpoints. If not, we then need to add that
support on that project's devstack-plugin. One example of missing this setting
is in senlin's devstack plugin (as of drafting this goal) which directly use
``HOST_IP`` as listen address so setting the ``SERVICE_IP_VERSION=6`` does not
make senlin to listen on IPv6
- https://opendev.org/openstack/senlin/src/commit/f4a00ff076df16591ef3cd073f51f42405d2c34c/devstack/lib/senlin#L44


Gate jobs for IPv6-only setting
-------------------------------

* ``devstack-IPv6``
  This base job already exists and configures devstack for IPv6-only setting.
  This base job set ``SERVICE_HOST: ""`` to make ``SERVICE_IP_VERSION: 6``
  working. If ``SERVICE_HOST`` is not reset or overridden by any derived
  job then ``SERVICE_IP_VERSION: 6`` has no effect.

* All ``*-IPv6-only`` integration jobs will use the devstack base job as
  parent.

* Tempest will provide the IPv6-only integration job which can be added
  in ``integrated-gate`` template.


References
==========

Devstack has `base job
<https://opendev.org/openstack/devstack/src/branch/master/.zuul.yaml#L486>`__
ready to use.

Tempest run the `Tempest IPv6 job
<https://opendev.org/openstack/tempest/src/branch/master/.zuul.yaml#L175>`__
running but as non voting.

Oslo utils common `netutils
<https://opendev.org/openstack/oslo.utils/src/branch/master/oslo_utils/netutils.py>`__
to use for IPv6 settings and checks.

Reference of this goal idea in `community-goals
<https://etherpad.openstack.org/p/community-goals>`__
etherpad(#14).

Current State / Anticipated Impact
==================================

Most projects might be working fine with IPv6, but there is no testing
to confirm IPv6 functionality and to avoid any breaking change to merge.
By having a voting job running IPv6-only setting will make sure we have
basic IPv6 scenario working and will not regress.
