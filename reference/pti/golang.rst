.. _pti-golang:

=============================
Project Testing Interface: Go
=============================

Go language (golang) repositories shall use the following interface
for testing and automation purposes.  This includes both pure golang
repos and mixed-language repos as some of the OpenStack tooling defined
for Python repos is re-used here.

A major criteria here is to not create an environment that is totally
foreign to what developers are accustomed to in their respective
communities.  Remember these are first OpenStack projects
and they follow OpenStack processes where feasible.

Each golang project must be able to do:

- Dependency installation
- Code style checks
- Unit tests
- Functional tests
- Test Coverage Report
- Documentation generation
- Translations import/export and merge for translated projects

There is not yet a consensus among the to golang community for build
and package management tools as the ``go`` tool itself was intended to
be sufficient. The traditional ``make(1)`` command is often used to
supplement this role and provide the sort of interface that is common
in many languages.

OpenStack has adopted the practice of using ``make`` for golang CTI as
it provides a similar role fulfilled by ``tox`` in Python projects.  It
is also possible (and highly recommended) to use make to proxy tox or
tox to proxy make in a mixed-language repo.  Both tools use files that
should remain transparent enough to most developers to understand what
operations are actually being performed.

Specific commands
-----------------

To drive the above tasks, the following commands should be supported in
a clean tree:

``make depend``
    Install dependencies required to build the project

``make build``
    Execute build process

``make install``
    Execute binary install

``make test``
    Execute tests

``make fmt``
    Execute code style checks

``make docs``
    Generate HTML documentation from the in-tree developer docs

``make godoc``
    Generate the golang docs from the source

``make releasenotes``
    Generate HTML release notes

Additional commands may be supported, but are not required:

``make cover``
    Generate coverage reports

``make lint``
    Execute more code style checks

``make translation``
    Perform translation-related tasks (TBD)

Project Setup
-------------

Project repos shall use a structure that is a hybrid of the typical OpenStack
structure and those commonly found in the golang community.  Because
these are OpenStack projects, the top-level structure shall contain
the existing process-related components.  All golang source code and modules
shall be in one or more subdirectories named in a manner to identify its
contents distinctly from the Python namespace directories currently used.
This allows the golang code to maintain its native style and not be
mixed in with the OpenStack tool-related pieces such as Sphinx documentation
and Reno release notes.

The source subdirectory naming is intentionally flexible in order to
accommodate unforeseen situations, however the following guidelines should
be strongly considered:

- Simple projects or projects that only need one golang workspace can use
  a single top-level directory named ``go``.

- Projects that may have multiple distinct golang workspaces should use
  names that include a ``-go`` suffix.  This allows similarly named modules
  in multiple languages to co-exist. For example: the CloudTool project
  should continue to put Python sources in its Python namespace ``cloudtool``
  and the golang source in ``cloudtool-go`` (do not use a period!).

Dependency Management
---------------------

OpenStack has chosen to use Glide_ as the common dependency management tool
for golang.  The ``depend`` target provides a common interface to Glide's
``install`` command.

``make depend``
   Install dependencies required to build the project

Golang dependencies shall not be vendored in golang repos. Each project shall
include a list of its dependencies and acceptable/tested versions in the repo.
The required dependencies shall be installed into a golang workspace compatible
with the results of running ``go get``.

Dependencies are specified in golang via full paths of the form
``opendev.org/openstack/golang-client``.  All dependencies that are OpenStack
projects will be required to use the ``opendev.org`` host to minimize
unnecessary mirrors.

To support OpenStack CI and to ensure the Depends-On footers work properly,
this target must not modify existing git repo state for a given dependency
if the git repository is already present in ``${GOPATH}/src/${repo}``. The
CI system will pre-populate all necessary git repos that it knows about into
the appropriate locations in the appropriate states.

External dependencies outside of the OpenStack CI should be installed as
usual.  It is expected that a mirror of required dependencies will be
maintained in the CI system.

Further details will be included here as the dependency tooling is finalized.

.. _Glide: https://glide.sh/

Build and Install
-----------------

The golang toolchain automatically performs the build step when required by
other operations such as ``go test``.  Build and install are split out here
as they are common operations and useful in their own right.  These targets
are not strictly necessary for CI testing.

``make build``
    Execute build process

``make install``
    Execute binary install

Codestyle Checks
----------------

OpenStack uses ``gofmt`` directly to check for proper coding style.
As we do not want to be making changes to the repo in CI the default
target shall not use ``go fmt`` which rewrites source files by default.
As a developer convenience a second target called ``fmtfix`` shall be
defined that does the source fixups (equivalent to ``gofmt -l -w``).

``make fmt``
    Run the gofmt tool non-destructively to validate code formatting

``make fmtfix``
    Run the gofmt tool and overwrite source files with gofmt's version
    if changes are required.  This is primarily a developer convenience.

Tests
-----

OpenStack uses ``go test`` to run all test types at once invoked via
the ``Makefile``.

``make test``
    Run tests

This is the general test target and may simply call some subset of additional
``test-*`` targets.  Specific test targets should be named with a ``test-*``
prefix as a convention.

Go test output is not natively in a format consumable by subunit, however
there is at least one tool available that can easily be made to support
subunit.

Generated Files
---------------

ChangeLog and AUTHORS files are generated at <TBD>.

``.mailmap`` files should exist where a developer has more than one email
address or identity, and should map to the developer's canonical identity.

Documentation
-------------

Narrative Documentation
~~~~~~~~~~~~~~~~~~~~~~~

In order to reuse existing templates, styles, and tooling, OpenStack uses
Sphinx to generate our Narrative Project documentation.

In addition to the normal PTI :ref:`pti-documentation` requirements, for
developer convenience, Go projects are recommended to provide:

``make docs``
    Generate HTML documentation from the in-tree developer docs

that should:

* Either install any needed distro dependencies from the ``doc`` tag in
  ``bindep.txt`` or emit an error if they are not installed.
* Install Python dependencies for Sphinx from ``doc/requirements.txt``.
* Execute ``sphinx-build -W -b html doc/source doc/build``

Source
~~~~~~

Go has a well-defined documentation tool `godoc`_ that produces
developer documentation extracted from source code comments, similar to
Python's Docstring.

``make godoc``
    Generate the golang docs from the source

.. TBD(dtroyer): define how the godoc output is integrated with the current
.. sphinx process

.. _godoc: https://blog.golang.org/godoc-documenting-go-code

Release notes
~~~~~~~~~~~~~

OpenStack uses Reno to manage release notes.  This uses Sphinx to generate
the final HTML documentation.

In addition to the normal PTI :ref:`pti-documentation` requirements, for
developer convenience, Go projects are recommended to provide:

``make releasenotes``
    Generate HTML release notes

Translations
------------

A common translation process is not yet well-defined in the golang community.
This section will be completed once a process is developed that is compatible
with the existing OpenStack translation workflow.

Build Tools
-----------

A number of the tools used by OpenStack projects are written in Python and
require local developer installation.  This is something that tox is very good
at and shall be used to manage those tools in its local virtual environments.

These tools should all be Python 3 compatible so non-Python projects should use
only Python 3 in their local virtual environments for tooling support.
