Consistent Role Based Access Control (RBAC)
===========================================

Description
-----------

OpenStack is comprised of APIs that allow users to manage physical and virtual
infrastructure. Contributors wrote these APIs for end users and operators
alike. With tenancy being a pillar of OpenStack's technical vision, ensuring
isolation between users and layers of the infrastructure is imperative to
OpenStack's long-term success.

The OpenStack project has grown a tremendous amount of functionality over the
last several years. Unfortunately, evolution in the way services protect their
APIs failed to maintain pace with feature development. As a result, services
today do not protect APIs in ways that expose functionality effectively to
users, support security requirements, reduce operational complexity for
operators, or aid interoperability.

Since the Pike release, there has been renewed efforts to improve tools and
libraries for contributors to use to correct these issues.

Value
-----

Increased Functionality
~~~~~~~~~~~~~~~~~~~~~~~

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

Contact
-------

For more information on how to contribute to this initiative, please read the
`authorization documentation`_ dedicated to describing the problem.
For questions about getting involved with this initiative, reach out to the
OpenStack Discuss mailing `list`_.

.. _authorization documentation: https://docs.openstack.org/keystone/latest/contributor/services.html#why-are-authorization-scopes-important
.. _list: http://lists.openstack.org/cgi-bin/mailman/listinfo/openstack-discuss
