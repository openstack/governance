::

  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

========================================================================
team:diverse-affiliation
========================================================================

A project with this tag has achieved a level of diversity in the affiliation of
contributors that is indicative of a healthy collaborative project.  This tag
exists in the 'team' category, which as the name implies, covers information
about the team itself.  Another example of a tag that could exist in this
category is one that conveys the size of the team that is actively contributing.

Rationale
=========

We value having a broad base of contributors to a project for several reasons.
One such reason is that it's more risky to rely on a project controlled by a
single company as the project will immediately come to a halt if that one
company chooses to stop working on it.  We also value a project where priorities
must be set and agreed upon in a community fashion instead of purely controlled
by a single company.


Requirements
============

No one company should represent a majority (>50%) of any of the following:

* the sum of all commits merged into any of the git repositories managed by the
  team

* the sum of all reviews done against patches submitted to any of the git
  repositories managed by the team

* the sum of all reviews done by core reviewers against patches submitted to any
  of the git repositories managed by the team

* the union of the memberships of the core review teams associated with the git
  repositories managed by the team

The timeline used for evaluation is aligned with the 6-month release cycle.  The
current cycle's timeline should be used unless the cycle has not yet been longer
than 2 months, in which case the previous cycle should be used.  This definition
is purely for convenience, as it makes it easy to check using existing tools
(stackalytics, in particular).

Based on how requirements are defined, this tag is only applicable for projects
where their primary deliverables are represented by commits and reviews in git.
An example of where this doesn't make sense is the release management team.

It would be better to use a fixed 6-month window for this.  Once we come up with
a convenient way to evaluate this criteria against a fixed 6-month window, the
requirements can be changed.


Tag application process
=======================

The criteria for this tag is very objective.  The TC could approve any future
updates to the tag definition and otherwise defer application of the tag.  A
method for delegating this is TBD, so in the meantime, we default back to the
following process:

Anyone may propose adding or removing this tag to a set of projects by
proposing a change to the openstack/governance repository. The change is
reviewed by the Technical Committee and approved using standard resolution
approval rules, including discussion at at least one Technical Committee
public IRC meeting.


Deprecation
===========

There is no deprecation period required for this tag.  It can be added or
removed at any time.


Attributes
==========

This tag has no attributes.


Application to current projects
===============================

It's worth pointing out that the criteria used for this tag is applied across
all git repositories managed by a team.  However, tags are applied to repos.
So, the result is that an evaluation is done for the whole team and either all
repos or none get the tag.

Using the current criteria, the following teams would have the tag applied to
their repositories::

  <Team> (top commit % | top review % | top core review % | (top core reviewer %)
  Nova               (20.03% | 20.03% | 26.07% | 31.25%)
  Swift              (27.78% | 27.61% | 38.08% | 36.36%)
  Glance             (24.05% | 29.76% | 40.07% | 33.33%)
  Keystone           (43.08% | 29.40% | 45.95% | 37.50%)
  Horizon            (28.41% | 15.90% | 21.84% | 30.77%)
  Neutron            (26.74% | 19.60% | 24.33% | 16.67%)
  Cinder             (12.59% | 11.36% | 16.49% | 20.00%)
  Heat               (33.15% | 34.04% | 37.94% | 27.78%)
  Trove              (34.02% | 36.00% | 46.20% | 42.86%)
  Ironic             (25.13% | 28.41% | 31.16% | 33.33%)
  Oslo               (30.90% | 28.30% | 34.65% | 23.68%)
  Infrastructure     (38.69% | 49.80% | 48.23% | 42.22%)
  Documentation      (19.72% | 26.67% | 34.89% | 19.05%)
  Quality Assurance  (27.22% | 26.81% | 33.65% | 33.33%)

The following official projects would not get the tag::

  Ceilometer         (52.02% | 32.20% | 61.99% | 50.00%)
  TripleO            (54.59% | 56.19% | 62.69% | 60.87%)
  Sahara             (53.08% | 59.00% | 60.75% | 57.14%)
  Barbican           (50.35% | 48.97% | 52.81% | 50.00%)
  Manila             (47.27% | 31.72% | 45.84% | 50.00%)
  Zaqar              (48.24% | 66.90% | 78.51% | 66.67%)
  Designate          (55.80% | 63.66% | 64.11% | 60.00%)
  OpenStackClient    (34.52% | 36.89% | 56.60% | 33.33%)

We can also look at whether currently proposed projects would receive the tag.
Magnum would, while Murano and Group Based Policy would not::

  Murano             (84.91% | 93.20% | 99.26% | 87.50%)
  Group Based Policy (47.96% | 57.31% | 58.20% | 33.33%)
  Magnum             (33.78% | 37.08% | 37.22% | 28.57%)

A script used when checking the projects:
https://gist.github.com/russellb/cc89a390eefbb33e252b
