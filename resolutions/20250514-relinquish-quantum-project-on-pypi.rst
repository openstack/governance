=====================================================
2025-05-14 Relinquish the ``quantum`` project on PyPI
=====================================================

Whereas:

* The OpenStack Networking service was historically named `quantum`
  prior to its renaming to `neutron` in 2013. This `renaming`_ was approved by
  the OpenStack Technical Committee.
* No active OpenStack project or community-maintained package currently
  requires the `quantum` namespace on `PyPI`_
* PyPI does not support reclaiming project names `once deleted`_,
  making deletion a final and permanent action.
* A request has been made on the `OpenStack Discuss mailing list`_
  to transfer ownership of the `quantum` project on PyPI to a new maintainer.
* The existing content under the `quantum` name on PyPI is legacy and
  can be deleted

It is hereby resolved that:

* The OpenStack Technical Committee agrees to relinquish control of
  the `quantum` name on PyPI.
* The OpenStack Infra team is authorized to delete all OpenStack-owned
  package versions under the `quantum` name on PyPI.
* The OpenStack Infra team shall then transfer the project name to the
  requester as per the standard PyPI project `transfer process`_.
* The OpenStack Technical Committee disclaims any responsibility or
  liability for the legal use or implications associated with the "quantum"
  name.


.. _renaming: https://lists.launchpad.net/openstack/msg22544.html
.. _PyPI: https://pypi.org/project/quantum/
.. _once deleted: https://pypi.org/help/#deletion
.. _OpenStack Discuss mailing list: https://lists.openstack.org/archives/list/openstack-discuss@lists.openstack.org/thread/2OHLYITMHMMQU5O2XKMCDNZCX4E3UOJD/
.. _transfer process: https://pypi.org/help/#request-ownership
