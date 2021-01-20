==================================
Quality Assurance Developers
==================================

Summary
-------

The OpenStack community is seeking developers with a background in Python, bash
shell, or Javascript programming and free software to join the OpenStack QA
team.  This team is responsible for maintaining and evolving OpenStack's robust
and comprehensive quality assurance tools, which form the backbone of the
OpenStack CI pipeline.

Attrition due to shifts in employment or availability of personal time
impacts the team's ability to support the community effectively, and
so there is a constant need for new contributors who can commit to
investing sufficient effort to overcome the steep learning curve
associated with these varied technologies.

Business Case
-------------

Sponsorship of a team member is a way to visibly help build and maintain the
development and testing tools used by one of the most active open source project
in the world.  Team members interact with contributors across all the OpenStack
projects as well as with the OpenStack infrastructure system administrators who
ensure reliable access to resources for OpenStack CI systems.

Sponsors gain in-house expertise and experience building complex, comprehensive,
and modular software testing suites with open-source tools.  There is no better
way to gain exposure to and expertise with the testing suites that power a
leading-edge CI/CD in advance of potential deployment at home than to place
someone on the team that creates testing frameworks that are used by dozens of
software projects to run tests in the `Zuul project`_.

The software developed, skills involved, and open community practices learned
can have high value downstream in a sponsor's own enterprises and software
products.

Technical Details
-----------------

The OpenStack QA team is responsible for designing, building and maintaining the
testing harnesses and tools that are used in the day to day development and CI
process of the OpenStack project, as well as production cloud testing also.  In
the OpenStack paradigm, project teams are responsible for writing tests that
exercise and validate the code that they are contributing.  The definition of
what needs to be tested is standardized in the `Project Testing Interface`_.
The OpenStack QA team writes code that:

* deploys the OpenStack services in a form usable for testing (devstack)
* runs a gauntlet of API tests against the control plane of each OpenStack
  service (tempest)
* including complex RBAC operations (patrole),
* OpenStack-health dashboard for visualizing test results of OpenStack CI jobs
* grenade for upgrade testing
* hacking for code style

In addition to being used in the OpenStack CI pipeline, tempest and patrole can
also be used for large scale testing of production clouds.  All of the software
it runs is open source, and under public configuration management so that
everyone in the community has the opportunity to participate.  One very
effective way to get involved in OpenStack and gain a deep understanding and
visibility within the community is by helping maintain and evolve these tools.
Everything possible goes through code review, and gets extensively documented
and communicated with the rest of the community over IRC and mailing lists.

Value
~~~~~

The OpenStack project is composed of dozens of project teams that focus on
delivering specific services that together compose OpenStack.  What defines code
as being part of OpenStack is that it has passed review by the tools built by
the QA team.  Contributors to the QA team have a special vantage point, being
able to see how these services fit together, and how those integrations can have
problems.  This is first-hand experience with the challenges of integrating a
large, distributed multi-component project, which is a valuable skill.
Experiences with integration challenges with projects of this scale can be
transferred to other large projects within the enterprise.

Innovating On Top Of A Massive Effort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The culture built around extensive testing in OpenStack makes it easier for us
to trust patches proposed for review.  There are many kinds of testing
performed: unit, functional, style, API, scenario, upgrade, and end-to-end
(fullstack) testing are all supported by the toolset developed by the QA team.
For more information, see the `Project Team Guide, Testing Chapter`_.
In addition, we are constantly looking forward to innovate our testing
framework to provide more accurate simulations of customer issues.  Duplicating
a social and technical quality control system of this size takes incredible
amounts of time, people, and patience. Bolstering the QA system we already have
in place allows you to focus on testing that is specific to your product or
service while benefitting from the best of breed for testing innovation that
occurs anywhere in the project..

Contact
-------

Join the OpenStack QA IRC channel (``openstack-qa`` on `Freenode IRC`_), email
the openstack-discuss mailing list at list.openstack.org, or contact the `QA
PTL`_ directly if you would like to get involved.


.. _`Zuul project`: https://zuul-ci.org
.. _`Project Testing Interface`: https://governance.openstack.org/tc/reference/project-testing-interface.html
.. _`Project Team Guide, Testing Chapter`: https://docs.openstack.org/project-team-guide/testing.html
.. _`Freenode IRC`: https://freenode.net
.. _`QA PTL`: https://governance.openstack.org/tc/reference/projects/quality-assurance.html
