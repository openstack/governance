========================
 Licensing requirements
========================

Official OpenStack projects need to follow a number of rules when it comes
to licensing. This document clarifies what those requirements are.

In order to be considered for inclusion in the **TC-approved release**
(the subset of OpenStack projects that may be included in a Defcore
trademark program), the project must be licensed under ASLv2.

**OpenStack projects and libraries produced under the Big Tent** should
generally be licensed under ASLv2, and otherwise must be licensed under
a license supported by the CLA, which allows redistribution under ASLv2
(currently limited to MIT and BSD (both forms)). In particular, service
projects are recommended to always pick ASLv2 so that they may be included
in the TC-approved release in the future.

In order to be acceptable as dependencies of OpenStack projects,
**external libraries** (produced and published by 3rd-party developers)
must be licensed under an OSI-approved license that does not restrict
distribution of the consuming project. That includes ASLv2, BSD (both
forms), MIT, PSF, LGPL, ISC, and MPL. That excludes GPLv2, GPLv3, and AGPL.

**Projects run as part of the OpenStack Infrastructure** (in order to
*produce* OpenStack software) may be licensed under any OSI-approved license.

Other licenses (not explicitly listed in this document) may be considered
in the future on a case-by-case basis by the Technical Committee, with the
help of the OpenStack Foundation legal counsel.
