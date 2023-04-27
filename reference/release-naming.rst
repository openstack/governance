===========================
Release Identification/Name
===========================

Release Identification
----------------------

After the release "Zed", each OpenStack release has an
identification code: "year"."release count within the year"

Example:

* OpenStack 2023.1 Axxxx

Where "2023" is the year of the release, "1" represents the first release
of the year and "Axxxx" is the release name.

Other examples:

* OpenStack 2023.2 Bxxxx
* OpenStack 2024.1 Cxxxx

With this release identification schema we get an easy and sustainable
approach to identify different OpenStack releases without dealing with the
ambiguity of the release name and alphabet iteration.

The OpenStack Technical Committee has passed a :doc:`resolution
<../resolutions/20220524-release-identification-process>` for the release
identification process. The release number will be used as the primary
identifier in the development cycle but the release name will also be used
in some places.

* Stable branches: Use release number for stable branch name.
  Example: stable/2023.1

* Spec repo or any other directory structure: Use release number which is more
  aligned with what stable branches are going to use.

* Testing tools: Use release number which is more aligned with what stable
  branches are going to use.

* Release notes: For the version of specific project use combined OpenStack release
  number and the project's version, like "OpenStack 2023.1 (Nova 27.X.Y)".
  There should not be OpenStack release name, like "Antelope" included in the version.

  Examples:

  * OpenStack 2023.1 (Nova 27.0.0)
  * OpenStack 2023.2 (Neutron 23.0.0)

  In case when there is no need to give version of the specific project, but
  just version of OpenStack, there should be only release number used, like
  "OpenStack 2023.1".

  Examples:

  * OpenStack 2023.2
  * OpenStack 2024.1

* Project specific documentation: use release number combined with version of the project.

  Examples:

  * OpenStack 2023.1 (Nova 27.0.0)
  * OpenStack 2023.2 (Neutron 23.0.0)

* OpenStack documentation: in cases when there is need to just give version of OpenStack
  without specific project's version, use release number without marketing name.

  Examples:

  * OpenStack 2023.2
  * OpenStack 2024.1

* Release page/tooling/milestone name: The release team can choose either to
  continue using the release name or use number for release tooling and
  milestone name.

* Marketing materials: Release name is still there to be used in any marketing or
  other non-technical materials. Release number must be also used in such cases.

* Other, non-marketing related places: use release number combined with version of
  the project unless there is clear reason to use OpenStack release name instead.

  Examples:

  * OpenStack 2023.1 (Nova 27.0.0)
  * OpenStack 2023.2 (Neutron 23.0.0)

  Or if there is no specific project version needed:

  * OpenStack 2023.2
  * OpenStack 2024.1

Release Name
------------

We will continue with the release name but mainly for marketing usage.

* OpenStack release names will be handled by the staff of the OpenInfra
  Foundation.

* Foundation staff will define the naming criteria and process but make sure
  they satisfy the OpenStack release team's tooling requirements.

* The OpenStack release team PTL sign-off is needed on naming criteria defined
  by the Foundation staff.

* The OpenStack Technical Committee will not be involved in the process,
  the release team will directly coordinate with the foundation staff.

Release Name Selection History
------------------------------

=======  ==============  ================  ==========  ==========  ==================
Release  Coordinator     Nominations Open  Poll Open   Poll Close  Geographic Region
=======  ==============  ================  ==========  ==========  ==================
M_       Monty Taylor    2015-06-01        2015-06-08  2015-06-15  Tokyo
N_       Monty Taylor    2015-11-08        2015-11-30  2015-12-07  Texas Hill Country
O_       Monty Taylor    2015-11-08        2015-11-30  2015-12-07  Catalonia
P_       Monty Taylor    2016-06-22        2016-07-06  2016-07-13  New England
Q_       Monty Taylor    2016-06-22        2016-07-06  2016-07-13  New South Wales
R_       Monty Taylor    2017-03-22        2017-04-05  2017-04-12  British Columbia
S_       Paul Belanger   2018-02-21        2018-03-14  2018-03-21  Berlin
T_       Tony Breeds     2018-09-15        2018-10-15  2018-10-22  Colorado
U_       Rico Lin        2019-07-01        2019-08-12  2019-08-19  China
V_       Sean McGinnis   2019-11-11        2019-12-09  2019-12-16  British Columbia
W_       Sean McGinnis   2020-01-20        2020-02-17  2020-02-23  N/A [*]_
X_       Sean McGinnis   2020-11-02        2020-11-30  2020-12-06  N/A
Y_       Ghanshyam Mann  2021-05-13        2021-06-10  2021-06-17  N/A
Z_       Ghanshyam Mann  2022-01-11        2022-01-25  2022-02-01  N/A
=======  ==============  ================  ==========  ==========  ==================

The Zed release is the last release for which the OpenStack Technical Committee
was involved in the selection of the release name.

.. [*] Starting with the W release, the naming criteria changed from referring
   to the physical or human geography of the region encompassing the location
   of the OpenStack Summit, to any name proposed by the community that starts
   with the designated release letter.

.. _M: http://lists.openstack.org/pipermail/openstack-dev/2015-July/069496.html
.. _N: http://lists.openstack.org/pipermail/openstack-dev/2016-January/084432.html
.. _O: http://lists.openstack.org/pipermail/openstack-dev/2016-January/084432.html
.. _P: http://lists.openstack.org/pipermail/openstack-dev/2016-August/101891.html
.. _Q: http://lists.openstack.org/pipermail/openstack-dev/2016-August/101891.html
.. _R: http://lists.openstack.org/pipermail/openstack-dev/2017-April/116100.html
.. _S: http://lists.openstack.org/pipermail/openstack-dev/2018-March/128899.html
.. _T: http://lists.openstack.org/pipermail/openstack-dev/2018-November/136464.html
.. _U: http://lists.openstack.org/pipermail/openstack-discuss/2019-August/008904.html
.. _V: http://lists.openstack.org/pipermail/openstack-discuss/2020-January/011947.html
.. _W: http://lists.openstack.org/pipermail/openstack-discuss/2020-March/013006.html
.. _X: http://lists.openstack.org/pipermail/openstack-discuss/2020-December/019537.html
.. _Y: http://lists.openstack.org/pipermail/openstack-discuss/2021-July/023512.html
.. _Z: http://lists.openstack.org/pipermail/openstack-discuss/2022-February/027242.html
