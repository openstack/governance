.. -*- mode: rst -*-

==================================
Remove Use of mox/mox3 for Testing
==================================

Mocking in unit tests in OpenStack started off using the mox package.
Unfortunately, this package is no longer actively maintained and had its last
update published to PyPi in August of 2010.

Due to this long period of inactivity, mox was never updated to add support for
Python 3. To get around this, the oslo team has been maintaining a mox3 fork to
support migration of consuming projects to Python 3. This was done as a short
term solution to allow projects to migrate to the more supported mock package.

Most projects have adopted mock, but many still have some use of mox/mox3 in
their tests. To get rid of mox, retire mox3, and provide a clean path to full
Python 3 support, we need to finish moving all projects off of mox and update
tests to use mock.

Champion
========
Goals need a main driver to project-manage them to completion. Project teams
need assistance, reminders and sometimes direct help in order for them to
complete the goals.

Chandan Kumar (chandankumar) has volunteered to drive this goal.

Gerrit Topic
============

To facilitate tracking, commits related to this goal should use the
gerrit topic::

  mox-removal

Storyboard
==========

Progress on this goal is tracked via
https://storyboard.openstack.org/#!/story/2001546

Completion Criteria
===================

In order to call this goal complete, we need:

#. All projects using mox to update their tests to use mock
#. Removal of mox from all test-requirements.txt and other requirements files
#. mox removed from openstack/requirements global-requirements.txt
#. openstack/mox3 marked as retired

References
==========

While there is not a quick and easy guide to migrating tests from mox to mock,
mock usage is fairly straight forward with many existing examples in our code
base.

The mock module is also well `documented
<https://docs.python.org/3/library/unittest.mock.html>`_.

Developers with experience using mock can be found in #openstack-qa,
#openstack-dev, as well as many of the individual project channels.

Nova is a good example of a large existing unit test code base that was
migrated from using mox to mock. There are many good examples available from
that effort that may be used as a reference:

https://review.opendev.org/#/q/topic:bp/remove-mox-pike+(status:open+OR+status:merged)

Current State / Anticipated Impact
==================================

Many of the projects using mox are also using mock. Some of the smaller
projects have not picked up mock yet, but have fewer tests that require
conversion.

Most of these projects should be able to finish converting their tests with
minimal guidance. Some of the smaller teams may need some assistance
completing the work.

It is hoped that this will also be a good opportunity to take care of some
bitrot in the unit tests. For some of the projects, there are areas of the unit
test code that has not been touched for a long time. As the conversion is done
to mock and the tests are inspected to understand the necessary changes, it
will also be a good time to validate that the tests are still needed and
testing the code in a useful way. While not a primarily goal, it may be a nice
side-effect if this work results in some clean up and updates in this way.
