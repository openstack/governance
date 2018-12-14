=====================================================
 Requirements for new OpenStack Project applications
=====================================================

Teams in OpenStack can be created as-needed and grow organically.
By becoming an official OpenStack Project, they place
themselves under the authority of the OpenStack Technical Committee. In return,
their contributors get to vote in the Technical Committee election.

Official project teams are documented in the `reference/projects.yaml` file
from the `openstack/governance` repository. To propose an addition or a
change, propose the corresponding `projects.yaml` file change for review.

When considering new projects for addition, the TC will check that:

* The project aligns with the OpenStack Mission:
  The project must have a clear and defined scope. It should either:

  * help :doc:`further the OpenStack mission <technical-vision>` by providing a
    cloud service;
  * help further the OpenStack mission by providing a service for operators of
    OpenStack clouds;
  * provide deployment and lifecycle management tooling for OpenStack;
  * provide packaging recipes to be used when deploying OpenStack;
  * provide client-side tools to enable users to interact with OpenStack; or
  * provide integration to enable adjacent systems to interoperate with
    OpenStack.

* The project follows the OpenStack way ("the 4 opens"):

  * Open Source:

    * The proposed project uses an open source license (preferably the Apache
      v2.0 license, since it is necessary if the project wants to be used in
      an OpenStack trademark program)
    * The project must have no library dependencies which effectively restrict
      how the project may be distributed or deployed

  * Open Community:

    * The leadership is chosen by the contributors to the project
    * If the project has meetings, regular or otherwise, they should be public
      and in IRC. They should all be logged and published. Project teams have
      discretion as to where meetings are held.  They can be in the project
      specific IRC channel, if it exists or one of the general meeting channels
      available.  The advantage of hosting meetings in the project specific
      channel is that project participants not present can catch-up more
      easily.  Whereas holding the meeting in a general channel gives extra
      visibility and makes it easier to ping other contributors.
    * The project shall provide a level and open collaboration playing field
      for all contributors. The project shall not benefit a single vendor, or
      a single vendors product offerings; nor advantage contributors from a
      single vendor organization due to access to source code, hardware,
      resources or other proprietary technology available only to those
      contributors.

  * Open Development:

    * The project uses public code reviews on the OpenStack infrastructure
    * The project has core reviewers and adopts a test-driven gate in the
      OpenStack infrastructure for changes
    * The project provides liaisons that serve as contacts for the work of
      cross-project teams in OpenStack
    * Where it makes sense, the project cooperates with existing projects
      rather than gratuitously competing or reinventing the wheel
    * Where appropriate, the project adopts technology and patterns
      used by existing OpenStack projects

  * Open Design:

    * The project direction is discussed at the Design Summit and/or on
      public forums
    * The project uses the openstack-dev ML to discuss issues

* The project ensures basic interoperability with the rest of OpenStack:
  User-facing API services should support Keystone for discovery and
  authentication.

* The project has an active team of one or more contributors.

* The project participates in any goals specified by the TC, as
  defined by :ref:`release-cycle-goals`. Any existing goals that are
  not met should be prioritized and completed within the first year of
  a team joining.

* The project meets any policies that the TC requires all projects to
  meet. For instance, the :doc:`project-testing-interface`.

In order to do an evaluation against this criteria, the TC expects the project
to be set up and have some history to evaluate.  A few months of operating and
following these project requirements is a rough guideline for how long
to wait before applying to be approved by the TC.

However, in order to facilitate adoption of existing established projects,
candidate projects may ask the Technical Committee for an early answer on
the question of alignment with the OpenStack Mission, before the project is
set up on OpenStack development infrastructure.

If the project has not followed the 4 Opens since its inception - i.e. it was
seeded with the release of a pre-existing code base - then the TC may look for
evidence of active engagement from the community, beyond the original authors.
If the community did not get the opportunity to contribute to the earliest
decisions (which are usually the hardest to change), then a lack of subsequent
community engagement is of greater concern, as it may indicate that the project
only meets the needs of a single organisation. Projects that have always
followed the 4 Opens are not subject to any particular standard of community
engagement.

Once a project has joined OpenStack, it may create additional source code
repositories as needed at the discretion of its Project Team Lead (PTL) without
prior approval from the TC as long as the additional source code repositories
fall within the scope of the approved project mission statement.

Releases of OpenStack deliverables are handled by the OpenStack Release
Management team through the openstack/releases repository. Official projects
are expected to relinquish direct tagging (and branch creation) rights in
their Gerrit ACLs once their release jobs are functional.

Official project teams are expected to participate in all `elections`_ held
after the team is accepted as official, regardless of how recently the team
leadership may have been established.

.. _elections: https://docs.openstack.org/project-team-guide/open-community.html#technical-committee-and-ptl-elections
