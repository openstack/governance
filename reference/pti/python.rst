.. _pti-python:

=================================
Project Testing Interface: Python
=================================

Each python project must be able to do:

- Unit tests for python (see below for version details)
- Codestyle checks
- Testing Coverage Report
- Source Tarball Generation
- Translations import/export and merge for translated projects
- Documentation generation

Specific commands
-----------------

To drive the above tasks, the following commands should be supported in a clean
tree:

- ``tox -e pep8``
- ``tox -e cover``
- ``python setup.py sdist``
- ``python setup.py bdist_wheel``
- ``sphinx-build -W -b html doc/source doc/build``

The Python 3 version may change from cycle to cycle. Projects should
target the following, replacing `3x` with the :ref:`tested Python 3 runtimes
<pti-tested-runtimes>` for the current development cycle:

- ``tox -e py3x``

Projects that are translated should also support:

- ``tox -e venv python setup.py extract_messages``
- ``tox -e venv python setup.py update_catalog``

Some basic prerequisites for test running (system packages, database
configuration, custom filesystem types) are acceptable as long as they are
documented in a visible location such as a CONTRIBUTING, TESTING, or README
file in the root of the repository.

Requirements Listing
--------------------

Each project should list its operations dependencies in requirements.txt
and additional dependencies required for testing in test-requirements.txt.
If there are requirements that are specific to python3 or pypy support,
those may be listed in requirements.txt or test-requirements.txt using
environment markers.

Constraints
===========

The requirements project maintains a set of constraints with packages pinned
to specific package versions that are known to be working. The goal is to
ease the diagnosis of breakage caused by projects upstream to OpenStack and
to provide a set of packages known to work together.

Projects may opt into using the constraints in one or more of their
standard targets via their tox.ini configuration.

Virtual Environment Management
------------------------------

To support sensible testing across multiple python versions, we use tox
config files in the projects.

Python test running
-------------------

OpenStack uses stestr as its test runner. stestr should be used for running
all python tests, this includes unit tests, functional tests, and integration
tests. stestr is used because of its real time subunit output and its support
for parallel execution of tests. In addition, stestr only runs tests conforming
to the python stdlib unittest model (and extensions on it like testtools). This
enables people to use any test runner they prefer locally. Other popular test
runners often include a testing ecosystem which is tied directly to the runner.
Using these precludes the use of alternative runners for other users.

To have a consistent interface via tox between projects' unit test
jobs the command for running stestr in tox should be set to::

    stestr run {posargs}

.. note::
    While the use of wrapper scripts can sometimes be useful as a short term
    crutch to work around a specific temporary issues, it should be avoided
    because it creates a divergent experience between projects, and can mask
    real issues.

If there are additional mandatory args needed for running a test suite they
can be added before the posargs. (this way the end user experience is the same)
For example::

    stestr --test-path ./tests/unit run {posargs}

However, these arguments should try to be minimized because it just adds to the
complexity that people will need to understand when running tests on a project.

Coverage Jobs
-------------

For coverage jobs you need to invoke the test runner in the same way as for the
normal unit test jobs, but to switch the python executable to be
``coverage run``. To do this you need to setup the tox ``cover`` job like::

  [testenv:cover]
  setenv =
      PYTHON=coverage run --source $project --parallel-mode
  commands =
      stestr run {posargs}
      coverage combine
      coverage html -d cover
      coverage xml -o cover/coverage.xml

Specifically, the output html directory ``cover`` and the ``coverage.xml`` file
added to that directory are mandatory output artifacts.


Project Configuration
---------------------

All OpenStack projects use `pbr` for consistent operation of setuptools.
To accomplish this, all setup.py files only contain a simple setup function
that setup_requires on an unversioned pbr, and a directive to pass processing
to the pbr library. Actual project configuration is then handled in setup.cfg.

Generated Files
---------------

ChangeLog and AUTHORS files are generated at setup.py sdist time. This is
handled by pbr.

.mailmap files should exist where a developer has more than one email address
or identity, and should map to the developer's canonical identity.

Translations
------------

To support translations processing, projects should have a valid babel config.
There should be a locale package inside of the top project module, and in that
dir should be the $project.pot file. For instance, for nova, there should be
nova/locale/nova.pot. Babel commands should be configured out output their .mo
files in to $project/locale as well.

Release Notes
-------------

As a convenience for developers, it is recommended that projects provide
a ``releasenotes`` environment for tox that will run

.. code-block:: bash

  sphinx-build -a -E -W -d releasenotes/build/doctrees -b html \
      releasenotes/source releasenotes/build/html

The project infrastructure will not use ``tox -e releasenotes`` to build the
documentation. Therefore it is **STRONGLY** discouraged for people to put
additional logic into the command section of that tox environment. Additional
logic needed around releasenotes generation should go into reno.
