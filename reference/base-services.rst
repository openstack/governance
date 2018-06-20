=============
Base services
=============

Definition
==========

Base services are services that OpenStack components can assume will be
present in any OpenStack deployment. OpenStack components *may* therefore
leverage advanced features exposed by those base services without fear of
increasing the overall operational complexity for OpenStack deployers.


Rationale
=========

There are two related reasons behind the existence of this list. First and
most straightforward, as stated by the Definition above, OpenStack
components are allowed to rely on a solution listed here without needing to
provide an alternative or fallback mechanism to account for situations when
the solution is not present. The other and perhaps more subtle reason is to
drive consistency of implementation between different OpenStack components
who may have similar needs but would otherwise likely end up embedding
their own varied implementations.

When someone developing a new feature is aware that there is a standard
solution provided by this list, they are likely (and encouraged) to use it
instead of designing something from scratch. This helps mitigate the risk
that multiple components might otherwise independently provide similar but
divergent solutions to the same basic problem space. It's also intended to
encourage more useful base functionality by default across OpenStack
components, because the perceived cost (to performance or complexity) of
including this one extra dependency is lessened by each other component of
the system which may also benefit from using it.


Current list of base services
=============================

**A Castellan-compatible key store**
  OpenStack components may keep secrets in a key store, using Oslo's
  Castellan library as an indirection layer. While OpenStack provides a
  Castellan-compatible key store service, Barbican, other key store backends
  are also available for Castellan. Note that in the context of the base
  services set Castellan is intended only to provide an interface for
  services to interact with a key store, and it should not be treated as a
  means to proxy API calls from users to that key store. In order to reduce
  unnecessary exposure risks, any user interaction with secret material
  should be left to a dedicated API instead (preferably as provided by
  Barbican).

**An oslo.db-compatible database**
  OpenStack components store data in a database, using oslo.db as an
  indirection layer. While most OpenStack deployments use MySQL, other
  databases are supported.

**An oslo.messaging-compatible message queue**
  Some inter-process and inter-service communication in OpenStack
  components is accomplished using message queues through oslo.messaging
  as an indirection layer. While most OpenStack deployments use RabbitMQ,
  other message queues are supported.

**Etcd**
  OpenStack components may use Etcd, a distributed reliable key-value store
  for distributed key locking, storing configuration, keeping track of
  service live-ness and other scenarios.

**Keystone**
  Keystone handles AuthN/AuthZ for OpenStack components.
  Deployments can assume that Keystone will be present to perform that role.


Process for addition or removal
===============================

Leveraging features from a base service (rather than working around
limitations or badly reinventing the wheel) is key to reaching acceptable
levels of stability, performance and scaling. However, since they will likely
have to be deployed in most OpenStack deployments, base services increase the
operational complexity of running OpenStack. It is therefore very important
to balance those two sides and conservatively consider proposed additions to
the base services list, especially when those additions introduce a whole new
class of operational challenges.

Once services start to make use of advanced features in a base service, it
is difficult to remove it from the list and make it a specific dependency
instead. Removals from the base service list should therefore be a rare and
carefully considered event.

Proposed modifications to this document require a formal vote from the
Technical Committee membership.
