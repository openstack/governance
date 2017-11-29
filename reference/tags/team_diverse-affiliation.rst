::

  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

.. _`tag-team:diverse-affiliation`:

========================
team:diverse-affiliation
========================

A project with this tag has achieved a level of diversity in the affiliation of
contributors that is indicative of a healthy collaborative project.  This tag
exists in the 'team' category, which as the name implies, covers information
about the team itself.  Another example of a tag that could exist in this
category is one that conveys the size of the team that is actively contributing.


Application to current teams
============================

It's worth pointing out that the criteria used for this tag is applied across
all git repositories managed by a team.

.. tagged-projects:: team:diverse-affiliation


Script used to apply this tag:
http://git.openstack.org/cgit/openstack/governance/tree/tools/validate_tags.py


Rationale
=========

We value having a broad base of contributors to a project for several reasons.
One such reason is that it's more risky to rely on a project controlled by a
single organization as the project will immediately come to a halt if that one
organization chooses to stop working on it.  We also value a project where
priorities must be set and agreed upon in a community fashion instead of purely
controlled by a single organization.


Requirements
============

No one organization should represent a majority (>50%) and no two organizations
should represent >80% of any of the following:

* the sum of all commits merged into any of the git repositories managed by the
  team

* the sum of all reviews done against patches submitted to any of the git
  repositories managed by the team

* the sum of all reviews done by active core reviewers against patches submitted
  to any of the git repositories managed by the team

* the union of the active memberships of the core review teams associated with
  the git repositories managed by the team

This tag is applied based on the `tools/teamstats.py` script. The output of this
script is then reviewed by the TC to verify it matches the reality.

The timeline used for evaluation is based on the past 6 months, and should be
updated around the same time as the 6 month release.

Based on how requirements are defined, this tag is only applicable for projects
where their primary deliverables are represented by commits and reviews in git.
An example of where this doesn't make sense is the release management team.


Deprecation
===========

There is no deprecation period required for this tag.  It can be added or
removed at any time.
