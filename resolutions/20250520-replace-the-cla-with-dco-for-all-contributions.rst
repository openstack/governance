=====================================================
2025-05-20 Replace CLA with DCO for all contributions
=====================================================

The OpenStack community has required contributors to sign a
Contributor License Agreement (CLA) before submitting code
contributions. This process has addressed legal and organizational
needs but has long been seen as being cumbersome to the contribution process
and imposes administrative overhead.

The OpenStack Technical Committee (TC) `requested
in 2014`_ that the Foundation Board of Directors implement
the `Developer Certificate of Origin`_ (DCO) as the Contributor
License Agreement (CLA) for the OpenStack project. The DCO is a
simpler, developer-affirmed certification that contributors
have the right to submit the code they are contributing.
We are pleased that the Foundation board has now found
this `transition feasible`_.

The OpenStack Technical Committee approves the transition from a
CLA-based contribution model to a Developer Certificate of Origin
(DCO) model. The move aligns us with governance practices in other large open
source projects, like the Linux Kernel, and will streamline our contributor
experience.

The OpenStack Technical Committee therefore resolves to:

- Replace the Contributor License Agreement (CLA) with the Developer
  Certificate of Origin (DCO) as the core legal framework for contributions to
  OpenStack projects.
- Set the transition effective date to **July 1, 2025**. From that
  date, all commits to OpenStack repositories must include a valid
  `Signed-off-by` line in the commit message as stated in the DCO.
- Direct the OpenDev Infrastructure team to enforce DCO compliance on the
  OpenStack `code review system`_, i.e., require a valid DCO sign-off for
  all new commits.
- Ensure that the OpenStack Contributor Documentation features the Developer
  Certificate of Origin and includes clear and practical guidance for
  contributors on how to sign their commits and what the sign-off represents.
- Encourage OpenStack project maintainers to update their own contributor
  documentation to point to the OpenStack Contributor Documentation regarding
  the DCO. We don't need to reproduce the DCO within project documentation
  or the source code. All existing documents referring to the prior CLA have to
  be modified to remove that information.
- Clarify that existing contributors **will not** be required to retroactively
  sign or re-submit anything. However, all new commits made on or after
  July 1, 2025 must adhere to the DCO requirements. Changes already uploaded to
  the code review system need not be modified just to include the
  `Signed-off-by` line in the commit message. However, when changes need to be
  modified for other reasons, the commit message must be amended to include the
  `Signed-off-by` line.

This adoption of the DCO will lower the barrier to contribution, reduce
administrative burden, and bring OpenStack in line with best practices across
the open-source world. It's a key step towards a more accessible and welcoming
OpenStack.

.. _requested in 2014: ../resolutions/20140909-cla.html
.. _Developer Certificate of Origin: https://developercertificate.org/
.. _transition feasible: https://lists.openinfra.org/archives/list/foundation@lists.openinfra.org/thread/PXMTX67TRL2B4ONICTT2E2XZLG4J4LAL/
.. _code review system: https://review.opendev.org
