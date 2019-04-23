======================
 openstack-governance
======================

The repository https://opendev.org/openstack/governance/
contains OpenStack Technical Committee reference documents and tracks
official resolutions voted by the committee. It also contains a
library for accessing some of the machine-readable data in the
repository.

Directory structure:

    reference/
        Reference documents which need to be revised over time.
        Some motions will just directly result in reference doc changes.
    resolutions/
        When the motion does not result in a change in a reference doc, it
        can be expressed as a resolution.
        Those must be named YYYYMMDD-short-name with YYYYMMDD being the
        proposal date in order to allow basic sorting.
    goals/
        Documentation for OpenStack community-wide goals, organized by
        release cycle. These pages will be updated with project status
        info over time, and if goals are revised.

See https://governance.openstack.org/tc/ for details.
