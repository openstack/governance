=============================================
2022-04-14 Drop Lower Constraints Maintenance
=============================================

History
-------

OpenStack has tried to maintain the lower bounds of dependency
in lower-constraints.txt file and also testing them in unit test
jobs on every project's repository. This was the best effort to tell
that these are the minimum versions of the dependencies you should
have in your environment for a particular OpenStack release.

Lower bounds of dependencies are present in lower-constraints.txt
as well as in requirements.txt file. The former one is used in lower
constraints unit testing job but latter one is not tested at all.

Challenges
----------

#. Lower constraints are not easy to test and they need more maintenance
   to keep them correct. In every distro upgrade in our testing, we spend
   most of the time fixing the lower constraints testing. In the Yoga cycle,
   it was broken by pip's latest resolver feature [1]_. From there discussion
   started on whether it is worthwhile to maintain and test these lower
   constraints [2]_ [3]_ [4]_.

#. We do not test them completely. The lower constraints are tested only in
   unit tests and we are not even sure that lower constraints maintained by one
   project are compatible with lower constraints maintained by the other
   dependent/related project. We can only manage the OpenStack direct
   dependencies lower bound since indirect dependencies, e.g. from packages
   outside of OpenStack, do not maintain compatible lower bounds.

#. We do not test them correctly. Before pip's coherent dependency resolver,
   we were testing with versions of dependencies that were different from
   what we thought they were [5]_. Adapting an individual project's
   lower-constraints.txt files to pass the coherent resolver was a lot of work,
   and revealed that there were problems maintaining transitive dependencies
   in the lower-constraints.txt (we were not systematically tracking when
   dependencies added new dependencies).

#. In the current situation, when we migrated the testing of lower constraints
   to min python version supported (python 3.8 on ubuntu focal) then it was
   failing on stable branches. This kind of python version migration requires
   a separate job to maintain for stable branches and master lower constraints
   testing.

#. To check lower constraints testing worthiness, TC did check who
   uses the lower constraints and it seems only Debian package maintainers
   use them as a reference and the rest of the distro/packagers use upper
   constraints [6]_. Based on that, TC agreed to explicitly clarify that the
   testing of lower constraints is optional and up to projects to keep or drop
   it [7]_. And many projects like Oslo have dropped it entirely, Neutron
   dropped it from all stable branches.

In summary, lower constraints and their testing is half baked and maintaining
them without correct and complete testing does not make sense. Distros can
always test the versions of their packages with OpenStack master code.

Proposal
--------
In Zed cycle PTG [8]_, after discussing all the challenges mentioned above, TC
agreed on the below points:

* Keep the lower bounds in the requirements.txt file with some statements at
  the top of this file saying that these are not confirmed or tested lower
  bounds and we try our best to keep them updated.

* Drop the lower-constraints.txt file, its env, and testing from master as
  well as from stable branches.


.. [1] http://lists.openstack.org/pipermail/openstack-discuss/2020-December/019521.html
.. [2] http://lists.openstack.org/pipermail/openstack-discuss/2021-January/019659.html
.. [3] http://lists.openstack.org/pipermail/openstack-discuss/2020-December/019390.html
.. [4] http://lists.openstack.org/pipermail/openstack-discuss/2021-January/019672.html
.. [5] http://lists.openstack.org/pipermail/openstack-discuss/2021-January/019921.html
.. [6] http://lists.openstack.org/pipermail/openstack-discuss/2021-February/020619.html
.. [7] http://lists.openstack.org/pipermail/openstack-discuss/2021-March/021204.html
.. [8] https://etherpad.opendev.org/p/tc-zed-ptg#L326
