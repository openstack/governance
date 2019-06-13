.. _pti-javascript:

=====================================
Project Testing Interface: JavaScript
=====================================

This document outlines common ways to meet the Project Testing Interface
requirements for JavaScript. Each JavaScript project must be able to do:

- Codestyle checks.
- Execute Tests and Code Coverage
- Package Tarball Generation
- Documentation Generation
- Validate dependency licenses

Projects which are browser based must also be able to do:

- Unit tests in Firefox and Chromium.

Projects which are server based must also be able to do:

- Unit tests in Node.js.

Projects which require translation must also be able to do:

- Translation import/export and merge for translated objects.

Specific commands
-----------------

The following commands must be supported at the root of a clean tree, in
order to initialize your project.

``npm install``
    This command installs all of the project's dependencies.

To drive the above required steps, the following commands should be
supported at the root of an initialized tree.

``npm test``
    This command executes all available test suites, and generate
    appropriate code coverage reports.
``npm run lint``
    This command performs codestyle checks against the project.
``npm pack``
    This command generates a release tarball.
``npm publish <tarball>--no-scripts``
    This command will publish a release tarball to npm. It may not be
    necessary for all projects.
``npm run document``
    This command builds documentation for the project.

The following commands are still under discussion:

``npm run license``
    This command ensures that no incompatible licenses have accidentally been
    included.
``npm run translate``
    This command imports translations into this project, if necessary.


Project Setup
-------------

Node.js and npm version
=======================
We support versions of Node.js and npm available in the from nodesource.com
debian archive for our LTS versions of Ubuntu.

npm scripts
===========
All JavaScript specific testing tools are invoked via `NPM package scripts`_.
These are useful because they provide a 'virtual' runtime environment
whose dependencies are contained entirely in the project directory. They also
allow us to create a consistent interface between the commands that are
invoked by our build, and the tools required by the project.

Requirements Listing
====================
Each project should list its runtime, peer, and development dependencies
in package.json and (if applicable) bower.json.

``dependencies``
    Packages required by your project to run in production. These should
    never use fuzzy version matching.
``devDependencies``
    Packages that are required by your project during the test and build
    phase. These should never use fuzzy version matching.
``peerDependencies``
    Packages that are used to run your project, but whose version does not
    strictly matter. For example, eslint-config-openstack has eslint as a
    peer dependency.

Virtual Environment Management
==============================

To support sensible testing, we use npm's environment management, as it
permits the installation of dependencies by project.

Build Step Details
------------------
The following describes each individual command, what it should do, and its
expected output.

Codestyle Checks
================
:Command: ``npm run lint``

OpenStack requires the custom npm script 'lint' to execute our codestyle
checks. The tool we use is called `ESLint`_, and our rules are published to npm
as eslint-config-openstack_.

Executing Tests and Code Coverage
=================================
:Command: ``npm test``

OpenStack requires a sane testing and code coverage strategy for each
project, though we do not prescribe the tools and coverage threshold, as
these may differ based on circumstance and project type. Generated test
reports should be placed in `./reports` in your projects' root directory.
Generated coverage output should similarly be placed in `./cover`.

Package Tarball Generation
==========================
:Command: ``npm pack``

OpenStack uses ``npm pack`` to generate a release tarball, which will
compile all files listed in `package.json`. If your project requires
concatenation, minification, or any other preprocessing to create a valid
tarball, you may use the npm `prepublish` hook to trigger these steps.

All packages should include:

- A README
- A LICENSE file
- All source code

Generate Documentation
======================
:Command: ``npm run document``

In order to reuse existing templates, styles, and tooling, OpenStack uses
Sphinx to generate our JavaScript Project documentation.

In addition to the normal PTI :ref:`pti-documentation` requirements, Javascript
projects are recommended to provide an `npm run document` command for
developer convenience that should:

* Either install any needed distro dependencies from the ``doc`` tag in
  ``bindep.txt`` or emit an error if they are not installed.
* Install Python dependencies for Sphinx from ``doc/requirements.txt``.
* Execute ``sphinx-build-b html doc/source doc/build``

The project infrastructure will not use ``npm`` to build the documentation.
Therefore it is **STRONGLY** discouraged for people to put additional logic
into the `npm run document` command. Additional logic needed around
Sphinx generation should go into Sphinx plugins which should be listed in
``doc/requirements.txt``.

Generate Release Notes
======================
:Command: ``npm run releasenotes``

OpenStack uses `reno <https://docs.openstack.org/reno/latest/>`_ for generating
release notes.

In addition to the normal PTI :ref:`pti-documentation` requirements, Javascript
projects are recommended to provide an `npm run releasenotes` command for
developer convenience that should:

* Either install any needed distro dependencies from the ``releasenotes`` tag
  in ``bindep.txt`` or emit an error if they are not installed.
* Execute: ``sphinx-build -a -E -W -d releasenotes/build/doctrees-b html
  releasenotes/source releasenotes/build/html``

The project infrastructure will not use `npm run releasenotes` to build
the release notes. Therefore it is **STRONGLY** discouraged for people to put
additional logic into the `npm run releasenotes` command. Additional
logic needed should go into reno.

.. _NPM package scripts: https://docs.npmjs.com/misc/scripts
.. _ESLint: http://eslint.org
.. _eslint-config-openstack: https://www.npmjs.com/package/eslint-config-openstack
