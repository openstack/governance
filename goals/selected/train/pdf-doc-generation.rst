=========================================================
Enabling PDF generation support for project documentation
=========================================================

During the Ocata cycle, the OpenStack-manuals, infra, and translations
team worked together to enable the generation of PDF doc files from
rst-based guide documents. This change generated a single downloadable
PDF per Sphinx project. This means that each "book" built from a single Sphinx
project could generate a PDF, allowing users who want to see documents offline
the ability to do so.

The work was completed at the end of the Ocata release, but was never
implemented within the project repositories. This means that our users
are only able to download PDF documents for the Installation Guide, the
Contributor Guide, and the Image Guide, limiting the scope for our
offline users.

This goal proposes we enable support across the project repositories
to further our goal of being an accessible open source community.

.. note::

   With regards to ensuring the information is up-to-date, doc patches will
   continue to be implemented as per usual in the project repositories.
   It is important to note that the generation of these guides is to be
   the responsibility of the user to ensure the content they are reading
   is relevant to their deployment.

* `Storyboard stories <https://storyboard.openstack.org/#!/story/list?tags=pdf-doc-enabled>`__
* `Storyboard dashboard <https://storyboard.openstack.org/#!/board/175>`__

Champion
========

Alexandra Settle (asettle) - SUSE

Gerrit Topic
============

To facilitate tracking, commits related to this goal should use the
gerrit topic::

  pdf-doc-enabled

Completion Criteria
===================

The completion criteria for this goal is as follows:

#. Each team needs to ensure they can build PDFs and that the PDFs look
   respectable and readable. This definition is dependent per-project and
   should be explored at the discretion of the project team.

#. Each team needs to define a new tox env to enable the PDF build.

#. It is possible to run Sphinx using the configuration in `doc/source` and generate a
   single PDF file containing all of the documentation in that directory.

   .. note::

      Publishing multiple PDFs not part of this goal, and should be deferred until
      after this goal is complete.

#. Each guide generated includes the release version to ensure the user is fully aware of the
   content they have built. It would also be helpful to add a disclaimer that this
   information is updated regularly in the project repositories and to check for
   updates during maintenance periods.

References
==========

The OpenStack-manuals project has already enabled support for PDF generation.
The specification is viewable `here <https://specs.openstack.org/openstack/docs-specs/specs/ocata/build-pdf-from-rst-guides.html>`_.

This work was proposed earlier, but never went further than
a draft specification for docs-specs. Ian Choi proposed
`PDFs for project-specific docs with unified doc builds <https://review.openstack.org/#/c/509297/>`_
in October of 2017.

Discussion did happen on the `mailing list <http://lists.openstack.org/pipermail/openstack-dev/2017-October/123076.html>`_
but did not go much further, but there has been interest for some time.

Current State / Anticipated Impact
==================================

The above resources provide an overview of the work that was started, but
never completed. At this point in time, I see this as a necessary final
task to ensure our documentation is as accessible as it can be for all users.
