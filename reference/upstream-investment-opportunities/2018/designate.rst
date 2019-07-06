Designate Contributors
======================

Description
-----------

`Designate`_ is a service that manages DNS Zones and Recordsets. It supports
multiple DNS Servers, and DNS Service Providers, making it vital for any
network or web-based application.

They need contributors to help find and fix bugs, develop new features, and
help maintain the quality of the project, including cross-project initiatives.
Designate is quite stable, with any new features requiring long term planning,
design, and phased implementation.

Designate welcomes everyone, from someone starting in the community to senior
contributors who want new, interesting problems to tackle. Contributors will
get to work on a project that will be a central part of any OpenStack
deployment and work on a project that needs to scale from a small single node
install to a system controlling DNS servers worldwide.

Value
-----

Flexibility
~~~~~~~~~~~

DNS is fundamental in gracefully directing users and applications to services.
It allows the flexibility to replace underlying hardware while presenting
consumers with a consistent endpoint. Designate provides this flexibility to
operators and end users.

Designate supports a wide range of drivers for various `DNS servers`_ and
providers, which allows deployers to integrate Designate into pre-existing
DNS infrastructures.

Self-Service
~~~~~~~~~~~~

Self-serviceability is a core tenet of OpenStack `technical vision`_. Designate
helps OpenStack clouds adhere to that principle by exposing DNS functionality
directly to end-users. Designate allows cloud operators to delegate the control
of DNS zones to end users, to avoid complex ticket based workflows for DNS
updates.


User Experience
---------------

When end users are building applications in a cloud native way, relying on
external tooling to provision DNS entries adds complexity. With the advancement
of IPv6, services required to have DNS entries, to avoid application user
confusion.

Designate adds an important part of the value add for cloud infrastructure,
and ensures that OpenStack has feature parity with other cloud providers.


Integrations
------------

Designate integrates with many other tools to allow for zero touch management
of DNS Zones and Records. The integration with neutron allows admins to have
PTR records (for reverse DNS lookups) managed for Floating IP ranges, without
giving direct privileged access to the reverse zone to users.

Tools like `letsencrypt certbot`_ allow for auto provisioning of SSL certs
using DNS-01 validation, while tools like `Heat`_, `Terraform`_ and `Ansible`_
allow for the provisioning of DNS Zones and Records to be integrated into
pre-existing workflows for applications.

Kubernetes `external-dns`_ support adds simple annotation based DNS management for
applications running in kubernetes clusters with load balancers or ingress
support.

Consistency
~~~~~~~~~~~

The OpenStack community continues to evolve, and this evolution requires large
cross-project initiatives. Furthermore, users and operators expect consistency
across the OpenStack platform. Examples from recent history include
OpenStack-wide support for `Python 3`_ and easing operator pain by moving
`policy configuration`_ into code. Ensuring Designate stays up-to-date with
these initiatives is imperative in reducing operational costs, complexity, and
user frustration.

Contact
-------

If you are interested, please join #openstack-dns on Freenode or contact the
Designate PTL (Graham Hayes - mugsie), the Technical Committee sponsor (TBD).
You may also email the openstack discuss mailing list with the tag [designate]
in the subject.

.. _`Designate`: https://governance.openstack.org/tc/reference/projects/designate.html
.. _`DNS servers`: https://docs.openstack.org/designate/latest/admin/support-matrix.html
.. _`technical vision`: https://governance.openstack.org/tc/reference/technical-vision.html
.. _`letsencrypt certbot` : https://pypi.org/project/certbot-dns-openstack/
.. _`Heat`: https://docs.openstack.org/heat/rocky/template_guide/openstack.html#OS::Designate::RecordSet
.. _`Terraform`: https://www.terraform.io/docs/providers/openstack/r/dns_recordset_v2.html
.. _`Ansible`: https://docs.ansible.com/ansible/latest/modules/os_zone_module.html#os-zone-module
.. _`external-dns`: https://github.com/kubernetes-incubator/external-dns
.. _`Python 3`: https://governance.openstack.org/tc/goals/stein/python3-first.html
.. _`policy configuration`: https://governance.openstack.org/tc/goals/queens/policy-in-code.html
.. _`list`: http://lists.openstack.org/cgi-bin/mailman/listinfo/openstack-discuss
