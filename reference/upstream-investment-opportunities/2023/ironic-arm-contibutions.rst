==================
Ironic ARM Support
==================

Summary
-------

The OpenStack community is seeking ARM hardware and system administrators or
developers with background in provisioning ARM devices to partner with the
Ironic bare metal team. The Ironic project produces the OpenStack service and
libraries to manage and provision physical machines.

With an experimental image for Ironic Python Agent already available, some
operators have successfully provisioned ARM hardware with Ironic. However,
in order to promote it to supported status, we still need testing on
actual hardware with third-party CI to bring it in parity with our support
for x86 hardware. Also, Ironic documentation needs to contain information
about what types of ARM hardware is supported and how to configure it. Companies
interested in investing in this opportunity can provide hosted hardware for
third-party CI or staff time to contribute to this goal.

Business Case
-------------

Ironic supports many different hardware platforms; many in cooperation with
hardware vendors who create the hardware Ironic provisions. Historically, this
cooperation has led those pieces of hardware to have well-tested drivers with
support of many of the advanced features of the hardware.

Sponsoring the first Ironic ARM third-party CI environment, as well as providing
one or more system administrators or developers with experience in managing it,
would ensure that the provided ARM hardware would be well-supported in Ironic.
Ironic has always been on the forefront of hardware automation, and working
with the Ironic team is an extremely good way to level up your knowledge of
hardware and how it interacts with cloud computing.

As an additional benefit, your hardware, running as part of the OpenStack CI
system, will be tested automatically with any Ironic patch relating to ARM
support. This helps you ensure your hardware provides a stable interface for
any hardware automation system, not just Ironic.

Technical Details
-----------------

Ironic is a collection of services and libraries for supporting automated
deployment of bare metal servers. In the OpenStack ecosystem, it enables users
to provision bare metal servers as if they were virtual machines. Outside of
the OpenStack ecosystem, it's also used standalone or with other cloud
management tools such as `Metal3 <https://metal3.io/>`_.

Most Ironic features are hardware-agnostic, and tested against fake hardware
emulated using VMs fronted by an emulated BMC interface. However, Ironic also
has multiple third-party CI systems that test hardware driver code against
actual hardware. This insures that operators can trust that those hardware
specific features work properly in Ironic. Having actual hardware to test on
is even more important when evaluating support for an entirely new system
architecture.

A successful contribution to this Ironic project would include:
#. Hosted hardware, integrated with Ironic via third-party CI.
#. A system administrator or developer with experience in managing the hardware.
#. Providing technical expertise about the BMC and how to interact with it.

Contact
-------

Join the OpenStack Ironic (#openstack-ironic) or TC (#openstack-tc) channel
on `OFTC <https://www.oftc.net/>`_ via matrix or IRC.

You can also reach out through the `OpenStack Community Mailing List
<mailto:openstack-discuss@lists.openstack.org>`_ if you would like to get
involved.
