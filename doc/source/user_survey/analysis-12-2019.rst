=====================================
Analysis of 2019 User Survey Feedback
=====================================

Introduction
------------

The OpenStack Technical Committee (TC) added questions to the User Survey for
the first time in 2019.  The following questions were asked by the TC:

* How do you upgrade your version of OpenStack?
* Once on a given release, do you use stable branches for bugfix upgrades?
* To which projects does your organization contribute maintenance resources,
  such as patches for bug fixes and code reviews on master or stable
  branches?
* How do members of your organization contribute to OpenStack?
* What prevents you or your organization from contributing more maintenance
  resources, or makes contributing difficult?
* Other ways to participate?

The intention of these questions was to understand how users are maintaining
their OpenStack clouds and how they are interacting with the community.  In the
case that they weren't currently interacting with the community it was hoped
that the questions would spark thoughts on how they could participate in the
future.

In general the TC was pleased with the number of responses they got to the
questions and the information provided.  As a result it was decided that the
TC won't revise the questions before the next User Survey.  The plan is to
look at the responses to the next survey and then decide if any questions need
to be revised or changed.

Below we will summarize the responses that were received to each of the
questions:

How do you upgrade your version of OpenStack?
---------------------------------------------

This is the question to which we got the greatest response.  The following
were the available responses to choose from and the associated number of
responses:

+--------------------------------------------------------+-----------------+-------------------------+
| Question                                               | Number of Users | Percentage of Responses |
+--------------------------------------------------------+-----------------+-------------------------+
| Upgrade all coordinated releases (once every 6 months) |        73       |            22           |
+--------------------------------------------------------+-----------------+-------------------------+
| Skip/Fast-forward releases                             |        91       |            27           |
+--------------------------------------------------------+-----------------+-------------------------+
| Not Upgrade                                            |       119       |            35           |
+--------------------------------------------------------+-----------------+-------------------------+
| Deploy Regularly from master branch                    |        30       |             9           |
+--------------------------------------------------------+-----------------+-------------------------+
| Deploy all intermediary releases and all               |        24       |             7           |
| coordinated releases                                   |                 |                         |
+--------------------------------------------------------+-----------------+-------------------------+

So the responses here were spread pretty widely.  The number of users who
respond that they don't upgrade explains why there are so many people still
running on releases like Mitaka and Newton.  The number of users that do
skip or fast-forward updates supports the efforts that have gone into making
such an upgrade path possible.

For a future survey it would be interesting to ask the users who are not
upgrading why that is the case.  Would be good to know if this is due to it
being seen as too dificult a thing to do or if it is just that the users
don't see a need.  At this point, however, the TC doesn't feel that the
current results warrant a revision to the questions.

Once on a given release, do you use stable branches for bugfix upgrades?
------------------------------------------------------------------------

This question also had good participation with about two thirds of the users
responding to the question.  The responses were also pretty evenly spread
across four of the five options:

+-------------------------------------------------------------+-------+-------------------------+
| Answer                                                      | Users | Percentage of Responses |
+-------------------------------------------------------------+-------+-------------------------+
| I do not do bugfix upgrades                                 |   40  |            19           |
+-------------------------------------------------------------+-------+-------------------------+
| Yes, backporting specific fixes                             |   45  |            21           |
+-------------------------------------------------------------+-------+-------------------------+
| Yes, deploying every commit on the stable branch            |   9   |            4            |
+-------------------------------------------------------------+-------+-------------------------+
| Yes, upgrading at various points in time depending on fixes |   56  |            26           |
+-------------------------------------------------------------+-------+-------------------------+
| Yes, using only official point releases                     |   66  |            31           |
+-------------------------------------------------------------+-------+-------------------------+

Not surprisingly, deploying every commit being the least popular option.
The fact that the majority of users reported using the official point
releases speaks to the importance of continuing to do stable releases.

Similar to the previous question, it would be interesting to know why the
people who do not do bugfix upgrades choose that route.  It would also be
interesting to correlate if these are the same people who responded that
they don't upgrade at all or if this is a different group of users that
go from major release to major release only.

To which projects does your organization contribute maintenance resources such as patches for bug and reviews on master or stable branches?
-------------------------------------------------------------------------------------------------------------------------------------------

About one third of users responded to this question.  The results
were as one would expect with `core projects
<https://docs.openstack.org/security-guide/introduction/introduction-to-openstack.html#openstack-service-overview>`_ having the
greatest participation.  The top 5 were as follows:

+----------+-------+
| Project  | Users |
+----------+-------+
| Nova     | 45    |
+----------+-------+
| Neutron  | 43    |
+----------+-------+
| Cinder   | 27    |
+----------+-------+
| Keystone | 26    |
+----------+-------+
| Glance   | 25    |
+----------+-------+

In discussing these results the TC wanted to know how this
compared to the number of users who report they are using the
project.  To get this information we considered the number of
users who reported that they were using the project in production
with one exception.  Karbor had 4 respondents report they were using
it but only 3 in production so the number of respondents that
indicated they were testing it was used.  Here are the results of
that investigation:

+-------------------+--------------+-------+-----------------+
| Project           | Contributors | Users | % Participation |
+-------------------+--------------+-------+-----------------+
| Aodh              | 12           | 48    | 25%             |
+-------------------+--------------+-------+-----------------+
| Barbican          | 9            | 48    | 19%             |
+-------------------+--------------+-------+-----------------+
| Blazar            | 3            | 3     | 100%            |
+-------------------+--------------+-------+-----------------+
| Ceilometer        | 21           | 153   | 14%             |
+-------------------+--------------+-------+-----------------+
| Cinder            | 27           | 285   | 9%              |
+-------------------+--------------+-------+-----------------+
| Cloudkitty        | 3            | 13    | 23%             |
+-------------------+--------------+-------+-----------------+
| Cyborg            | 2            | 2     | 100%            |
+-------------------+--------------+-------+-----------------+
| Designate         | 15           | 61    | 25%             |
+-------------------+--------------+-------+-----------------+
| Glance            | 25           | 296   | 8%              |
+-------------------+--------------+-------+-----------------+
| Heat              | 18           | 212   | 8%              |
+-------------------+--------------+-------+-----------------+
| Horizon           | 17           | 271   | 6%              |
+-------------------+--------------+-------+-----------------+
| Ironic            | 21           | 77    | 27%             |
+-------------------+--------------+-------+-----------------+
| Karbor            | 4            | 7     | 57%             |
+-------------------+--------------+-------+-----------------+
| Keystone          | 26           | 291   | 9%              |
+-------------------+--------------+-------+-----------------+
| Kolla             | 24           | 46    | 52%             |
+-------------------+--------------+-------+-----------------+
| Kuryr             | 5            | 7     | 71%             |
+-------------------+--------------+-------+-----------------+
| LOCI              | 2            | 5     | 40%             |
+-------------------+--------------+-------+-----------------+
| Magnum            | 14           | 48    | 29%             |
+-------------------+--------------+-------+-----------------+
| Manila            | 9            | 39    | 23%             |
+-------------------+--------------+-------+-----------------+
| Masakari          | 1            | 6     | 17%             |
+-------------------+--------------+-------+-----------------+
| Mistral           | 9            | 26    | 35%             |
+-------------------+--------------+-------+-----------------+
| Monasca           | 5            | 22    | 23%             |
+-------------------+--------------+-------+-----------------+
| Murano            | 3            | 17    | 18%             |
+-------------------+--------------+-------+-----------------+
| Neutron           | 43           | 294   | 15%             |
+-------------------+--------------+-------+-----------------+
| Nova              | 45           | 297   | 15%             |
+-------------------+--------------+-------+-----------------+
| Octavia           | 23           | 66    | 35%             |
+-------------------+--------------+-------+-----------------+
| OpenStack Client  | 15           | 192   | 8%              |
+-------------------+--------------+-------+-----------------+
| OpenStack Ansible | 24           | 63    | 38%             |
+-------------------+--------------+-------+-----------------+
| OpenStack Helm    | 3            | 13    | 23%             |
+-------------------+--------------+-------+-----------------+
| Panko             | 9            | 20    | 45%             |
+-------------------+--------------+-------+-----------------+
| Rally             | 9            | 57    | 16%             |
+-------------------+--------------+-------+-----------------+
| Sahara            | 5            | 24    | 21%             |
+-------------------+--------------+-------+-----------------+
| Swift             | 15           | 141   | 11%             |
+-------------------+--------------+-------+-----------------+
| Tacker            | 6            | 8     | 75%             |
+-------------------+--------------+-------+-----------------+
| Trove             | 4            | 27    | 15%             |
+-------------------+--------------+-------+-----------------+
| TripleO           | 9            | 34    | 16%             |
+-------------------+--------------+-------+-----------------+
| Zaqar             | 3            | 13    | 23%             |
+-------------------+--------------+-------+-----------------+

It is interesting to note how the rate of participation in
the core projects is generally lower than other projects. As we
don't have this data from previous surveys we can't tell if this
rate of participation has been consistent over time or if it has
changed. It will be worthwhile to continue to look at these numbers
in future surveys.

Another interesting thing to note in the results is the fact that
users who responded, generally contributed to more than one
project.  There were a few examples where contribution to
only one project was indicated, but this was not the majority
case.

How do members of your organization contribute to OpenStack?
------------------------------------------------------------

More than half of the users responded to this question.  For
the most part the answers were evenly spread with the
exception of submitting bug reports which was the clear
winner for participation.  Here is the breakdown:

+----------------------------------------------+-------+-------------------------+
| Contribution                                 | Users | Percentage of Responses |
+----------------------------------------------+-------+-------------------------+
| Bug reports                                  |  123  |            86           |
+----------------------------------------------+-------+-------------------------+
| Participate in forum sessions at the summit  |   70  |            47           |
+----------------------------------------------+-------+-------------------------+
| Pariticpate in ops meetups                   |   57  |            39           |
+----------------------------------------------+-------+-------------------------+
| Bug fixes on master                          |   54  |            36           |
+----------------------------------------------+-------+-------------------------+
| Documentation improvement                    |   49  |            33           |
+----------------------------------------------+-------+-------------------------+
| Code review on master                        |   46  |            31           |
+----------------------------------------------+-------+-------------------------+
| Participate in PTG sessions                  |   38  |            26           |
+----------------------------------------------+-------+-------------------------+
| Backporting bug fixes to stable branches     |   34  |            23           |
+----------------------------------------------+-------+-------------------------+
| Feature design review                        |   33  |            22           |
+----------------------------------------------+-------+-------------------------+
| Code review on stable branches               |   30  |            20           |
+----------------------------------------------+-------+-------------------------+
| Sponsor in-person events                     |   30  |            20           |
+----------------------------------------------+-------+-------------------------+
| Host third-party jobs downstream             |   13  |            9            |
+----------------------------------------------+-------+-------------------------+
| Contribute resources to run CI jobs upstream |   12  |            8            |
+----------------------------------------------+-------+-------------------------+

Keeping in mind that this was a user survey, these
results are very interesting.  Over one quarter
of the users that responded submit bug fixes on
master and nearly as many also do code reviews.
Many of the users are also taking advantage of the
Forum Sessions and Ops Meetups.  As with the previous
question, it seemed that users who participated indicated
participation in multiple ways.

This would seem to support one of the things that
we highlight as being unique about our community.  We
are users and developers collaborating together.

What prevents you or your organization from contributing more maintenance resources, or makes contributing difficult?
---------------------------------------------------------------------------------------------------------------------

This question elicited a response from 19% of the participants.
The field was also a free-form field, rather than multiple
choice which seems to generally get fewer response.

Of the 69 user responses, the majority of them had
to do with a lack of time or human resources.  Other
responses indicated that they were busy running
their data centers, going along with the theme
of insufficient time.

There were a few surprising responses with regards to
it not being clear how to contribute.  Hopefully
the user survey got them thinking about other
ways to contribute.  There has been a good focus
in OpenStack on making how to contribute easier
to understand both through documentation and
through education opportunities.  Perhaps there
is a need to better socialize these opportunities?

Other ways to participate:
--------------------------

This was another free-form field that only got responses
from 1% of participants. There were a few responses
that are worth noting as they show other ways
that users work to participate.

There were responses indicating that they particpate
in OpenStack User Groups.  Doing such things
is important to keep communication in the
community flowing.  Another user indicated that
they write blogs on how to do things.  We talk
about documentation as a way to contribute but
forget to mention that blogs can also be a great
way to contribute and share information.  Similarly,
another user indicated that they help write
troubleshooting guides.  Another great way to help
the wider community.  Finally, one other user indicated
that they work with their distributor to communicate
and create requirements for future enhancements.
This was interesting as it is an indication
that we may not directly see the ways that people
are participating with the community.

All-in-all these responses continued to support
the collaborative nature of the OpenStack community.

Summary
-------

The TC was pleased with the first round of answers
we got from the User Survey.  We don't feel a need
to change the questions for the next survey.  This
will give us a chance to see if responses are
consistent between surveys or if there appears to be
variation.  After that round we may choose
to refine the questions.

There weren't any really surprising responses this
time around.  The collaborative nature of OpenStack
Users is aparent in the results.  We will want to
ensure that we don't see a decline in those numbers.
In the mean time, we should be proud of the unique
and diverse nature of the community we have helped to
develop.

Additional Resources
--------------------

For those interested in more details please see the
`mailing list <http://lists.openstack.org/pipermail/openstack-discuss/2019-September/009501.html>`_
thread that includes the results that were used to
create this analysis.  The `OpenStack Survey Report
<https://www.openstack.org/analytics>`_ also provides
a graphical overview of the OpenStack Survey
results.
