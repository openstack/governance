===============================
 OpenStack Technical Committee
===============================

The OpenStack Technical Committee is the governing body of the OpenStack
open source project. It is an elected group that represents the contributors
to the project, and has oversight on all technical matters. This includes
developers, operators and end users of the software.

The Technical Committee is formally defined in the
`Open Infrastructue Foundation bylaws`_ (in particular article 4.1(b) and article 4.13)
and further refined in the :doc:`reference/charter`.

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

Meeting
=======

Beyond discussing on the mailing-list and participating in ad-hoc IRC meetings,
TC members will hold meeting at the following time every week:

* `Weekly Meeting <http://eavesdrop.openstack.org/#Technical_Committee_Meeting>`__

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


.. _`Open Infrastructue Foundation bylaws`: http://www.openstack.org/legal/bylaws-of-the-openstack-foundation/

.. _`Special Interest Groups (SIGs)`: https://governance.openstack.org/sigs/

.. _`current proposals tracker`: https://wiki.openstack.org/wiki/Technical_Committee_Tracker

.. _`Developer's guide section of the Infra manual`: https://docs.openstack.org/infra/manual/developers.html

Summary of User Survey Questions Responses
==========================================

Since 2019 the OpenStack Technical Committee has added questions to the annual
OpenStack User Survey. In 2019, 2021 and 2022 survey the following questions
were asked by the TC:

* How do you upgrade your version of OpenStack?
* Once on a given release, do you use stable branches for bug-fix upgrades?
* To which projects does your organization contribute maintenance resources,
  such as patches for bug fixes and code reviews on master or stable
  branches?
* How do members of your organization contribute to OpenStack?
* What prevents you or your organization from contributing more maintenance
  resources, or makes contributing difficult?
* Other ways to participate?

The intention of these questions was to understand how users are maintaining
their OpenStack clouds and how they are interacting with the community.  In the
case that they weren't currently interacting with the community it was hoped
that the questions would spark thoughts on how they could participate in the
future.

In the 2023 survey the following questions were added by the TC:

* How are you consuming OpenStack?
* How do your users interact with OpenStack?
* Participation in UI is lacking in maintenance. Do you contribute in UI
  maintenance?
* What library, if any, are you using to interface with OpenStack?
* What software or services in your cloud environment are enabled by OpenStack
  and OpenStack provisioned resources, for example: Kubernetes?


Below are links to summaries and analysis of those responses.

.. toctree::
   :maxdepth: 2
   :titlesonly:

   user_survey/analysis-2019
   user_survey/analysis-2021
   user_survey/analysis-2022
   user_survey/analysis-2023
