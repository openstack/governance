==================================================
 Handling the OpenStack name in external services
==================================================

The OpenStack projects are building and producing artifacts outside its own
infrastructure, like python packaging on PyPI, container images on docker hub,
etc.

When an external service can hold an official "OpenStack" namespace or user,
we should clarify which teams are responsible for it. Please note that
the team can delegate the credentials management to a different team, like
the OpenStack-infra team for example.

.. list-table::
   :header-rows: 1

   * - Service name
     - Team
   * - supermarket.chef.io
     - openstack-chef team
   * - jaas.ai
     - OpenStack Charms team
   * - galaxy.ansible.com
     - Ansible SIG
