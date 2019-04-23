=============================================================
 2014-12-02 OpenStack project structure reform specification
=============================================================

Problem description
===================

Our project structure is currently organized as a ladder. Developers form
teams, work on a project, then apply for incubation and ultimately graduate
to be part of the OpenStack integrated release. Only integrated projects
(and the few horizontal efforts necessary to build them) are recognized
officially as "OpenStack" efforts. This creates a number of issues, which
were particularly visible at the Technical Committee level over the Juno
development cycle.

First, the integrated release as it stands today is not a useful product for
our users. The current collection of services in the integrated release spans
from cloud native APIs (swift, zaqar in incubation), base-level IaaS blocks
(nova, glance, cinder), high-level aaS (savana, trove), and lots of things
that span domains. Some projects (swift, ironic...) can be used quite well
outside of the rest of the OpenStack stack, while others (glance, nova)
really don't function in a different context. Skilled operators aren't
deploying "the integrated release": they are picking and choosing between
components they feel are useful. New users, however, are presented with a
complex and scary "integrated release" as the thing they have to deploy and
manage: this inhibits adoption, and this inhibits the adoption of a slice of
OpenStack that could serve their need.

Second, the integrated release being the only and ultimate goal for projects,
there is no lack of candidates, and the list is always-growing. Why reject
Sahara if you accepted Trove? However, processes and services are applied
equally to all members of the integrated release: we gate everything in the
integrated release against everything else, we do a common, time-based
release every 6 months, we produce documentation for all the integrated
release components, etc. The resources working on those integrated horizontal
tasks are very finite, and complexity grows non-linearly as we add more
projects. So there is outside pressure to add more projects, and internal
pressure to resist further additions.

Third, the binary nature of the integrated release results in projects
outside the integrated release failing to get the recognition they deserve.
"Non-official" projects are second- or third-class citizens which can't get
development resources. Alternative solutions can't emerge in the shadow of
the blessed approach. Becoming part of the integrated release, which was
originally designed to be a technical decision, quickly became a
life-or-death question for new projects, and a political/community minefield.

In summary, the "integrated release" is paradoxically too large to be
effectively integrated, installed or upgraded in one piece, and too small to
express the diversity of our rich ecosystem. Its slow-moving, binary nature
is too granular to represent the complexity of what our community produces,
and therefore we need to reform it.

The challenge is to find a solution which allows to address all those three
issues. Embrace the diversity of our ecosystem while making sure that what
we produce is easily understandable and consumable by our downstream users
(distributions, deployers, end users), all that without putting more stress
on the already overworked horizontal teams providing services to all
OpenStack projects, and without limiting the current teams access to common
finite resources.


Proposed change
===============

Provide a precise taxonomy to help navigating the ecosystem
-----------------------------------------------------------

We can't add any more "OpenStack" projects without dramatically revisiting
the information we provide. It is the duty of the Technical Committee to
help downstream consumers of OpenStack understand what each project means
to them, and provide them with accurate statuses for those projects.

Currently the landscape is very simple: you're in the integrated release, or
you're not. But since there was only one category (or badge of honor), it
ended up meaning different things to different people. From a release
management perspective, it meant what we released on the same day. From a
CI perspective, it meant what was co-gated. From an OpenStack distribution
perspective, it meant what you should be packaging. From some operator
perspective, it meant the base set of projects you should be deploying. From
some other operator perspective, it meant the set of mature, stable projects.
Those are all different things, and yet we used a single category to describe
it.

The first part of the change is to create a framework of tags to describe
more accurately and more objectively what each project produced in the
OpenStack community means. The Technical Committee will define tags and the
objective rules to apply them. This framework will allow us to progressively
replace the "integrated release" single badge with a richer and more nuanced
description of all "OpenStack" projects. It will allow the Technical
Committee to provide more precise answers to the Foundation Board of
Directors questions about which set of projects may make sense for a given
trademark license program. It will allow our downstream users to know which
projects are mature, which are security-supported, which are used in more
than one public cloud, or which are really massively scalable.

Recognize all our community is a part of OpenStack
--------------------------------------------------

The second part of the change is recognizing that there is more to
"OpenStack" than a finite set of projects blessed by the Technical
Committee. We already have plenty of projects that are developed on
OpenStack infrastructure, follow the OpenStack way of doing things, have
development discussions on the openstack-dev mailing-list and use
#openstack-meeting channels for their team meetings. Those are part of
the OpenStack community as well, and we propose that those should considered
"OpenStack projects" (and be hosted under openstack git namespaces), as
long as they meet an objective criteria for inclusion (to be developed as one
of the work items below). This might include items such as:

* They align with the OpenStack Mission: the project should help further the
  OpenStack mission, by providing a cloud infrastructure service, or
  directly building on an existing OpenStack infrastructure service

* They follow the OpenStack way: open source (licensing), open community
  (leadership chosen by the contributors to the project), open development
  (public reviews on Gerrit, core reviewers, gate, assigned liaisons), and
  open design (direction discussed at Design Summit and/or on public forums)

* They ensure basic interoperability (API services should support at least
  Keystone)

* They submit to the OpenStack Technical Committee oversight

These criteria are objective, and therefore the Technical Committee may
delegate processing applications to another team. However, the TC would
still vote to approve or reject applications itself, based on the
recommendations and input of any delegates, but without being bound to
that advice. The TC may also decide to encourage collaboration between
similar projects (to reduce unnecessary duplication of effort), or to
remove dead projects.

This proposed structure will replace the current program-driven structure.
We'll still track which team owns which git repository, but this will let
multiple different "OpenStack" teams potentially address the same problem
space. Contributors to projects in the OpenStack git namespace will all be
considered ATCs and participate in electing the Technical Committee.

Transition
----------

As for all significant governance changes, we need to ensure a seamless
transition and reduce the effect of the reform on the current development
cycle. To ensure this seamless transition, the OpenStack taxonomy will
initially define one tag, "integrated-release", which will contain the
integrated projects for the Kilo cycle. To minimize disruption, this tag
will be used throughout the Kilo development cycle and for the Kilo end
release. This tag may be split, replaced or redefined in the future, but
that will be discussed as separate changes.

Future evolution
----------------

These proposed changes are just the base foundational step, enabling the
future evolution of our project structure and governance. It puts in place
the framework that will be used to discuss future changes (new tags and the
rules to apply them).


Implementation
==============

Assignee(s)
-----------

The work on this transition is assigned to the Technical Committee members,
under the coordination of the Chair of the Technical Committee.

Work Items
----------

* Communication about the changes and their impact to the wider OpenStack
  community (end of December, start of January, ttx)

* Create project taxonomy base structure and templates in governance
  repository (mid-January, ttx)

* Replace incubation-integration-requirements.rst by rules definition for
  the "integrated-release" transitional tag (end of January, assignee tbd)

* Create base taxonomy navigation website, to make the taxonomy easily
  discoverable, searchable and browseable (kilo-2 milestone, jaypipes)

* Define new objective OpenStack project requirements (to replace old
  new-programs-requirements.rst) (kilo-2 milestone, assignee tbd)

* Update Technical Committee charter to get rid of the "Programs" concept
  (and redefine ATC as contributors to any OpenStack project) (kilo-2
  milestone, ttx)

Most of those work items will result in governance changes that will be
discussed, reviewed and approved by the Technical Committee separately.


Impact
======

Impact for horizontal teams
---------------------------

Horizontal teams (documentation, infrastructure, QA, release management,
stable maintenance, vulnerability management, translators...) have set a
number of expectations toward the projects in the "integrated release".
This is what created tension as the Technical Committee added more projects
which those horizontal teams had to support. Those expectations have to be
revisited as we replace the "integrated release" with a richer landscape.

With this proposed change, the work of horizontal teams shall gradually move
away from centrally handling work for all projects, to a more decentralized
model where they provide processes and tools to empower projects to do the
work themselves. The horizontal teams become responsible for passing along
the knowledge, tools and processes to the projects in order to produce
quality artifacts, rather than being the direct producers of those artifacts.

Each horizontal team will have to redefine how they organize their work
under the new project structure, and which (if any) projects they still
directly handle. They will be able to define tags to communicate that new
organization. Note that most teams already started that transition as more
projects were being added to the integrated release, so this will help them
to more explicitly describe the service they provide.

Impact for existing integrated projects and the Kilo cycle
----------------------------------------------------------

This change in itself doesn't adversely impact existing integrated projects:
they will continue to exist and be defined under the transitional
"integrated-release" tag. However, one end goal of the reform is to
deconstruct the "integrated release" binary concept and replace it with
more precise and objective groupings, so there should come a time in the
future where the "integrated-release" concept won't mean anything anymore,
and the transitional tag will be discontinued. This change puts in place the
framework that will allow us to do that, but doesn't actually do anything
yet. In particular, the "integrated release" as a concept will still very
much exist at least until the end of the Kilo development cycle.

Impact for currently-incubated projects
---------------------------------------

Currently-incubated projects would directly become "OpenStack projects"
under the new structure, without needing another formal application. Future
tags will be defined and applied to them to further describe their nature
and maturity status.

Trademark checks
----------------

The OpenStack Foundation legal staff currently performs trademark checks as
a project is incubated, before its inclusion in the integrated release. It
will continue to apply the same preventive analysis to any project that will
be used as part of OpenStack Foundation trademark license programs. However
projects under the openstack git namespaces are considered projects from the
OpenStack Community, and won't all be preventively checked for potential
trademark conflicts. To communicate that, a note will be posted on the
relevant git organization pages stating that the OpenStack Foundation is not
responsible for the project names or content below, which are posted by
independent developers.

The Technical Committee however expects that if a reasonable challenge is
presented to a given project under an openstack git namespace, a rename of
the project has to be considered.


References
==========

* Original mailing-list discussion:
  http://lists.openstack.org/pipermail/openstack-dev/2014-August/041929.html

* Blogposts:

  * "OpenStack as Layers"
    https://dague.net/2014/08/26/openstack-as-layers/ (Sean Dague)

  * "OpenStack as Layers but also a Big Tents but also a bunch of Cats"
    http://inaugust.com/post/108 (Monty Taylor)

  * "The problem space in the big tent"
    http://ttx.re/problem-space-in-the-big-tent.html (Thierry Carrez)

  * "So, What is the Core of OpenStack?"
    http://www.joinfu.com/2014/09/so-what-is-the-core-of-openstack/ (Jay Pipes)

  * "On Layers"
    http://www.stillhq.com/openstack/kilo/000002.html (Mikal Still)

* Strawman governance change proposals:

  * Doug's strawman v1:
    https://review.opendev.org/#/q/status:open+topic:big-tent,n,z

  * Doug's strawman v2:
    https://review.opendev.org/#/c/131422/

  * Jay's strawman:
    https://review.opendev.org/#/c/126582/

* Public notes from discussions between TC members:
  https://etherpad.openstack.org/p/project-restructure-hangouts
