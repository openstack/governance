========================
 Licensing requirements
========================

Official OpenStack projects need to follow a number of rules when it comes
to licensing.

The project must be licensed under `Apache License, Version 2.0`_ (ASLv2).

.. _Apache License, Version 2.0: https://www.apache.org/licenses/LICENSE-2.0

**OpenStack projects and libraries** (produced by official OpenStack
project teams) should generally be licensed under the Apache License,
Version 2.0 (ASLv2), or under a license that is both compatible with
ASLv2 and allows redistribution or sublicensing under ASLv2 terms.
Currently, only the MIT license and the BSD 2-Clause and 3-Clause
licenses meet this requirement. In particular, service projects are
strongly recommended to use ASLv2 as their license.

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

.. _legal-discuss: https://lists.openstack.org/mailman3/lists/legal-discuss.lists.openstack.org/

**Projects run as part of the OpenStack Infrastructure** (in order to
*produce* OpenStack software) may be licensed under any `OSI-approved license`_.

This includes tools that are run with or on OpenStack projects only
during validation or testing phases of development (e.g., a source
code linter).

.. _OSI-approved license: https://opensource.org/license

Other licenses (not explicitly listed in this document) may be considered
in the future on a case-by-case basis by the Technical Committee, with the
help of the OpenInfra Foundation legal counsel.
