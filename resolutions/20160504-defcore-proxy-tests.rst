==========================================================
 2016-05-04 Recommendation on API Proxy Tests for DefCore
==========================================================

At the Newton summit discussion about `QA, DefCore, and
interoperability testing`_ the DefCore committee asked for clear
direction about whether or not to use API tests that proxy through one
service to use features of another service.

For example, there are tests in Tempest, used for DefCore compliance
testing, that call a Nova API to test the "image list"
capability. That is a feature of Glance, and should be tested using
the Glance API directly. Testing through another service does not
ensure that the Glance API stays consistent across releases, and locks
the testable version of a feature to something that has been adopted
by a project that did not implement the feature. So we all lose some
ability for testing backwards-compatibility and the Glance team loses
autonomy for defining their API.

For these reasons, the TC encourages the DefCore committee to avoid
using tests that proxy through one service to exercise the features of
another when considering trademark compliance and interoperability.

Some existing tests being used by DefCore are not compatible with this
policy, and either need to be rewritten or replaced with new
tests. Project teams should work with the DefCore committee to
identify and fix those tests.

.. _QA, DefCore, and interoperability testing: https://etherpad.openstack.org/p/newton-qa-defcore-and-interoperability
