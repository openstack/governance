=============================================
 2017-03-17 OpenStack and Cloud Applications
=============================================

The OpenStack Mission
---------------------

OpenStack's mission is:

  To produce a ubiquitous Open Source Cloud Computing platform that is
  easy to use, simple to implement, interoperable between deployments,
  works well at all scales, and meets the needs of users and operators of
  both public and private clouds.


Implications for Cloud Applications
-----------------------------------

Proprietary APIs lock users in to a single vendor and thus expose them to
possible `rent-seeking`_. We develop OpenStack because we believe this should
not be the price of entry to cloud computing. Our goal is to provide a viable
alternative Open Source cloud API `and implementation`_ so that users can
select, and switch, vendors (including moving between public and private
clouds) based on the value they provide instead of being hostage to a
proprietary API.

Even Open Source APIs create lock-in, of course, but not *vendor* lock-in_.
Every user who is locked in to an OpenStack API is a user we have saved from
being locked in to a single proprietary vendor. This is OpenStack's highest
purpose. (Conversely, every user who is locked in to a single OpenStack vendor
due to non-interoperability of solutions represents a failure of our mission.)

Therefore, excellent support for cloud-aware applications -- that is,
applications that access the cloud's APIs directly -- is imperative if
OpenStack is to fulfill its mission. There are many existing applications that
are self-contained (that is, they could run on any server or VPS_) and it is
important that they run well in OpenStack clouds. However, this cannot be a
substitute for OpenStack's support of cloud-aware applications. Only if
developers of cloud-aware applications see OpenStack as a competitive platform
on which to build new cloud-aware applications can we help them to avoid
proprietary lock-in.

Many factors contribute to making a platform attractive to developers, but
robust security is the *sine qua non* for that large proportion of applications
that are network-facing. OpenStack therefore requires an application-centric
(not just user-centric) authentication and authorization model. It must give
fine-grained control to the application developer (not administrator) to
delegate, in perpetuity until revoked, **minimal** privileges to access
OpenStack APIs to the **parts** of the application that need them.\ [#]_
Application developers can also benefit from the broad range of cloud services
that are already, or in the future will become, part of OpenStack. These
services can help them to, for example, reduce development effort, centralize
scarce operational skillsets in their organization, scale at finer levels of
granularity, share expensive resources efficiently, provide reliability
guarantees cheaply by amortizing the cost over multiple applications, help the
application to manage its own infrastructure, or obtain from the cloud
information that it needs to do so. Many OpenStack services offer more than one
of those benefits. Some of those services themselves comprise cloud-aware
applications running on the virtual compute infrastructure.

We recognise that some cloud-aware application developers may work with
additional layers of abstraction on top of OpenStack's virtual compute
infrastructure, such as that provided by a Container Orchestration Engine (COE)
or Platform as a Service (PaaS). In such cases, we may regard the COE or PaaS
as part of the application layer from OpenStack's perspective. OpenStack can
add considerable value to these layers by allowing them to become cloud-aware
themselves or to be supplemented by cloud-aware management services.

Furthermore, we anticipate that many applications of the future will be
heterogeneous in their infrastructure needs: parts of an application may be
implemented running directly on the virtual compute infrastructure, other parts
in shared multi-tenant cloud services, and still others on top of a third-party
COE or PaaS layer. For this reason, we will seek to partner and integrate with
Open Source COE and PaaS projects to ensure that their workloads also have
seamless access to the full range of OpenStack cloud services and to other
application components deployed directly on the virtual compute infrastructure.

We invite all OpenStack projects to review their development priorities for
alignment with the most critical aspects of our mission: to provide a secure,
simple, scalable, interoperable set of services to the applications that depend
on OpenStack APIs.

.. _rent-seeking: https://en.wikipedia.org/wiki/Rent-seeking
.. _lock-in: https://en.wikipedia.org/wiki/Vendor_lock-in
.. _and implementation: https://governance.openstack.org/tc/reference/principles.html#openstack-primarily-produces-software
.. _VPS: https://en.wikipedia.org/wiki/Virtual_private_server

.. rubric:: Footnotes

.. [#] For instance, the first steps toward this might be to `eliminate write
   access`_ to the whole project for every user in the default policy;
   establish a Keystone domain, or method of provisioning domains, in which to
   create application user accounts that is consistent between clouds; and
   provide a secure method to `provision, rotate, and deliver credentials`_ to
   the application. Obviously the exact technical solutions will be determined
   through the usual open design process.

.. _eliminate write access: https://review.opendev.org/#q,Ib4cc7141d900881a7dc20842eb5d68eb90521fdd,n,z
.. _provision, rotate, and deliver credentials: https://review.opendev.org/#q,I86a994ca94e2d6a2a4e3753ffab107afc38d3dec,n,z
