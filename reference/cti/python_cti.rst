.. _cti-python:

====================================
Consistent Testing Interface: Python
====================================

Each python project must be able to do:

 - Unit tests for python2.7
 - Codestyle checks
 - Testing Coverage Report
 - Source Tarball Generation
 - Translations import/export and merge for translated projects
 - Documentation generation

Projects which are compatible with Python 3 must also be able to do:

 - Unit tests for python3.5

Specific commands
-----------------

To drive the above tasks, the following commands should be supported in a clean tree:

 - tox -epy27
 - tox -epep8
 - tox -ecover
 - tox -evenv python setup.py sdist
 - tox -evenv python setup.py build_sphinx

Projects that are translated should also support:

 - tox -evenv python setup.py extract_messages
 - tox -evenv python setup.py update_catalog

Projects which are compatible with Python 3 must also be able to do:

 - tox -epy35

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
environment makers.

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

unittest running
----------------

OpenStack uses testrepository and stestr as its test runner, which supports a
number of things, most importantly to the expanded project is the subunit output
stream collection. This is useful for aggregating and displaying test output.
In support of that, the oslotest library is built on top of testtools,
testscenarios and fixtures. The usage of the testrepository project is
deprecated and things are being migrated to stestr which is an active and
currently maintained fork of testrepository.


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

Documentation
-------------

Developer docs are generated from Sphinx sources in the tree. Additionally,
there are end user docs and API docs which are maintained outside of the
context of a project's repo. To support documentation generation, projects
should have sphinx documentation source in doc/source and build_sphinx should
output the documentation to doc/build.
