==========================
Tested Runtimes for Ussuri
==========================

It is the policy that each OpenStack release cycle will target the
currently available runtimes on the :ref:`LTS or stable
distributions <pti-linux-distros>` at the start of a development cycle.

At the start of the Ussuri development cycle, the current versions are:

* Ubuntu 18.04
* CentOS 8
* openSUSE Leap 15

Python Runtime for Ussuri
=========================

Based on the available Python runtimes for the supported Linux distributions,
all Python-based projects must target and test against, at a minimum:

* Python 3.6
* Python 3.7

More details on Python requirements can be found in :ref:`pti-python`.

Node.js Runtime for Ussuri
==========================

Based on the availible versions of Node.js supported in our :ref:`LTS or stable
distributions <pti-linux-distros>` all JavaScript testing should target:

* Node.js 10

More details on Javascript requirements can be found in :ref:`pti-javascript`.

Golang Runtime for Ussuri
=========================

At this time, there are still frequent releases of Go with a wide variety of
distribution packaged versions. Given the current state of Go support and the
number of projects within OpenStack using Go, no formal version declaration is
being made at this time.

More details on Go requirements can be found in :ref:`pti-golang`.
