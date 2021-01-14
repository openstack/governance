===========================
Tested Runtimes for Wallaby
===========================

At the start of the Wallaby development cycle, the current :ref:`LTS or stable
distribution <pti-linux-distros>` versions are:

* Ubuntu 20.04
* CentOS 8

Python Runtimes for Wallaby
============================

It is the :doc:`policy <../../resolutions/20181024-python-update-process>` that
each OpenStack release cycle will target the latest available version of
Python; default Python runtimes on the distributions listed above; and versions
used in integration tests at the start of the cycle, at least until the point
when all projects have migrated to a later version.

Based on the criteria above, all Python-based projects must target and test
against, at a minimum:

* Python 3.6 (default in CentOS 8.0)
* Python 3.8 (latest available; default in Ubuntu 20.04)

More details on Python requirements can be found in :ref:`pti-python`.

Node.js Runtime for Wallaby
===========================

Based on the available versions of Node.js supported in our :ref:`LTS or stable
distributions <pti-linux-distros>` all JavaScript testing should target:

* Node.js 10

More details on Javascript requirements can be found in :ref:`pti-javascript`.

Golang Runtime for Wallaby
==========================

At this time, there are still frequent releases of Go with a wide variety of
distribution packaged versions. Given the current state of Go support and the
number of projects within OpenStack using Go, no formal version declaration is
being made at this time.

More details on Go requirements can be found in :ref:`pti-golang`.
