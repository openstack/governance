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

******************
Intended Audiences
******************

This document was written with at least two audiences in mind.

The first audience consists of contributors who would be working on the items
listed here. Each item should provide a descriptive summary that helps
developers grasp the overall problem and possibly how to solve it or
contribute.

The second audience is corporate or business sponsors. Ultimately, this
audience consists of people who have the ability to delegate resources to work
on various initiatives. The description of each item should justify why the
item is on the list. Descriptions should refrain from being overly technical.
Additionally, business sponsors will find the "Value" section beneficial
because it describes how investing resources helps reduce maintenance cost,
increase interoperability, provide stability, or deliver value to your
customers. Essentially, this section should help businesses understand what
they are getting out of the investment.

Both audiences will find the contact information supplied with each item useful
for connecting with the right group of people to get resources up-to-speed.

.. _`tragedy of the commons`: https://en.wikipedia.org/wiki/Tragedy_of_the_commons


1. Documentation owners
=======================

Description
-----------

The #1 pain point in OpenStack, for contributors and users alike, is
complexity.  While cutting down complexity everywhere we can is critical;
proper documentation is essential in addressing that complexity. It directly
benefits operators and users of OpenStack, but also facilitates ramping up new
direct contributors to the project itself.

The documentation team has been struggling with limited resources since the
dawn of OpenStack, despite the heroic efforts of previous team members. The
community outlined an ambitious `plan`_ to decentralize the Documentation team,
turning it into a guidance and mentoring support team. To be successful,
project teams need to own their documentation, which means that the role of
documentation owners will be critical.

Volunteers for this role will drive this ambitious transition, by being members
of their project team and members of the new decentralized documentation team.
On the long-term, they will become a reference go-to person in their project,
and respected mentors in the OpenStack community.

Value
-----

Increased Operational Efficiency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Documentation naturally disseminates knowledge, but it should also be easy for
readers to find what they are looking for. This process reduces bottlenecks on
human resources and support by allowing users, operators, and contributors to
find answers to questions themselves. Less time spent answering common
questions means more time focusing on more complicated requests, maintenance,
and code.

Faster Onboarding
~~~~~~~~~~~~~~~~~

Contributors come from all different backgrounds and experiences. As a result,
they often share similar questions about high-level concepts or processes used
within the OpenStack community or components. Consistently documenting
processes enables contributors without requiring them to pull tribal knowledge
from an existing developer. This documentation fast-tracks contributors to
making productive contributions.

Consistency
~~~~~~~~~~~

Users, customers, and operators are required to reference a vast pool of
documentation spread across multiple repositories and sites. Implementing
consistency in wording, format, content, and location provides readers with a
first-class experience. Additionally, users build confidence and trust in
software when it is well documented.

Contact
-------

For questions about getting involved with this initiative, reach out to the
OpenStack Discuss mailing `list`_. You may also contact the `Documentation`_
PTL or the Technical Committee sponsor for this item (dhellmann).

.. _`plan`: https://review.openstack.org/#/c/472275/
.. _`list`: http://lists.openstack.org/cgi-bin/mailman/listinfo/openstack-discuss
.. _`Documentation`: https://governance.openstack.org/tc/reference/projects/documentation.html

2. Community Infrastructure Sysadmins
=====================================

*TC Sponsor: Jeremy Stanley (fungi)*

The :ref:`project-infrastructure` team is responsible for designing,
building and maintaining the systems that are used in the day to day
operation of the OpenStack project as a whole; this includes
development, testing, and collaboration tools. All of the software
it runs is open source, and under public configuration management so
that everyone in the community has the opportunity to participate.
One very effective way to get involved in OpenStack, gaining a deep
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

3. Designate Contributors
=========================

Description
-----------

`Designate`_ is a service that manages DNS Zones and Recordsets. It supports
multiple DNS Servers, and DNS Service Providers, making it vital for any
network or web-based application.

They need contributors to help find and fix bugs, develop new features, and
help maintain the quality of the project, including cross-project initiatives.
Designate is quite stable, with any new features requiring long term planning,
design, and phased implementation.

Designate welcomes everyone, from someone starting in the community to senior
contributors who want new, interesting problems to tackle. Contributors will
get to work on a project that will be a central part of any OpenStack
deployment and work on a project that needs to scale from a small single node
install to a system controlling DNS servers worldwide.

Value
-----

Flexibility
~~~~~~~~~~~

DNS is fundamental in gracefully directing users and applications to services.
It allows the flexibility to replace underlying hardware while presenting
consumers with a consistent endpoint. Designate provides this flexibility to
operators and end users.

Self-Service
~~~~~~~~~~~~

Self-serviceability is a core tenet of OpenStack `technical vision`_. Designate
helps OpenStack clouds adhere to that principle by exposing DNS functionality
directly to end-users.

Consistency
~~~~~~~~~~~

The OpenStack community continues to evolve, and this evolution requires large
cross-project initiatives. Furthermore, users and operators expect consistency
across the OpenStack platform. Examples from recent history include
OpenStack-wide support for `Python 3`_ and easing operator pain by moving
`policy configuration`_ into code. Ensuring Designate stays up-to-date with
these initiatives is imperative in reducing operational costs, complexity, and
user frustration.

Contact
-------

If you are interested, please join #openstack-dns on Freenode or contact the
Designate PTL (Graham Hayes - mugsie), the Technical Committee sponsor (Sean
McGinnis - smcginnis). You may also email the openstack discuss mailing list
with the tag [designate] in the subject.

.. _`Designate`: https://governance.openstack.org/tc/reference/projects/designate.html
.. _`technical vision`: https://governance.openstack.org/tc/reference/technical-vision.html
.. _`Python 3`: https://governance.openstack.org/tc/goals/stein/python3-first.html
.. _`policy configuration`: https://governance.openstack.org/tc/goals/queens/policy-in-code.html
.. _`list`: http://lists.openstack.org/cgi-bin/mailman/listinfo/openstack-discuss

4. Glance Contributors
======================

Description
-----------

`Glance`_ is a service to manage disk images for OpenStack clouds. It was one
of the first projects developed in the OpenStack ecosystem. Nearly every
OpenStack deployment contains a Glance service. Without Glance, Nova cannot
create servers.

Glance is looking for new contributors who would be willing to provide reviews,
to work on bugs, or to work on new features. Glance has welcomed interns,
junior developers, and more senior developers. In every case, it is a great way
to grow and contribute to OpenStack.

Value
-----

Maintenance Costs
~~~~~~~~~~~~~~~~~

Glance is a critical service in OpenStack. Contributions to the future of the
image registry are essential to the stability of OpenStack. More importantly,
Glance is not feature-complete. There is significant technical debt that needs
to be taken care of and several features to implement.

Consistency
~~~~~~~~~~~

The OpenStack community continues to evolve, and this evolution requires large
cross-project initiatives. Furthermore, users and operators expect consistency
across the OpenStack platform. Examples from recent history include
OpenStack-wide support for `Python 3`_ and easing operator pain by moving
`policy configuration`_ into code. Ensuring Glance stays up-to-date with these
initiatives is imperative in reducing operational costs, complexity, and user
frustration.

Contact
-------

Interested? Join the Glance IRC channel (#openstack-glance) or reach out to the
OpenStack discuss `mailing list`_ using the `[glance]` tag.

.. _`Glance`: https://governance.openstack.org/tc/reference/projects/glance.html
.. _`Python 3`: https://governance.openstack.org/tc/goals/stein/python3-first.html
.. _`policy configuration`: https://governance.openstack.org/tc/goals/queens/policy-in-code.html
.. _`mailing list`: http://lists.openstack.org/cgi-bin/mailman/listinfo/openstack-discuss

5. Goal Champions
=================

Description
-----------

As OpenStack matures, large initiatives linger that affect the community as a
whole. Like with any large body of work, someone needs to step up and
coordinate the group, keep track of progress, call for and chair regular
meetings, and publish status updates. PTLs do this work for project teams,
leaders do it for various cross-project working groups and SIGs, and champions
do it to help us complete :ref:`release-cycle-goals` over a cycle.
Additionally, efficient coordination is one of the most productive ways to get
things done, especially in large communities.

The work of those champions is essential to the success of OpenStack, and yet
it is often challenging to find volunteers for those positions. Contributing as
a goal champion takes time (several hours per week), and that commitment needs
to be properly recognized and celebrated.

Volunteers for this role will make a direct impact on the productivity of
others, become respected leaders in OpenStack community, build influence among
their peers, and make great candidates for future elected leadership positions
in OpenStack.

Value
-----

Opportunity for Influence
~~~~~~~~~~~~~~~~~~~~~~~~~

As a sponsor or partial sponsor of a community-wide initiative, you have the
opportunity to influence the decision-making process. This influence is
particularly true if you have existing workarounds or have attempted
alternative solutions, both of which are essential perspectives to have in the
goal selection process.

Early Adoption
~~~~~~~~~~~~~~

By sponsoring a community goal champion, you have someone in-house to answer
questions about the ongoing work and decision making process upstream. This can
be an excellent resource in minimizing disruption to downstream products and
services, especially tracking a large piece of work across services and
projects.

Contact
-------

If you are interested in helping with community goals, contact the Technical
Committee sponsor for this item (dhellmann).
