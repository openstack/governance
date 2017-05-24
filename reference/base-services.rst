=============
Base services
=============

Definition
==========

Base services are services that OpenStack components can assume will be
present in any OpenStack deployment. OpenStack components *may* therefore
leverage advanced features exposed by those base services without fear of
increasing the overall operational complexity for OpenStack deployers.


Current list of base services
=============================

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
