==================================
Consistent and Secure Default RBAC
==================================

Existing policy defaults suffer from three major faults:

#. The admin-ness problem: use of policy rules like 'is_admin' or hard-coded
   is-admin checks results in the admin-anywhere-admin-everywhere problem and
   drastically inhibits true multi-tenancy since by default customers cannot
   have admin rights on their own projects or domains.

#. Insecure custom roles: many policy rules simply use "" as the rule, which
   means there is no rule: anyone can perform that action. This means creation
   of a custom role (say, "nova-autoscaler" requires editing every policy file
   across every service to block users with such a rule from performing actions
   unrelated to their role

#. Related to #2, no support for read-only roles: keystone now has a "reader"
   role that comes out of the box when keystone is bootstrapped, but it
   currently has very little value because of the use of empty rules in service
   policies: users with the "reader" role can still perform write actions on
   services if the policy rule for such an action is empty.

To solve the above issues, Keystone comes with member, admin and reader roles.
OpenStack Services should use `these default roles
<https://specs.openstack.org/openstack/keystone-specs/specs/keystone/rocky/define-default-roles.html>`_

Keystone also implemented the new concept `Scope Type
<https://specs.openstack.org/openstack/keystone-specs/specs/keystone/queens/system-scope.html>`_
to define which users are global administrators.

Keystone, Nova and many other projects have migrated their default
policies to:

#. Use oslo.policy's scope_types attribute, which allows the policy engine
   to understand "system scope" and distinguish between an admin role
   assignment on a project versus an admin role assignment on the entire
   system.

#. Ensure all rules use one of the default roles (admin, member, and reader),
   which both ensure support for a read-only role and prevent custom roles
   from accidental over-permissiveness.

Completed pre-work related to this goal:

* From Rocky to Train cycle, Keystone implemented and migrated their policies
  to new `defaults
  <https://review.opendev.org/q/topic:%22implement-default-roles%22+(status:open%20OR%20status:merged)>`_
  and `scope_type <https://review.opendev.org/q/topic:%22add-scope-types%22+(status:open%20OR%20status:merged)>`_

* In the ussuri cycle, Nova migrated their policies to `new RBAC
  <https://review.opendev.org/q/topic:%22bp%252Fpolicy-defaults-refresh-deprecated-apis%22+(status:open%20OR%20status:merged)>`_

* In the ussuri cycle, we created the `policy popup team <https://governance.openstack.org/tc/reference/popup-teams.html#secure-default-policies>`_ to trigger this work for more projects.

* In the victoria cycle, we completed the oslo policy framework to `migrate
  default policy format from JSON to YAML
  <oslo specs <https://specs.openstack.org/openstack/oslo-specs/specs/victoria/policy-json-to-yaml.html>`_

* In the wallaby cycle, we completed the community-wide goal of migrating the
  policy format from JSON to YAML for `all the OpenStack services
  <http://lists.openstack.org/pipermail/openstack-discuss/2021-June/023327.html>`_

* In the wallaby and xena cycle, many projects completed or started the new RBAC
  work.

Refer to the policy pop-up team wiki page for the details:
 https://wiki.openstack.org/wiki/Consistent_and_Secure_Default_Policies_Popup_Team

Champion
========

#. Lance Bragstad <lbragstad@redhat.com> (lbragstad)
#. Ghanshyam Mann <gmann@ghanshyammann.com> (gmann)


Gerrit Topic
============

To facilitate tracking, commits related to this goal should use the
gerrit topic::

  secure-rbac


Completion Criteria
===================

#. Migrate the API policies to new defaults. But keep legacy policies
   rule supported as deprecated rules.

#. Add ``scope_type`` to the policies. By default, scope checks will be
   disabled.

#. Test coverage for the legacy and new RBAC.


References
==========

* policy pop-up team: https://wiki.openstack.org/wiki/Consistent_and_Secure_Default_Policies_Popup_Team


Current State / Anticipated Impact
==================================

Around nine projects have completed the work, and five are in progress.

* Progress is maintained on the below wiki page:
  https://wiki.openstack.org/wiki/Consistent_and_Secure_Default_Policies_Popup_Team#Team_Progress
