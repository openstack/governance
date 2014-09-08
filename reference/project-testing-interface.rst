============================
Consistent Testing Interface
============================

OpenStack has a lot of projects. For each project, the OpenStack Jenkins
needs to be able to perform a lot of tasks. If each project has a slightly
different way to accomplish those tasks, it makes the management of a
consistent testing infrastructure very difficult to deal with. Additionally,
because of the high volume of development changes and testing, the testing
infrastructure has to be able to pre-cache artifacts that are normally fetched
over the internet. To that end, each project should support a consistent
interface for driving tests and other necessary tasks.

End results needed
------------------

Each python project must be able to do:

 - Unit tests for python2.6
 - Unit tests for python2.7
 - Codestyle checks
 - Testing Coverage Report
 - Source Tarball Generation
 - Translations import/export and merge for translated projects
 - Documentation generation

Specific commands
-----------------

To drive the above tasks, the following commands should be supported in a clean tree:

 - tox -epy26
 - tox -epy27
 - tox -epep8
 - tox -ecover
 - tox -evenv python setup.py sdist
 - tox -evenv python setup.py build_sphinx

Projects that are translated should also support:

 - tox -evenv python setup.py extract_messages
 - tox -evenv python setup.py update_catalog

Requirements Listing
--------------------

Each project should list its operations dependencies in requirements.txt
and additional dependencies required for testing in test-requirements.txt.
If there are requirements that are specific to python3 or pypy support,
those may optionally be listed in requirements-py3.txt or
requirements-pypy.txt.

Virtual Environment Management
------------------------------

To support sensible testing across multiple python versions, we use tox
config files in the projects.

unittest running
----------------

OpenStack uses testrepository as its test runner, which supports a number
of things, most importantly to the expanded project is the subunit output
stream collection. This is useful for aggregating and displaying test output.
In support of that, the oslotest library is built on top of testtools,
testscenarios and fixtures.

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
