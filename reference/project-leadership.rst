==================
Project Leadership
==================

OpenStack project teams are self-governing groups of contributors that produce
and maintain a set of deliverables. The primary leadership model for a project
team is the **Project Team Lead** (PTL) model, in which a single elected
individual serves as the team's point of accountability and decision-making
authority for the duration of a release cycle.

This document describes what the PTL role involves and how a PTL-led project
operates. Project teams that prefer to distribute leadership responsibilities
across multiple contributors instead of electing a single PTL may opt in to the
:doc:`Distributed Project Leadership <distributed-project-leadership>` model.

.. seealso::

   The `Project Team Guide`_ provides a practical guide for people who are new
   to the PTL role or are considering running for it.

What the PTL Role Is
--------------------

The :ref:`charter <charter-ptls>` defines the PTL's core authority. Beyond that
formal definition, the PTL serves as the primary external face of the project:
the person other contributors, SIGs, and the TC go to first when they need
input or action from the team. The role is one of coordination and facilitation
at least as much as it is one of decision-making authority.

The scope of what the PTL actually does day-to-day varies significantly between
project teams. Larger teams may have the PTL focus primarily on coordination
and delegation, while smaller teams may have the PTL more directly involved in
every aspect of operations. PTLs are strongly encouraged to delegate
responsibilities wherever they can, to avoid the role becoming a bottleneck.

Responsibilities
----------------

The responsibilities of a PTL have continually evolved over time. As a result,
this document makes no attempt to codify much of these responsibilities and
instead defers to the `Project Team Guide`_ or the individual contributors
guides for each project. With that said, there are a number of key
responsibilities that are required of a PTL.

Core team management
~~~~~~~~~~~~~~~~~~~~

The PTL is responsible for the health of the project's core reviewer group. A
decision to add or remove a core reviewer may be made by the PTL alone, though
consulting the existing core team first is strongly encouraged. A PTL does not
have to be core reviewer themselves and may opt to delegate management of the
core team to the existing core team. However, like the delegation of other
responsibilities, accountability for this role ultimately remains with the PTL.

.. seealso::

    The `Project Team Guide`_ provides a guide on how to maintain core
    membership, including guidelines on when and how to add or remove cores.

Liaisons
~~~~~~~~

A number of cross-team interactions require a named point of contact from the
project team. The individuals who fill these roles are called *liaisons*. The
formal liaison roles are the **Release Liaison**, the **TaCT SIG Liaison**,
and the **Security Liaison**. The responsibilities of these roles are described
in full in the :doc:`Distributed Project Leadership
<distributed-project-leadership>` document, where under that model they are
:ref:`required roles <dpl-required-roles>`.

Under the PTL model, **the PTL holds all liaison roles by default** and is not
required to appoint a separate person for each. Where the PTL does delegate a
role, the appointee's name is recorded in :repo:`the governance repo
<openstack/governance/src/branch/master/reference/projects.yaml>`. In either
case, accountability for each role remains with the PTL.

Relationship with the TC
------------------------

Although the TC has ultimate technical oversight over all official project
teams, it generally does not involve itself in team-internal decisions. The TC
delegates the responsibility and authority to conduct the day-to-day running of
the team and its accountability to the PTL. The PTL is trusted to manage the
team's affairs within the OpenStack community norms and the TC's published
guidelines and may further delegate there roles and responsibility to liaisons
they appoint.

The TC does expect PTLs to:

* Respond to community goal requirements and communicate the team's progress
  toward them.

* Engage with cross-project discussions that affect the team's deliverables.

* Escalate to the TC when a dispute cannot be resolved within the team.

The TC may intervene when team decisions affect other project teams or conflict
with general OpenStack goals.

Delegating and stepping down
----------------------------

The PTL is not expected to personally execute every duty listed in this
document. Healthy delegation, be that to individual contributors or to named
liaison roles, is a sign of a well-run team and not an abdication of
responsibility.

If a PTL needs to step down before the end of a cycle, they should:

1. Identify any interested candidates from the active contributor base.

2. Notify the TC so that it can appoint a replacement or initiate
   alternative arrangements.

3. Hand over knowledge of in-progress work, pending releases, and any
   time-sensitive commitments.

If the project team would prefer to move away from the PTL model entirely, it
may opt in to the :doc:`Distributed Project Leadership
<distributed-project-leadership>` model.

.. _TaCT SIG: https://governance.openstack.org/sigs/tact-sig.html
.. _First Contact SIG: https://wiki.openstack.org/wiki/First_Contact_SIG
.. _Project Team Guide: https://docs.openstack.org/project-team-guide/ptl.html
