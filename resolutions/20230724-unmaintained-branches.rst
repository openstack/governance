=============================================================
 2023-07-24 Unmaintained status replaces Extended Maintenance
=============================================================

.. note::
   This resolution has been amended by
   :doc:`20231114-amend-unmaintained-status`.
   See :ref:`the amendment note<20231114-amend-note>`, below.


Motivation
----------

In "2018-03-01 Extended maintenance for stable branches"[0] the OpenStack
Technical Committee specified a new process for transitioning branches to
end-of-life, allowing for a phase called extended maintenance where these
branches are still open to receive backports, but without receiving
official releases.

Recent discussions in the mailing list[1], forum[2], and in TC meetings
highlighted that:

- The reality of most current EM branches is that they are generally not
  maintained and may not receive security or bug fixes, or are in
  a state of not being able to merge those fixes if proposed.
- There is a false expectation from users and operators that these branches
  are in a state of maintenance from the project team and receiving the above.
- Project teams have felt a responsibility themselves to attempt to maintain
  these branches due to the above expectation, in the absence of external
  actors (operators, users, vendors, etc.)
- These branches are taking attention and resources away from maintained
  branches and new development.
- There are no clear processes for transitioning a branch from EM to EOL, and
  due to the process being manual, the interdependencies in testing between
  projects, and the burden and goodwill required to transition a project from
  EM to EOL, only 3 branches have done so in the 5 years since the introduction
  of the policy.
- There are currently 7 extended maintenance branches and this is starting
  to also affect the good operation of the QA infrastructure.

Goals
-----

This resolution acknowledges that

- We need better communication with regard to the status of these branches,
  specifically, that it is not (and has not been) the responsibility of the
  project's core team to maintain them. In other words, it is not the
  responsibility of each project's core team to review, approve, or merge
  changes, or to keep the CI gates running on these branches.
- There is still value and desire in creating a space for collaboration to
  backport fixes beyond just the officially maintained releases.
- There is a need for a clear step-by-step process when transitioning a branch
  through these phases.

This resolution therefore attempts to preserve the ability for backports to be
proposed and merged to unmaintained branches, while improving communication
around the responsibilities and defining clearer processes.

Unmaintained branches
---------------------

- The phase of Extended Maintenance for a branch is renamed to Unmaintained.
- Only SLURP releases are eligible for having an Unmaintained branch.
- After a branch is no longer officially maintained, the branch is deleted and
  a new branch is created under unmaintained/<branch_name>, for example,
  unmaintained/train.

  .. _20231114-amend-note:
- A group in Gerrit called "<project>-unmaintained-core", for example,
  "keystone-unmaintained-core", will have +2/+W on these branches. This group
  may be bootstrapped with or include the "<project>-stable-maint" group, but
  membership is separate from that group.

  .. note::
     The above point has been amended by a subsequent resolution.
     See :doc:`20231114-amend-unmaintained-status` for details.
- The PTL, or a new Unmaintained branch liaison assigned by the PTL, makes
  group membership decisions for "<project>-unmaintained-core".
- No SLURP branches may be skipped between the oldest unmaintained branch
  and the current maintained releases. This makes sure operators have an
  upgrade path from one SLURP to the next all the way to maintained releases.
- By default, only the latest eligible Unmaintained branch is kept. When a new
  branch is eligible, the Unmaintained branch liaison must opt-in to keep all
  previous branches active.
- The PTL or Unmaintained branch liaison are allowed to delete an Unmaintained
  branch early, before its scheduled branch deletion.
- The CI for all branches must be in good standing at the time of opt-in.
  At a minimum this needs to contain all integrated jobs, unit tests, pep8,
  and functional testing.
  However, as this is a best-effort CI and to preserve resources, Unmaintained
  branches will include periodic jobs of no higher than monthly frequency.
- The TC will maintain and document the full steps and guidelines for
  transitioning from maintained to unmaintained, and for the eventual branch
  deletion.

Transition
----------

The current Extended Maintenance branches are not SLURP releases and wouldn't
be eligible for Unmaintained branches with the guidelines above.
The first SLURP release is 2023.1.

- Until the first SLURP release ends its maintained phase, all current branches
  are eligible for Unmaintained.
- The last 3 active Extended Maintenance branches are automatically
  transitioned to Unmaintained branches.
- The unmaintained branch liaison needs to opt-in to keep more than 3 branches
  (instead of 1 for SLURP) and the guidelines for opt-in described above apply.

| [0]. https://governance.openstack.org/tc/resolutions/20180301-stable-branch-eol.html
| [1]. https://lists.openstack.org/pipermail/openstack-discuss/2023-June/033980.html
| [2]. https://etherpad.opendev.org/p/vancouver-2023-em
