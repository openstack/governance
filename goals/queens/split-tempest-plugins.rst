.. -*- mode: rst -*-

==================================================
Split Tempest Plugins into Separate Repos/Projects
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

#. Create a new separate repo for the tempest plugin
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

The tempest documentation elaborates on why separate plugins are a better
pattern:

https://docs.openstack.org/tempest/latest/plugin.html#standalone-plugin-vs-in-repo-plugin

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

  url = 'https://review.opendev.org/projects/'
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
          "https://opendev.org/openstack/%s/src/branch/master/setup.cfg" % proj)
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

The barbican project does not have in-tree tempest plugin.

Completion Artifacts:

The barbican team is maintaining its tempest plugin in a separate repo:

http://opendev.org/openstack/barbican-tempest-plugin

blazar
------

Planning Artifacts:

The blazar team followed the documented steps outlined in this goal as the
planning document.

Completion Artifacts:

The following review removed the tempest plugin that blazar was maintaining
in tree and links to the new repository the plugin was moved to:

* https://review.opendev.org/#/c/531138/

Chef OpenStack
--------------

Planning Artifacts:

* The Chef OpenStack team does not have tempest plugins and therefore has
  nothing to do.

Completion Artifacts:

* Not applicable.

cinder
------

Planning Artifacts:

https://blueprints.launchpad.net/cinder/+spec/goal-split-tempest-plugin

Completion Artifacts (work still in progress):

https://review.opendev.org/#/q/topic:goal-split-tempest-plugins+(status:open+OR+status:merged)+message:cinder

cloudkitty
----------

Planning Artifacts:

The cloudkitty project does not have in-tree tempest plugin.

Completion Artifacts:

The cloudkitty team is maintaining its tempest plugin in a separate repo:

http://opendev.org/openstack/cloudkitty-tempest-plugin

congress
--------

Planning Artifacts:

The congress team followed the documented steps outlined in this goal as
the planning document.

* `congress planning <https://bugs.launchpad.net/congress/+bug/1724713>`_

Completion Artifacts:

The following review removed the tempest plugin that congress was maintaining
in tree and links to the new repository the plugin was moved to:

* https://review.opendev.org/#/c/531689/

cyborg
------

Planning Artifacts:

* The cyborg team does not have tempest plugins and therefore has nothing
  to do.

Completion Artifacts:

* Not applicable.

designate
---------

Planning Artifacts:

Completion Artifacts:

The Designate team was already compliant before that the goal was defined.
Here is the tempest plugin repo:

https://opendev.org/openstack/designate-tempest-plugin

Documentation
-------------

Planning Artifacts:

* The Documentation team does not maintain tempest plugins and therefore has
  nothing to do.

Completion Artifacts:

* Not applicable.

dragonflow
----------

Planning Artifacts:

* The dragnonflow team does not have tempest plugins and therefore has nothing
  to do.

Completion Artifacts:

* Not applicable.

ec2-api
-------

Planning Artifacts:

Completion Artifacts:

freezer
-------

Planning Artifacts:

The freezer team followed the documented steps outlined in this goal as the
planning document.

Completion Artifacts:

The following review removed the tempest plugin that freezer and freezer-api
were maintaining in tree and links to the new repository the plugin was
moved to:

* https://review.opendev.org/526667 - Removes the bundled intree tempest
  plugin from Freezer project
* https://review.opendev.org/526914 - Remove bundled intree freezer_api
  tempest plugin

glance
------

Planning Artifacts:

* The glance team does not have tempest plugins and therefore has nothing
  to do.

Completion Artifacts:

* Not applicable.

heat
----

Planning Artifacts:

The Heat team followed the documented steps outlined in this goal as the
planning document.

Completion Artifacts:

The following review removed the tempest plugin that heat was maintaining
in tree and links to the new repository the plugin was moved to:

* https://review.opendev.org/#/c/528491/

horizon
-------

Planning Artifacts:

Completion Artifacts:

The Horizon team was already compliant before that the goal was defined. Here
is the tempest plugin repo:

https://opendev.org/openstack/tempest-horizon

I18n
----

Planning Artifacts:

* The I18n team does not have tempest plugins and therefore has nothing
  to do.

Completion Artifacts:

* Not applicable.

Infrastructure
--------------

Planning Artifacts:

* The Infrastructure team does not have tempest plugins and therefore has
  nothing to do.

Completion Artifacts:

* Not applicable

ironic
------

Planning Artifacts:

The Ironic team followed the documented steps outlined in this goal as the
planning document.

Completion Artifacts:

The following reviews removed the tempest plugin from Ironic and Ironic-inspector
that  was maintained in tree and moved to ironic-tempest-plugin repo:

* https://review.opendev.org/532585 (Ironic)
* https://review.opendev.org/527743 (Ironic-inspector)

karbor
------

Planning Artifacts:

* The karbor team does not have tempest plugins and therefore has nothing
  to do.

Completion Artifacts:

* Not applicable.

keystone
--------

Planning Artifacts:

The keystone team followed the documented steps outlined in this goal as the
planning document.

Completion Artifacts:

The following review removed the tempest plugin that keystone was maintaining
in tree and links to the new repository the plugin was moved to:

  https://opendev.org/openstack/keystone/commit/6f4e37e9e6810e24f45d034261f4a6ec4aa85fb1

kolla
-----

Planning Artifacts:

* The kolla team does not have tempest plugins and therefore has nothing
  to do.

Completion Artifacts:

* Not applicable.

kuryr
-----

Planning Artifacts:

The kuryr project does not have in-tree tempest plugin.

Completion Artifacts:

The kuryr team is maintaining its tempest plugin in a separate repo:

https://opendev.org/openstack/kuryr-tempest-plugin

loci
----

Planning Artifacts:

* The loci team does not have tempest plugins and therefore has nothing
  to do.

Completion Artifacts:

* Not applicable.

magnum
------

Planning Artifacts:

The magnum team followed the documented steps outlined in this goal as the
planning document.

Completion Artifacts:

The following review removed the tempest plugin that magnum was maintaining
in tree and links to the new repository the plugin was moved to:

* https://review.opendev.org/#/c/526618/

manila
------

Planning Artifacts:

The manila team followed the documented steps outlined in this goal as the
planning document.

Completion Artifacts:

The following review removed the tempest plugin that manila was maintaining
in tree and links to the new repository the plugin was moved to:

* https://review.opendev.org/#/c/512300/

masakari
--------

Planning Artifacts:

* The masakari team does not have tempest plugins and therefore has nothing
  to do.

Completion Artifacts:

* Not applicable.

mistral
-------

Planning Artifacts:

The mistral team followed the documented steps outlined in this goal as the
planning document.

Completion Artifacts:

The following review removed the tempest plugin that mistral was maintaining
in tree and links to the new repository the plugin was moved to:

* https://review.opendev.org/#/c/526918/

monasca
-------

Planning Artifacts:

Completion Artifacts:

murano
------

Planning Artifacts:

The murano project does not have in-tree tempest plugin.

Completion Artifacts:

The murano team is maintaining its tempest plugin in a separate repo:

https://opendev.org/openstack/murano-tempest-plugin

neutron
-------

Planning Artifacts:

The neutron team followed the documented steps outlined in this goal as the
planning document.

Completion Artifacts:

The following review removed the tempest plugin that neutron was maintaining
in tree and links to the new repository the plugin was moved to:

* https://review.opendev.org/506672

nova
----

Planning Artifacts:

* The nova team does not have tempest plugins and therefore has nothing
  to do.

Completion Artifacts:

* Not applicable.

octavia
-------

Planning Artifacts:

* `Octavia tracking story <https://storyboard.openstack.org/#!/story/2001387>`_

Completion Artifacts:

OpenStack Charms
----------------

Planning Artifacts:

* The OpenStack Charms team does not have tempest plugins and therefore has
  nothing to do.

Completion Artifacts:

* Not applicable.

OpenStackAnsible
----------------

Planning Artifacts:

* The OpenStackAnsible team does not have tempest plugins and therefore has
  nothing to do.

Completion Artifacts:

* The OpenStack Ansible Deployment tool is ready to handle the installation and configuration of
  tempest plugins.

OpenStackClient
---------------

Planning Artifacts:

* The OpenStackClient team does not have tempest plugins and therefore has
  nothing to do.

Completion Artifacts:

* Not applicable.

OpenStack-Helm
--------------

Planning Artifacts:

* The OpenStack-Helm team does not have tempest plugins and therefore has
  nothing to do.

Completion Artifacts:

* Not applicable.

oslo
----

Planning Artifacts:

* The oslo team does not have tempest plugins and therefore has nothing
  to do.

Completion Artifacts:

* Not applicable

Packaging-deb
-------------

Planning Artifacts:

* The Packaging-deb team does not have tempest plugins and therefore has
  nothing to do.

Completion Artifacts:

* Not applicable.

Packaging-rpm
-------------

Planning Artifacts:

* The Packaging-rpm team does not have tempest plugins and therefore has
  nothing to do.

Completion Artifacts:

* Not applicable.

Puppet OpenStack
----------------

Planning Artifacts:

* The Puppet OpenStack team does not have tempest plugins and therefore has
  nothing to do.

Completion Artifacts:

* Not applicable

Quality Assurance
-----------------

Planning Artifacts:

* The Quality Assurance team does not have tempest plugins and therefore has
  nothing to do.

Completion Artifacts:

* Not applicable.

rally
-----

Planning Artifacts:

* The rally team does not have tempest plugins and therefore has nothing
  to do.

Completion Artifacts:

* Not applicable

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

* The Release Management team does not have tempest plugins and therefore has
  nothing to do.

Completion Artifacts:

* Not applicable.

requirements
------------

Planning Artifacts:

* The requirements team does not have tempest plugins and therefore has
  nothing to do.

Completion Artifacts:

* Not applicable.

sahara
------

Planning Artifacts:

Completion Artifacts:

The Sahara team was already compliant before that the goal was defined. Here
is the commit link for the same:

https://opendev.org/openstack/sahara/commit/83a6a2868377dd61530a9de80c6ca49061c5f248

searchlight
-----------

Planning Artifacts:

* The searchlight team does not have tempest plugins and therefore has nothing
  to do.

Completion Artifacts:

* Not applicable.

Security
--------

Planning Artifacts:

* The Security team does not have tempest plugins and therefore has nothing
  to do.

Completion Artifacts:

* Not applicable.

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

The solum project does not have in-tree tempest plugin.

Completion Artifacts:

The solum team is maintaining its tempest plugin in a separate repo:

https://opendev.org/openstack/solum-tempest-plugin

Stable branch maintenance
-------------------------

Planning Artifacts:

* The Stable branch maintenance team does not have tempest plugins and
  therefore has nothing to do.

Completion Artifacts:

* Not applicable.

storlets
--------

Planning Artifacts:

* The storlets team does not have tempest plugins and therefore has nothing
  to do.

Completion Artifacts:

* Not applicable.

swift
-----

Planning Artifacts:

* The swift team does not have tempest plugins and therefore has nothing
  to do.

Completion Artifacts:

* Not applicable.

tacker
------

Planning Artifacts:

* The tacker team does not have tempest plugins and therefore has nothing
  to do.

Completion Artifacts:

* Not applicable.

Telemetry
---------

Planning Artifacts:

* The telemetry team followed the documented steps outlined in this goal as
  the planning document.

Completion Artifacts:

The following review removed the tempest plugin that telemetry team (Aodh,
Panko, Ceilometer) was maintaining in tree and links to the new
repository telemetry-tempest-plugin, was moved to:

* https://review.opendev.org/530467
* https://review.opendev.org/526299
* https://review.opendev.org/525072

tricircle
---------

Planning Artifacts:

* The tricircle team does not have tempest plugins and therefore has nothing
  to do.

Completion Artifacts:

* Not applicable.

tripleo
-------

Planning Artifacts:

The tripleo project does not have in-tree tempest plugin.

Completion Artifacts:

The tripleo team is maintaining its tempest plugin in a separate repo for
testing tripleo workflows:

https://opendev.org/openstack/tripleo-common-tempest-plugin

trove
-----

Planning Artifacts:

The trove team followed the documented steps outlined in this goal as the
planning document.

Completion Artifacts:

The following review removed the tempest plugin that trove was maintaining
in tree and links to the new repository the plugin was moved to:

* https://review.opendev.org/528533

vitrage
-------

Planning Artifacts:

The vitrage team followed the documented steps outlined in this goal as the
planning document.

Completion Artifacts:

The following review removed the tempest plugin that vitrage was maintaining
in tree and links to the new repository the plugin was moved to:

* https://review.opendev.org/528528

watcher
-------

Planning Artifacts:

The watcher team followed the documented steps outlined in this goal as the
planning document.

Completion Artifacts:

The following review removed the tempest plugin that watcher was maintaining
in tree and links to the new repository the plugin was moved to:

https://opendev.org/openstack/watcher/commit/0c4b439c5ea1206263f39c118daf6d2ff1422480

winstackers
-----------

Planning Artifacts:

The os-win project does not have in-tree tempest plugin.

Completion Artifacts:

The Winstackers team is maintaining its tempest plugin in a separate repo:

https://opendev.org/openstack/oswin-tempest-plugin

zaqar
-----

Planning Artifacts:

The watcher team followed the documented steps outlined in this goal as the
planning document.

Completion Artifacts:

https://review.opendev.org/504899 marks the removel of intree bundled tempest
plugin from Zaqar leading to marks the completion of the goal.

zun
---

Planning Artifacts:

Completion Artifacts:

The Zun team is maintaining its tempest plugin in a separate repo:

https://opendev.org/openstack/zun-tempest-plugin
