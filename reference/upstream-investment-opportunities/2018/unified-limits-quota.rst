Unified Limits and Quota Management
===================================

Description
-----------

Most OpenStack services allow users to manage a resource, or a group of
resources, via an API. Operators use limits to ensure users are getting the
resources they pay for and need for their cloud use cases. These limits and
quotas are imperative to accurate billing, settings up price structure,
maximizing hardware usage, and ensuring resources are distributed throughout
the deployment as operators see fit.

Currently, there isn't a unified approach to limits across OpenStack services.
Services that do have an API for managing resource limits share a commonality
in the implementation but still suffer from inconsistencies. It is considered
risky to implement limit management separately across services since the
hierarchical nature of project namespaces in OpenStack can be complicated.
This forces developers to solve the same hard problem over and over again. This
design leaves limit API consistency across OpenStack up to the developers from
each project and hoping they all implement public APIs the same way. There is
work underway to consolidate the management of limits to a single service,
making it consumable to other services in the deployment while minimizing the
risk of deviating implementations in ways that negatively impact end users and
operators.

Value
-----

Improved Manageability
~~~~~~~~~~~~~~~~~~~~~~

By implementing a unified approach to limits, operators can efficiently manage
and view resource limits and quota across a deployment. Today, that experience
is fragmented and requires operators to query services individually if they
support limits. A unified limit interface allows operators to be more efficient
since they don't have to aggregate resource limits and information manually, or
by maintaining separate tooling and scripts to do it for them.

Consistent Interfaces
~~~~~~~~~~~~~~~~~~~~~

End users and operators benefit from a consistent interface. This reduces the
ability for interfaces to develop differences by using a centralized, unified
limit API. End users and operators expect the same experience regardless of the
resource, or which service controls that resource. Ensuring consistency reduces
cognitive load on behalf of the user and allows for a better experience with
the software.

Resource Flexibility
~~~~~~~~~~~~~~~~~~~~

A unified approach, where limits are defined in a consistent place and consumed
across services makes it easier to implement validation of resource limits.
This flexibility is powerful for operators in modeling how available resources
should, or should not, flow between projects. For example, a deployment
interested in maximizing resource utilization may choose to let free resource
flow between peer projects. This allows resources to move from stable projects
to ones that are more resource-intensive.

Reduced Complexity
~~~~~~~~~~~~~~~~~~

OpenStack's support for hierarchical multi-tenancy makes associating limits
across projects challenging. With unified limits, we're minimizing the area for
mistakes by allowing developers to reuse common code. Reuse reduces potential
complexity by isolating complicated logic into a few key places, instead of
duplicating it across many services. This reduction makes it less likely for
services to develop implementations or public facing APIs that deviate, even
slightly, from one another.

Contact
-------

For questions about getting involved with this initiative, reach out to the
OpenStack Discuss mailing `list
<http://lists.openstack.org/cgi-bin/mailman/listinfo/openstack-discuss>`_.
