.. _20160504_defcore_test_location:

============================================================
 2016-05-04 Recommendation on Location of Tests for DefCore
============================================================

.. note:: This resolution has been superseded by 
          ref:`201180305_interop_test_location`

At the Newton summit discussion about `QA, DefCore, and
interoperability testing`_ the DefCore committee asked for direction
about where they should look for tests to consider for verifying
capabilities that are selected as criteria for interoperability
testing. Two options were discussed.

1. Use the tests within the Tempest git repository by themselves.
2. Add to those Tempest tests by allowing projects to host tests in
   their tree using Tempest's plugin feature.

Many projects do want to host their own functional tests, and the QA
team is understandably hesitant to host all functional and integration
tests for all projects. However, there are several reasons for
maintaining a centralized set of the tests we use for trademark
enforcement.

First, as interop tests are adopted for DefCore, an additional set of
review requirements for changes becomes especially important. For
example, API and behavioral changes must be carefully managed, as must
mundane aspects such as test and module naming and location within the
test suite. Even changes that leave tests functionally equivalent may
cause unexpected consequences for their use in DefCore processes and
validation. Placing the tests in a central repository will make it
easier to maintain consistency and avoid breaking the trademark
enforcement tool.

Centralizing the tests also makes it easier for anyone running the
validation tool against their cloud or cloud distribution to use the
tests. It is easier to install the test suite and its dependencies,
and it is easier to read and understand a set of tests following a
consistent implementation pattern. Finally, having the tests in a
central location makes it easier to ensure that all members of the
community have equal input into what the tests do and how they are
implemented and maintained.

For all of these reasons, the OpenStack community will benefit from
having the interoperability tests used by DefCore in a central
location. The TC therefore encourages the DefCore committee to
consider it an indication of future technical direction that we do not
want tests outside of the `Tempest repository`_ used for trademark
enforcement, and that any new or existing tests that cover
capabilities they want to consider for trademark enforcement should be
placed in Tempest.

Project teams should work with the DefCore committee to move any
existing tests that need to move as a result of this policy. Project
team contributors should also be prepared to work with the QA and
DefCore teams on reviews and updates to tests that cover capabilties
needed for DefCore, but where the test implementation is not
suitable. Using a central repository for interoperability tests does
not remove the responsibility for helping to maintain them.

Adopting this policy may also require the QA team to expand the `scope
of what they consider suitable for Tempest`_ to allow tests that cover
projects that the DefCore committee wants to have available for
trademark status. Only tests related to capabilities would need to be
moved into Tempest, and the DefCore committee, QA team, and project
teams should collaborate to ensure that those tests are identified and
implemented in a suitable way.

.. _QA, DefCore, and interoperability testing: https://etherpad.openstack.org/p/newton-qa-defcore-and-interoperability
.. _Tempest repository: https://opendev.org/openstack/tempest
.. _scope of what they consider suitable for Tempest: https://wiki.openstack.org/wiki/QA/Tempest-test-removal#Tempest_Scope
