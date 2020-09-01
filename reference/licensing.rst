========================
 Licensing requirements
========================

Official OpenStack projects need to follow a number of rules when it comes
to licensing.

The project must be licensed under `Apache License, Version 2.0`_ (ASLv2).

.. _Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0

**OpenStack projects and libraries** (produced by official OpenStack project
teams) should generally be licensed under ASLv2, and otherwise must be
licensed under a license supported by the `Contributor License
Agreement`_ (CLA) which allows redistribution by the OpenStack
Foundation under ASLv2 (currently only the MIT and both forms of the
BSD license meet this requirement). In particular, service projects
are recommended to *always* pick ASLv2.

.. _Contributor License Agreement: https://wiki.openstack.org/wiki/How_To_Contribute#Contributor_License_Agreement

In order to be acceptable as dependencies of OpenStack projects,
**external libraries** (produced and published by 3rd-party developers)
must be licensed under an `OSI-approved license`_ that does not restrict
distribution of the consuming project. The list of acceptable licenses
includes ASLv2, BSD (both forms), MIT, PSF, LGPL, ISC, and MPL. Licenses
considered incompatible with this requirement include GPLv2, GPLv3, and AGPL.

[A]GPL libraries used during validation or testing phases of development fall
into a gray area - they are not presumed to be compatible or incompatible and
instead are reviewed on a case by case basis. Please use the `legal-discuss`_
mailing list to bring up any such cases.

.. _legal-discuss: http://lists.openstack.org/cgi-bin/mailman/listinfo/legal-discuss

**Projects run as part of the OpenStack Infrastructure** (in order to
*produce* OpenStack software) may be licensed under any `OSI-approved license`_.

This includes tools that are run with or on OpenStack projects only
during validation or testing phases of development (e.g., a source
code linter).

.. _OSI-approved license: http://opensource.org/licenses/alphabetical

Other licenses (not explicitly listed in this document) may be considered
in the future on a case-by-case basis by the Technical Committee, with the
help of the OpenStack Foundation legal counsel.
