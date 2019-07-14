============================================
 2019-07-11 Mandatory Repository Retirement
============================================

When development ceases on any official OpenStack team deliverable
repository and it is no longer maintained, its contents are replaced
by a clear statement describing this status, all open changes for it
in code review are abandoned with an explanatory message, and access
controls are modified to automatically reject future proposed
changes. This act is known as **repository retirement**.

When a repository which was governed by the OpenStack Technical
Committee ceases to be its responsibility any longer, the
deliverable repository entry in the official `list of projects
<https://opendev.org/openstack/governance/src/branch/master/reference/projects.yaml>`_
is moved to a `legacy projects list
<https://opendev.org/openstack/governance/src/branch/master/reference/legacy.yaml>`_
with its proximate ``retired-on`` date recorded. This act is known
as **governance removal**.

Following conclusion of the *Train* development cycle, any new
**governance removal** for a repository in the `openstack Git namespace
of OpenDev <https://opendev.org/openstack/>`_ must undergo
**repository retirement** even if development will be continuing in
another Git namespace on OpenDev. The OpenStack Technical Committee
may defer this requirement if responsibility over the repository is
being transferred to another official OpenStack governance body with
which it shares the ``openstack`` Git namespace on OpenDev (for
example, a recognized `OpenStack special interest group
<https://governance.openstack.org/sigs/>`_ or `OpenStack User
Committee working group
<https://governance.openstack.org/uc/#working-groups>`_), but can
still enforce it at a later date if the repository moves to a
different OpenDev Git namespace or leaves OpenDev hosting entirely.

Rationale
---------

With the 2019-03-22 resolution to :doc:`Namespace Unofficial
Projects <20190322-namespace-unofficial-projects>`, only currently
or previously-official OpenStack deliverable repositories (or those
managed by SIGs, working groups and other officially-recognized
bodies) remain within the ``openstack`` Git namespace prefix on
OpenDev. Formerly-official software, which left OpenStack governance
with the intent of continuing development outside it, was in many
cases subsequently abandoned in place by its authors. This created
an attractive nuisance and unwitting surprise for source code
consumers who (in at least some cases) likely continued unaware that
it was no longer supported by anyone at all.

When OpenStack ceases development on a source code repository,
OpenDev's recommended `retirement process
<https://docs.openstack.org/infra/manual/drivers.html#retiring-a-project>`_
is followed. This process replaces the repository's source code with
a prominent ``README`` message indicating its new situation, makes
sure open changes for it are abandoned, and sets Gerrit to reject
future change proposals for review. When projects choose to continue
development for formerly-official OpenStack deliverables outside
OpenStack governance, no corresponding process exists to clarify to
users that OpenStack is no longer responsible for these
repositories. This problem is further complicated by OpenDev's use
of Gitea and its automatic redirect feature. Simply renaming those
projects to move them to a new Git prefix namespace leaves their old
``openstack`` URLs working for browsers and Git client operations so
many existing users may never notice the transition.

The solution to this problem is to follow the repository retirement
process in ``openstack`` any time a deliverable repository is
removed from current governance, regardless of whether its authors
intend to continue development on it outside governance. OpenDev
allows multiple repositories to have the same base names across
different namespaces, so this does not mean a project has to change
its new name. It does however mean that the repository must be
forked into the new namespace, leaving behind its Gerrit reviews and
no redirection (the ``README`` file can certainly mention where to
find continued development however). This forces existing consumers
of the source code to take note of the change in governance,
clarifying that no official OpenStack project team is responsible
for it any longer.

Because this is a significant change in policy, it cannot easily be
retroactively applied to old repositories which are no longer under
OpenStack's governance (but the damage this would mitigate for them
is probably already done anyway). To provide ample warning for any
existing projects considering exiting OpenStack in the near future,
only removals after the conclusion of the Train development cycle
will be subject to the new mandatory retirement policy. Removals
prior to the end of the Train cycle can be renamed to new namespaces
in OpenDev (with redirects) per our previous de facto process, if
maintainers prefer.
