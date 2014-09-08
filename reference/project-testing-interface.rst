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

Each project should list its operations dependencies in tools/pip-requires
and additional dependencies required for testing in tools/test-requires.

Virtual Environment Management
------------------------------

To support sensible testing across multiple python versions, we've use tox
config files in the projects with the hope that eventually we can remove having
install_venv.py copied in to each of the projects.

unittest running
----------------

Nova uses a specialized test runner, which is a subclass of nose. Most of the
functionality of this has been extracted in to openstack.nose_plugin. There are
still a few test failures currently when running nova unittests directly under
nose, but once those are solved, the projects should really all have a config
for openstack.nose_plugin and then support running nose directly with no
special setup ... this will help in writing code to exploit the features of
nose.

Helper Scripts
--------------

The projects up until now have all had a run_tests.sh and a with_venv.sh
script. run_tests.sh should be able to be easily re-written to pass things
along to the above tox commands. with_venv.sh is also easy - the tox venv
environment (tox -evenv) is available to run arbitrary commands in the context
of a tox virtualenv.

Generated Files
---------------

ChangeLog and AUTHORS files should be generated at setup.py sdist time. Code
exists in oslo in the setup module to support that.

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
