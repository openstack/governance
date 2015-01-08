======================================================
 Requirements for new OpenStack Projects applications
======================================================

Teams in OpenStack can be created as-needed and grow organically. As the team
work matures, some technical efforts will be recognized as being part of the
OpenStack community. By becoming an official OpenStack Project, they place
themselves under the authority of the OpenStack Technical Committee. In return,
their contributors get to vote in the Technical Committee election.

When considering new projects for addition, the TC will check that:

* The project aligns with the OpenStack Mission:
  The project must have a clear and defined scope. It should help further
  the OpenStack mission, by providing a cloud infrastructure service, or
  directly building on an existing OpenStack infrastructure service.

* The project follows the OpenStack way ("the 4 opens"):

  * Open Source:

    * The proposed project uses an open source license (preferably the Apache
      v2.0 license, since it is necessary if the project wants to be used in
      an OpenStack trademark program)
    * Project must have no library dependencies which effectively restrict
      how the project may be distributed or deployed

  * Open Community:

    * The leadership is chosen by the contributors to the project
    * The project has regular meetings on IRC and those meetings are logged

  * Open Development:

    * The project uses public code reviews on the OpenStack infrastructure
    * The project has core reviewers and adopts a test-driven gate for changes
    * The project provides liaisons that serve as contacts for the work of
      cross-project teams in OpenStack
    * Where it makes sense, the project cooperates with existing projects
      rather than gratuitously competing or reinventing the wheel
    * Project should use oslo libraries or oslo-incubator where appropriate

  * Open Design:

    * The project direction is discussed at the Design Summit and/or on
      public forums
    * The project uses the openstack-dev ML to discuss issues

* The project ensures basic interoperability with the rest of OpenStack:
  User-facing API services should support Keystone for discovery and
  authentication.

* The project should have an active team of contributors
