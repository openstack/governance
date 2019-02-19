=========================
Project Testing Interface
=========================

OpenStack has a lot of projects. For each project, the OpenStack CI system
needs to be able to perform a lot of tasks. If each project has a slightly
different way to accomplish those tasks, it makes the management of a
consistent testing infrastructure very difficult to deal with. Additionally,
because of the high volume of development changes and testing, the testing
infrastructure has to be able to pre-cache artifacts that are normally fetched
over the internet. To that end, each project should support a consistent
interface for driving tests and other necessary tasks.

The following tasks are required for every project. Every project must:

- Execute tests
- Enforce code style
- Generate a code coverage report
- Generate a source tarball
- Generate documentation
- Generate releasenotes

The following are other common tasks, which may not be relevant for every
project:

- Enforce code coverage
- Generate a release artifact
- Publish a release artifact
- Import translation strings
- Export translation strings

Tools and approaches vary by language, please choose which language is
relevant to you.

.. _pti-documentation:

Documentation
-------------

OpenStack has decided to standardize on using Sphinx for project documentation,
regardless of programming language.

.. note:: The use of sphinx for documentation is intended for documentation
          that is not written inside of docstrings or code comments.
          Languages, such as Go, that natively support a system for documenting
          the code through code comments, should use those native systems.
          Sphinx is intended to be used for documentation that is not written
          inline with the code.

To support documentation generation, projects should:

* Have sphinx documentation source in ``doc/source``
* List python dependencies needed for documentation in ``doc/requirements.txt``
* List distro package pre-reqs for dependencies in ``bindep.txt`` using the
  ``doc`` tag.
* Depend on ``openstackdocstheme`` for documentation and configure it to be
  used in ``doc/source/conf.py``.
* Have a ``docs`` environment set up in a ``tox.ini`` file within the
  repository.

Assuming non-Python requirements have been properly installed as
indicated by ``bindep.txt``, the following command should work with no
additional setup and should result in the documentation being emitted
into ``doc/build/html``.

.. code-block:: bash

  tox -e docs

.. note::

   We strongly discourage project teams from adding commands to the
   ``docs`` environment beyond:

   .. code-block:: bash

      sphinx-build -W -b html doc/source doc/build/html

   Additional logic needed around Sphinx generation should go into
   Sphinx plugins.

Language specific instructions supplement these and are in addition to
them.

Release Notes
-------------

OpenStack uses `reno <https://docs.openstack.org/reno/latest/>`_ for generating
release notes regardless of programming language.

To support releasenotes generation, projects should:

* Have releasenotes documentation source in ``releasenotes/``
* Configure ``openstackdocstheme`` to be used in
  ``releasenotes/source/conf.py``.
* Optionally list distro package pre-reqs for dependencies in ``bindep.txt``
  using the ``releasenotes`` tag.

Assuming requirements have been properly installed, the following command
should work with no additional setup and should result in the releasenotes
being emitted into ``releasenotes/build/html``.

.. code-block:: bash

  sphinx-build -a -E -W -d releasenotes/build/doctrees -b html \
      releasenotes/source releasenotes/build/html

Language specific instructions supplement these and are in addition to them.

.. _pti-linux-distros:

Linux Distributions
-------------------

The following free operating systems are representative of platforms regularly
used to deploy OpenStack on:

- `Latest Ubuntu LTS <https://wiki.ubuntu.com/Releases>`_
- `Latest CentOS Major <https://www.centos.org/download/>`_
- `Latest openSUSE Leap <https://software.opensuse.org/>`_

Each project should run some functional tests on these platforms so we make sure
OpenStack works with distros used in production. The scope of these functional tests
are discussed for every project, and may adjust their coverage depending of resources
and support investment.
These tests are run by using existing tooling, which comes with a reasonable
expectation that it's viable on the indicated distributions.

Sometimes, these distributions might not support all dependencies required
by new features in OpenStack. Development of these features should not be
blocked, though it has to be documented in project release notes, and some
tests might have to be skipped on these distributions.

.. toctree::
   :maxdepth: 1
   :glob:

   pti/*

.. _pti-tested-runtimes:

Tested Runtimes
---------------

In order to focus development efforts and prevent breaking changes midway
through a development cycle, the policy for officially tested runtimes is
based on the LTS or stable release of the :ref:`pti-linux-distros` at the start of
the development cycle.

The officially tested runtimes for each cycle can be found here:

.. toctree::
   :maxdepth: 1
   :glob:

   runtimes/*
