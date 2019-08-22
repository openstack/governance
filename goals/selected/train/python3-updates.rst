.. -*- encoding: utf-8 -*-

=========================================
 Update Python 3 test runtimes for Train
=========================================

This goal is to implement the process set out in the
:doc:`../../../resolutions/20181024-python-update-process` TC resolution, for
the Train cycle to ensure unit testing is in place for all of the
:doc:`../../../reference/runtimes/train`.

In practice, this generally means adding unit tests for Python 3.7 and dropping
unit tests for Python 3.5. Using the Zuul template for Train will ensure that
all projects that support Python3 will be tested against the agreed runtime
versions, and make it easier to update them in future.

Champions
=========

* Corey Bryant (coreycb)

Gerrit Topic
============

Use |python3-train|_.

Some existing patches that do not use the Zuul template exist under the topics
|py37-job|_ and |dropping-py35-testing|_. Any of these not yet merged should be
updated to use the Zuul template instead (and the topic changed to
|python3-train|), or abandoned.

.. |python3-train| replace:: ``python3-train``
.. _python3-train: https://review.opendev.org/#/q/topic:python3-train+(status:open+OR+status:merged)
.. |py37-job| replace:: ``py37-job``
.. _py37-job: https://review.opendev.org/#/q/topic:py37-job+(status:open+OR+status:merged)
.. |dropping-py35-testing| replace:: ``dropping-py35-testing``
.. _dropping-py35-testing: https://review.opendev.org/#/q/topic:dropping-py35-testing+(status:open+OR+status:merged)+branch:master

Completion Criteria
===================

Any repositories with Python 3 unit tests are exclusively using the
``openstack-python3-train-jobs`` Zuul template or one of its variants (e.g.
``openstack-python3-train-jobs-neutron``) to run unit tests, and the tests are
passing. None of the Zuul templates that hard-code a Python3 version (e.g.
``openstack-python35-jobs``) remain in use.

Details
=======

The scope of this goal is all official OpenStack repositories that include at
least one Zuul job that runs unit tests on some version of Python3.

The goal champions will propose patches to all affected repositories to add one
of the following templates to their Zuul configuration (depending on the
existing template used):

* ``openstack-python3-train-jobs``
* ``openstack-python3-train-jobs-horizon``
* ``openstack-python3-train-jobs-neutron``
* ``openstack-python3-train-jobs-ceilometer``

The patch should also remove all
``openstack-python3*-jobs[-horizon/neutron/ceilometer]`` templates from the
Zuul config.

The change will be self-testing in Zuul. If py37 tests are failing, it is the
responsibility of the project team to fix them so that the change can merge.
Project teams should merge the change to the Zuul config before the end of the
Train cycle.

Stretch Goals
-------------

Ideally the proposed patch should update ``setup.cfg`` for any repositories
where the classifier contains ``Programming Language :: Python :: 3`` to ensure
it contains::

    Programming Language :: Python :: 3
    Programming Language :: Python :: 3.6
    Programming Language :: Python :: 3.7

and no other Python 3 versions.

Also, it would be nice to update the list of default environments in
``tox.ini`` to include ``py37`` and remove ``py34`` and ``py35``.

Future Process
--------------

As part of this goal, we will add support to the release management tools to
have a bot submit the change as part of the process of cutting the previous
release's feature branch. Graham Hayes (mugsie) has volunteered for this task.

Having done the initial switch over of the Zuul templates in Train will make
those patches simpler to generate (they will need only to substitute the next
release name). It will still be up to project teams to fix any test failures
and merge the patch even in future release cycles.

Non-Goals
---------

Python 2 testing remains unchanged. Repositories that unit test on Python 2
should continue to do so using the ``openstack-python27-jobs`` Zuul template,
and declare support for Python 2.7 in ``setup.cfg``. Testing of Python 2 must
not be dropped before the U cycle, as detailed in the
:doc:`../../../resolutions/20180529-python2-deprecation-timeline` TC
resolution.

References
==========

* :doc:`../../../resolutions/20181024-python-update-process`
* :doc:`../../../reference/runtimes/train`
* `Porting to Python 3.7
  <https://docs.python.org/3/whatsnew/3.7.html#porting-to-python-3-7>`_
* :doc:`../../../resolutions/20180529-python2-deprecation-timeline`

Current State / Anticipated Impact
==================================

There are a handful of breaking changes between Python 3.6 and 3.7. The most
notable one is `PEP 479 <https://www.python.org/dev/peps/pep-0479>`_ (making it
an error to raise a ``StopIteration`` exception from a function or generator),
but much of the impact is in exposing pre-existing bugs which ought to be fixed
anyway (non-erroneous uses are generally trivial to eliminate).

Many projects have `already merged patches to test on Python 3.7
<https://review.opendev.org/#/q/topic:py37-job+status:merged>`_, so in those
cases the project should have nothing to do but merge the patch.

Because the goal champion team will prepare the patches to change the Zuul
configuration, we expect project teams to require minimal effort outside of
fixing any Python 3.7 incompatibilities.
