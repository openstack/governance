=================================
 Add standard SECURITY.rst files
=================================

Description
===========

Official OpenStack deliverable repositories should include discoverable
instructions for reporting vulnerabilities, or a link to a central location
where those instructions can be found.

With the recent increase in international regulations which touch on
vulnerability management, there is a resulting rise in interest from consumers
(operators, distributors and users) in reporting discovered vulnerabilties to
upstream maintainers of open source projects. Similarly, researchers armed with
new LLM technologies are directing agents to find and report vulnerabilities to
projects in bulk.

In order to avoid costly mistakes, OpenStack will improve the discoverability
of its official vulnerability reporting instructions for anyone starting from
Git repositories rather than documentation sites (which are already
well-covered).

Design & Implementation details
===============================

Like other priority documentation specific to our repositories, a
``SECURITY.rst`` file will be added to the top-level directory including
information about reporting and learning about vulnerabilities affecting the
software. For example::

  Security Policy
  ---------------

  See https://security.openstack.org/ for directions on reporting suspected
  security vulnerabilities. There you will also find the list of OpenStack
  Security Advisory publications, along with the community's official
  vulnerability handling processes and secure development guidelines.

If a deliverable repository's documentation is primarily in Markdown format
instead, a similar ``SECURITY.md`` file is an acceptable alternative, or just
``SECURITY`` or ``SECURITY.txt`` for projects documented entirely in plain
text.

While the convention on GitHub is to automatically link files named
``SECURITY.md`` as a "security policy" most OpenStack projects write their
documentation in reStructuredText, so a ``SECURITY.rst`` file is more
consistent with the repository's existing ``CONTRIBUTING.rst``,
``HACKING.rst``, ``README.rst``, and so on. Some projects on GitHub have
already used ``SECURITY.rst`` to this purpose since years (e.g.
``joke2k/django-environ``), and if enough projects follow that convention then
GitHub will eventually update their interface to detect it as well. However,
OpenStack is not developed on GitHub, so we are free to choose the solution
which makes the most sense for us.

Projects which publish Python packages to PyPI should also amend their package
metadata to include a ``Security`` link to ``https://security.openstack.org/``
in the ``project.urls`` table of their ``pyproject.toml`` file or
``metadata.project_urls`` list in their ``setup.cfg`` file. Projects publishing
binary artifacts to other kinds of public repositories should add similar
pointers if possible.

Goal Checklist
==============

Is design finalized?
--------------------

Status: YES

Is implementation finalized?
----------------------------

Status: YES

Is there any dependency or blocker?
-----------------------------------

Status: NO

Completion Date & Criteria
==========================

Completion Date: 2027-07-01

Items to complete:

#. All repositories assigned to the project team include a SECURITY.rst or
   similar file conforming to the goal's expectations, and update any package
   metadata if relevant.

#. Any official cookie-cutter templates for OpenStack include an example
   SECURITY.rst file based on the text provided within this goal, and update
   accompanying example package metadata.

Champion
========

Jeremy Stanley (fungi)

Status & Tracking
=================

:Etherpad: https://etherpad.opendev.org/p/openstack-security-rst-goal-burndown

Gerrit Tracking
---------------

To facilitate tracking, commits related to this goal should use the
gerrit hashtag or topic::

  security-rst
