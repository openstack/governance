.. _20211224_tags_framework_removal:

========================================
2021-12-24 Removal of the tags framework
========================================

With the advent of :doc:`20141202-project-structure-reform-spec`, the TC
started using a tags framework to describe various expectations of the projects
making up OpenStack. The primary target audience was operators. However,
it turned out that the tags framework data was neither complete
(i.e., certain assumptions were not asserted with the tags)
nor precise
(i.e., the assumptions tags made might not have been exercised in practice)
and, at least recently, there was no positive feedback on the usefulness of
the tags framework. [1]_
Hence, the TC has concluded that the tags frameworks should be removed.
[2]_ [3]_

.. [1] http://lists.openstack.org/pipermail/openstack-discuss/2021-September/024804.html
.. [2] http://lists.openstack.org/pipermail/openstack-discuss/2021-October/025554.html
.. [3] http://lists.openstack.org/pipermail/openstack-discuss/2021-October/025571.html
