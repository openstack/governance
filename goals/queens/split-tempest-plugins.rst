.. -*- mode: rst -*-

==================================================
Split Tempest Plugins into Seperate Repos/Projects
==================================================

Tempest plugins rely on setuptools entrypoints and therefore can be included
in any python project as long as it properly sets up the entrypoint. A common
pattern has emerged of bundling these plugins inside a project repo. This is
likely because it makes contributing tests at the same time as an API feature
must simpler. However, this is really an antipattern and makes consuming the
test plugins much more difficult, especially in all-in-one deployments. In
order to make using plugins more consistent and easier for end users,
packagers, and deployers this goal is to make sure we always use a separate
python project for each plugin.

There are several issues with the current situation including:

1. When you deploy an all in one system with multiple services that have
bundled tempest plugins and then run tempest outside of a venv tempest will see
the tests for all the plugins whether you intended to use them or not.
It is also a fairly common occurrence for a project to ship a broken plugin
that breaks at import time. This prevents unittest discovery from working which
will block any tests from running.

2. A packager tries to use a stable version of your project with a newer
tempest. This results in conflicting requirements because tempest is branchless
and follows master requirements and makes using stable release plugins with
master tempest impossible.

3. Most projects don't actually use the same tests across release boundaries
(or just don't use plugins on stable branches), which means breaking api
changes can land. There are 2 exceptions to this trove and ironic which we
hacked together a mechanism to install the project repo from master in the
tempest venv.

4. Plugin requirements aren't exposed at install time. Some projects use
test-requirements to set tempest plugin requirements (since it is for tests)
which do not get installed when you pip install a project. However the
entrypoint always gets exposed and tempest will pick it up regardless of
whether all the requirements are installed.

Having tempest plugins in a separate repo/project solves all of these issues
and makes using a plugin opt-in in all cases. (ie you have to ``pip install
plugin-foo`` to use it and won't show up as an unexpected side effect of
installing a service) For community development and testing it means we are
actually ensuring API compatibility across releases. It also means for packagers
that you don't have to install all of a project repo to ship a plugin package.

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

  goal-split-tempest-plugins

Completion Criteria
===================

For all projects with a bundled tempest plugin:

#. Create a new seperate repo for the tempest plugin
#. Migrate all the functionality from the bundled plugin to the new repo
#. Switch gating jobs to use the new plugin project instead of the bundled one
#. Delete the bundled tempest plugin from the project repo

Note, there is no change in governance or ownership of a repository involved
with this change. The new plugin repo/project will still be owned by the
project it was spun out from.

More detailed recommended steps for accomplishing the split can be found here:

https://etherpad.openstack.org/p/tempest-separate-plugin

References
==========

The tempest documentation elaborates on why seperate plugins are a better
pattern:

http://docs.openstack.org/developer/tempest/plugin.html#standalone-plugin-vs-in-repo-plugin

The following links may be useful to developers attempting to create their
tempest plugin project:

* https://www.openstack.org/videos/boston-2017/tempest-plugin-crash-course
* https://etherpad.openstack.org/p/tempest-separate-plugin
* https://etherpad.openstack.org/p/tempest-plugin-testing
* https://etherpad.openstack.org/p/pike-tempest-plugin-dev

Current State / Anticipated Impact
==================================

The following script was used to find all the openstack projects with tempest
plugins.

.. code-block:: python

  import json
  import re
  import sys

  import requests
  import yaml

  url = 'https://review.openstack.org/projects/'
  with open(sys.argv[1], 'r') as fd:
      projects_list = yaml.load(fd.read())

  repo_list = []
  for i in projects_list:
      deliverables = projects_list[i]['deliverables']
      repo_paths = [x['repos'] for x in deliverables.values()]
      for repos in repo_paths:
          for name in repos:
              repo_list.append(name)

  # This is what a project looks like
  '''
    "openstack-attic/akanda": {
      "id": "openstack-attic%2Fakanda",
      "state": "READ_ONLY"
    },
  '''

  def is_openstack_proj(proj):
      res = False
      if proj in repo_list:
          res = True
      return res

  # Rather than returning a 404 for a nonexistent file, cgit delivers a
  # 0-byte response to a GET request.  It also does not provide a
  # Content-Length in a HEAD response, so the way we tell if a file exists
  # is to check the length of the entire GET response body.


  def has_tempest_plugin(proj):
      r = requests.get(
          "https://git.openstack.org/cgit/%s/plain/setup.cfg" % proj)
      p = re.compile('^tempest\.test_plugins', re.M)
      if p.findall(r.text):
          return True
      else:
          False

  r = requests.get(url)
  # Gerrit prepends 4 garbage octets to the JSON, in order to counter
  # cross-site scripting attacks.  Therefore we must discard it so the
  # json library won't choke.
  projects = sorted(filter(is_openstack_proj, json.loads(r.text[4:])))

  found_plugins = filter(has_tempest_plugin, projects)

  # Every element of the found_plugins list begins with "openstack/".
  # We drop those initial 10 octets when printing the list.
  for project in found_plugins:
      print(project)

On 03 Jan 2017 this was run and found all the projects with bundled tempest
plugins. 4 matches were found that are standalone plugins:
barbican-tempest-plugin, tempest-horizon, designate-tempest-plugin, and
sahara-tests (this is a multitest repo but it's not bundled with the project so
it's not applicable here either) Also all the deb packaging repos were removed
as they are duplicates. This list is:

::

  openstack/aodh
  openstack/ceilometer
  openstack/cinder
  openstack/congress
  openstack/ec2-api
  openstack/freezer
  openstack/freezer-api
  openstack/gnocchi
  openstack/heat
  openstack/ironic
  openstack/ironic-inspector
  openstack/keystone
  openstack/magnum
  openstack/manila
  openstack/mistral
  openstack/monasca-api
  openstack/monasca-log-api
  openstack/murano
  openstack/networking-bgpvpn
  openstack/networking-midonet
  openstack/networking-sfc
  openstack/neutron
  openstack/neutron-dynamic-routing
  openstack/neutron-fwaas
  openstack/neutron-lbaas
  openstack/octavia
  openstack/senlin
  openstack/tricircle
  openstack/trove
  openstack/vitrage
  openstack/watcher
  openstack/zaqar
  openstack/zun

Project Teams
=============

barbican
--------

Planning Artifacts:

Completion Artifacts:

Chef OpenStack
--------------

Planning Artifacts:

Completion Artifacts:

cinder
------

Planning Artifacts:

Completion Artifacts:

cloudkitty
----------

Planning Artifacts:

Completion Artifacts:

Community App Catalog
---------------------

Planning Artifacts:

Completion Artifacts:

congress
--------

Planning Artifacts:

Completion Artifacts:

designate
---------

Planning Artifacts:

Completion Artifacts:

Documentation
-------------

Planning Artifacts:

Completion Artifacts:

dragonflow
----------

Planning Artifacts:

Completion Artifacts:

ec2-api
-------

Planning Artifacts:

Completion Artifacts:

freezer
-------

Planning Artifacts:

Completion Artifacts:

fuel
----

Planning Artifacts:

Completion Artifacts:

glance
------

Planning Artifacts:

Completion Artifacts:

heat
----

Planning Artifacts:

Completion Artifacts:

horizon
-------

Planning Artifacts:

Completion Artifacts:

I18n
----

Planning Artifacts:

Completion Artifacts:

Infrastructure
--------------

Planning Artifacts:

Completion Artifacts:

ironic
------

Planning Artifacts:

Completion Artifacts:

karbor
------

Planning Artifacts:

Completion Artifacts:

keystone
--------

Planning Artifacts:

The keystone team followed the documented steps outlined in this goal as the
planning document.

Completion Artifacts:

The following review removed the tempest plugin that keystone was maintaining
in tree and links to the new repository the plugin was moved to:

  http://git.openstack.org/cgit/openstack/keystone/commit/?id=6f4e37e9e6810e24f45d034261f4a6ec4aa85fb1

kolla
-----

Planning Artifacts:

Completion Artifacts:

kuryr
-----

Planning Artifacts:

Completion Artifacts:

magnum
------

Planning Artifacts:

Completion Artifacts:

manila
------

Planning Artifacts:

Completion Artifacts:

mistral
-------

Planning Artifacts:

Completion Artifacts:

monasca
-------

Planning Artifacts:

Completion Artifacts:

murano
------

Planning Artifacts:

Completion Artifacts:

neutron
-------

Planning Artifacts:

Completion Artifacts:

nova
----

Planning Artifacts:

Completion Artifacts:

octavia
-------

Planning Artifacts:

Completion Artifacts:

OpenStack Charms
----------------

Planning Artifacts:

Completion Artifacts:

OpenStack UX
------------

Planning Artifacts:

Completion Artifacts:

OpenStackAnsible
----------------

Planning Artifacts:

Completion Artifacts:

OpenStackClient
---------------

Planning Artifacts:

Completion Artifacts:

oslo
----

Planning Artifacts:

Completion Artifacts:

Packaging-deb
-------------

Planning Artifacts:

Completion Artifacts:

Packaging-rpm
-------------

Planning Artifacts:

Completion Artifacts:

Puppet OpenStack
----------------

Planning Artifacts:

Completion Artifacts:

Quality Assurance
-----------------

Planning Artifacts:

Completion Artifacts:

rally
-----

Planning Artifacts:

Completion Artifacts:

RefStack
--------

Planning Artifacts:

* The RefStack team does not have tempest plugins and therefore has nothing
  to do.

Completion Artifacts:

* Not applicable.

Release Management
------------------

Planning Artifacts:

Completion Artifacts:

requirements
------------

Planning Artifacts:

Completion Artifacts:

sahara
------

Planning Artifacts:

Completion Artifacts:

searchlight
-----------

Planning Artifacts:

Completion Artifacts:

Security
--------

Planning Artifacts:

Completion Artifacts:

senlin
------

Planning Artifacts:

Completion Artifacts:

shade
-----

Planning Artifacts:

* The shade team does not have tempest plugins and therefore has
  nothing to do.

Completion Artifacts:

* None

solum
-----

Planning Artifacts:

Completion Artifacts:

Stable branch maintenance
-------------------------

Planning Artifacts:

Completion Artifacts:

storlets
--------

Planning Artifacts:

Completion Artifacts:

swift
-----

Planning Artifacts:

Completion Artifacts:

tacker
------

Planning Artifacts:

Completion Artifacts:

Telemetry
---------

Planning Artifacts:

Completion Artifacts:

tricircle
---------

Planning Artifacts:

Completion Artifacts:

tripleo
-------

Planning Artifacts:

Completion Artifacts:

trove
-----

Planning Artifacts:

Completion Artifacts:

vitrage
-------

Planning Artifacts:

Completion Artifacts:

watcher
-------

Planning Artifacts:

Completion Artifacts:

winstackers
-----------

Planning Artifacts:

Completion Artifacts:

zaqar
-----

Planning Artifacts:

Completion Artifacts:

zun
---

Planning Artifacts:

Completion Artifacts:
