============================
Consistent Testing Interface
============================

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

The following are other common tasks, which may not be relevant for every
project:

- Enforce code coverage
- Generate a release artifact
- Publish a release artifact
- Import translation strings
- Export translation strings

Tools and approaches vary by language, please choose which language is
relevant to you.

.. toctree::
   :maxdepth: 1
   :glob:

   cti/*
