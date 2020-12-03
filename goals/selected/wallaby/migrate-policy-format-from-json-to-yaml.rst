============================================
Migrate RBAC Policy Format from JSON to YAML
============================================

Oslo policy supports both JSON as well as YAML formatted
policy file and config option for passing the ``policy_file``
defaults to ``policy.json``.

JSON formatted file caused issues while deprecating policies
with the combination of below things:

* Packagers like to generate a sample policy for users to
  reference as they configure a service.

* oslo.policy still defaults the filename of the policy file
  to policy.json for backward compatibility reasons. This
  encourages packages to generate a JSON sample policy file,
  which is not what we want.

* Generating a sample policy file in JSON results in all the
  policy-in-code rules being overridden because it is not
  possible to comment out the default rules in JSON.

Because of the above, when a policy rule is deprecated in a
service, users who have a JSON sample policy file will have
the new rule applied immediately on upgrade. This does not
give them a chance to deal with the change, as intended by
the deprecation mechanism in oslo.policy (which would ordinarily
apply an OR operation on the old rule and the new rule to ensure
environments relying on the old rule will continue to work). This
causes a lot of issues while doing the new policy changes of
consistent and secure policy because we need to deprecate every
policy rules.

After policy-in-code, the expectation was everyone will be relying
on policy-in-code default unless they want to override any rule and
if so then use YAML formatted file but that did not happen and from
OpenStack side also we did not communicate it well to operators.

In Victoria cycle, we completed the below common part in oslo
policy (`oslo specs <https://specs.openstack.org/openstack/oslo-specs/specs/victoria/policy-json-to-yaml.html>`_):

#. Adding the warnings for JSON format file Oslo policy

#. Providing the tool to convert the existing JSON

#. Deprecate JSON output in policy CLI tools.

The operator can migrate their existing JSON file via
`oslo policy tool <https://docs.openstack.org/oslo.policy/latest/cli/oslopolicy-convert-json-to-yaml.html>`_

As we are planning to make RBAC more secure and consistent, doing
this in advance will help operators to move to YAML format and avoid
any break when the operator re-generated the policy file in JSON format.

What projects need to do:

#.  Enable upgrade checks to detect the JSON format file which is defined
    in oslo.upgradecheck 1.2.0 and warn about it.
    `Example <https://review.opendev.org/c/openstack/keystone/+/764240/2/keystone/cmd/status.py>`_

#. Change the default for config ``policy_file`` via ``set_defaults``. To avoid
   breaking the deployment, a fallback logic to use the existing
   ``policy.json`` is added in oslo.policy 3.6.0.

#. Deprecate the JSON format support via warnings in doc and release notes.

Once all project finish this, we will be able to deprecate it in Oslo policy
also which allow policy deprecation without causing pain to OpenStack deployers.

Release notes sample::

  ---
  upgrade:
    - |
      The default value of ``[oslo_policy] policy_file`` config option has
      been changed from ``policy.json`` to ``policy.yaml``.
      Operators who are utilizing customized or previously generated
      static policy JSON files (which are not needed by default), should
      generate new policy files or convert them in YAML format. Use the
      `oslopolicy-convert-json-to-yaml
      <https://docs.openstack.org/oslo.policy/latest/cli/oslopolicy-convert-json-to-yaml.html>`_
      tool to convert a JSON to YAML formatted policy file in
      backward compatible way.
  deprecations:
    - |
      Use of JSON policy files was deprecated by the ``oslo.policy`` library
      during the Victoria development cycle. As a result, this deprecation is
      being noted in the Wallaby cycle with an anticipated future removal of support
      by ``oslo.policy``. As such operators will need to convert to YAML policy
      files. Please see the upgrade notes for details on migration of any
      custom policy files.

Doc warning sample::

  .. warning::

     JSON formatted policy file is deprecated since <project version>(Wallaby).
     This `oslopolicy-convert-json-to-yaml`__ tool will migrate your existing
     JSON-formatted policy file to YAML in a backward-compatible way.

  .. __: https://docs.openstack.org/oslo.policy/latest/cli/oslopolicy-convert-json-to-yaml.html

Example:

* Keystone: https://review.opendev.org/c/openstack/keystone/+/764240
* Nova (common code is moved from nova to oslo side): https://review.opendev.org/#/c/748059/

* Work done till now: https://review.opendev.org/#/q/topic:bp/policy-json-to-yaml+(status:open+OR+status:merged)


Tracking for this work will be done in `this etherpad <https://etherpad.opendev.org/p/migrate-policy-format-from-json-to-yaml>`_

Champion
========

Ghanshyam Mann <gmann@ghanshyammann.com> (gmann)


Gerrit Topic
============

To facilitate tracking, commits related to this goal should use the
gerrit topic::

  policy-json-to-yaml


Completion Criteria
===================

#. Add upgrade checks to detect the JSON format file and warn about it.

#. Change the default for config ``policy_file`` via ``set_defaults``.

#. Deprecate the JSON format support via warnings in doc and release notes.


References
==========

* https://specs.openstack.org/openstack/oslo-specs/specs/victoria/policy-json-to-yaml.html
* https://review.opendev.org/#/q/topic:bp/policy-json-to-yaml+(status:open+OR+status:merged)
* https://etherpad.opendev.org/p/policy-popup-wallaby-ptg


Current State / Anticipated Impact
==================================

Olso side works to provide migration tool and two projects Nova and Cyborg completed it.
Also, Cinder did one part of changing the default value.

* Nova: https://review.opendev.org/#/c/748059/
* Cyborg: https://review.opendev.org/#/c/752576/
