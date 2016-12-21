::

  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-team:single-vendor`:

==================
team:single-vendor
==================

This tag communicates that a given project team is currently driven by a
single organization.

This tag exists in the 'team' category, which as the name implies,
covers information about the team itself.


Application to current projects
===============================

It's worth pointing out that the criteria used for this tag is applied across
all git repositories managed by a team.

.. tagged-projects:: team:single-vendor

Script used to apply this tag:
http://git.openstack.org/cgit/openstack/governance/tree/tools/validate_tags.py


Rationale
=========

Knowing that a given project is produced by a team essentially from a single
organization is a critical factor in the decision to deploy a project, as it
changes the dynamics of who you trust to continue to deliver this project.

In particular, such a project could be abandoned due to the budgeting
decisions of a single party. Additional steps (like engaging early on with
that single party) could be taken before investing significantly on such a
project.


Requirements
============

The tag applies to any project team where one organization represents >=90% of
any of the following over the prior six months:

* the sum of all commits merged into any of the git repositories managed by the
  team

* the sum of all reviews done against patches submitted to any of the git
  repositories managed by the team

* the sum of all reviews done by active core reviewers against patches submitted
  to any of the git repositories managed by the team

* the union of the active members of the core review teams associated with the
  git repositories managed by the team

This tag is applied based on the `tools/teamstats.py` script. The output of this
script is then reviewed by the TC to verify it matches the reality.

The application of this tag to new projects should be updated around the same
time as the 6 month release. But the removal of this tag should happen shortly
after it does not apply to a given project.

Based on how requirements are defined, this tag is only applicable for projects
where their primary deliverables are represented by commits and reviews in git.


Deprecation
===========

There is no deprecation period required for this tag.  It can be added or
removed at any time.
