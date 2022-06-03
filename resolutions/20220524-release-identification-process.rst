===================================================
2022-05-24 OpenStack release identification process
===================================================

After the Zed cycle, the OpenStack release naming process has been changed.
We introduced the release number as an identification code to release but
will still have the release name especially to use for marketing usage.

* Each OpenStack release will have an identification code: “year”.”release
  count within the year”. Example: "OpenStack 2023.1"

* OpenStack release names selection criteria and the process will be handled
  by the staff of the OpenInfra Foundation. Foundation staff will make sure
  that they satisfy the OpenStack release team tooling requirements. The
  OpenStack release team PTL sign-off is needed on naming criteria defined by the
  Foundation staff.

* The OpenStack Technical Committee will not be involved in the process,
  the release team will directly coordinate with the foundation staff.

* The release number will be used as the primary identifier in the development
  cycle but the release name will also be used in some places. we will use
  release number in the stable branch (Example: stable/2023.1), spec repo or
  any other directory structure, testing tools etc. The release team can choose
  either to continue using the release name or use number for release
  tooling and milestone name.

All the changes mentioned in this resolution will be applied immediately after
the Zed release cycle.

Reference
=========

* `The Technical Committee meeting Etherpad
  <https://etherpad.opendev.org/p/openstack-release-identification-schema>`__
* Mailing list discussion threads from `April 2022
  <http://lists.openstack.org/pipermail/openstack-discuss/2022-April/028354.html>`__
  and `May 2022
  <http://lists.openstack.org/pipermail/openstack-discuss/2022-May/028539.html>`__
