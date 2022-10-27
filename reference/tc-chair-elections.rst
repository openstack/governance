=========================
TC Chair Election Process
=========================

As mentioned in `TC charter <https://governance.openstack.org/tc/reference/charter.html#tc-chair>`_,
in case of multiple candidates for TC chair, we need to conduct the election.
This document defines the process and timeline for the TC Chair election.

TC Chair Nomination
===================

* TC chair nomination will be open for three business days after the TC
  elections are closed.

* Each candidate will propose a gerrit change to add their nomination as
  a text file (with name <email_address>.txt) containing the candidate
  statement to the ``openstack/governance/reference/tc-chair-candidates/<cycle>/``
  repository.

* Current TC chair will merge the nominations by confirming that they are from
  the elected TC members.

TC Chair Election
=================

* In case of single nomination, no election is needed and candidate can propose
  a patch to the member list to add "chair" status next to their name and use
  `election-results` as gerrit topic name.

* If there are multiple nominations, select a TC member who is not running for
  the TC chair to establish a CIVS poll to choose the single winner.

* All the elected TC members including the TC chair candidates will be the
  electorates for chair election.

* Election poll will be open for seven days or until all the TC members have
  voted.

* Winner will propose a patch to the member list to add "chair" status next to
  their name and use `election-results` as gerrit topic name.
