===================================================
2018-03-01 Extended maintenance for stable branches
===================================================

The OpenStack `stable branch maintenance team`_, among other teams such as
`QA`_, `infra`_, `vulnerability management team (VMT)`_, the `release team`_,
alongside users, operators, vendors and distributions, have talked for years
about extending the life of the stable branches.

There was a cross-project discussion about this during the Newton summit:

https://etherpad.openstack.org/p/stable-branch-eol-policy-newton

And another at the Queens summit:

https://etherpad.openstack.org/p/SYD-forum-upstream-lts-releases

There have been discussions about stable branch end of life, release process,
long-term support releases, etc, at every face-to-face event (PTG, summit)
for years.

This resolution does not intend to cover all of the history, viewpoints,
use cases, caveats, etc - it would never end. The purpose of this resolution
is to summarize and state the stance of the various upstream stable branch
maintainers and related teams (mentioned above) with respect to extended
maintenance windows for stable branches and their end of life process.

The first branch this will apply to is stable/ocata.

End of life
-----------

The stable branches shall remain open to accept fixes as long as reasonably
possible. Codifying when a branch can no longer be maintained is not within
the scope of this resolution, but it typically means no one is maintaining
the branch, it is not tested and fixes cannot merge.

The current end of life process of applying the ``<branch>-eol``
tag and deleting the branch, cleaning up related infra scripts, etc, will
change to not delete the branch. Instead, a ``<branch>-em`` tag will be
applied on the final release indicating the branch is now in
*extended maintenance (EM)* mode.

If at some point fixes cannot land in a given project and there is no
reasonable solution, then the branch will need to be EOL for that project.
Note that it is possible for our CI infrastructure to `function based on EOL
tags`_.

Releases
--------

The upstream stable branch maintenance team shall maintain and release each
branch for typically 18 months, which has been the historical lifespan of a
branch in OpenStack. After that, there will be no releases as a release
would indicate the same level of support from the upstream teams, which may
not be the case. Contributors can continue to push fixes and they can be
merged but they will not be released upstream.

Keep in mind that the overarching goal of this resolution is to provide a
common place (and infrastructure) for deployers, contributors and vendors
to share and get fixes for older branches. It is not to indefinitely extend
the same level of upstream support for all branches for all time.

Support phases
--------------

The traditional `maintenance phases`_ may change as a result of this resolution
but the details are out of scope for this document, and any changes would be
part of the stable branch guidelines documentation.

Note that the traditional **Phase III** for stable branch maintenance may be
dropped since its purpose was mostly to highly restrict applicable fixes to a
branch that will soon be end of life. In other words, teams must take extra
care to not backport regressions to a branch before it is EOL and then
cannot be fixed upstream.

With the removal of EOL after 18 months, the need for Phase III type
restrictions is severely reduced to the point of no longer being necessary.

.. note:: VMT coverage for EM branches would be on a best-effort basis due
          to the confidence of the VMT being able to research a
          vulnerability's presence in very old EM branches or that
          backported security fixes to said branches actually address the
          vulnerability there.

Core teams
----------

The stable branch core teams will remain unchanged between EM and non-EM
branches. If people are doing good work on the EM stable branches, then
they likely should be included in the regular stable branch core team for
the project.

Testing
-------

The EM branches will continue to run the same level of CI testing after
the standard 18 month window, as long as feasible.

Tempest is branchless and has historically dropped support for testing
older branches once they are end of life. This allows Tempest (and devstack)
to drop compatibility code and other technical debt.

Once a branch enters extended maintenance mode, the QA team *may* move
forward with changes that disrupt an old branch if those changes cannot be
easily made another way. This resolution will not attempt to predict or
codify what those types of changes might be, or how maintenance on older
branches can be extended and still run integration tests with Tempest. The
point is the QA team can move forward and not be hindered by the extended
maintenance of the stable branches.

In other words, these older branches might, at some point, just be running
pep8 and unit tests but those are required at a minimum.

Appropriate fixes
-----------------

Backports to these branches must follow the upstream
`stable branch maintenance guide`_. This includes but is not limited to:

* Bug fixes only. Features will not be accepted on stable branches.
* Backports must go in order from the newest branch where the bug exists.
  This means if a bug is to be fixed in Ocata, it must also be fixed first
  in Pike, and Queens before Pike, Rocky before Queens, etc. Fixes cannot
  skip branches lest people would upgrade and be regressed.
* Project teams should not block proposed fixes for a branch based on the
  non-technical merit of the proposed branch.
* Following on the last point, projects teams will not pick and choose EM
  branches. For example, a project shall not say that Ocata and Queens can
  have extended maintenance but Pike will not.

It is worth noting that the stable branch maintenance guide provides
guidelines for appropriate fixes, but each backport should be judged on its
own by the core team based on relative risk versus severity of the bug being
fixed.

.. _stable branch maintenance team: https://governance.openstack.org/tc/reference/projects/stable-branch-maintenance.html
.. _QA: https://governance.openstack.org/tc/reference/projects/quality-assurance.html
.. _infra: https://governance.openstack.org/tc/reference/projects/infrastructure.html
.. _vulnerability management team (VMT): https://docs.openstack.org/project-team-guide/vulnerability-management.html
.. _release team: https://governance.openstack.org/tc/reference/projects/release-management.html
.. _function based on EOL tags: https://review.opendev.org/#/c/520095/
.. _maintenance phases: https://docs.openstack.org/project-team-guide/stable-branches.html#maintenance-phases
.. _stable branch maintenance guide: https://docs.openstack.org/project-team-guide/stable-branches.html#appropriate-fixes
