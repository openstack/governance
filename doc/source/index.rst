===============================
 OpenStack Technical Committee
===============================

The OpenStack Technical Committee is one of the governing bodies of the
OpenStack project. It is an elected group that represents the contributors
to the project, and has oversight on all technical matters.

The Technical Committee is formally defined in the
`OpenStack Foundation bylaws`_ (in particular article 4.1(b), article 4.13
and Appendix 4) and further refined in the :doc:`reference/charter`.

Upstream work under the Technical Committee is organized under official
:doc:`reference/projects/index` and more informal `Working Groups`_.

These pages contain OpenStack Technical Committee reference documents
and track official resolutions voted by the committee.

Current Members
===============

.. memberstable::
      :datafile: ../../reference/members

Reference documents and Resolutions
===================================

.. toctree::
   :maxdepth: 2
   :glob:
   :titlesonly:

   reference/index
   goals/index
   resolutions/index
   resolutions/superseded/index

How to propose governance changes
=================================

Motions need to be presented before Friday 0800 UTC to be added to the next
Tuesday meeting agenda for discussion. They should either be posted as a
proposed change to the governance repository (on review.openstack.org) or as
a "[tc]" thread to openstack-dev@lists.openstack.org (with a pointer to that
thread being posted to openstack-tc@lists.openstack.org to make sure it gets
the required attention from TC members). Upon verification, the chair will
put the motion on the `agenda for the next meeting`_.

There might be a backlog of requests, in which case the discussion will be
scheduled for a subsequent meeting. We use Gerrit to record votes, so before
being formally voted on or approved, motions will have to be presented as a
change in the governance git repository. You can find instructions on how to
do that in the `Developer's guide section of the Infra manual`_. Please
contact the TC chair in case you need help. Note that a number of simpler
changes do not require formal voting by the majority of the Technical
Committee membership. Those exceptions are listed in the
:doc:`reference/house-rules` document.


.. _`OpenStack Foundation bylaws`: http://www.openstack.org/legal/bylaws-of-the-openstack-foundation/

.. _`Working Groups`: https://wiki.openstack.org/wiki/Upstream_Working_Groups

.. _TechnicalCommittee: https://wiki.openstack.org/wiki/Governance/TechnicalCommittee

.. _`agenda for the next meeting`: https://wiki.openstack.org/wiki/Meetings/TechnicalCommittee

.. _`Developer's guide section of the Infra manual`: https://docs.openstack.org/infra/manual/developers.html
