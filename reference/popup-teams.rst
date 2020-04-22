===========
Popup teams
===========

The work to produce OpenStack software is organized around
:doc:`projects/index` which are responsible for producing the various
deliverables up to release. However, some features or architectural
changes need to be coordinated across multiple project teams to be considered
successfully completed. To drive this work for the duration of those specific
objectives, contributors can temporarily set up Popup teams.

Popup teams are lightweight structures that are recognized by the Technical
Committee as pursuing a goal considered desirable for OpenStack. Beyond
extra visibility and recognition, popup teams are also assigned an experienced
community member to help them establish or grow connections necessary to the
success of their work.

When they are formed, popup teams should have at least two leaders,
a clear objective, and a clear disband criteria. If the team does not
have a clear time-limited objective, they should be set up as
`Special Interest Groups (SIGs)`_ instead. If an objective affects
most project teams, it should be made light enough to fit in the
:doc:`../goals/index` process instead.

.. _`Special Interest Groups (SIGs)`: https://governance.openstack.org/sigs/

Current OpenStack popup teams
=============================

Image encryption
----------------

* **Co-leads**: Josephine Seifert and Markus Hentsch

* **TC Liaison**: Jeremy Stanley

* **Objective**: Implementing encryption and decryption of images and the
  handling of those images in OpenStack

* **Disband criteria**: Handling of encrypted images works in Nova, Cinder and
  Glance and can be triggered via an openstackclient-plugin

Secure Default Policies
-----------------------

Co-leads
~~~~~~~~

* Raildo Mascena (raildo)
* Ghanshyam Mann (gmann)

TC Liaison
~~~~~~~~~~

Ghanshyam Mann (gmann)

Objective
~~~~~~~~~

The keystone project has migrated all of its default policies to 1) use
oslo.policy's scope_types attribute, which allows the policy engine to
understand "system scope" and distinguish between an admin role assignment on a
project versus an admin role assignment on the entire system, 2) ensure all
rules use one of the default roles (admin, member, and reader) which both
ensures support for a read-only role and prevents custom roles from accidental
over-permissiveness. Although the problems being solved are slightly different,
the keystone team found it was easiest to migrate everything at once. The rest
of the OpenStack services can use this migration as a template for securing
their own policies.

More information: https://wiki.openstack.org/wiki/Consistent_and_Secure_Default_Policies_Popup_Team

Disband criteria
~~~~~~~~~~~~~~~~

This team will be disbanded after:

#. The majority of the participating projects have completed their policy
   migrations

#. A document is published detailing any pitfalls, lessons learned, and best
   practices that other teams should be aware of

#. A community goal to migrate the remaining projects is proposed and accepted
   by the TC

Process for addition or removal
===============================

Proposed modifications to this document, such as addition or removal of a
popup team, require a formal vote from the Technical Committee membership.

TC members should evaluate if the popup team objective, as described in this
document, appears to be beneficial to the OpenStack project and worth
supporting. The TC's role is not to vet popup teams implementation specs,
which will likely be produced by the team once it is set up. The TC should
err on the side of accepting rather than denying: only vetting teams that
are 100% sure of completing their objective would put too much of an upfront
barrier to entry.

If the popup team is supported and added to this document, the TC is
responsible for seeking a volunteer experienced sponsor to help the new
popup team be successful and act as a liaison with the TC.

Popup teams are removed from this document in three different cases:

* They may become abandoned (for example if nobody volunteers to lead the
  effort).
* The specification work may end up revealing that implementation is too
  complex or makes the objective not desirable.
* The popup team may fulfill its original disband criteria.

None of those outcomes should be seen as a failure. Experimentation and
discussion around a desirable outcome is always good.
