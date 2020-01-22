============================
Tested Runtimes for Victoria
============================

At the start of the Victoria development cycle, the current :ref:`LTS or stable
distribution <pti-linux-distros>` versions are:

* Ubuntu 20.04
* CentOS 8
* openSUSE Leap 15

Python Runtimes for Victoria
============================

It is the :doc:`policy <../../resolutions/20181024-python-update-process>` that
each OpenStack release cycle will target the latest available version of
Python; default Python runtimes on the distributions listed above; and versions
used in integration tests at the start of the cycle, at least until the point
when all projects have migrated to a later version.

Based on the criteria above, all Python-based projects must target and test
against, at a minimum:

* Python 3.6 (default in CentOS 8.0 and OpenSUSE Leap 15.1)
* Python 3.7 (currently used in integration tests)
* Python 3.8 (latest available; default in Ubuntu 20.04)

The Python 3.7 tests are no longer required once the migration of integration
tests from Ubuntu 18.04 (Bionic - Python 3.7) to 20.04 (Focal - Python 3.8) is
complete, even if that occurs during the Victoria development cycle. The TC
adjudges that Python 3.7 testing is unlikely to be needed in a future release,
so it is unnecessary to maintain even periodic jobs after that point.

More details on Python requirements can be found in :ref:`pti-python`.

Node.js Runtime for Victoria
============================

Based on the available versions of Node.js supported in our :ref:`LTS or stable
distributions <pti-linux-distros>` all JavaScript testing should target:

* Node.js 10

More details on Javascript requirements can be found in :ref:`pti-javascript`.

Golang Runtime for Victoria
===========================

At this time, there are still frequent releases of Go with a wide variety of
distribution packaged versions. Given the current state of Go support and the
number of projects within OpenStack using Go, no formal version declaration is
being made at this time.

More details on Go requirements can be found in :ref:`pti-golang`.
