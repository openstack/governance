===============================================
 2013-31-06 Ceilometer and Heat Official Names
===============================================

The OpenStack Foundation bylaws state:

  https://wiki.openstack.org/wiki/Governance/Foundation/Bylaws

  4.1(b)

  [..]
  The "OpenStack Project" shall consist of a "Core OpenStack Project,"
  library projects, gating projects and supporting projects. . The
  Core OpenStack Project means the software modules which are part of
  an integrated release and for which an OpenStack trademark may be
  used. The other modules which are part of the OpenStack Project, but
  not the Core OpenStack Project may not be identified using the
  OpenStack trademark except when distributed with the Core OpenStack
  Project.

  The role of the Board of Directors in the management of the
  OpenStack Project and the Core OpenStack Project are set forth in
  Section 4.13. On formation of the Foundation, the Core OpenStack
  Project is the Block Storage, Compute, Dashboard, Identity Service,
  Image Service, Networking, and Object Storage modules. The Secretary
  shall maintain a list of the modules in the Core OpenStack Project
  which shall be posted on the Foundation's website.

  4.13

  For modules of the Core OpenStack Project, the Technical Committee
  may recommend to the Board of Directors the modules for addition,
  combination, split or deletion from the Core OpenStack
  Project. Except as provided below, the Board of Directors shall
  consider only those additions, combinations, splits or deletions
  that are recommended by the Technical Committee, but shall have the
  sole authority to approve or reject such additions, combinations,
  splits and deletions from the Core OpenStack Project.


The Technical Committee's interpretation of these clauses is that only
the projects which are currently included in the "Core OpenStack
Project" may use an official OpenStack project name even when they are
distributed standalone. For example, Nova may call itself OpenStack
Compute because it is included in the "Core OpenStack Project".

The Ceilometer and Heat projects became Integrated during the Havana
release cycle and we feel it makes sense for these projects to also
be allowed use their official project names in isolation:

  OpenStack Telemetry (Ceilometer)
  OpenStack Orchestration (Heat)

Given our interpretation of the bylaws, we formally recommend that the
Board of Directors approve the addition (by the Secretary) of these
projects to the list of the modules in the Core OpenStack Project.

For the avoidance of doubt, the Technical Committee is not taking a
stance here on whether these projects should be required to be
included in OpenStack products which use the OpenStack trademark. This
is a whole other, commonly understood, meaning of the term "Core" and
we recognize there is not consensus around including these projects
under this meaning of the term.
