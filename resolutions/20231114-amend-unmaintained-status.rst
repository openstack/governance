=====================================================
 2023-11-14 openstack-unmaintained-core Gerrit Group
=====================================================

Amendment
---------

The resolution :doc:`20230724-unmaintained-branches` contains the following
text in the "Unmaintained branches" section:

- A group in Gerrit called "<project>-unmaintained-core", for example,
  "keystone-unmaintained-core", will have +2/+W on these branches. This group
  may be bootstrapped with or include the "<project>-stable-maint" group, but
  membership is separate from that group.

The above point is hereby replaced by the following two points:

- A group in Gerrit called "openstack-unmaintained-core" will by default have
  +2/+W on these branches for all projects.  This group will be self-managed
  and will be owned by the OpenStack Technical Committee.  The Technical
  Committee will only have the ability to maintain group membership; TC
  members will not be members of openstack-unmaintained-core through their
  membership in the TC.

- Each individual project team has the option to create a group in Gerrit
  called "<project>-unmaintained-core", for example,
  "keystone-unmaintained-core", that has +2/+W solely on that project's
  "unmaintained/\*" branches.  This group may be bootstrapped with or include
  the "<project>-stable-maint" group, but membership is separate from that
  group.  Further, this group may override the powers of the
  openstack-unmaintained-core group for the project's Unmaintained branches.

Effect of this Change
---------------------

- There is an OpenStack-wide group with the responsibility to handle branches
  in Unmaintained status across all projects.
- It is possible for individual project teams to override the OpenStack-wide
  group for that project's Unmaintained branches.
