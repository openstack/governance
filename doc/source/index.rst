===============================
 OpenStack Technical Committee
===============================

The OpenStack Technical Committee is the governing body of the OpenStack
open source project. It is an elected group that represents the contributors
to the project, and has oversight on all technical matters. This includes
developers, operators and end users of the software.

The Technical Committee is formally defined in the
`OpenStack Foundation bylaws`_ (in particular article 4.1(b), article 4.13
and Appendix 4) and further refined in the :doc:`reference/charter`.

Work under the Technical Committee is organized under official
:doc:`reference/projects/index` (responsible for the production of the
software up to release), `Special Interest Groups (SIGs)`_ (groups working
to advance a particular facet of OpenStack), :doc:`reference/popup-teams`
(formed around a limited cross-project objective) and
:doc:`reference/working-groups` (delegations from the TC to fill specific
functions like election organization).

These pages contain OpenStack Technical Committee reference documents
and track official resolutions voted by the committee.

Current Members
===============

.. memberstable::
      :datafile: ../../reference/members.yaml

Reference documents and Resolutions
===================================

.. toctree::
   :maxdepth: 2
   :titlesonly:

   reference/index
   goals/index
   resolutions/index
   resolutions/superseded/index

Office hours
============

Beyond discussing on the mailing-list and participating in ad-hoc IRC meetings,
TC members will hold office hours (for one hour) on the #openstack-tc IRC
channel at the following times every week:

* `01:00 UTC on Tuesdays <http://www.timeanddate.com/worldclock/fixedtime.html?hour=01&min=00&sec=0>`__

* `15:00 UTC on Wednesdays <http://www.timeanddate.com/worldclock/fixedtime.html?hour=15&min=00&sec=0>`__

You can contact TC members at any time, but there will be an effort to
be present at those specific hours. So don't hesitate to reach out if you
have any question!

How to propose governance changes
=================================

Motions should be posted for discussion as a proposed change to the
openstack/governance repository (on review.opendev.org) and/or as a
"[tc]" thread to the openstack-discuss@lists.openstack.org mailing-list.
Upon verification, the chair will put the motion on the
`current proposals tracker`_.

We use Gerrit to record votes, so before being formally voted on or approved,
motions will have to be presented as a change in the openstack/governance git
repository. You can find instructions on how to do that in the
`Developer's guide section of the Infra manual`_. Please contact the TC chair
in case you need help. Note that a number of simpler changes do not require
formal voting by the majority of the Technical Committee membership. Those
exceptions are listed in the :doc:`reference/house-rules` document.


.. _`OpenStack Foundation bylaws`: http://www.openstack.org/legal/bylaws-of-the-openstack-foundation/

.. _`Special Interest Groups (SIGs)`: https://governance.openstack.org/sigs/

.. _`current proposals tracker`: https://wiki.openstack.org/wiki/Technical_Committee_Tracker

.. _`Developer's guide section of the Infra manual`: https://docs.openstack.org/infra/manual/developers.html

Summary of User Survey Questions Responses
==========================================

Since 2019 the OpenStack Technical Committee has added questions to the
annual OpenStack User Survey.  Below are links to summaries and analysis
of those responses.

.. toctree::
   :maxdepth: 2
   :titlesonly:

   user_survey/analysis-12-2019
