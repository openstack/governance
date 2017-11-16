=========================
 'Help most needed' list
=========================

This document lists at most 5 areas where the OpenStack Technical Committee
seeks contributions to significantly help OpenStack as a whole. While in most
cases things happen naturally through the normal contribution dynamics
in the community, in some cases a `tragedy of the commons`_ is at play.
Guidance, leadership and proper recognition of efforts is therefore needed
to encourage individuals or organizations to contribute in areas where they
could make a big impact.

Each item should clearly explain why the item matters (value of the effort
to the community, operators and users), why we need help there (description
of the current situation) and what experience or benefit the volunteer can
expect to gain from tackling it. It should also include the name of a TC
sponsor (responsible for evangelizing, articulating and channelling the work,
but also facilitating connections between candidates and target teams). For
an estimate of the commitment required, interested candidates should reach
out to the TC sponsor, or the PTL of the affected project.

.. _`tragedy of the commons`: https://en.wikipedia.org/wiki/Tragedy_of_the_commons


1. Documentation owners
=======================

The #1 pain point in OpenStack, especially for new potential adopters, is
complexity. While cutting down complexity everwhere we can is critical,
proper documentation is essential in addressing that complexity. It directly
benefits operators and users of OpenStack, but also facilitates ramping up
new direct contributors to the project itself.

The documentation team has been struggling with limited resources since the
dawn of OpenStack, despite the heroic efforts of previous team members. An
ambitious `plan`_ to further decentralize the Documentation team (and turn it
into a guidance and mentoring support team) has been outlined. To be
successful, this plan requires project teams to own their own documentation,
which means that the role of documentation owners will be critical.

Volunteers for this role will in the short term drive this ambitious
transition, by being members of their project team and members of the new
decentralized documentation team. On the long-term they will become a
reference go-to person in their project, and respected mentors in the
OpenStack community.

Interested? Contact the Documentation PTL (pkovar) or the TC sponsor for
this item (dhellmann).

.. _`plan`: https://review.openstack.org/#/c/472275/

2. Community Infrastructure Sysadmins
=====================================

*TC Sponsor: Jeremy Stanley (fungi)*

The Infrastructure_ team is responsible for designing, building and
maintaining the systems that are used in the day to day operation of
the OpenStack project as a whole; this includes development,
testing, and collaboration tools. All of the software it runs is
open source, and under public configuration management so that
everyone in the community has the opportunity to participate. One
very effective way to get involved in OpenStack, gaining a deep
understanding of and visibility within the community, is by helping
operate this infrastructure. Attrition due to shifts in employment
or availability of personal time impacts the team's ability to
support the community effectively, and so there is a constant need
for new contributors who can commit to investing sufficient effort
to overcome the steep learning curve associated with these varied
technologies.

Because our community is global, its support needs span most
timezones. Unfortunately, the bulk of long-term contributors to
Infrastructure are concentrated in the Americas and so this leaves
APAC and EMEA community members with far fewer options for immediate
assistance with urgent issues. Gaining more contributors who are
active during those times (whether they live in those parts of the
World or not) would provide a substantial benefit to the community.
This is not necessarily as easy as it sounds because it's harder to
get as much overlap with the current bulk of the team for shadowing
and knowledge transfer, but there are still some existing team
members in those timezones who can help mitigate that somewhat.

In particular, the team seeks developers and systems administrators
with a background both in maintaining Unix/Linux servers and free
software, and places heavy emphasis on systems automation and
configuration management (primarily Ansible and Puppet at the
moment). Everything possible goes through code review, and gets
extensively documented and communicated with the rest of the
community over IRC and mailing lists. Server resources are donated
by companies operating OpenStack services, and the team also
operates a persistent deployment of OpenStack too, so there is
substantial opportunity both for people who have experience in those
technologies as well as anyone wishing to gain more familiarity with
them.

Join the #openstack-infra channel on the Freenode IRC network or
reach out through the openstack-infra mailing lists on
lists.openstack.org if you would like to get involved. It's a
rewarding chance to learn and help others, but most of all it's fun!

.. _Infrastructure: :ref:project-infrastructure

3. Designate Contributors
=========================

`Designate`_ is a service that manages DNS Zones and Recordsets in an OpenStack
way. We support multiple DNS Servers, and DNS Service Providers. DNS is a vital
service for any network or web based application. DNS is a core part of
directing users and applications to a service - it allows the entire underlying
infrastructure to be replaced, even moved across regions or clouds, while
presenting a consistent endpoint. DNS should be managed along side the servers,
load balancers and other equipment in an OpenStack cloud and the integration
with Neutron allows for DNS entries to be created when something is connected
to a network. For more complicated examples, Heat can be used to manage the DNS
zones and records, allowing for entire zones to be created, updated and deleted
along side the resources that they point at. Once Designate is in every cloud,
you can bring a heat template from cloud to cloud, and have a user ready
deployment with a simple ``openstack stack create`` command.

Designate has had issues finding contributors to replace previous contributors
who have moved on from the project mainly due to major restructuring in the
organisations that sponsored development.

They need contributors to help find and fix bugs, develop new features, and
help maintain the quality of the project. Designate is quite stable, with any
new features requiring long term planning, design and phased implementation.

This makes Designate a good project for everyone, from  a person starting out
in the community, who wants to work on an interesting and important section of
infrastructure, to very senior developers who want new, interesting problems
to tackle. Contributors will get to work on a project that will be a central
part of any OpenStack deployment, and work on a project that needs to scale
from a small single node install to a system controlling DNS servers worldwide.

If you are interested, please join the IRC channel (#openstack-dns) or contact
the Designate PTL (Graham Hayes - mugsie on IRC), the TC sponsor
(Sean McGinnis - smcginnis), or email the `openstack dev`_ mailing list with
the tag `[designate]`.

.. _`Designate`: https://governance.openstack.org/tc/reference/projects/designate.html
.. _`openstack dev`: http://lists.openstack.org/cgi-bin/mailman/listinfo/openstack-dev

4. Glance Contributors
======================

`Glance`_ is a service to manage images for OpenStack clouds. It's one of the
early projects in OpenStack and it's deployed in almost every OpenStack cloud.
Without Glance, Nova can't boot instances.

Glance is looking for new contributors who would be willing to provide reviews,
to work on bugs, or to work on new features.

Glance is a great project to ramp up on OpenStack and it's a great project for
developers regardless of their experience. Glance has welcomed interns, junior
developers, and more senior developers. In every case, it's a great way to grow
and contribute to OpenStack.

Glance is a critical project in OpenStack. Contributions to the future of the
image registry are essential to the stability of OpenStack. More importantly,
Glance is not "done". There's significant technical debt that needs to be taken
care of and several features that can be implemented.

Interested? Join the Glance IRC channel (#openstack-glance) or reach out to the
Glance PTL (rosmaita), the TC sponsor for this item (flaper87) or starting a new
email thread on the ML using the tag `[glance]`.

.. _`Glance`: https://governance.openstack.org/tc/reference/projects/glance.html

5. Goal Champions
=================

Things get done in OpenStack when a group of people work together
toward a shared goal. In order to do that, one or more people in the
group need to step up and coordinate the group, keep track of
progress, call for and chair regular meetings, and publish status
updates.  PTLs do this work for project teams, leaders do it for
various cross-project working groups and SIGs, and champions do it to
help us complete :ref:`release-cycle-goals` over a cycle.

The work of those champions is essential to the success of OpenStack,
and yet it is often challenging to find volunteers for those
positions. Contributing as a goal champion takes time (several hours
per week), and that commitment needs to be properly recognized and
celebrated.

Volunteers for this role will make a direct impact on the productivity
of others, become respected leaders in OpenStack community, build
influence among their peers, and make great candidates for future
elected leadership positions in OpenStack.

If you are interested in helping with community goals, contact the TC
sponsor for this item (dhellmann).
