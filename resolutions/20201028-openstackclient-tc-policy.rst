====================================
2020-10-28 OpenStackClient TC Policy
====================================
OpenStackClient (aka OSC) is a command-line client for OpenStack that
brings the command set for OpenStack service APIs together in a single
shell with a uniform command structure[0].

For several releases now, there has been much debate about unifying on
a single client and the best way to approach reaching parity between
the OSC and project specific clients that exist.

Having to use more than one client in a basic workflow is a very
confusing and frustrating experience for OpenStack users. Using a
combination of clients makes OpenStack feel disjointed and overly
complex.

In order to better support the user experience and encourage adoption
by new users of the unified client, we will have a twofold policy.

Firstly, going forward, OpenStack services should focus on ensuring
that all user-oriented documents use OpenStackClient CLIs wherever
possible, close gaps in it where necessary to enable this, and call
out specific and intentional uses of the python clients as
transitional until support can be added.

Secondly, in an effort to consume our preferred tooling, any scripts
or tests (outside of tempest) that interact with an OpenStack service
in our CI environment should use the OpenStackClient or OpenStackSDK
wherever possible. When this is not possible, a bug should be filed
highlighting the feature gap.

This resolution is not going to dictate a completion date, but is to
ensure that we make continuous forward progress in that direction.

[0] https://docs.openstack.org/python-openstackclient/latest/
