==================================
Consistent and Secure Default RBAC
==================================


Problem Summary
===============

OpenStack's initial goal to be a multi-tenant platform drove the idea that
users operate within the confines of one project at a time. Early versions of
the authorization system, which included keystone and various middleware,
fulfilled this requirement.

However, OpenStack's explosive growth and adoption added services and API
surface area to the ecosystem. This growth quickly outpaced the authorization
engine. This allowed the community to develop rich APIs, across services, that
operate on different layers of the infrastructure. For example, OpenStack has
APIs that manage compute hosts, services, endpoints, domains, physical
networks, and storage pools. All of these resources require knowledge about the
underlying hardware, deployment architecture, and usage within a given
organization. These APIs are clearly targeted at different users from APIs that
expose resources, like instance, block storage devices, or virtual networks.

The authorization strategy didn't age gracefully with the rest of OpenStack.
This means we used the best available tools at the time to protect the API we
were developing across OpenStack.

This led to the following problems:

#. By default, users were either average end-users or operators, which is far
   too `restrictive <https://launchpad.net/bugs/968696>`_ for real-world clouds
#. The design violated the principle of least privilege
#. Inconsistent authorization behavior across services, resulting in some
   default policies being completely open to any user
#. Operators need to be intimately familiar with the policy implementation to
   supply overrides for valid use cases (read-only privileges)
#. Auditing OpenStack APIs requires administrative access
#. Having no role hierarchy makes it hard to establish any low-level collection
   permission collection, like a role for read-only access, which is
   implemented inconsistently across deployments

The above issues aren't a complete set of all problems related to authorization
in OpenStack, but they are pain points we, as the upstream community, know
about. They also prohibit the adoption of OpenStack by:

- Requiring operators to understand and configure policy for any compliance
  target
- Aggregating all authoritative power into select users, violating the
  constrained RBAC model
- Not providing a role hierarchy that allows for easy authorization management
- Not providing a granular set of permissions
- Not providing an easy way for operators to audit what a particular user can
  do within the deployment


Where are we today?
===================

The following initiatives are in progress or complete:

#. Moved `policy and documentation into code
   <https://governance.openstack.org/tc/goals/selected/queens/policy-in-code.html>`_
#. Created a default role hierarchy in keystone (`default roles specification
   <https://specs.openstack.org/openstack/keystone-specs/specs/keystone/rocky/define-default-roles.html>`_)
#. Added a new scope to keystone (`system scope specification
   <https://specs.openstack.org/openstack/keystone-specs/specs/keystone/queens/system-scope.html>`_)
#. Updated all libraries to understand the new scope
#. Documented the idea of `personas
   <https://docs.openstack.org/keystone/latest/admin/service-api-protection.html>`_
#. Created a `policy popup team
   <https://governance.openstack.org/tc/reference/popup-teams.html#secure-default-policies>`_
   to enable this work across more OpenStack services.
#. Proposed and implemented several testing strategies using tempest,
   functional, and unit tests for projects to use as a reference
#. Audited every active OpenStack project API and mapped administrative
   functionality into the system-scope personas
#. Applied the reader and member role consistently to project-scoped resources
#. Converted each service policy file from using `JSON to YAML
   <https://governance.openstack.org/tc/goals/selected/wallaby/migrate-policy-format-from-json-to-yaml.html>`_

To date, the work to audit each API, propose new default policies, and
implement unit, functional, or tempest tests has accumulated more than 130,000
lines of code change across 41 repositories.


Direction change
================

Throughout this process we've communicated with operators and end users about
the changes to implement a new scope type. Early feedback on the approach to
isolate system-level APIs behind a new authorization target alluded to the
ability for operators to continue supporting their users by interacting with
project-owned resources. A good example of this use case is evacuating an
instance from a host.

Based on the initial discussions of how system-scope would be used, we decided
to allow operators to interact with project-owned resources using system-scoped
tokens.

It wasn't until we started applying this idea to various services that we
realized it was going to cause issues with service-to-service communication and
require significant refactoring in each service. This is due to the fact that
OpenStack services have been developed with the assumption that project IDs
will always be present, and it's rare to interact with a resource without a
project ID associated to the request.

For example, if an operator uses a system-scoped token to create an instance
for a user in a specific project, they need to specify the project ID that owns
the instance and they need to pass their system-scoped token to the service.
Each service would need to understand the concept of system-scope and make sure
to use the correct project ID. This approach is error prone, especially since
each OpenStack service can have multiple clients to other services. We worked
through the design and uncovered these issues while implementing a
`specification
<https://specs.openstack.org/openstack/keystone-specs/specs/keystonemiddleware/xena/secure-rbac-project-id-passthrough.html>`_
we targeted for the Xena release that allowed system users to pass-through
project IDs with a system-scoped token. This work would have required
significant refactoring and non-trivial changes to multiple projects,
increasing the risk in implementing the functionality consistently and safely.

We spent significant amount of time during the Yoga PTG revisiting the
discussion (`etherpad
<https://etherpad.opendev.org/p/policy-popup-yoga-ptg>`_).  Ultimately, we
stepped back and realized that the primary use case for allowing system users
to operate on project-owned resources with a system-scoped token was to allow
for backwards compatibility.

While we certainly want to make things as easy as possible for operators to
use, we're not sure the additional overhead required to teach each OpenStack
service about system-scope in this way would be beneficial. This is especially
true when we considered the fact that a single user account, or bearer token,
carries a significant amount of authorization. We're really just pushing the
problem from a user with the `admin` role on a project to anyone with the
`admin` role on the system.

Instead, we decided to remove the assumption that anyone using a system-scoped
token should automatically be able to access any OpenStack API.

To clarify, we did agree that system administrators (e.g., operators) should be
able to manage resources within a project, but we don't want to conflate that
use case into the system-scope construct for the reasons described above.
System administrators have the ability to grant themselves authorization to
projects, domains, and the deployment system itself. A few extra steps would
allow them to get the correct authorization to the intended project and perform
the necessary operations using a token flow that's already supported.
Additionally, it provides a very clear audit trail.

So, where do we go from here?

We have a set of OpenStack services that have over-extended the usage of
system-scope and applied it to project-specific resources. Other services have
yet to adopt the system-scope feature.

Currently, none of the policy work we've done since Queens is widely usable by
default since it's not applied consistently across services. The idea of this
community goal is to define the absolute minimum amount of work required to
allow operators to opt into the new authorization behavior and start using the
personas we've been developing since Queens.

We should defer any policy work that isn't absolutely necessary to the criteria
of this goal for future improvements. Otherwise we risk delaying the
functionality another release. Instead, we can acknowledge the gaps, order them
on a timeline for future improvements, and at least deliver something useful to
operators sooner rather than later.

Phase 1
=======

Implement support for system-admin, project-admin, project-member, and
project-reader personas.

The project-member and project-reader changes are relatively trivial. The
majority of the work in this phase is focused on breaking administrative
functionality into the project-admin and system-admin personas.

Re-evaluate project-specific API policies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We need to go through each policy across OpenStack services and make sure it
aligns with the direction described above. *Ideally, each policy should only
include a single scope type*. Please refer to `Crafting check strings for APIs
that interact with multiple scopes`_ for APIs that are truly designed for
multiple scopes. For example, the following policy was written to eventually
allow system administrators to create instances on a targeted host using a
system-scoped token:

.. code-block:: python

   policy.DocumentedRuleDefault(
       name='os_compute_api:servers:create:forced_host',
       check_str='role:admin and project_id:%(project_id)s',
       scope_types=['system', 'project']
   )

Since instances are project-owned resources we want to keep the functionality
isolated to project-scoped tokens. The policy should be updated accordingly:

.. code-block:: python

   policy.DocumentedRuleDefault(
       name='os_compute_api:servers:create:forced_host',
       check_str='role:admin and project_id:%(project_id)s',
       scope_types=['project']
   )

This will only allow operators with a project-scoped token containing the
``admin`` role to perform targeted boot. If or when nova sanitizes hypervisor
discovery to expose information safely to end users, the policy could evolve
further (potentially in `Phase 2`_):

.. code-block:: python

   policy.DocumentedRuleDefault(
       name='os_compute_api:servers:create:forced_host',
       check_str='role:manager and project_id:%(project_id)s',
       scope_types=['project']
   )

This would push the functionality even closer to end users, making the API more
self-serviceable.

Isolate system-specific API policies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We need to perform the same exercise for system-specific API policies and
ensure system-level APIs are only accessed with system-scoped tokens. These
cases should be much more rare than the previous examples, since the majority
of OpenStack's APIs and resources have grown to expect project ownership.

We need to make sure APIs that are truly system-specific set the appropriate
scope type. An example of these resources are hypervisors:

.. code-block:: python

   policy.DocumentedRuleDefault(
       name='os_compute_api:os-hypervisors:list',
       check_str='role:admin',
       scope_types=['system']
   )

Managed volumes:

.. code-block:: python

    policy.DocumentedRuleDefault(
        name='volume_extension:volume_manage',
        check_str='role:admin',
        scope_types=['system'],
    )

Services and endpoints:

.. code-block:: python

   policy.DocumentedRuleDefault(
       name='identity:delete_service',
       check_str='role:admin',
       scope_types=['system']
   )
   policy.DocumentedRuleDefault(
       name='identity:create_endpoint',
       check_str='role:admin',
       scope_types=['system']
   )

.. note::
   Each example above only uses a role check in the check string. This is by
   design and allows for backwards compatibility while the ``[oslo_policy]
   enforce_scope=False`` because a user with the ``admin`` role on a project is
   still allowed to access that API.

   Once ``[oslo_policy] enforce_scope=True``, the API will only be exposed to
   system users. After we guarantee that scope enforcement happens in
   oslo.policy using ``enforce_scope`` we can re-assess the roles of each
   policy and loosen them as necessary (e.g., moving from ``role:admin`` to
   ``role:member`` or ``role:reader`` where system-member or system-reader is
   appropriate).

Crafting check strings for APIs that interact with multiple scopes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At this point, any remaining policies that are not either project-scoped or
system-scoped should have a valid use case for interacting with both scopes.

Flavors are a good example of a resource that should operate with multiple
scopes. Operators should be able to create, update, and delete flavors for a
deployment, which affects every project and user of the deployment. Project
users should be able to view flavors available for them to use. Additionally,
users with authorization on a domain should also be able to view flavors.

The following shows how you can specify multiple scopes for a single rule:

.. code-block:: python

  scope_types=['system', 'domain', 'project'],

Listing project resources across the deployment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now that we're taking a firm stance on how scope interacts with different types
of resources, we're presented with a problem.

Traditionally, anyone with the ``admin`` role, usually on a project, could list
all resources. This is usually implemented as a query parameter telling the
service that the user wants all instances in the entire deployment (e.g., ``GET
/v2.1/servers/detail?all_tenants=True``.) This pattern is applied across
resources and service, and it's applicable to instances, volumes, backups,
snapshots, etc.

The direction defined in this goal suggests that anyone with the ``admin`` role
on a project should only be able to view resources within that project, even if
that persona is reserved for operators. Additionally, we're also standing firm
in our decision to not allow system users to interact with project-owned
resources.

How do we support operators that wish to view all resources in a deployment?

There are at least four potential solutions:

#. Add domain-admin to `Phase 1`_
#. Add domain-admin to `Phase 2`_
#. Implement client-side functionality to brute force resource lists in `Phase
   1`_
#. Allow project-admins to view resources across the entire deployment

The first solution is to add formal support for domain-admin. This would allow
someone with the ``admin`` role on a domain to use a domain-scoped token to
call ``GET /v2.1/servers/detail``, and nova would understand that it needs to
filter the instance list by all projects owned by the domain. This is probably
the correct solution, but it adds to an already full schedule for services
implementing `Phase 1`_.

The second solution would push implementing domain-admin off to `Phase 2`_,
giving the community more time to focus on delivering `Phase 1`_. If we take
this approach, operators waiting to use this functionality won't have a way to
list all resources in the deployment in the Yoga, or potentially Z-release.

The third solution takes a brute force approach where the client recognizes it's
dealing with a domain-scoped token, queries keystone for all projects within
that domain, gets a token scoped to each project, and asks the service for all
resources with each project-scoped token. Then, it would aggregate all those
results together and present it to the user.

The fourth solution would be to continue allowing people with the ``admin``
role on a project to list all resources across the deployment (for applicable
APIs only.) The following is an example of what a policy would look like using
this approach:

.. code-block:: python

   policy.DocumentedRuleDefault(
       name='os_compute_api:servers:detail:get_all_tenants',
       check_str='role:admin',
       scope_types=['project']),

This would allow things to work as they do today for operators, but with the
understanding that this functionality is going to change when services adopt
`Phase 2`_. Eventually, domain users will be allowed to use list all resources
across projects and at that point, we should restrict project-admins from being
allowed to list resources outside their project:

.. code-block:: python

   policy.DocumentedRuleDefault(
       name='os_compute_api:servers:detail:get_all_tenants',
       check_str='role:admin',
       scope_types=['domain']),

This functionality is important for operators finding resources, especially for
support cases, like rebooting or live migrating an instance.

The direction for `Phase 1`_ is to use solution #4, where a project-admin can
continue listing resources across the deployment, while we target domain
support for `Phase 2`_ or `Phase 3`_.

How operators opt into the new functionality
--------------------------------------------

If we can complete each item above for the Yoga release, operators will be able
to configure each service to opt into the new defaults across all services,
securely implementing the same personas across the deployment::

  [oslo_policy]
  enforce_new_defaults=True
  enforce_scope=True

This configuration enables the following personas:

- System Administrator
   - Denoted by someone with the ``admin`` role on the ``system``
   - Intended for the most trusted operators or support personnel
   - Not intended for end users
   - Has the ability to interact with any resource in the deployment because
     they can give themselves any role on any authorization target (project,
     domain, or system)
   - *Can grant any role to any user or group on any project, domain, or
     system*
   - *Add or delete services and endpoints*
   - *Create new volume types*
   - *Move pre-existing volumes in and out of projects*
   - *Create or delete HSM transport keys*

- Project Admin
   - Denoted by someone with the ``admin`` role on a project
   - Intended for operators who need elevated privilege on project resources
   - Can perform operations on project resources that affect other projects in
     the deployment
   - Not intended for end users
   - *Forcibly reset the state of an instance*
   - *Forcibly deleting an application stack*
   - *Making an image public to the entire deployment*
   - *Create physical provider networks*

- Project Member
   - Denoted by someone with the ``member`` role on a project
   - Intended to be used by end users who consume resources within a project
   - *Create, delete, or update an instance*
   - *Create, delete, or update a volume*
   - *Create, delete, or update a network*

- Project Reader
   - Denoted by someone with the ``reader`` role on a project
   - Intended to be used by end users for read-only access within a project
   - Not allowed to make any writable changes to project-owned resources
   - *List and get instances*
   - *List and get volumes*
   - *List and get images, including private images within the project*
   - *List and get networks*

These new persona divide the current role of an operator between system-admin
and project-admin personas. This is by design and starts to slowly break down
the authorization associated to administrative tokens.

For increased usability, operators could bootstrap their trusted team of
operators or support with inherited role assignments on each domain, making it
easier for operators to get project-scoped tokens for each project in the
deployment::

  $ openstack role add --os-cloud system-admin --user 2c0865 --domain foo --inherited reader
  $ openstack role add --os-cloud system-admin --group b3dbc2 --domain foo --inherited admin

Phase 2
=======

#. Isolate service-to-service APIs to the ``service`` role
#. Update policies to incorporate project-manager
#. Implement domain-admin support where service keep track of domain IDs in
   addition to project IDs as owners of a resource

Any API developed for machines to communicate with each other should use the
``service`` role. This is an important part in reducing authorization for each
service. For example, neutron needs to inform nova about network changes, but
it shouldn't need the ability to create new users and groups in keystone, which
it currently has. The project-manager persona is described as follows:

- Project Manager
   - Denoted by someone with the ``manager`` role on a project
   - Intended to be used by end users
   - Slightly more privileged than regular project-members
   - *Locking and unlocking an instance*
   - *Setting the default volume type for a project*
   - *Setting the default secret store for a project*

Phase 3
=======

Implement system-member and system-reader personas. This allows operators to
use the principle of least privilege for their team members, support personnel,
or auditors.

#. Implement system-member persona for applicable system APIs
#. Implement system-reader persona for applicable system APIs

After we update the default for ``[oslo_policy] enforce_scope=True`` we can
re-assess all system-admin policies and loosen them to implement the
system-member and system-reader personas, resulting in the following
functionality.

- System Member
   - Denoted by someone with the ``member`` role on the ``system``
   - Intended for operators or lab technicians
   - Not intended for end users
   - *Manage hypervisors and aggregates*
   - *Manage resources in placement*

- System Reader
   - Denoted by someone with the ``reader`` role on the ``system``
   - Intended for operators or auditors for system-specific resources
   - Not intended for end users
   - *View hypervisor and aggregate information*
   - *List all cinder services*
   - *View all domains and identity providers within the deployment*

Champion
========

#. Lance Bragstad <lbragstad@redhat.com> (lbragstad)
#. Ghanshyam Mann <gmann@ghanshyammann.com> (gmann)


Gerrit Topic
============

To facilitate tracking, commits related to this goal should use the
gerrit topic::

  secure-rbac


Completion Date & Criteria
==========================

Yoga Timeline (7th Mar 2022)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Keystone implements a new default role called ``manager``

   The ``manager`` role will be a part of the role hierarchy and it will sit in
   between the ``admin`` and ``member`` roles. This work requires a keystone
   specification.

#. Keystone implements a new default role called ``service``

   The ``service`` will standardize a role that's already required in some
   default policies across OpenStack. This role must be built outside the
   existing role hierarchy, where ``admin`` implies ``manager`` implies
   ``member`` implies ``reader``. This work requires a keystone specification.

#. Keystone enforces scope by default

   Keystone sets ``keystone.conf [oslo_policy] enforce_scope = True``.

   Keystone has fully supported system-admin, system-member, system-reader,
   domain-admin, domain-member, domain-reader, project-admin, project-member,
   and project-reader since the Train release.

   For the Yoga release, Keystone should remove all deprecated policies, which
   will require operators to use the new personas. This will be relatively
   low-touch for end-users since Keystone's API is mostly administrative.
   This gives operators the opportunity to experiment with the domain and
   system personas.

#. Services start implementing `Phase 1`_

   At this point, all services are free to start implementing system-admin,
   project-admin, project-member, and project-reader personas as described
   above in `Phase 1`_. By the end of the Yoga release, at least one service
   must have `Phase 1`_ complete. `Phase 1`_ introduces the new personas but
   allows operators to opt into the new behavior for services that complete
   `Phase 1`_, allowing operators to upgrade smoothly to the new permission
   model on a per-service basis.

   It's important that we have an OpenStack-wide release note or statement that
   explicitly states the status of this work and how permissions behave across
   OpenStack services.

#. OpenStack-wide Personas Documentation

   We need very clear documentation that describes all the potential personas,
   what they mean, who they were designed for, and how to use them. By the end
   of the Yoga release, this document should include each persona and what its
   support is across OpenStack services.

   Engineers should use this documentation to determine what the default policy
   should be for APIs they're developing and maintaining. Operators should use
   it to understand what personas are the most appropriate for their users
   based on the permissions they need. The documentation should also clearly
   describe the scope associated to each API. Highlighting the relationship
   between scope and a resource will help build a frame of reference for
   operators delegating authorization on various scopes. It will also help
   establish the expectation that mixing and matching scopes won't be supported
   in future releases.

At this point, operators must run keystone with ``enforce_scope=True`` since
the deprecated policies will be gone, and the default value for this specific
option in keystone will be updated accordingly. They can also choose to run any
service that's completed `Phase 1`_. This will require the operator to
configure the service to use ``enforce_scope=True`` and
``enforce_new_defaults=True`` if they chose to adopt the new behavior for
services that support it.

This means that operators must use the correct scope when interacting with
services they've configured to enforce scope. For example, an operator will
need a system-scoped token to manage domains or service endpoints in keystone.
If the operator also deploys nova to enforce scope, they will need a
system-scoped token to manage hypervisors or aggregates.

Z-Release Timeline
^^^^^^^^^^^^^^^^^^

#. Keystone implements `Phase 2`_ and updates policies to include the
   ``manager`` role where applicable

   Keystone starts implementing support for ``manager`` across project, domain,
   and system scopes. Keystone has supported system-admin, system-member, and
   system-reader since Train, which completes the `Phase 3`_ goals

#. All services must implement `Phase 1`_

#. Any service that completed `Phase 1`_ in Yoga can set ``enforce_scope=True``
   by default

At this point, every OpenStack service will have completed `Phase 1`_, which
allows operators to opt into using system-admin, project-admin, project-member,
and project-reader across their entire deployment.

To summarize, operators will need to update every service configuration file
where they want to use system-admin, project-admin, project-manager,
project-member, and project-reader. For example:

#. Set ``glance-api.conf [DEFAULT] enforce_secure_defaults=True``
#. Set ``glance-api.conf [oslo_policy] enforce_scope=True``
#. Set ``glance-api.conf [oslo_policy] enforce_new_defaults=True``
#. Set ``neutron.conf [oslo_policy] enforce_scope=True``
#. Set ``neutron.conf [oslo_policy] enforce_new_defaults=True``
#. Set ``cinder.conf [oslo_policy] enforce_scope=True``
#. Set ``cinder.conf [oslo_policy] enforce_new_defaults=True``
#. Set ``ironic.conf [oslo_policy] enforce_scope=True``
#. Set ``ironic.conf [oslo_policy] enforce_new_defaults=True``
#. Set ``barbican.conf [oslo_policy] enforce_scope=True``
#. Set ``barbican.conf [oslo_policy] enforce_new_defaults=True``

AA-Release Timeline
^^^^^^^^^^^^^^^^^^^

#. Update oslo.policy ``enforce_scope=True``

   Since all services have completed `Phase 1`_, we can update the default in
   oslo.policy so that enforcement checks scope by default. This will allow
   each service to remove code to override the ``enforce_scope=True`` and use
   the upstream default from oslo.policy.

#. Any service that implemented `Phase 1`_ in Yoga and enabled
   ``enforce_scope`` in Z can removed deprecated policies used to implement
   `Phase 1`_ and can start implementing `Phase 2`_

Operators consuming the AA release will have the personas delivered in `Phase
1`_ available and enabled by default. This includes system-admin for all
system-level administrative APIs, project-admin for project-level
administrative APIs, project-member for common end-user interactions, and
project-reader for a read-only variant of project-member.

BB-Release Timeline
^^^^^^^^^^^^^^^^^^^

#. All services can remove deprecated policies used to implement `Phase 1`_

#. All services must implement `Phase 2`_

#. Any service that completed `Phase 2`_ in the AA release can remove the
   deprecated policies used to implement `Phase 2`_ and start implementing
   `Phase 3`_

Operators consuming the BB release will have full support for system-admin,
project-admin, project-member, project-reader, and service role dedicated for
service-to-service communication. Additionally, they will have a
project-manager persona for elevated privileges safe for end users on a
project.

CC-Release Timeline
^^^^^^^^^^^^^^^^^^^

#. All services can remove deprecated policies used to implement `Phase 2`_

#. All services must implement `Phase 3`_ and remove deprecated policies in a
   future release following an acceptable deprecation cycle

#. Any service that completed `Phase 3`_ in the BB release can remove the
   deprecated policies used to implement `Phase 3`_

Operator will have all the benefits from the BB release, as well as two
additional system personas called system-member and system-reader that will
enable operators, support personnel, and auditors who need access to system
resources.

References
==========

* Policy Pop-Up Team `wiki`_
* https://etherpad.opendev.org/p/policy-popup-yoga-ptg


Current State / Anticipated Impact
==================================

Current progress is maintained on the `wiki`_ page.

.. _wiki: https://wiki.openstack.org/wiki/Consistent_and_Secure_Default_Policies_Popup_Team
