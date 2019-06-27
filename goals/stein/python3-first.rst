.. -*- encoding: utf-8 -*-

===============================
 Run under Python 3 by default
===============================

As we agreed in the :ref:`python2-deprecation-timeline` resolution,
the next phase of our adoption of python 3 is to begin running all
jobs using python 3 by default, and only using python 2 to test
operating under python 2 (via unit, functional, or integration
tests). This goal describes the activities needed to move us to this
"python 3 first" state.

* `Storyboard stories <https://storyboard.openstack.org/#!/search?tags=goal-python3-first>`__
* `Storyboard dashboard <https://storyboard.openstack.org/#!/board/104>`__

Champions
=========

* Doug Hellmann (doug@doughellmann.com)
* Nguyễn Trí Hải (nguyentrihai93@gmail.com)
* Ma Lei (ma.lei@99cloud.net)
* Huang Zhiping (huang.zhiping@99cloud.net)

Gerrit Topic
============

`python3-first <https://review.opendev.org/#/q/topic:python3-first+(status:open+OR+status:merged)>`__

Completion Criteria
===================

1. The Zuul settings to attach jobs have been moved from the
   ``openstack-infra/project-config`` repository into each project
   repository.
2. Documentation build and publish jobs use python 3.
3. Release notes build and publish jobs use python 3.
4. Source code linter jobs (pep8, pylint, bandit, etc.) should use
   python 3.
5. Release artifact build and publish jobs use python 3 and publish to
   PyPI.
6. There are functional test jobs running under python 3.
7. The wiki tracking page is up to date for the project.
8. Projects are running python 3.6 unit test jobs.

The goal champions will start by preparing the patches for steps
1-5. That will give project teams more time to focus on steps 6-8,
which will need the expertise of someone on the team. Project teams
should be prepared to review the changes quickly, and assist if there
are any questions about jobs with branch-specifiers (see below). Step
7, updating the wiki tracking page, is the responsibility of the
project team. Steps 6 and 8 involve adding more test jobs and may also
require code changes or tox settings updates, so those will be left to
the project team as well.

Details
=======

Moving settings from project-config
-----------------------------------

A big part of the work for this goal for each project is to configure
different sets of jobs to run the same tasks differently on different
branches. Although Zuul supports doing this using branch specifiers,
it will be easier to maintain the job settings over time if we place
them in each repository. This lets us set different jobs, or variants
of jobs, to run against each branch just by modifying the Zuul
settings in that branch.

The first step, therefore, is to take the project settings that
control the branch-aware jobs out of the
``openstack-infra/project-config`` repository and put them into each
git repository in the appropriate branch.

https://review.opendev.org/580736/ is an example of adding the
project settings to the master branch of ``openstack/whereto``. The
patch was constructed by using the ``python3-first`` command from the
``openstack/goal-tools`` repository (see the ``README.rst`` there for
directions).

.. note::

   Not all of the job settings should be moved into the project tree:

   1. The line applying the ``translation-jobs`` project template (or
      any of its branch-specific variants) should stay in
      ``openstack-infra/project-config``.

   2. Settings for jobs that should only ever run on the ``master``
      branch should stay in ``openstack-infra/project-config``.

   3. Any project templates that are not "branch-aware" (because they
      run based on a tag event) need to remain configured in
      ``zuul.d/projects.yaml`` in ``openstack-infra/project-config``.

Each repository needs a patch like 574393 on the master branch.  The
settings can go into any of the Zuul configuration files
(``.zuul.yaml``, ``zuul.yaml``, ``.zuul.d/project.yaml``, etc.) and
should be organized based on the way the project team has their Zuul
configuration set up already.

Similar patches should then be created for the ``stable/rocky``,
``stable/queens``, ``stable/pike``, and ``stable/ocata`` branches.
Sometimes it will be possible to just backport the change from the
master branch, but many projects have jobs configured with branch
specifiers to control which branches run the tests. We do not want to
mix branch specifiers with branch-specific configuration, so the
settings will need to be modified or removed. This may mean that the
versions of the change on stable branches are different from the
version on master. The ``python3-first jobs extract`` command in the
``goal-tools`` repository should correctly compute the set of jobs to
move into each branch.

After all of the settings are in place within the branches of a
repository, they can be removed from ``openstack-infra/project-config``.
https://review.opendev.org/580737/ shows how to remove the settings
for whereto.

.. note::

   Due to the large number of changes involved, we want to update the
   ``openstack-infra/project-config`` repository with 1 patch per
   project team. That patch **must not** be approved before all of the
   settings are added to each repository in all of the relevant
   branches. Normally we would manage that requirement using
   ``Depends-On`` to link the patches together, but for some teams
   that will produce a very very long list of inter-patch dependencies
   (Oslo would take 128 patches). Rather than listing them all as
   dependencies, therefore, we will wait to submit the update to
   project-config until *after* all of the changes to the project
   repositories have been approved.

At this point, most of the job configuration for each repository can
be managed directly by the project team, and each branch will have a
separate list of jobs. This will make future job management much
simpler and should make it possible for the project team to do the
rest of the work for the goal without waiting for anyone else to
review their patches.

Documentation Jobs
------------------

The ``publish-openstack-docs-pti`` project template defines a set of
jobs for testing and building documentation using tox as a wrapper
around Sphinx, and replaces the old ``publish-openstack-sphinx-docs``
project template. The new jobs use a ``docs`` tox environment, defined
in each repository, so the tox settings can be used to provide a
self-testing patch to the repository to switch the version of python
used.

https://review.opendev.org/580738 shows how to change the
project settings for a repository to use the new documentation
jobs. The change will be self-testing, and should only be made on the
master branch.

https://review.opendev.org/572895 shows how to update the
tox.ini settings in the project to set the ``basepython`` variable for
the ``docs`` environment, used for developer testing. This change
should only be made on the master branch.

Common issues to anticipate:

* Under python 3 the output of subprocess.check_output() is a bytes
  instance, but sphinx expects values for version and timestamps to be
  str objects. Doc builds that do things in conf.py (or extensions)
  like extract the modification date from the most recent commit will
  need to properly decode the return
  values. https://review.opendev.org/#/c/575483 shows one example of
  how to fix this sort of problem.

Release Notes Jobs
------------------

The ``release-notes-jobs-python3`` project template defines a set of
jobs for testing and building release notes using python 3. The
release notes jobs do not use tox, but the tox settings should still
be updated.

In the Zuul configuration on the master branch of the repository,
change the project template ``release-notes-jobs`` to
``release-notes-jobs-python3``. If the patch to change the project
template does not run the new job, it may be necessary to add a dummy
release note to make the patch self-testing.

https://review.opendev.org/#/c/572895/ shows how to update the
tox.ini settings in the project to set the ``basepython`` variable for
the ``releasenotes`` environment, used for developer testing. This
change should only be made on the master branch.

Common issues to anticipate:

* Under python 3 the output of subprocess.check_output() is a bytes
  instance, but sphinx expects values for version and timestamps to be
  str objects. Doc builds that do things in conf.py (or extensions)
  like extract the modification date from the most recent commit will
  need to properly decode the return values.

Source Code Linter Jobs
-----------------------

Most of the jobs we have that run source code linters *do* use tox to
control the versions of the linter tool. These jobs typically have
names like ``openstack-tox-linters`` or ``openstack-tox-pep8``.

https://review.opendev.org/#/c/572895/ shows how to update the
tox.ini settings in the project to set the ``basepython`` variable for
the environments. All of the linter jobs running against python source
code in the master branch should be updated. These changes should be
self-testing.

Any linter jobs that use python-based tools to check other sorts of
source should also be updated to use python 3, if possible.

Common issues to anticipate:

* The built-in ``file``() no longer exists under python 3, so using it
  causes pylint to report an undefined name. Use ``open()`` instead.

* The built-in ``unicode`` no longer exists under python 3, so using
  it causes pylint to report an undefined name. Use ``six.text_type``
  instead.

* Under python 3 the flake8/hacking/pep8/pylint tools run different or
  additional checks. This may mean new code formatting issues will
  have to be fixed as part of changing the linter jobs over.

* There is a bug in the older version of pylint that many projects are
  using that prevents it from working correctly under python 3. Pylint
  will have to be upgraded as part of this transition; version 1.9.2
  is known to work.

  The error message from the broken version is::

    AttributeError: 'Call' object has no attribute 'starargs'

  Updating the version of pylint brings new rules, and will require
  modifications either to source code or to the pylint configuration.
  https://review.opendev.org/#/c/573024/ is an example of updating
  to the latest version of pylint in the freezer repository, with a
  combination of fixes and disabling rules.

Release Artifact Publishing
---------------------------

We will be making several changes to artifact publishing for
Python-based projects simultaneously. The job settings for the release
artifact publishing need to be defined in
``openstack-infra/project-config/zuul.d/projects.yaml`` rather than in
each project repository, because those jobs are not "branch aware" and
therefore we do not want different versions of the jobs on different
branches.

First, a new job that uses ``setuptools`` to validate the packaging
metadata for a repository will run in the check and gate queues when
``README.rst``, ``setup.cfg``, or ``setup.py`` are modified. This will
be an early warning for issues that may come up as part of publishing
the build artifacts, and runs the same step that was added recently to
the validation job in ``openstack/releases`` as well as actually
building an sdist and a wheel.

Second, the new packaging test, build, and publish jobs will all run
under python 3.

Third, all python-based deliverables will have their sdists and wheels
published to PyPI. This will simplify dependency management between
plugins and server projects and will streamline the number of
variations of release jobs that we have.

In order to make this change, project teams may first need to register
their project name on PyPI. Refer to `the creator's guide in the infra
manual`_ for details of how to do this.

.. note::

   The original goal contained an additional step: "After the name is
   configured on PyPI, change any existing release project template to
   ``publish-to-pypi-python3``. https://review.opendev.org/580740
   shows an example of changing the job setting."

   Infra now has made ``publish-to-pypi`` using python3, so all repos
   use again ``publish-to-pypi`` and thus the step mentioned above is
   not needed anymore.

It is not possible to test the job change, because it needs to be made
in the ``openstack-infra/project-config`` repository. Therefore, after
the first change merges it will be useful to create a second patch in
the project repository with a whitespace or other typo-fix change in
the ``README.rst`` to trigger the packaging test job in this patch to
ensure everything works properly. https://review.opendev.org/580741
shows an example of such a change.

.. note::

   Teams using release jobs that rely on python to publish artifacts
   for projects not written in python (and therefore not covered by
   ``publish-to-pypi-python3``) should work with the release and infra
   teams to update their release jobs to use python 3.

Common issues to anticipate:

* Projects that have not published to PyPI before may need to fix
  their ``README.rst`` file if it uses RST directives only defined by
  Sphinx and not by docutils. The new test job will catch any issues.

* Projects that cannot reserve their project name on PyPI because it
  is owned by another community may need to change the sdist name in
  their ``setup.cfg`` in order to be able to publish to PyPI under a
  different name. That will not change how the code is imported, but
  it will change package names and may require setting
  ``tarball-base`` in the release settings managed in
  ``openstack/releases``. The release management team can help if you
  end up needing to change names, so contact them before starting to
  make the change.

.. _the creator's guide in the infra manual: https://docs.openstack.org/infra/manual/creators.html#give-openstack-permission-to-publish-releases

.. _on the mailing list: http://lists.openstack.org/pipermail/openstack-dev/2018-June/131193.html

Functional Test Jobs
--------------------

Updating the functional test jobs for a project will require more
knowledge of the jobs that exist, which ones need to be duplicated
under python 3, and which can be changed to python 3 without being run
under python 2. Changing the job configuration will require knowledge
of the job implementation details. For these reasons, the analysis and
implementation work for updating the functional test jobs is left up
to each project team.

Libraries used by services that run in the default integrated gate can
add the ``lib-forward-testing-python3`` project template to ensure
they have full integration tests run.
https://review.opendev.org/#/c/575927/ shows an example of doing
this for oslo.config.

Where possible, when modifying existing jobs, a variable should be
added to control the version of python so that the same job
implementation (playbooks, roles, etc.) can be used instead of
duplicating the entire job definition. This will simplify cleaning up
the old job definitions when python 2 support is finally dropped.

It should be possible to update functional and integration test jobs
that run through tox by setting ``basepython = python3`` for the
appropriate tox environment, as in
https://review.opendev.org/#/c/572895/.

Wiki Tracking Page
------------------

We have been using https://wiki.openstack.org/wiki/Python3 to track
the status of support in each project. Teams should keep the page up
to date with information about blockers, test jobs, etc. as they work
on this goal (and after, ideally).

Python 3.6 Unit Test Jobs
-------------------------

`On the mailing list`_ Zane proposed updating to test with Python 3.6
when it is available. Adding those test jobs will be easier after the
Zuul configuration is moved out of the project-config repository, so
this step is left for last. Because adding the test job may require
code changes, it will be up to each project team to take this step by
adding ``openstack-python36-jobs`` to the list of templates associated
with the project on the master branch. The change will be
self-testing, and can either be structured to include the code changes
(if they are trivial) or end a series of patches (if the code changes
are significant).

.. note::

   We do not plan to update the minimum version of python 3 we support
   as part of this goal. Projects already running python 3.5 jobs
   should continue to do so.

References
==========

* :ref:`goal-support-python-3.5`
* `Updating python packaging jobs <https://review.opendev.org/#/q/topic:python3-packaging+(status:open+OR+status:merged)>`__
* `Configuring library forward testing jobs <https://review.opendev.org/#/q/topic:python3-lib-forward-testing+(status:open+OR+status:merged)>`__
* `Planning etherpad <https://etherpad.openstack.org/p/python3-first>`__
* `Status of OpenStack projects
  <https://wiki.openstack.org/wiki/Python3#Python_3_Status_of_OpenStack_projects>`__
  from the Python3 wiki page.

Current State / Anticipated Impact
==================================

A significant number of patches to update the tox settings for
projects have already been proposed and many have been merged:

https://review.opendev.org/#/q/topic:python3-first

Some of the Oslo libraries are using the python 3 versions of these
jobs already.

Because the goal champion team will prepare a lot of the patches to
move the Zuul settings, we expect project teams to be able to focus on
unique aspects of their testing such as branch-specific jobs or
functional jobs.
