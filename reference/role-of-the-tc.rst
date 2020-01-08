=========================================
Role of the OpenStack Technical Committee
=========================================

The OpenStack Technical Committee ("TC") is chartered under the
`OpenStack Foundation bylaws`_ (section 4.13) with the task of managing
"technical matters relating to the OpenStack Project". Its first and foremost
role is therefore to define the technical governance of the OpenStack
project. The current model uses a two-level structure (with project
teams responsible for sets of git repositories or specific tasks,
electing their own leadership) which means that the TC is not directly
in charge of organizing day-to-day work. OpenStack being an open
collaboration with volunteers, the TC also does not command development
resources that can be applied to priorities or to meet certain deadlines.

So what is the role of the TC under the current OpenStack technical
governance model? This living document aims to answer that question.

Defining the OpenStack open source project governance model
===========================================================

The main role of the TC is to define the model under which the OpenStack
open source project is governed. Defining governance means defining the
processes of interaction and decision-making among the actors involved
in producing OpenStack, through the creation, reinforcement, or
reproduction of social norms and institutions. It is therefore the duty of
the TC to describe the community structure, systems, operating principles,
and values by creating and maintaining corresponding documentation. This is
done in the :doc:`Technical Committee charter <charter>`,
the `TC governance website`_ documents and other TC-maintained publications
such as the `Project Team guide`_.

The TC is just one of the governance bodies more widely involved in
OpenStack governance. An important part of its role is therefore to
handle the relationships with other OpenStack governance bodies like
the OSF Board of Directors, or the OpenStack User Committee.

Refining and applying the current OpenStack governance model
============================================================

While the governance model itself is changed very rarely, it is
constantly tweaked to better handle corner cases as they are discovered,
using amendments to the :doc:`TC charter <charter>`, resolutions, or changes
in other TC-maintained documents.

The current governance model institutes a two-level structure with
:doc:`project teams <projects/index>` in charge of specific sets of git
repositories or tasks. The TC is responsible for making sure the model
is followed, and fair elections are held for every project team.
Finally, while most conflicts should be resolved at the project team level,
the TC remains ultimately responsible in case issues cannot be solved at
that level, for example in case there is a dispute between two project
teams on the common way forward.

Scope of the project
====================

The `OpenStack Foundation bylaws`_ explicitly state in section 4.13 that
the TC's authority over technical matters includes the authority to
determine the scope of the "OpenStack" released software.

Under the current governance model, that means the TC constantly refines
the rules used to decide which teams are part of the project and which
groups are independent (and building on the work of the project). It
reviews applications from new project teams that want to place their work
under the oversight of the TC, effectively deciding the scope of the project.

As part of this authority on scope, the TC also provides technical input
to the trademark programs defined at the OSF Board level, for example by
designating sections of code which are required to be present in an
OpenStack installation in order for it to be eligible to use the "OpenStack
Powered" trademark.

Defining global technical goals
===============================

While most technical details are handled at the project team level, you
still need a body caring about the "OpenStack" experience, beyond each
component user experience. It is part of the TC role to take that step
back, consider OpenStack as "one platform" that users and operators
choose to leverage, and define reasonable technical goals for the
OpenStack community as a whole. This includes looking at gaps between
established project teams, driving a common user experience (common
operational behavior, limited dependencies, base quality levels, minimum
feature set...), pushing cross-project initiatives and influencing its
general direction. One way to achieve that is through the definition of
OpenStack :doc:`release goals <../goals/index>`.

Ensuring a healthy, open collaboration
======================================

The TC is responsible for making sure the OpenStack project follows
the :doc:`four opens <opens>` and operates as a truly open collaboration
on a level playing field. This includes checking that project teams follow
open source :doc:`licensing rules <licensing>`, are not artificially limiting
the features of the open source software to sell a proprietary "enterprise"
version, operate in a transparent and accessible manner, and encourage
cultural, professional and personal diversity in contributions.

Beyond that, TC members are engaged in proactively assessing the health of
the various project teams, and provide advice and help to team members.


.. _OpenStack Foundation bylaws: https://www.openstack.org/legal/bylaws-of-the-openstack-foundation/
.. _TC governance website: https://governance.openstack.org/tc/
.. _Project Team guide: http://docs.openstack.org/project-team-guide
