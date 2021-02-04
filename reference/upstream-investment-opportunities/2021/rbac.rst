=====================================
Consistent and Secure Policy Defaults
=====================================

Summary
-------

The OpenStack community is seeking contributors to the Secure Policy Defaults
initiative.  This ongoing initiative aims to provide set of common roles that
will enable secure enforcement of authorization policies across OpenStack
projects and deployments.

Business Case
-------------

Supporting consistent and secure default RBAC configuration in OpenStack
provides the best means to secure your organization's OpenStack deployment and
to make security maintenance less error-prone. This is especially incumbent upon
organizations that are subject to security audits and strict regulations for
whom OpenStack's lack of consistent RBAC prohibits production use.

Sponsorship of contributors to this RBAC initiative positions them to
influence direction and drive implementation choices on critical
infrastructure used by every OpenStack project and every OpenStack
deployment -- ensuring that an organization's downstream requirements
are fully understood and taken into account.

Because of its use in every OpenStack project, work on this RBAC
initiative is a good way to build reputation and influence upstream,
and at the same time gain vital in-house expertise for an
organization's downstream deployments or software distributions.

Technical Details
-----------------

Currently, most OpenStack services have a very binary approach to Role Based
Access Control (RBAC) enforcement. This approach usually handicaps new
functionality from being exposed to users because users typically do not fall
in one of two camps.  Contributors either need to lock down the feature to only
system administrators, or open it up to nearly every user in the deployment.
This is especially true for APIs that expose details about multiple tenants.

Implementing better API protection allows contributors to expose more
functionality to end users and operators by default. Lowering the bar for users
to access a feature means more opportunities for feedback loops, more end users
getting access to the functionality they need, and makes OpenStack more usable
overall.

Enhanced Security
~~~~~~~~~~~~~~~~~

OpenStack has a wide variety of users. Auditing APIs and adjusting default
access control increases security across the entire OpenStack platform. This
exercise gives contributors the ability to provide secure defaults for new
deployments. Reasonable default values that are inherently secure makes it
easier for organizations with strict security requirement to deploy OpenStack.

Reduced Operational Complexity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Today's RBAC enforcement implementation lacks secure defaults, but it is
somewhat configurable. Deployments that must have a more secure enforcement
implementation are forced to maintain arduously complex configuration files.
Furthermore, many organizations re-implement similar use cases.

Interoperability
~~~~~~~~~~~~~~~~

Because policy configuration gives deployments the flexibility to maintain
complicated policies at their own expense, it is common to see many
organizations solve the same problem. Unfortunately, it's unlikely
organizations are sharing the same solution. This pattern impedes
interoperability between deployments, making it frustrating for users
interacting with different OpenStack clouds.

Offering a reasonable set of roles and implementing basic RBAC improves
interoperability by not requiring each organization to solve the same problem
individually.

-----------------

Contact
-------

To contribute to this initiative, join the `Secure Default Policies Popup
Team`_. Read the `popup team wiki page`_ for references on how to contribute and
how to communicate with the team.

.. _Secure Default Policies Popup Team: https://governance.openstack.org/tc/reference/popup-teams.html#secure-default-policies
.. _popup team wiki page: https://wiki.openstack.org/wiki/Consistent_and_Secure_Default_Policies_Popup_Team
