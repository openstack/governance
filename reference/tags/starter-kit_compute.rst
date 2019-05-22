..
  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-starter-kit:compute`:

===================
starter-kit:compute
===================

A common starting point for a Compute oriented OpenStack cloud that
can be expanded over time to include more of the OpenStack universe.


Application to current deliverables
===================================

.. tagged-projects:: starter-kit:compute


Rationale
=========

The OpenStack Mission Statement: "To produce the ubiquitous Open
Source Cloud Computing platform that will meet the needs of public and
private clouds regardless of size, by being simple to implement and
massively scalable."

When new deployers first approach OpenStack as a project, they are
presented with a vast and wonderful array of choices of components
they could choose to begin with. So vast and wonderful that it becomes
really hard for people to understand where to start; be confident
that decisions they make will prevent them from deploying something
usable; and ensure they are able to expand the scope of their
OpenStack over time.

This paralysis of choice leads to substantial confusion and
frustration, and drives a lot of would-be-adopters away for other
stacks where there is a more clear starting point.

Because there has been such a robust discussion around this proposed
tag, this tag definition attempts to clarify major questions and
rationale that we've seen up to this point.

Why a *Compute* Starter Kit?
----------------------------

There are many ways one can use OpenStack, but based on the most
recent User Survey, 98% of Production and Dev / Test clouds are using
Nova [1], the highest of all OpenStack components. Even with a margin
of error, we can assume that a Compute cloud is a key feature that's
wanted by nearly everyone that enters our community.

Why a Compute *Starter Kit*?
----------------------------

The intent is to define a small subset of projects that allow the
deployer to experiment with both stateful and stateless uses of
OpenStack. The target audience is someone new to cloud computing that
is kicking the tires on a small number of servers in a basement or
back room. It's an attempt to frame OpenStack in a way that it will
come in through the back door of an organization by curious and
adventurous Ops folks (like Linux did in the early days), not just
through the front door via a sales channel.

Starter Kit implies this is not the end point, but just a beginning.

Why is this needed?
-------------------

The 'big tent' project structure reform of 2014 has been great for expanding
the scope and features that are part of OpenStack. However that has scared and
confused many members of our community who used the integrated release as
their starting point, and see that now going away. Smaller Operators,
Trainers, Hobbyists all have been asking the question, "where do I
start?".

The TC can either frame the question and provide the answer, or we can
abdicate on this issue and leave it to others. I think we do a
disservice to our community to punt on this issue.

Isn't this just Defcore?
------------------------

The starter kit doesn't intend to be Defcore. It's not expected that a
starter kit compute cloud has enough features to actually be Defcore
compliant. This is about a base minimal set of features to get people
familiar with the OpenStack universe. It's the hope that compute
starter kits could grow up into actual Defcore compatible clouds
before they move into production.

How would one expand on the Starter Kit?
----------------------------------------

The vision for the starter kit is it's a starting place, with function
that nearly all clouds will eventually want to have, and then
documented ways to expand the cloud into additional functions. Where at all
possible, expanding the Starter Kit should be a non-disruptive add rather
than a replacement of one option for another.

For instance, a Compute Starter Kit which starts with a file based
Glance is completely suitable for a small number of base
images. However as the needs of such a cloud grow, there becomes a
point at which this is no longer true, and adding a Swift installation
to handle image storage is a much better option. The user could then
migrate their content from file based to Swift. This also exposes them
to a new set of things they can do with an Object API in their
OpenStack environment.

The same kind of natural expansion could be done with projects such as
Heat, Trove, Sahara and others when higher level functionality is
desired out of their OpenStack cloud.

For some things where there are natural choices, such as Nova Network
or Neutron, it's important to keep the ability to naturally expand the cloud
over time in mind. While Nova Network is simpler to set up and run, the
transition to a Neutron-based cloud is not the same as swapping out a
Glance storage backend. It is for that reason that the starter-kit
recommends starting with Neutron configured for Provider Networks
with Linux Bridge as a simple enough configuration which still has the
possibility to add more complex SDN backends at a later date.

Doesn't this conflate multiple compute use cases?
-------------------------------------------------

The moment you start a conversation about cloud "use cases" you assume
a reasonably mature understanding of cloud and all its possible use
cases (aka: stateful mail servers, stateless build servers, elastic
webservers to handle holiday load). People that already have "use
cases" likely do not need a starter kit.

The starter kit concept is for people that are early in their cloud
journey. These are people that do not yet have use cases, and probably
won't until they experiment some with a starter kit.

For those people starting their journey into cloud computing,
it provides an easy way to get used to API driven ephemeral computes.
This allows them to see how existing workloads
would fit in OpenStack, as well as the possibilities for building new
OpenStack / cloud native workloads. Although support for persistent
volumes is not included, the persistence of ephemeral drives is actually
already as good as the persistence of local-disk workloads, and it is a
non-disruptive addition to include persistent volumes in the future
should the user decide they want them.

Does this mean all users have to start here?
--------------------------------------------

Absolutely not. OpenStack is a wide and vast ecosystem of really
interesting projects. Anyone who feels they don't need this guidance
is welcome to ignore it and build the right purpose built cloud for
them. This is meant as a bridge to those users who don't feel
confident doing that to bring them into the OpenStack universe.

Requirements
============

* All projects must actively maintain stable branches

  Rationale: these users will typically deploy stable releases only,
  and upgrade on stable point releases before jumping to the next
  stable release.

* All projects must only use relational database and queue system

  Rationale: providing HA stories for a relational database and amqp
  is substantial operational burden. Additional storage / messaging
  technologies provide too high an operational burden to meet for
  initial setup.

* All projects must use oslo.config, oslo.log

  Rationale: both of these are operator in / out surfaces. All
  projects in here should have the same mechanisms for input / output
  from an operational standpoint.

* All projects must support upgrade without config file change

  Rationale: the expected upgrade model is code upgrade on existing
  config files, cleaning up deprecation issues before upgrading to the next.

* All projects must be a required to put a persistent VM on the network.

  Rationale: we'd like to create a small enough starting point that
  getting everything up and running is a manageable project. We'd like
  to support persistent VMs because it's something most operators are
  going to immediately have a use for, and can thus try it out for
  real in their environment.

* The projects in this tag should make it easy to add new OpenStack
  projects into such a deployment over time.

  Rationale: we'd like this to be a solid bit of 'seed corn' from
  which a larger and richer OpenStack deployment can be built out
  over time. Starting small with the ability to grow helps OpenStack adoption.


Tag application process
=======================

There is no need to apply for addition or removal.

Deprecation
===========

No deprecation assumed, though there is the assumption that this
concept will be revisited at every major release boundary for
suitability.


References
==========
[1] - http://superuser.openstack.org/articles/openstack-users-share-how-their-deployments-stack-up
