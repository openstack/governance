=================================================================
 2017-07-18 Allow for meetings to happen outside meeting channels
=================================================================

Meeting channels have been a part of the OpenStack community for quite a while.
These channels have provided a way for members of the community to schedule
their team meetings in a central, known, place where they would have:

* Ease of cross-team communications (since several folks kept presence in
  meeting channels at all times)
* Guarantee that every meeting would be logged
* Fewer overlaps of meetings
* Avoidance of silos

Central meeting channels worked very well for this long because the community
was small in terms of existing projects, which made it relatively easy to find a
free spots among the available channels.

Unfortunately, this model is not scaling well for the community anymore. The
number of existing projects has outgrown the number of usable slots and channels
a couple of times already. We started adding new meeting channels, stretching
this model as much as possible, as the community grew but doing so resulted in
an unmanageable number of meeting channels and projects very soon.

There have been several discussions on the mailing list suggesting to move on
from this model. An agreement was reached in the `latest discussion
<http://lists.openstack.org/pipermail/openstack-dev/2017-June/118899.html>`_ in
favor of adopting the model presented in this resolution.

The new proposed model is to allow teams to host meetings in their own channels.
By doing this we would solve the following issues:

* Easier to know where teams meet.
* The need for more meeting channels
* Scheduling nightmares due to best spots having been taken already

The main drawbacks of this new model are:

* It is harder to ensure arbitrary channels are logged
* It will be harder to ping folks during meetings if they are not in the meeting channel
* It might increase the number of overlapping meetings
* It might increase the silo effect if some teams, too focussed on their
  meetings, fail to communicate on the mailing lists.

The discussion on the mailing list thread suggests that these objections can be
worked on. Some of the points can be automated - ensuring channels are logged,
for example - whereas others require doing more community work to ensure
cross-communication is not lost with the new model.

This model and other recent changes in the community encourage project
teams to rely more on the mailing list and to provide team updates. By doing
this, we'll make sure more information about every project is available to other
members of the community in a common place.

This resolution doesn't propose eliminating the existing meeting channels nor
rescheduling existing meetings. Project teams are free to keep their meetings
where they are.

It is also worth noting that the requirement on meetings has been `dropped
<https://review.opendev.org/#/c/462077/>`_. This change not only removed the
need for teams to hold meetings but encouraged other forms of synchronous
communications like office-hours, which the Technical Committee is
`experimenting with already <https://review.opendev.org/#/c/462077/>`_.

Considering the several discussions there have been, the results of the latest
discussion, the latest changes around meetings and community interactions, it
makes sense for the community to also relax the rule on where meetings should be
held. Give project teams more freedom to schedule their office-hours, meetings
and other, planned, synchronous communications.
