=================================================================
2025-11-17 Retirement and Handover of the `os-net-config` Project
=================================================================

Background
----------

The `os-net-config` project was `formally
retired <https://review.opendev.org/c/openstack/governance/+/905145>`_
from OpenStack in April 2024 and is no longer under the governance of the
OpenStack Technical Committee (TC).

Following the project's retirement, concerns were raised regarding the
continued use of the project's name and PyPI entry under external maintenance
without prior coordination with the OpenStack community. Users and operators
depend on the integrity and transparency of the OpenStack release process to
make informed decisions about the software upon which they build their
infrastructure and business operations. Uncoordinated changes to project
ownership, particularly for packages that retain OpenStack branding,
risk undermining this trust by creating ambiguity about what
software is—and what is not—subject to OpenStack's governance, quality
standards, and security response processes.

When projects transition out of OpenStack governance, clear communication and
coordinated handover procedures are essential to maintain ecosystem integrity
and protect users from confusion about a project's provenance, maintenance
status, and relationship to OpenStack's coordinated release cycle.

Resolution
----------

The external maintainers of `os-net-config` have subsequently `taken steps`_
to address these concerns by:

* Removing OpenStack CI from the list of maintainers in relevant places
* Correcting the declared Author of the package to reflect current ownership

The TC recognizes the logistical complexity involved in forcing a complete
package name change on PyPI after the fact. Nevertheless, the TC emphasizes
that the integrity of the OpenStack ecosystem depends on transparent and
coordinated transitions when projects leave OpenStack governance.

Therefore, the OpenStack Technical Committee retroactively acknowledges and
formalizes the effective handover of the `os-net-config` project and its
corresponding PyPI package to its current external maintainers, while noting
that future transitions should follow established community processes to
avoid confusion and protect user trust.

The TC explicitly states it has no objection to the continued, independent use
of the `os-net-config` PyPI package name by its new custodians, provided
all documentation and metadata clearly reflect its status outside of
OpenStack governance.

The TC mandates that all remaining OpenStack-controlled artifacts related to
`os-net-config` be updated or corrected. Specifically, the external
maintainers must publish a new release to PyPI that:

* Removes references to the project's former OpenStack documentation
* Updates project URLs on the PyPI page to reflect current, non-OpenStack
  hosting locations
* Clearly indicates in the package description that the project is no longer
  maintained under OpenStack governance

Expectations for Future Transitions
------------------------------------

The TC reaffirms that any future projects transitioning out of OpenStack
governance must follow coordinated handover procedures, including:

* Clear communication with the TC and broader community via the
  `OpenStack mailing list`_ before changes to package ownership or branding
* Explicit updates to all documentation, metadata, and artifact repositories
  to reflect the change in governance
* Consideration of namespace changes where appropriate to avoid user confusion

These procedures exist to protect OpenStack's users, who rely on the
transparency and integrity of our release processes to sustain their
operations.

.. _taken steps: https://lists.openstack.org/archives/list/openstack-discuss@lists.openstack.org/message/OOUOSYN3MVPJH7ARAAW6WW5F6ZXUF2GP/
.. _OpenStack mailing list: https://lists.openstack.org/cgi-bin/mailman/listinfo/openstack-discuss
