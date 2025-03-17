=====================================================
2025-03-17 Extend scope of VMT to cover all projects
=====================================================

The OpenStack `vulnerability management team (VMT)`_ is responsible
for vulnerability management practices across most OpenStack
project repositories. The team coordinates the progressive disclosure
of vulnerabilities by working with bug reporters, project contributors
and project maintainers. Their work is crucial not only in handling
different classes of security issues in or related to the
OpenStack code base, but also in ensuring a common entry point and a
consistent process around such issues. This consistency is essential to
users, operators and developers of OpenStack since they needn't be burdened
from following team-specific processes, intentionally or
inadvertently violating disclosures because of differences in security
processes between different OpenStack project teams.

Historically, OpenStack teams have been encouraged to work with the
`OpenStack Security SIG`_, which includes the VMT, by opting-into this security
process. VMT's oversight has been restricted to deliverables from a `subset of
OpenStack project teams`_.

The OpenStack Technical Committee resolves to extend the mandate of the
OpenStack Vulnerability Management Team, and add all
:doc:`/reference/projects/index` under their purview.

This resolution does not automatically bring all code repositories
under the ``openstack/`` namespace on opendev.org under VMT. Individual project
teams retain the discretion to determine which repositories should be subject
to vulnerability management.

The VMT commits its efforts to the ``master`` branch (the primary development
branch) and all `maintained`_ stable branches. This resolution does not
require the VMT to extend vulnerability management to any other code branches.

This resolution requires OpenStack project teams to:

- nominate a security liaison for their projects. This is already
  a requirement of teams following
  :doc:`/reference/distributed-project-leadership`. Project team leaders
  must update the `VMT liaisons`_ list and ensure it remains current
  through each release cycle.
- ensure that project bug trackers follow the VMT guidelines including
  defining a ``<project>-coresec`` team and granting access to the
  `VMT Launchpad team`_ to view private security bugs in the project.
- ensure that project bug trackers, project teams and the above-mentioned
  ``coresec`` groups on https://launchpad.net are owned by
  ``OpenStack Administrators``.
- limit membership in the project’s coresec group to a small subset of
  trusted contributors and update the group each release cycle by
  removing inactive members.

In rare occasions, project teams may not comply to the guidelines of the VMT,
such as respecting bug embargo timelines, or responding to questions
on bug reports within a reasonable timeframe. With each term of the
OpenStack TC, we resolve to nominate two representatives to interface with the
OpenStack VMT. These members may participate in triaging security bugs and
helping with the VMT process, however, the primary responsibility would be to
ensure that project teams are attentive and responsive through the
vulnerability management process.

.. _vulnerability management team (VMT): https://docs.openstack.org/project-team-guide/vulnerability-management.html
.. _subset of OpenStack project teams: https://opendev.org/openstack/ossa/src/commit/dca905784d01aace07e35bac7cb9bc8d87891cbb/doc/source/repos-overseen.rst
.. _OpenStack Security SIG: https://wiki.openstack.org/wiki/Security-SIG
.. _VMT liaisons: https://wiki.openstack.org/wiki/CrossProjectLiaisons#Vulnerability_management
.. _maintained: https://docs.openstack.org/project-team-guide/stable-branches.html
.. _VMT Launchpad team: https://launchpad.net/~openstack-vuln-mgmt
