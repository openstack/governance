========================
Tested Runtimes for Yoga
========================

At the start of the Yoga development cycle, the current :ref:`LTS or stable
distribution <pti-linux-distros>` versions are:

* Ubuntu 20.04
* CentOS Stream 8
* CentOS Stream 9
* Debian 11

Python Runtimes for Yoga
========================

It is the :doc:`policy <../../resolutions/20181024-python-update-process>` that
each OpenStack release cycle will target the latest available version of
Python; default Python runtimes on the distributions listed above; and versions
used in integration tests at the start of the cycle, at least until the point
when all projects have migrated to a later version.

Based on the criteria above, all Python-based projects must target and test
against, at a minimum:

* Python 3.6 (available as default in CentOS Stream 8)
* Python 3.9 (available as default in Debian 11 and CentOS Stream 9)

Other than the above Python versions, Ubuntu 20.04 has Python 3.8 as default
which we are not suggesting to run unit tests. We assume that anything
that works on Python 3.6 and 3.9 will also work on 3.8. Do note, however,
Ubuntu is our primary target and thus the majority of tempest jobs run
with it and its Python 3.8 anyway.

More details on Python requirements can be found in :ref:`pti-python`.

Node.js Runtime for Yoga
========================

Based on the available versions of Node.js supported in our :ref:`LTS or stable
distributions <pti-linux-distros>` all JavaScript testing should target:

* Node.js 14

More details on Javascript requirements can be found in :ref:`pti-javascript`.

Golang Runtime for Yoga
=======================

At this time, there are still frequent releases of Go with a wide variety of
distribution packaged versions. Given the current state of Go support and the
number of projects within OpenStack using Go, no formal version declaration is
being made at this time.

More details on Go requirements can be found in :ref:`pti-golang`.
