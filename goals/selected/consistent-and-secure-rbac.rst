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

In yoga cycle, we redefined this goal with the changes mentioned above so that
allowing system administrators to access system level resources APIs only and
allow project users to access project-level resource APIs. These changes have
been done for nova and neutron.

This was not the end of the RBAC design discussion. After knowing the operators'
use cases we used the feedback to redefine the direction in the Zed cycle.

The issues we are facing with `scope` concept:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. It breaks OpenStack existing NFV use case and orchestration tooling:

   When the deployment project started consuming the nova new policy defaults
   with scope enabled, we got to know that the scope enable will break heat
   (orchestration tooling), Tacker (NFV deployment) users or any operators
   script interacting all the OpenStack interfaces with administrators user.

   Heat 'create stack' API uses the user credentials (admin) to create project
   and system-level resources in backend services. For example, it creates
   project users in keystone (system level resource), flavors in nova (system
   level resource), servers in nova (project level resource), and networks in
   neutron (project level resource). If we enable the scope checking in
   services, then the user calling heat 'create stack' APIs which are scoped to
   either project (existing way) or system (if we change that) will not be able
   to call the system and project scoped APIs on the service side. We discussed
   the possible solutions in `Zed PTG
   <https://etherpad.opendev.org/p/z-ptg-keystone#L44>`_ , `openstack-discuss ML
   <http://lists.openstack.org/pipermail/openstack-discuss/2022-March/027614.html>`_,
   and `in policy popup meetings
   <https://etherpad.opendev.org/p/rbac-zed-ptg#L99>`_ but none of those are
   good solutions and end up breaking the existing stack.

   Enabling scope checking also breaks Tacker (NFV Orchestration service) deployment
   as they use heat 'create stack' to build OpenStack infrastructure.

#. `Operator feedback <https://etherpad.opendev.org/p/rbac-operator-feedback>`_ on
   `scope`:

   We collected the operators' feedback on `scope` and how OpenStack APIs will be
   accessed with `scope` enabled.

   First feedback is taken in `ops meetup, Berlin
   <https://etherpad.opendev.org/p/BER-2022-OPS-SRBAC>`_ where it was clear that
   `scope` things are difficult to understand for most of the operators. It will
   break their use case of 'accessing everything with a single token'. 'Admin'
   is already a confusing concept for many of them and `admin` with `scope`
   combination makes it more confusing. The operators agreed with postponing the `scope`
   implementation to be able to land the project persona first.

   `KDDI, japanese telco company <https://etherpad.opendev.org/p/rbac-operator-feedback#L88>`_
   shared the feedback about their use case and how the `scope` will break their use
   case also. An "OpenStack Administrator" who is created by the "keystone-manage
   bootstrap" command, should be able to operate the complete stack even that is
   project-level or system-level resources. Dividing the permissions for project
   and system level resources may have an impact on echosystems or scripts outside
   OpenStack. Another point they raised is that there should be a way that the operator can
   configure the policy permissions in policy.json and with the `scope` that cannot be done
   as the `scope` is not the configurable thing.

Due to the above feedback and use case, we decided to postpone the `scope` implementation.
That is the way forward to at least implement the project personas which is asked by
many operators. Basically, we define the boundaries of this goal:

* Finish delivering project personas
  This is to introduce the `member` and `reader` roles to operate things within their project.
  By default, any other project role like `foo` will not be allowed to do anything in
  the project.

* Change the `scope` implementation to be `project` only

  Services with project resources that have already implemented scope (or have yet to)
  should make all policy rules set scope_types=['project']. This will help ensure
  that any API operations performed with a system-scoped token will fail early, with a
  403, instead of later in the process when a project_id is required. One exception
  here is Ironic, which has implemented scope and has some users adopting it. We must
  not break these users so it is okay to keep the scope implementation as-is.

So, where do we go from here?

We have a set of OpenStack services that have implemented or over-extended the usage of
system-scope and applied it to project-specific resources. Other services have yet to
adopt the system-scope feature.

Currently, none of the policy work we've done since Queens is widely usable by
default since it's not applied consistently across services. The idea of this
community goal is to define the absolute minimum amount of work required to
allow operators to opt into the new authorization behavior and start using the
personas we've been developing since Queens.

We should defer any policy work including `scope` that isn't absolutely necessary to
the criteria of this goal for future improvements. Otherwise we risk delaying the
functionality another release. Instead, we can acknowledge the gaps, order them
on a timeline for future improvements, and at least deliver something useful to
operators sooner rather than later. At least we have a clear understanding on
project persona from developer as well from operator side and if we again delay
implementing it, there is high possibility that developers involved in this work
will loose the motivation and we will never ship the usable project persona in
OpenStack RBAC. Let's accept all the challenges we have with `scope` concept and
be ready to revert the `scope` implemented even that is already implemented in
your project.

Phase 1
=======

Change in `scope` implementation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are some projects like nova, neutron, ironic and octavia that have already
implemented the `scope_type` in their policy. This section will provide a clear
direction for such project as well as if any new projects want to implement the
`scope`.

* As mentioned above, Ironic will keep scope implementation as-is.

* Other projects who have already implemented `scope` for example, Nova, Neutron,
  Octavia etc or any project who has not yet implemented it, should make everything
  scoped to `project` (`scope_type` to `project` only). Keeping everything as
  `project` scoped will make sure to fail the operations performed with a system
  scoped token (which does not have project_id) early with 403 instead of failing
  it with 500 in the lower layer.

* Keystone will continue supporting the `scope` implementation for deployment
  moved/can move to `system scope` enable for example, ironic + keystone. But we need to
  make sure it also works for deployments that do not use `system scope` token means
  continue working with the project scoped token. For that we need to do two changes in
  keystone:

  #. Remove the `scope string (system:all)
     <https://github.com/openstack/keystone/blob/7c2d0f589c8daf5c65a80ed20d1e7fbfcc282312/keystone/common/policies/base.py#L47>`_
     from the policy rule check_str.

  #. Add the `project` in `scope_type` in every policy rule.

Example:

.. code-block:: python

   policy.DocumentedRuleDefault(
       name='os_compute_api:os-hypervisors:list',
       check_str='role:admin',
       scope_types=['project']
   )

Implement support for `project-reader` and `project-member` personas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `project-reader` and `project-member` changes will make sure that by default
any other role for example `foo` in that project will not be able to do anything.

Legacy admin will be unchanged and continue to work same way as it does today._

`project-reader`:
~~~~~~~~~~~~~~~~~

`project-reader` is denoted by someone with the ``reader`` role on a project. It
is intended to be used by end users for read-only access within a project.

`project-reader` persona in the policy check string:

.. code-block:: python

    policy.RuleDefault(
        name="project_reader",
        check_str="role:reader and project_id:%(project_id)s",
        description="Default rule for Project level read only APIs."
    )

Using it in policy rule (with `admin` + `reader` access):
(because we want to keep legacy `admin` behavior the same we need
to give access of reader APIs to `admin` role too.)

.. code-block:: python

    policy.DocumentedRuleDefault(
        name='os_compute_api:servers:show',
        check_str='role:admin or (' + 'role:reader and project_id:%(project_id)s)',
        description="Show a server",
        operations=[
            {
                'method': 'GET',
                'path': '/servers/{server_id}'
            }
        ],
        scope_types=['project'],
    )

OR

.. code-block:: python

    policy.RuleDefault(
        name="admin_api",
        check_str="role:admin",
        description="Default rule for administrative APIs."
    )

    policy.DocumentedRuleDefault(
        name='os_compute_api:servers:show',
        check_str='rule:admin_api or rule:project_reader',
        description='Show a server',
        operations=[
            {
                'method': 'GET',
                'path': '/servers/{server_id}'
            }
        ],
        scope_types=['project'],
    )


`project-member`:
~~~~~~~~~~~~~~~~~

`project-member` is denoted by someone with the ``member`` role on a project. It
is intended to be used by end users who consume resources within a project. It
inherits all the permissions of a `project-reader`.

`project-member` persona in the policy check string:

.. code-block:: python

    policy.RuleDefault(
        name="project_member",
        check_str="role:member and project_id:%(project_id)s",
        description="Default rule for Project level non admin APIs."
    )


Using it in policy rule (with `admin` + `member` access):
(because we want to keep legacy `admin` behavior same we need
to give access of member APIs to `admin` role too.)

.. code-block:: python

    policy.DocumentedRuleDefault(
        name='os_compute_api:servers:create',
        check_str='role:admin or (' + 'role:member and project_id:%(project_id)s)',
        description='Create a server',
        operations=[
            {
                'method': 'POST',
                'path': '/servers'
            }
        ],
        scope_types=['project'],
    )

OR

.. code-block:: python

    policy.RuleDefault(
        name="admin_api",
        check_str="role:admin",
        description="Default rule for administrative APIs."
    )

    policy.DocumentedRuleDefault(
        name='os_compute_api:servers:create',
        check_str='rule:admin_api or rule:project_member',
        description='Create a server',
        operations=[
            {
                'method': 'POST',
                'path': '/servers'
            }
        ],
        scope_types=['project'],
    )


'project_id:%(project_id)s' in the check_str is important to restrict the
access within the requested project.

This would push the functionality even closer to end users, making the API more
self-serviceable.

Legacy admin continues to work as it is
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

During the operator feedback, it is clear that we need to keep the legacy admin
working as it is currently. We will not do any change in legacy admin behavior
and access information. In `Phase 2`_, we will introduce the
`project manager` persona who will be able to do the more privileged operation
within the project than `project member`. More details in `Phase 2`_ section.

.. code-block:: python

   policy.DocumentedRuleDefault(
       name='os_compute_api:os-hypervisors:list',
       check_str='role:admin',
       scope_types=['project']
   )

Managed volumes:

.. code-block:: python

    policy.DocumentedRuleDefault(
        name='volume_extension:volume_manage',
        check_str='role:admin',
        scope_types=['project'],
    )

.. code-block:: python

   policy.DocumentedRuleDefault(
       name='identity:delete_service',
       check_str='role:admin',
        scope_types=['project'],
   )
   policy.DocumentedRuleDefault(
       name='identity:create_endpoint',
       check_str='role:admin',
   )

Listing project resources across the deployment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As we are keeping the legacy `admin` same as it is currently, legacy admin (meaning
anyone with the ``admin`` role on a project) will continue to be able to list all
the resources across the deployment (for applicable APIs only.) The following is an
example of what a policy would look like using this approach:

.. code-block:: python

   policy.DocumentedRuleDefault(
       name='os_compute_api:servers:detail:get_all_tenants',
       check_str='role:admin',
        scope_types=['project']
   ),

This functionality is important for operators finding resources, especially for
support cases, like rebooting or live migrating an instance.

How operators opt into the new functionality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If we can complete each item above in the Zed release, operators will be able
to configure each service to opt into the new defaults across all services,
securely implementing the same personas across the deployment::

  [oslo_policy]
  enforce_new_defaults=True

This configuration enables the following personas:

- Admin
   - Denoted by someone with the ``admin`` role on a project
   - This is existing admin we have in OpenStack policy.
   - Intended for operators who need elevated privilege on complete deployement
   - Not intended for end users
   - *List Hypervisors detail*
   - *Forcibly reset the state of an instance*
   - *Forcibly deleting an application stack*
   - *Making an image public to the entire deployment*
   - *Create physical provider networks*
   - *Add or delete services and endpoints*
   - *Create new volume types*
   - *Move pre-existing volumes in and out of projects*
   - *Create or delete HSM transport keys*

- Project Member
   - Denoted by someone with the ``member`` role on a project
   - Operate within their own project resource
   - Intended to be used by end users who consume resources within a project
   - *Create, delete, or update an instance*
   - *Create, delete, or update a volume*
   - *Create, delete, or update a network*
   - *Can get or list the instances from its own project*
   - *Cannot create, delete, or delete the instance, volume, or network of
     other project*
   - *Cannot get or list instances, volumes, or networks of other project*

- Project Reader
   - Denoted by someone with the ``reader`` role on a project
   - Operate within the own project resource
   - Intended to be used by end users for read-only access within a project
   - Not allowed to make any writable changes to project-owned resources
   - *List and get instances*
   - *List and get volumes*
   - *List and get images, including private images within the project*
   - *List and get networks*
   - *Cannot get or list instances, volumes, or networks of other project*

These new personas fix the existing issue where any user having any role within
project (for example 'foo' role) can create or delete the resources in that project.
It also provides the ability for the operator to assign the read-only role for cloud
auditing the project resources/activities. This does not directly solve the case
of doing global audit with single role.

Phase 2
=======

Isolate service-to-service APIs to the ``service`` role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Any API developed for machines to communicate with each other should use the
``service`` role. This is an important part in reducing authorization for each
service. For example, neutron needs to inform nova about network changes, but
it shouldn't need the ability to create new users and groups in keystone, which
it currently has.

Phase 3
=======

Implement support for `project-manager` personas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`project-manager`:
~~~~~~~~~~~~~~~~~~

A `project-manager` can use project-level management APIs and is denoted by someone
with the ``manager`` role on a project.  It is intended to perform more privileged
operations than `project-member` on its project resources.  A `project-manager` can
also perform any operations allowed to a `project-member` or `project-reader`.

An example of a project-level management API is the Block Storage default-types API,
which allows a default volume type to be set for a particular project. Since the change
affects only that project, it makes sense to allow a responsible person within the
project to set the default type, rather than require them to contact an administrator to
do it.  Implementing the `project-manager` persona will make this possible.

It is up to each service to define which API calls (if any) should be considered as
project-level management APIs.

The `project-manager` needs to be added in the role implication so that the ``admin``
role implies ``manager``, the ``manager`` role implies ``member``, the ``member`` role
implies ``reader``. This needs the modification in the already merged `keystone specification
<https://review.opendev.org/c/openstack/keystone-specs/+/818603>`_.

`project-manager` persona in the policy check string:

.. code-block:: python

    policy.RuleDefault(
        name="project_manager",
        check_str="role:manager and project_id:%(project_id)s",
        description="Default rule for  project-level management APIs."
    )

Using it in policy rule (with `admin` + `manager` access):
(because we want to keep legacy `admin` behavior same we need
to give access of project-level management APIs to `admin` role too.)

.. code-block:: python

    policy.DocumentedRuleDefault(
        name='os_compute_api:os-migrate-server:migrate_live',
        check_str='role:admin or (' + 'role:manager and project_id:%(project_id)s)',
        description="Live migrate a server to a new host without a reboot",
        operations=[
            {
                'method': 'POST',
                'path': '/servers/{server_id}/action (os-migrateLive)'
            }
        ],
    )

OR

.. code-block:: python

    policy.RuleDefault(
        name="admin_api",
        check_str="role:admin",
        description="Default rule for administrative APIs."
    )

    policy.DocumentedRuleDefault(
        name='os_compute_api:os-migrate-server:migrate_live',
        check_str='rule:admin_api or rule:project_manager',
        description="Live migrate a server to a new host without a reboot",
        operations=[
            {
                'method': 'POST',
                'path': '/servers/{server_id}/action (os-migrateLive)'
            }
        ],
    )


'project_id:%(project_id)s' in the check_str is important to restrict the manager
role access within the requested project and 'role:admin or' in check_str will make
sure the legacy admin continues working as it is.

This will provide a way for the operator to configure a user to give the more
privileged access within a project but no access to system-level resources or
cross-project operations.

The `project-manager` persona is described as follows:

- Project Manager (project-level management)
   - Denoted by someone with the ``manager`` role on a project
   - Intended for responsible end-users to give them slightly elevated privileges
     that affect only their own project's resources
   - Can perform more privileged than project-members on a project
   - *Forcibly reset the state of an instance*
   - *Forcibly deleting an application stack*
   - *Locking and unlocking an instance*
   - *Setting the default volume type for a project*
   - *Setting the default secret store for a project*

Tracking
========

Etherpad: https://etherpad.opendev.org/p/rbac-goal-tracking

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

Work completed by Yoga Timeline (7th Mar 2022)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Keystone has the project persona (admin, member, reader) ready to be
   used by the services.

#. Few projects like keystone, nova, neutron, octavia etc adopted the
   project persona but along with `scope type` which needs to be modified
   to drop the `scope type`.

Z-Release Timeline
^^^^^^^^^^^^^^^^^^

#. Convert the `scope_type` of every policy rule to `project`, or specify no
   `scope_type`, as appropriate

   Some standalone services like Ironic can still have their existing  `scope`
   implementation as long as it does not break any cross service communication.
   Nova, Neutron, Keystone and any other projects who have already implemented
   the `scope` as `system`, `domain` and `project` in their policy default need to
   make everything scoped to `project` (`scope_type` to `project` only).

#. Services start implementing `Phase 1`_

   At this point, all services are free to start implementing project-member and
   project-reader personas as described above in `Phase 1`_. By the end of the
   Zed release, at least all the base services must have `Phase 1`_ complete.
   `Phase 1`_ introduces the new personas but allows operators to opt into the
   new behavior for services that complete `Phase 1`_, allowing operators to
   upgrade smoothly to the new permission model on a per-service basis.

   It's important that we have an OpenStack-wide release note or statement that
   explicitly states the status of this work and how permissions behave across
   OpenStack services.

#. Keystone implements a new default role called ``manager``

   The ``manager`` role will be a part of the role hierarchy so that the ``admin``
   role implies ``manager``, the ``manager`` role implies ``member``. This need
   the modification in already merged `keystone specification
   <https://review.opendev.org/c/openstack/keystone-specs/+/818603>`_

#. Keystone implements a new default role called ``service``

   The ``service`` will standardize a role that's already required in some
   default policies across OpenStack. This role must be built outside the
   existing role hierarchy, where ``admin`` implies ``manager`` implies
   ``member`` implies ``reader``. This work requires a keystone specification.

#. OpenStack-wide Personas Documentation

   We need very clear documentation that describes all the potential personas,
   what they mean, who they were designed for, and how to use them. By the end
   of the Zed release, this document should include each persona and what its
   support is across OpenStack services.

   Engineers should use this documentation to determine what the default policy
   should be for APIs they're developing and maintaining. Operators should use
   it to understand what personas are the most appropriate for their users
   based on the permissions they need.

At this point, operators can choose to enable the new defaults for services that
have completed `Phase 1`_. This will require the operator to configure the service
to use ``enforce_new_defaults=True`` if they chose to adopt the new behavior for
services that support it.

2023.1 Release Timeline
^^^^^^^^^^^^^^^^^^^^^^^

#. All services must implement `Phase 1`_

#. Services start implementing `Phase 2`_

#. Services start implementing `Phase 3`_ and updates policies to include the
   ``manager`` role where applicable.

#. Any service that completed `Phase 1`_ in Zed can set ``enforce_new_defaults=True``
   by default. It means new defaults will be enabled by default but operator
   will have way to disable it with ``enforce_new_defaults=False`` for that service.
   Also make ``enforce_scope=True`` to make sure `project` scope is enforced.

At this point, every OpenStack service will have completed `Phase 1`_, which
allows operators to opt into using project-member and project-reader across their
entire deployment.

To summarize, operators will need to update every service configuration file
where they want to use project-member and project-reader. For example:

#. Set ``glance-api.conf [DEFAULT] enforce_secure_defaults=True``
#. Set ``glance-api.conf [oslo_policy] enforce_new_defaults=True``
#. Set ``neutron.conf [oslo_policy] enforce_new_defaults=True``
#. Set ``cinder.conf [oslo_policy] enforce_new_defaults=True``
#. Set ``ironic.conf [oslo_policy] enforce_new_defaults=True``
#. Set ``barbican.conf [oslo_policy] enforce_new_defaults=True``

2023.2 Release Timeline
^^^^^^^^^^^^^^^^^^^^^^^

#. All services must implement `Phase 2`_

#. All services must implement `Phase 3`_

#. Update oslo.policy ``enforce_new_defaults=True``

   Since all services have completed `Phase 1`_, we can update the default in
   oslo.policy so that enforcement checks new default by default. This will allow
   each service to remove code to override the ``enforce_new_defaults=True``
   and use the upstream default from oslo.policy.

#. Update oslo.policy ``enforce_scope=True``

   Since all services have completed `Phase 1`_, we can update the default in
   oslo.policy so that scope enforcement is checked by default. This will allow
   each service to remove code to override the ``enforce_scope=True``
   and use the upstream default from oslo.policy.

#. Any service that implemented `Phase 1`_ in Zed and enabled
   ``enforce_new_defaults`` in 2023.1 release can remove deprecated policies
   used to implement `Phase 1`_.

Operators consuming the 2023.1 release will have the personas delivered in
`Phase 1`_ available and enabled by default. This includes project-member for
common end-user interactions, and project-reader for a read-only variant
of project-member.

2024.1-Release Timeline
^^^^^^^^^^^^^^^^^^^^^^^

#. Any service that implemented `Phase 1`_ in 2023.1 and enabled
   ``enforce_secure_defaults`` in the 2023.2 release (non SLURP) needs to
   keep the old deprecated policies for the 2024.1 release (SLURP) also and
   can remove them after that. The Idea here is to have at least one SLURP
   release between the point when the new defaults are enabled and the
   old policies are removed.

#. Remove the oslo.policy ``enforce_scope`` config flag

   Since all services have completed `Phase 1`_, and have ``enforce_scope=True``
   by default in oslo.policy for every service, we can remove this configuration
   flag itself and have scope checks enable by default.

Operators consuming the 2024.1 release will have full support for project-manager,
project-member, project-reader, and service role dedicated for service-to-service
communication. There will not be support for deprecated policies in this release.

2024.2-Release Timeline
^^^^^^^^^^^^^^^^^^^^^^^

#. Update oslo.policy ``enforce_new_defaults=True``

   At this stage, all services are supposed to complete `Phase 1`_ and
   have the ``enforce_new_defaults`` flag enabled at service level. Now
   we can update the default value of config option ``enforce_new_defaults``
   in oslo.policy to True. This will allow each service to remove code to
   override the ``enforce_new_defaults=True`` and use the upstream default
   from oslo.policy. If any service still needs to keep the default value
   as False then they can do it by overriding the default.

#. Update oslo.policy ``enforce_scope=True``

   At this stage, all services are supposed to complete `Phase 1`_ and
   have the ``enforce_scope`` flag enabled at service level. Now we can
   update the default value of config option ``enforce_scope`` in oslo.policy
   to True. This will allow each service to remove code to override the
   ``enforce_scope=True`` and use the upstream default from oslo.policy. If
   any service still needs to keep the default value as False then they can
   do it by overriding the default.

2025.2-Release Timeline
^^^^^^^^^^^^^^^^^^^^^^^

#. Remove the oslo.policy ``enforce_scope`` config flag

   The config option ``enforce_scope``  was added temporarily to migrate to
   the new RBAC. This is enabled by default in the 2024.2 release (and also in
   2025.2 SLURP release) means all deployments get the scope enabled by
   default. Now we can remove this config flag and have scope checks enabled by
   default.

References
==========

* Policy Pop-Up Team `wiki`_
* https://etherpad.opendev.org/p/policy-popup-yoga-ptg


Current State / Anticipated Impact
==================================

Current progress is maintained on the `tracking etherpad`_ page.

.. _wiki: https://wiki.openstack.org/wiki/Consistent_and_Secure_Default_Policies_Popup_Team
.. _tracking etherpad: https://etherpad.opendev.org/p/rbac-goal-tracking
