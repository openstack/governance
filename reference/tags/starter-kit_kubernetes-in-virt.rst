..
  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-starter-kit:kubernetes-in-virt`:

==============================
starter-kit:kubernetes-in-virt
==============================

A common starting point for an OpenStack cloud that can be used to deploy
Kubernetes clusters on virtual machines in multiple tenants, and provides all
of the services that Kubernetes expects from a cloud.

Application to current deliverables
===================================

.. tagged-projects:: starter-kit:kubernetes-in-virt

Rationale
=========

Many application developers now target the Kubernetes API, rather than any
specific cloud API, as the 'operating system' for cloud-native applications.
Kubernetes is designed to run within a cloud, and to expect the cloud to
provide multitenant isolation between different Kubernetes clusters. OpenStack
can supply this, but it is not always clear to users without a lot of research
which capabilities are expected by Kubernetes and hence which OpenStack
services are required to support them. The starter kit provides guidance to
potential users on how to get started building a cloud that meets these
requirements.

Included Features
-----------------

Compute
~~~~~~~

Kubernetes runs on servers, and this starter kit focuses (as most clouds do) on
virtual machines, so the projects in the :doc:`Compute Starter Kit
<starter-kit_compute>` for providing minimal multitenant management of
virtual machines are required.

File Storage
~~~~~~~~~~~~

Almost all applications running on Kubernetes will require persistent storage,
and of those requiring persistent *local* storage, most will prefer RWX
(Read/Write Many) semantics to prevent downtime when pods move around. Manila
provides RWX-capable persistent file storage for containers running in
Kubernetes via the `Manila CSI plugin`_.

Networking
~~~~~~~~~~

Kubernetes clusters need to be connected to tenant networks, so the Neutron
project (which is also part of the :doc:`Compute Starter Kit
<starter-kit_compute>`) is included.

`Kuryr-kubernetes`_ is a collection of tools that run in tenant clusters to
enable direct use of Neutron networks from containers running in Kubernetes,
avoiding a second network overlay layer.

Load Balancing
~~~~~~~~~~~~~~

Most externally-facing HTTP services running in Kubernetes will typically use
an Ingress to provide load balancing and :abbr:`TLS (Transport Layer Security)`
termination (amongst other things). Octavia provides a highly-available, truly
load-balanced solution for this --- which is difficult or impossible to get
from anything but an underlying cloud --- via the `Octavia Ingress Controller`_

Both kuryr-kubernetes and the `OpenStack Cloud Controller Load Balancer
module`_ also use Octavia to provide load balancing for Services of type
``LoadBalancer``. Unlike Ingresses, which share a Layer 7 load balancer, each
Service of this type in Kubernetes gets its own load balancer. For OpenStack
clouds using the `OVN <https://www.ovn.org/>`_ backend for Neutron, the `OVN
driver for Octavia
<https://docs.openstack.org/ovn-octavia-provider/latest/admin/driver.html>`_
offers a lightweight Layer 4 network load balancing implementation for Services
that don't require higher-layer features.

DNS
~~~

Every Kubernetes cluster requires a DNS record for the control plane, and a
wildcard DNS record for any services running in the cluster. Designate allows
tenants to configure these autonomously, so that setting up clusters within a
tenant project doesn't require manual intervention from an administrator, and
its integration with Neutron means it can act as a trusted source of Reverse
DNS records.

DNS records for services running within the cluster can also be exported to
Designate via its integration with the Kubernetes `ExternalDNS
<https://github.com/kubernetes-sigs/external-dns#readme>`_ project.

Key Management
~~~~~~~~~~~~~~

By default, Kubernetes Secrets aren't. Even if you `enable encryption
<https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/>`_, the
encryption keys are merely stored in etcd alongside the data they encrypt,
meaning that if the database is leaked it might as well not be encrypted at
all. It's turtles all the way down until you get to a `key management service
<https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/>`_
(preferably backed by an HSM) provided by the cloud, such as Barbican. This is
accessed through the `Barbican KMS plugin`_.

Notable Omissions
-----------------

Bare Metal Compute
~~~~~~~~~~~~~~~~~~

The addition of Ironic would allow Kubernetes to be deployed on bare metal
also. However, this is not included in the starter kit both because it is not
strictly necessary and because the overall shape of a bare metal--specific
cloud for hosting Kubernetes might look `different
<https://governance.openstack.org/ideas/ideas/teapot/index.html>`_.

Block Storage
~~~~~~~~~~~~~

Although Cinder block storage can be, and often is, used from Kubernetes via
the `Cinder CSI plugin`_, it offers only RWO (Read/Write One) semantics, and is
thus more limited than Manila.

Users with other use cases for Cinder (such as requiring persistent volumes in
OpenStack) may choose to deploy it alongside or sometimes instead of Manila,
but it is not the first choice for a minimal starter kit.

Object Storage
~~~~~~~~~~~~~~

Object storage such as that provided by Swift is a very common requirement for
cloud-native applications, whether they run in Kubernetes or directly in a
cloud such as OpenStack. However, this storage tends to be accessed purely at
the application level, and not via Kubernetes APIs. (However, there is `a
proposal <https://github.com/kubernetes/enhancements/pull/1383>`_ to change
this.) Since the requirement is application-dependent, object storage is not
included in the starter kit.

Tag application process
=======================

There is no need to apply for addition or removal.

Deprecation
===========

No deprecation assumed, though there is the assumption that this concept may be
revisited at any major release boundary for suitability.


.. _Kuryr-kubernetes: https://docs.openstack.org/kuryr-kubernetes/
.. _Manila CSI plugin: https://github.com/kubernetes/cloud-provider-openstack/blob/master/docs/using-manila-csi-plugin.md#readme
.. _Octavia Ingress Controller: https://github.com/kubernetes/cloud-provider-openstack/blob/master/docs/using-octavia-ingress-controller.md#readme
.. _OpenStack Cloud Controller Load Balancer module: https://github.com/kubernetes/cloud-provider-openstack/blob/master/docs/using-openstack-cloud-controller-manager.md#load-balancer
.. _Barbican KMS plugin: https://github.com/kubernetes/cloud-provider-openstack/blob/master/docs/using-barbican-kms-plugin.md#readme
.. _Cinder CSI plugin: https://github.com/kubernetes/cloud-provider-openstack/blob/master/docs/using-cinder-csi-plugin.md#readme
