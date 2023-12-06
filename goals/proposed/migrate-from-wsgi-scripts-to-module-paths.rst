=========================================
Migrate from wsgi scripts to module paths
=========================================

We have long supported automated generation of WSGI scripts, which are Python
scripts that contain an ``application`` object as described in `PEP-333`__.
This automated generation was facilitated by PBR through the use of
``wsgi_scripts`` entrypoint declared in ``setup.cfg`` or ``setup.py``.

As a result of multiple changes in the Python packaging ecosystem, primarily
driven by `PEP-517`__, the approach we have used to implement this
functionality will eventually break. We are rapidly approaching the point where
it will no longer be possible to continue to support without likely large
investment in PBR.

This investment is hard to justify given the WSGI script approach is not
necessary for uWSGI and is not supported by gunicorn. Both of these utilities
instead support for specifying Python module paths. That is to say, instead of
providing a filesystem path to a Python script, we can provide a Python module
path to an ``application`` object. In more concrete terms, a uWSGI
configuration that currently looks like so:

.. code-block:: ini

    [uwsgi]
    wsgi-file = /bin/nova-api-wsgi

can also be configured as:

.. code-block:: ini

    [uwsgi]
    module = nova.wsgi.osapi_compute:application

All projects that expose a WSGI server and make use of PBR's ``wsgi_scripts``
functionality should provide a new ``<service>.wsgi`` module. This module
should contain one or more modules, each corresponding to an individual WSGI
server exposed by the service. Each of these server modules should contain an
``application`` object suitable for invocation by a WSGI reverse proxy server.

Services may choose to remove the ``wsgi_scripts`` entrypoint immediately upon
migration or wait a cycle to remove it. However, these entrypoints will soon
start to fail with newer versions of pip and setuptools thus they should not be
retained indefinitely.

Champion
========

Stephen Finucane (stephenfin)

Gerrit Topic
============

To facilitate tracking, commits related to this goal should use the
gerrit topic::

  remove-wsgi_scripts

Completion Criteria
===================

#. All official OpenStack service projects should provide one or more
   ``<service>.wsgi.<server>`` modules, each containing an ``application``
   object.

Current State / Anticipated Impact
==================================

Thus far, patches have been proposed against Nova and DevStack to demonstrate
the impact of this change. As services start implementing their own
``<service>.wsgi`` module, all deployment tools including DevStack will need to
to switch from WSGI script-based configuration to Python module path-based
configuration. From the initial work on the Nova and DevStack as well as
discussions with relevant people working on deployment tooling, it is expected
that the overall size of this effort will be minimal.

.. __: https://peps.python.org/pep-0333/
.. __: https://peps.python.org/pep-0517/
