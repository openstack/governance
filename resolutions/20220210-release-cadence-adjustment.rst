=====================================
2022-02-10 Release Cadence Adjustment
=====================================

History
-------

OpenStack has historically used a six month release cycle cadence for
the projects which participate in the coordinated release. Further,
upgrades were tested and supported between two adjacent coordinated
releases only, requiring deployers and distributions to either upgrade
every six months to stay current, or perform Fast Forward Upgrades
(FFUs) to move between non-adjacent releases at runtime. The latter is
an activity enabled by testing the individual upgrade steps, and is
not something we test specifically.

Challenges
----------

Some deployers and distributions have indicated that six month
upgrades are difficult, infeasible, or undesirable, especially in
large environments where the process itself takes long enough that
upgrades are constantly occurring. The FFU process can be laborious
and also requires running parts of a release that may have never been
deployed, productized, or tested in a given environment - purely
because each release must be used stepwise during the operation.

A number of opinions have been expressed about changing the release
cycle to either a slower (one year) or much slower (18 month) cadence
to address these concerns. The lack of consensus around what that
slower cadence should be makes it difficult to choose one that will be
beneficial, as one cycle length may cause people on a slower cycle to
need to wait much longer between upgrades. Further, community
involvement in a very long release can be difficult when attrition,
turnover, contract obligations and volunteer realities make slowing
down unpalatable in many cases. The community already struggles to
find candidates for six month (PTL) and one year (TC) duties. Further,
for environments that do need to move quickly, adopt new features and
deploy new technologies, double-digit months between landing a feature
and having it testable and usable in production is too long.

Proposed Solution
-----------------

It is very difficult to settle on any one change to the release
cadence that will address all of the above problems and concerns. As
such, the TC proposes an incremental change in release upgrade
expectations to help improve the slow-moving deployer experience,
without sacrificing the release-early-release-often goal.

The fundamental change comes to the expectation that upgrades are only
supported between adjacent coordinated releases. The TC will designate
major releases in a tick-tock arrangement, such that every other
release will be considered to be a "tick" release. Upgrades will be
supported between tick releases, in addition to between adjacent major
releases (as they are today). Deployments wishing to stay on the
six-month cycle will deploy every tick and tock release as they always
have. Deployments wishing to move to a one year upgrade cycle will
synchronize on a tick release, and then skip the following tock
release, upgrading when the subsequent tick is released.

Our letter-based release naming scheme is about to wrap back around to
A, so the proposal is that the "new A" release be the first one where
we enforce this scheme. Y->A should be a "dress rehearsal" where we
have the jobs enabled to help smoke out any issues, but where hard
guarantees are not yet made.

Occasionally, individual releases are chosen by a large number of
deployers and distributors by chance, which results in a larger than
normal community of maintainers that keep the release "alive" in
extended maintenance for longer. The expectation with this proposal is
that this will amplify that effect by increasing the likelihood that
"tick" releases will be chosen in this way and thus end up with more
focus on those releases for long-term community support.

Details
-------

#. **Testing**: Just as we test and guarantee that upgrades are
   supported between adjacent releases today, we will *also* test and
   guarantee that upgrades between two tick releases are supported.
   Upgrades are tested for most projects today with grenade. A
   skip-level job will be maintained in the grenade repository that
   tests a normal configuration between the last two tick
   releases. The job will be updated on every new tick release, and
   there will always be a regular single-release grenade job testing
   between the previous release and current one, as we have today.
#. **Tock upgrades**: Upgrades from tock to tock will not be tested
   nor required. On a given tock release, the only upgrade path will
   be to the following release (which would be a tick). This is
   unchanged from today.
#. **Intervals**: Upgrades that span more than one tick cycle are not
   tested or required. For example to move from tick A to tick E will
   still require an FFU style arrangement, but where tick C is the
   only intermediate step required.
#. **Deprecations**: Projects currently deprecate features and config
   for at least one cycle before removal. This change affects *when*
   that can happen, so that no required changes occur in a tock
   release which may be skipped. Effectively the same rules that we
   have today (both written and tribally-understood) apply to the new
   arrangement, with the exception that "cycle" refers to a tick-tick
   cycle and not a single pair of adjacent coordinated releases. Since
   the deprecation, waiting, and removal can only happen in tick
   releases, the result is also that the minimum *length* of time that
   things may be deprecated before removal will increase as well.
#. **Support**: We will expect to support both the most recent tick
   release as well as the one prior. During a tock release, that would
   effectively be similar to what we support today, which is 18 months
   of "maintained" releases. See the example sequence below.
#. **Rolling Upgrades**: This scheme does not necessarily dictate that
   live or rolling upgrades need to be supported between tick
   releases. Meaning RPC compatibility between N to N-1 guarantees can
   remain, resulting in deployments that are on a tick-tick release
   schedule requiring some downtime during an upgrade because
   components will be spanning more than two actual releases.
#. **Data migrations**: Part of supporting tick-tick upgrades involves
   keeping a stable (read "compatible" not "unchanging") database
   schema from tick-tick. This includes data migrations which need to
   do work in tick releases, and while they may do work in tock
   releases, the work done in tock releases cannot be
   *mandatory*. This can be solved (as it is today) by requiring
   operators to (force-)complete data migrations on a supported
   release before moving to one that drops compatibility. The
   tick-tock arrangement described in this resolution would require
   attention to those migrations to make sure they happen
   (automatically or manually) on the source tick before upgrading to
   the target tick, for example.

Example sequence
----------------

Assuming that A is the first release of this tick-tock arrangement,
the following examples help demonstrate the support lifecycle
expectation.

======= ==== ========= =======
Release Type Supported EM
A       tick X,Y,Z     W
B       tock Y,Z,A     W,X
C       tick A,B,C     W,X,Y,Z
D       tock A,B,C,D   X,Y,Z
E       tick C,D,E     Y,Z,A,B
F       tock C,D,E,F   Z,A,B
G       tick E,F,G     A,B,C
======= ==== ========= =======

(EM releases are arbitrarily pruned in the above example for brevity,
but no such change in how long they may be supported is made in this
resolution)
