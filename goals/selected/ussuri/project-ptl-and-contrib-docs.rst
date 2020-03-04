==================================================
Project Specific PTL and Contributor Documentation
==================================================

While there are a lot of similarities between OpenStack projects,
each project also has its own culture and way of doing things.

Some projects have more PTL duties than others or completely
different duties entirely e.g. Release PTL versus Cinder PTL.
Documenting these specific PTL duties outside of `the Becoming
a PTL Guide <https://docs.openstack.org/project-team-guide/ptl.html>`_
is important for smoothing transitions between PTLs from cycle
to cycle or during a cycle when unforeseen circumstances arise.
Having this information documented would also help with
transparency for current contributors working towards the role
themselves because there would be no question about what
the job entails.

Similarly to how PTLs of different projects have different duties,
the projects have different processes. While the general
information to get started as an OpenStack contributor is
provided in a variety of places like `the Contributor
Guide <https://docs.openstack.org/contributors/code-and-documentation/index.html>`_ ,
there are a lot of project specific details that aren't documented.
Does X project require blueprints or are specifications enough?
Does Y project require one or two plus twos to merge? Does Z
project use Launchpad or StoryBoard for their task tracking?
These project specific details should be documented in the
projects' own contributor guides. Having all this information
in a single place will lower the barrier to entry for new
contributors.

Champion
========

Kendall Nelson (diablo_rojo)

Gerrit Topic
============

To facilitate tracking, commits related to this goal should use the
gerrit topic::

  project-ptl-and-contrib-docs

Completion Criteria
===================

#. There exists project specific information about
   contribution to that project in each project's documentation
   in the form of a ``doc/source/contributor/contributing.rst``
   following the template in the cookiecutter repo [3].
#. There exists a PTL specific section in
   ``doc/source/contributor/contributing.rst`` with all extra duties
   they perform beyond the common set enumerated in the
   project team guide in the becoming a PTL section.
#. Each project's ``CONTRIBUTING.rst`` file is updated to the latest
   template from the cookiecutter repo[4], linking to both the
   OpenStack contributor guide and the project's own contribution
   documentation.

References
==========

#. `Becoming a PTL Guide <https://docs.openstack.org/project-team-guide/ptl.html>`_

#. `Contributor  Guide <https://docs.openstack.org/contributors/code-and-documentation/index.html>`_

#. `Cookie Cutter doc/source/contributor/contributing.rst Template <https://opendev.org/openstack/cookiecutter/raw/branch/master/%7b%7bcookiecutter.repo_name%7d%7d/doc/source/contributor/contributing.rst>`_

#. `Cookie Cutter CONTRIBUTING.rst Template <https://opendev.org/openstack/cookiecutter/raw/branch/master/%7b%7bcookiecutter.repo_name%7d%7d/CONTRIBUTING.rst>`_

#. `Nova PTL Guide <https://docs.openstack.org/nova/latest/contributor/ptl-guide.html>`_

Current State / Anticipated Impact
==================================

There are some projects, like Nova's above, that already have some of
the PTL information gathered that would be good to help other
PTLs brainstorm. Though I think a lot of this information will be
quite different from project to project, we can still try to standardize
on format and location across all projects documentation.

Other projects, like Octavia and Swift, already have a lot of project
specific docs for new contributors that could be used to make some
sort of basic outline/standard for other projects to follow.

