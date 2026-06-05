.. _pti-python:

=================================
Project Testing Interface: Python
=================================

Each project containing Python components must be able to do:

- Unit tests for Python (see below for version details)
- Linter checks
- Testing Coverage Report
- Source Tarball Generation
- Translations import/export and merge for translated projects
- Documentation generation

Specific commands
-----------------

To drive the above tasks, the following commands should be supported in a clean
tree:

``tox -e py3``
    Execute unit tests

``tox -e cover``
    Generate code coverage from tests

``tox -e pep8``
    Execute code style checks

``tox -e docs``
    Generate HTML documentation from the in-tree documentation

``python -m build -s .``
    Execute build process and build an sdist

``python -m build -w .``
    Execute build process and build a wheel

Additional commands may be supported, but are not required:

``tox -e functional``
    Execute functional tests

``tox -e releasenotes``
    Generate HTML release notes

``tox -e api-ref``
    Generate HTML documentation from the in-tree API reference

``pybabel extract``, ``pybabel update``
    Generate and update *Portable Object Template (``.pot``)* files for
    translations.

``tox -e bindep``
    Verify installed system dependencies.

Supported Python versions
-------------------------

The Python 3 version may change from cycle to cycle. Projects should
target the following, extending supported Python 3.x with the
:ref:`tested Python 3 runtimes <pti-tested-runtimes>` for the current
development cycle.

Projects should avoid removing Python versions that have not reached
`End Of Life <https://devguide.python.org/versions/>`_ without a solid
reason. It is recommended to keep compatibility with older Python versions
as long as possible.
While CI coverage of Python versions that are not mentioned in PTI can be reduced,
such reduction is not mandatory.

Dependency Management
---------------------

Each project should list its required dependencies in either
``project.dependencies`` in ``pyproject.toml`` or in a ``requirements.txt``
file, while dependencies for optional features should be defined as `extras`__ in
``project.optional-dependencies`` in ``pyproject.toml``.

Additional non-runtime dependencies required for testing, linting and
documentation should be provided via `dependency groups`__ in
``pyproject.toml`` or in a ``test-requirements.txt`` file and a
``doc/requirements.txt`` file. If using dependency groups, the following
well-known groups should be used:

- ``doc`` (for documentation dependencies)
- ``test`` (for unit test dependencies)
- ``cover`` (for coverage dependencies; this should include the ``test`` group)
- ``lint`` (for linting dependencies)
- ``types`` (for type checking dependencies)

`Environment marker`__ should be used if there are requirements that are
specific to a given Python version, platform (Windows, Linux, ...), or
implementation (CPython, PyPy, ...)

.. __: https://packaging.python.org/en/latest/specifications/dependency-specifiers/#extras
.. __: https://packaging.python.org/en/latest/specifications/dependency-groups/
.. __: https://packaging.python.org/en/latest/specifications/dependency-specifiers/#dependency-specifiers

Constraints
~~~~~~~~~~~

The requirements project maintains a set of constraints with packages pinned
to specific package versions that are known to be working. The goal is to
ease the diagnosis of breakage caused by projects upstream to OpenStack and
to provide a set of packages known to work together.

Projects may opt into using the constraints in one or more of their
standard targets via their ``tox.ini`` configuration.

Non-Python Dependencies
~~~~~~~~~~~~~~~~~~~~~~~

Projects that require non-Python system dependencies, such as databases (for
testing), TeX (for PDF documentation) or compilers, should rely on `bindep`_
and provide a ``bindep.txt`` file to indicate these.

Some basic prerequisites for test running (system packages, database
configuration, custom filesystem types) are acceptable as long as they are
documented in a visible location such as a ``CONTRIBUTING.rst``,
``TESTING.rst``, or ``README.rst`` file in the root of the repository.

.. _bindep: https://docs.opendev.org/opendev/bindep/latest/

Build and Install
-----------------

All OpenStack projects use `pbr`_ for consistent operation of `setuptools`_.
To accomplish this, all ``setup.py`` files only contain a simple setup function
that enabled *pbr*. Actual project configuration is then handled in
``pyproject.toml`` or ``setup.cfg``. This allows project to be built using
standard build frontends like `build`_.

To support sensible testing across multiple Python versions, we use `tox`_
config files in the projects.

.. _pbr: https://docs.openstack.org/pbr/latest/
.. _setuptools: https://setuptools.pypa.io/en/latest/
.. _build: https://build.pypa.io/en/stable/
.. _tox: https://tox.wiki/en/latest/

Tests
-----

OpenStack uses `stestr`_ as its test runner. *stestr* should be used for
running all Python tests, including unit, functional, and integration tests.
*stestr* is used because of its real time subunit output and its support for
parallel execution of tests. In addition, *stestr* only runs tests conforming
to the Python stdlib unittest model (and extensions on it like `testtools`_).
This enables people to use any test runner they prefer locally. Other popular
test runners often include a testing ecosystem which is tied directly to the
runner. Using these precludes the use of alternative runners for other users.

To have a consistent interface via tox between projects' unit test jobs the
command for running *stestr* in ``tox.ini`` should be set like so:

.. code-block:: ini

    [testenv]
    commands =
        stestr run {posargs}

.. note::

    While the use of wrapper scripts can sometimes be useful as a short term
    crutch to work around a specific temporary issues, it should be avoided
    because it creates a divergent experience between projects, and can mask
    real issues.

If there are additional mandatory arguments needed for running a test suite
they can be added before the positional arguments, ensuring the end user
experience remains the same. For example:

.. code-block:: shell

    [testenv]
    commands =
        stestr --test-path ./tests/unit run {posargs}

However, these arguments should try to be minimized because it just adds to the
complexity that people will need to understand when running tests on a project.

.. _stestr: https://stestr.readthedocs.io/
.. _testtools: https://testtools.readthedocs.io/

Coverage Jobs
-------------

For coverage jobs you need to invoke the test runner in the same way as for the
normal unit test jobs, but to switch the Python executable to be
``coverage run``. To do this you need to setup the tox ``cover`` job like:

.. code-block:: ini

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

Generated Files
---------------

``ChangeLog`` and ``AUTHORS`` files are generated at setup.py sdist time. This
is handled by pbr.

``.mailmap`` files should exist where a developer has more than one email
address or identity, and should map to the developer's canonical identity.

Documentation
-------------

Refer to :ref:`pti-documentation`.

Release Notes
-------------

Refer to :ref:`pti-releasenotes`.

Translations
------------

To support translations processing, projects should have a valid `babel`_ config.
There should be a ``locale`` package inside of the top project module, and in that
directory should be the ``$project.pot`` file. For instance, the ``.pot`` file
for nova should be found at ``nova/locale/nova.pot``. Babel commands should be
configured out output their ``.mo`` files in to ``$project/locale`` as well.

.. _babel: https://babel.pocoo.org/en/latest/
