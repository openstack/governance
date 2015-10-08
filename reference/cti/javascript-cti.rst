========================================
Consistent Testing Interface: JavaScript
========================================

This document outlines common ways to meet the Consistent Testing Interface
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

  :code:`npm install`
    This command installs all of the project's dependencies.

To drive the above required steps, the following commands should be
supported at the root of an initialized tree.

  :code:`npm test`
    This command executes all available test suites, and generate
    appropriate code coverage reports.
  :code:`npm run lint`
    This command performs codestyle checks against the project.
  :code:`npm pack`
    This command generates a release tarball.
  :code:`npm publish <tarball> --no-scripts`
    This command will publish a release tarball to npm. It may not be
    necessary for all projects.
  :code:`npm run document`
    This command builds documentation for the project.

The following commands are still under discussion:

  :code:`npm run license`
    This command ensures that no incompatible licenses have accidentally been
    included.
  :code:`npm run translate`
    This command imports translations into this project, if necessary.


Project Setup
-------------

node and npm version
====================
We support the current version of node.js and npm available in the LTS
releases of Ubuntu. As of this writing, these are Node v0.10.29 and
npm v1.4.21. While these versions are no longer supported, this restriction is
imposed by our package maintainers.

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

  :code:`dependencies`
    Packages required by your project to run in production. These should
    never use fuzzy version matching.
  :code:`devDependencies`
    Packages that are required by your project during the test and build
    phase. These should never use fuzzy version matching.
  :code:`peerDependencies`
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
:Command: :code:`npm run lint`

OpenStack requires the custom npm script 'lint' to execute our codestyle
checks. The tool we use is called `ESLint`_, and our rules are published to npm
as eslint-config-openstack_.

Executing Tests and Code Coverage
=================================
:Command: :code:`npm test`

OpenStack requires a sane testing and code coverage strategy for each
project, though we do not prescribe the tools and coverage threshold, as
these may differ based on circumstance and project type. Generated test
reports should be placed in :code:`./reports` in your projects' root directory.
Generated coverage output should similarly be placed in :code:`./cover`.

Package Tarball Generation
==========================
:Command: :code:`npm pack`

OpenStack uses :code:`npm pack` to generate a release tarball, which will
compile all files listed in :code:`package.json`. If your project requires
concatenation, minification, or any other preprocessing to create a valid
tarball, you may use the npm :code:`prepublish` hook to trigger these steps.

All packages should include:

 - A README
 - A LICENSE file
 - All source code

Generate Documentation
======================
:Command: :code:`npm run document`

In order to reuse existing templates, styles, and tooling, OpenStack uses
Sphinx to generate our JavaScript Project documentation. All documentation
output should be placed in the :code:`publish-docs` directory.

.. _NPM package scripts: https://docs.npmjs.com/misc/scripts
.. _ESLint: http://eslint.org
.. _eslint-config-openstack: http://git.openstack.org/cgit/openstack/eslint-config-openstack