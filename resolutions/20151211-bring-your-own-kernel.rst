======================================================
2015-12-11 Compute Requirements for Images and Kernels
======================================================

It has become clear that the myriad selections in both compute operating system
and underlying technology such as bare metal or containers mean we should be
clear in the intent to provide a unified user experience across many OpenStack
clouds.

It is the opinion of the OpenStack Technical Committee that the following statements
should be true in the definition of an `OpenStack Powered Compute`_ cloud.

The following use key words as found in `RFC 2119`_.

- An `OpenStack Powered Compute`_ Cloud MUST allow end user Image Uploads
- An `OpenStack Powered Compute`_ Cloud MUST be able to boot a Linux Guest
- An `OpenStack Powered Compute`_ Cloud MUST be able to boot arbitrary operating
  system kernels the user uploads, given matching processor architecture
- An `OpenStack Powered Compute`_ Cloud MUST be able to provide those
  capabilities using VMs
- An `OpenStack Powered Compute`_ Cloud MAY additionally provide users the
  ability to boot uploaded images on Bare Metal machines
- An `OpenStack Powered Compute`_ Cloud MAY additionally provide users the
  ability to boot using more restrictive technologies such as containers, zones
  or jails

Images as provided by cloud deployers diverge, and cause pain for our end users
from an interoperability standpoint. While cloud providers may choose to provide
value with special images, OpenStack should spend effort in facilitating end
user choice in what base images they run. Direct image upload is an example of
a way to facilitate end user choice.

We take a strong stand on the ability to test the inbound interfaces a cloud
provides to a running server instance. In order to test the interfaces that a
user of an OpenStack cloud should be able to expect (for instance, does
config-drive show up, does the instance have the IP that neutron says it has)
we have to be able to have tests in the gate. Since OpenStack follows
:doc:`The Four Opens <../reference/new-projects-requirements>`
that means that our tests must be Open Source. Alternate versions of the tests
that might test the same interfaces but use Close Source Operating Systems are
not possible to be validated since we can't run those Operating Systems in the
gate, so cannot be accepted.

Linux is not an undue burden to ask someone to run. It runs on x86, power,
sparc, mips, alpha, atom and arm processors and even IBM z-Series mainframes.
It runs on phones, TVs, and watches. It is free and anyone can get an
operational image. The utilities the tests require of a Linux guest are
standard and available.

Asking someone to boot a Linux guest in order to test inbound interfaces is,
therefore, not only completely reasonable, it's the most reasonable and most
obvious thing possible.

An OpenStack cloud that has LXC, Docker, Rocket, Solaris-zones or other
lightweight container technology sounds pretty neat at first pass, but it turns
out that an LXC cloud would not allow a Solaris image and a Solaris Zones cloud
would not allow a Linux image. That is too much deployer choice bleeding
through the abstraction layer, and as such is bad for interoperability. While
there is nothing preventing deployers from using the OpenStack software to
create clouds that are solely based on such technologies, those clouds are
divergent from what OpenStack clouds are.

.. _RFC 2119: https://www.ietf.org/rfc/rfc2119.txt
.. _OpenStack Powered Compute: http://www.openstack.org/brand/interop/
.. _The Four Opens: 
