========================
 Top 5 help wanted list
========================

This document lists areas where the OpenStack Technical Committee seeks
contributions to significantly help OpenStack as a whole. While in most
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

Interested? Contact the Documentation PTL (asettle) or the TC sponsor for
this item (dhellmann).

.. _`plan`: https://review.openstack.org/#/c/472275/


2. Glance Contributors
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
