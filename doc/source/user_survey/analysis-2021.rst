=====================================
Analysis of 2021 User Survey Feedback
=====================================

Introduction
------------

This is an analysis of the results from the 2021 User Survey in comparison to 
the `2019 results  <https://governance.openstack.org/tc/user_survey/analysis-2019.html>`_.
The 2019 User Survey result analysis is being used for comparison as
the TC did not perform an analysis of the 2020 User Survey results.
As with the previous analysis, the analysis will  be performed on a per-question
basis with an over-all summary at the end.

How do you upgrade your version of OpenStack?
---------------------------------------------

As with the 2019 User Survey, this is the question that got the greatest number of
responses.  Since responses to none of the questions are mandatory we need to infer the
total number that responded.  There were only a couple of respondents that answered other TC
questions while leaving this answer blank.  As a result, the number of responses, 276, was used
as the estimated total number of respondents to the TC's question.

+--------------------------------------------------------+-----------------+-------------------------+
| Response                                               | Number of Users | Percentage of Responses |
+--------------------------------------------------------+-----------------+-------------------------+
| Upgrade all coordinated releases (once every 6 months) |        83       |            30           |
+--------------------------------------------------------+-----------------+-------------------------+
| Skip/Fast-forward releases                             |        91       |            33           |
+--------------------------------------------------------+-----------------+-------------------------+
| Not Upgrade                                            |        65       |            23           |
+--------------------------------------------------------+-----------------+-------------------------+
| Deploy Regularly from master branch                    |        13       |             5           |
+--------------------------------------------------------+-----------------+-------------------------+
| Deploy all intermediary releases and all               |        20       |             7           |
| coordinated releases                                   |                 |                         |
+--------------------------------------------------------+-----------------+-------------------------+

The total number of responses for 2021 was somewhat lower than the 337 responses that
were submitted in 2019.  There are a couple of positive trends, however, to notice.  The first one
being that the number of 'Not Upgrade' responses decreased significantly.  In 2019 35% of
respondents indicated they did not upgrade as compared to 23% in 2021.  The percentage of users
that indicated that they 'Deployed Regularly from master branch' also decreased from 9% to 5%
while 'Deploy all intermediary releases and all coordinated releases' stayed constant at 7%.

The increase in users upgrading their releases appears to be pretty evenly spread, percentage wise,
between 'Upgrade all coordinated releases (once every 6 months)' and 'Skip/Fast-forward releases'
increasing from 22% to 30% and 27% to 33% respectively.  Unfortunately, we don't know that the
respondents that no longer indicated that they did not upgrade are the same ones that now indicate
that they do upgrade.  With that said, the decrease does appear to be a positive trend.  It will be
worth watching these results in subsequent surveys to see if that trend continues.

One other data point worth noting is the fact that we have reached a point where the number of
users using the 'Upgrade all coordinated releases' and 'Skip/Fast-forward releases' options
are comparable.  The TC sees this as an indication that the changes we have made in the
release process to allow doing Skip/Fast-forward upgrades have been worth the effort that
was required.  As we continue to improve/refine the upgrade options these are data points
that we will want to continue to watch.
 
Once on a given release, do you use stable branches for bug-fix upgrades?
-------------------------------------------------------------------------

Consistent with the 2019 survey, the number of responses to this question was high, at 265 responses
and had a notable total increase from 216 responses in 2019.

+-------------------------------------------------------------+-------+-------------------------+
| Answer                                                      | Users | Percentage of Responses |
+-------------------------------------------------------------+-------+-------------------------+
| I do not do bug-fix upgrades                                |   46  |            17           |
+-------------------------------------------------------------+-------+-------------------------+
| Yes, backporting specific fixes                             |   44  |            17           |
+-------------------------------------------------------------+-------+-------------------------+
| Yes, deploying every commit on the stable branch            |   18  |            7            |
+-------------------------------------------------------------+-------+-------------------------+
| Yes, upgrading at various points in time depending on fixes |   75  |            28           |
+-------------------------------------------------------------+-------+-------------------------+
| Yes, using only official point releases                     |   79  |            30           |
+-------------------------------------------------------------+-------+-------------------------+

The responses in 2021 were very consistent with the 2019 results.  The number of users reporting
that they do not do bug-fix upgrades or backport specific fixes decreased from 19% and
21% respectively. The number of respondents that indicate that they only deploy official point
releases also decreased slightly from 31% to 30%.

While the number of users to indicate that they deploy every commit remained the least reported
approach, it did increase from 4% in 2019 to 7% in 2021.  Users indicating that they upgrade
depending on the fixes available increased from 26% to 28%.

So, overall, the results for this question in the 2021 survey were consistent with those collected in 2019.

To which projects does your organization contribute maintenance resources such as patches for bug and reviews on master or stable branches?
-------------------------------------------------------------------------------------------------------------------------------------------

This question had a good increase in responses compared to 2019, with only about 33% of users
responding previously compared to 128, or 46%, in 2021.  As in 2019, the majority of contributions
are made to `core projects
<https://docs.openstack.org/security-guide/introduction/introduction-to-openstack.html#openstack-service-overview>`_ .
There is, however, a new entry in the top five projects: Kolla.

`Kolla <https://wiki.openstack.org/wiki/Kolla>`_ is an OpenStack community project that provides
production ready containers and deployment tools for operating OpenStack clouds.  Given the
continued growth in popularity of containerizing workloads, the increase in contributors is
not particularly surprising and would seem to be a good sign for OpenStack as users are seeking
newer and better ways to deploy OpenStack clouds.

All of the projects in the top 5 showed a notable increase in reported participation from the
2019 survey.  While Glance was knocked out of the Top 5 projects, it still had a reported
increase from 25 respondents indicating activity in the project to 27.

+----------+--------------+
| Project  | Contributors |
+----------+--------------+
| Nova     |      63      |
+----------+--------------+
| Neutron  |      56      |
+----------+--------------+
| Cinder   |      40      |
+----------+--------------+
| Keystone |      34      |
+----------+--------------+
| Kolla    |      34      |
+----------+--------------+

After the first review of these results in the 2019 user survey,
the TC wanted to compare the number of respondents who reported they
used a project as compared to the number who reported that they contribute
to the project.  For the 2021 results review we have continued this analysis
but have also added the previous percentage of participation for
reference.  To get this information we considered the number of
users who reported that they were using the project in production.
Note that we did not count users who indicated that they were just
testing a service or who indicated that they had the service
installed as part of a Proof of Concept.  So the number of users
that are using any given service may be notably larger than
indicated in the results below.  Here are the results of
that investigation.

+-------------------+--------------+-------+-----------------+----------------------+
| Project           | Contributors | Users | % Participation | 2019 % Participation |
+-------------------+--------------+-------+-----------------+----------------------+
| Aodh              | 3            | 31    |        9        |           25         |
+-------------------+--------------+-------+-----------------+----------------------+
| Barbican          | 8            | 70    |       11        |           19         |
+-------------------+--------------+-------+-----------------+----------------------+
| Blazar            | 6            | 4     |       150       |          100         |
+-------------------+--------------+-------+-----------------+----------------------+
| Ceilometer        | 10           | 84    |       12        |           14         |
+-------------------+--------------+-------+-----------------+----------------------+
| Cinder            | 40           | 216   |       19        |           9          |
+-------------------+--------------+-------+-----------------+----------------------+
| Cloudkitty        | 4            | 12    |       33        |           23         |
+-------------------+--------------+-------+-----------------+----------------------+
| Cyborg            | 3            | 4     |       75        |          100         |
+-------------------+--------------+-------+-----------------+----------------------+
| Designate         | 13           | 55    |       24        |           25         |
+-------------------+--------------+-------+-----------------+----------------------+
| Glance            | 27           | 231   |       12        |           8          |
+-------------------+--------------+-------+-----------------+----------------------+
| Heat              | 13           | 164   |        8        |           8          |
+-------------------+--------------+-------+-----------------+----------------------+
| Horizon           | 18           | 224   |        8        |           6          |
+-------------------+--------------+-------+-----------------+----------------------+
| Ironic            | 23           | 65    |       35        |           27         |
+-------------------+--------------+-------+-----------------+----------------------+
| Keystone          | 34           | 235   |       15        |           9          |
+-------------------+--------------+-------+-----------------+----------------------+
| Kolla             | 34           | 69    |       49        |           52         |
+-------------------+--------------+-------+-----------------+----------------------+
| Kuryr             | 5            | 8     |       63        |           71         |
+-------------------+--------------+-------+-----------------+----------------------+
| LOCI              | 3            | 7     |       43        |           40         |
+-------------------+--------------+-------+-----------------+----------------------+
| Magnum            | 13           | 42    |       31        |           29         |
+-------------------+--------------+-------+-----------------+----------------------+
| Manila            | 13           | 26    |       50        |           23         |
+-------------------+--------------+-------+-----------------+----------------------+
| Masakari          | 2            | 14    |       14        |           17         |
+-------------------+--------------+-------+-----------------+----------------------+
| Mistral           | 8            | 23    |       35        |           35         |
+-------------------+--------------+-------+-----------------+----------------------+
| Monasca           | 4            | 33    |       12        |           23         |
+-------------------+--------------+-------+-----------------+----------------------+
| Murano            | 3            | 6     |       50        |           18         |
+-------------------+--------------+-------+-----------------+----------------------+
| Neutron           | 56           | 229   |       24        |           15         |
+-------------------+--------------+-------+-----------------+----------------------+
| Nova              | 63           | 230   |       27        |           15         |
+-------------------+--------------+-------+-----------------+----------------------+
| Octavia           | 26           | 89    |       29        |           35         |
+-------------------+--------------+-------+-----------------+----------------------+
| OpenStack Client  | 21           | 191   |       11        |           8          |
+-------------------+--------------+-------+-----------------+----------------------+
| OpenStack Ansible | 27           | 59    |       46        |           38         |
+-------------------+--------------+-------+-----------------+----------------------+
| OpenStack Helm    | 5            | 14    |       36        |           23         |
+-------------------+--------------+-------+-----------------+----------------------+
| Panko             | 3            | 7     |       43        |           45         |
+-------------------+--------------+-------+-----------------+----------------------+
| QA                | 2            | N/A   |       N/A       |           N/A        |
+-------------------+--------------+-------+-----------------+----------------------+
| Rally             | 6            | 44    |       14        |           16         |
+-------------------+--------------+-------+-----------------+----------------------+
| Sahara            | 1            | 2     |       50        |           21         |
+-------------------+--------------+-------+-----------------+----------------------+
| Senlin            | 4            | 5     |       80        |           N/A        |
+-------------------+--------------+-------+-----------------+----------------------+
| Swift             | 19           | 102   |       19        |           11         |
+-------------------+--------------+-------+-----------------+----------------------+
| Tacker            | 1            | 3     |       33        |           75         |
+-------------------+--------------+-------+-----------------+----------------------+
| Trove             | 4            | 14    |       29        |           15         |
+-------------------+--------------+-------+-----------------+----------------------+
| TripleO           | 11           | 26    |       42        |           16         |
+-------------------+--------------+-------+-----------------+----------------------+
| Watcher           | 2            | 6     |       33        |           N/A        |
+-------------------+--------------+-------+-----------------+----------------------+
| Zaqar             | 2            | 9     |       22        |           23         |
+-------------------+--------------+-------+-----------------+----------------------+
| Zun               | 2            | 8     |       25        |           N/A        |
+-------------------+--------------+-------+-----------------+----------------------+

A couple of things to note from the results above.  The numbers seem to
confirm one concern that has been previously raised within the community.
There appear to be a number of the smaller projects that are being used
and maintained by a small group of OpenStack users.  It is also interesting
the disparity between the number of users and contributors for the core
projects like Cinder, Glance, Horizon and Keystone.  It is unclear from
these results as to whether the disparity is because these projects
have become more stable and don't require as much development or
if there are other reasons for this disparity.

When considering the percentage of participation as compared to the 2019
User Survey results there are a number of things to note.  First, there
has not been a notable decrease in user participation across projects.
Also, it is interesting to note that a majority of projects continued to
have consistent numbers as compared to  the previous survey.  A number of projects
even showed an increase in participation.  This is true for many of the
core projects like Cinder, Keystone, Glance, Ironic, Neutron and Nova.
We don't know if these changes are due to a change in the demographics of
the respondents (more user/developers responding vs. just users) or if it
is a positive indication in the health of the community.  Overall, a key take
away would be that project participation has remained largely stable or grown
slightly since the last user survey.

How do members of your organization contribute to OpenStack?
------------------------------------------------------------

As with the other questions in the user survey, this question also saw an increase
in responses.  173 users responded for a total of 63% of the total.

+----------------------------------------------+-------+-------------------------+
| Contribution                                 | Users | Percentage of Responses |
+----------------------------------------------+-------+-------------------------+
| Bug reports                                  |  173  |            100          |
+----------------------------------------------+-------+-------------------------+
| Bug fixes on master                          |   85  |            49           |
+----------------------------------------------+-------+-------------------------+
| Participate in forum sessions at the summit  |   59  |            34           |
+----------------------------------------------+-------+-------------------------+
| Participate in PTG sessions                  |   44  |            25           |
+----------------------------------------------+-------+-------------------------+
| Code review on master                        |   43  |            25           |
+----------------------------------------------+-------+-------------------------+
| Particpate in ops meetups                    |   43  |            25           |
+----------------------------------------------+-------+-------------------------+
| Documentation improvement                    |   39  |            23           |
+----------------------------------------------+-------+-------------------------+
| Backporting bug fixes to stable branches     |   37  |            21           |
+----------------------------------------------+-------+-------------------------+
| Sponsor in-person events                     |   28  |            16           |
+----------------------------------------------+-------+-------------------------+
| Code review on stable branches               |   26  |            15           |
+----------------------------------------------+-------+-------------------------+
| Feature design review                        |   22  |            13           |
+----------------------------------------------+-------+-------------------------+
| Contribute resources to run CI jobs upstream |   8   |            5            |
+----------------------------------------------+-------+-------------------------+
| Host third-party CI jobs downstream          |   4   |            2            |
+----------------------------------------------+-------+-------------------------+

In the 2019 survey the TC noted that the responses are very interesting given that
this is a 'User Survey'.  The responses show that OpenStack is unique in the fact that
it is a user driven community with many of the users also being contributors.  In fact
we had more respondents indicating that they contributed to OpenStack than in 2019.

A couple of things of interest to note.  First, the number of respondents that indicated
they contributed bug reports increased notably from 86% in 2019 to 100% in 2021.  More
importantly, the number of users that indicated that they contribute bug fixes on master
increased from 36% to 49%.  This takes this response from 4th most popular way of
contributing to 2nd!

Some of the decreased numbers in participation are likely to be due to the pandemic that
we all have been dealing with.  Reported participation in summit sessions and ops meetups
both decreased from 47% to 34% and 39% to 25% respectively.  Similarly, sponsorship of
in-person events dropped from 20% to 16%.  These drops, however, are not as significant as
expected given the pandemic, which leads to TC to question these results.  For future surveys
we may want to look at the wording of the questions.  Perhaps users are responding based
upon all previous activity, not just the activity since the last user survey.

A decrease in participation that could have been anticipated by many of the community
members is in code reviews for both master and stable branches.  The number of users indicating
participating in these activities decreased by 6% for master code reviews and 5% for stable
branch reviews.  This is consistent with what has been seen in many of the projects.  Code is
being submitted but the time required to get patches reviewed and merged has increased. This
is also contributed to by a notable decrease in participants hosting third-party and CI job
resources.

The rest of the participation responses were relatively consistent with what was reported
in the 2019 User Survey.

What prevents you or your organization from contributing more maintenance resources, or makes contributing difficult?
---------------------------------------------------------------------------------------------------------------------

This question is the one that had the most notable increase in
responses from 2019.  Only 19% of users (69) responded to this
question previously as compared to 47% (131) in 2021.  This could
be taken in a positive light, that more users are thinking
about contributing.  Unfortunately, the challenges continue to
be similar.

Some combination of time, resources and company support accounted
for more than half of the responses.  Not having the appropriate skills
to contribute was also a common theme in the responses.  The TC might
be able to help with this by raising awareness of the OpenStack Jobs
board.

A few responses indicated that they felt that they were not able to
contribute because the version of OpenStack that they are on was
so far behind the current release.  This response seems somewhat
surprising as problems found in the older releases may still need to
be fixed in the current release.  In some cases, it is possible that
the code will have changed significantly from the release that is running.
With that said, this is a response that probably deserves further
discussion by the TC.

The other response that was repeated by at least a few users was
communication and timezone barriers.  This is a challenge that has
been known by the TC and OpenInfra Foundation for some time.  Changes
have been made to try to alleviate some of this problem but it
sounds like it hasn't worked for everyone.

Other ways users participate:
-----------------------------

This was the field that we changed the wording for from the 2019 user
survey.  There were only two responses submitted: one listing bug reports
again and one indicating that they work with vendors to submit requests
for enhancement.

So, this field is not getting a lot of input.  Worth discussion among the
TC as to whether this should be removed or replaced with a different
question.

Summary
-------

In summary, the questions being asked by the TC in the User Survey are providing
useful information.  While it was unfortunate to see the total number of
responses decrease, the fact that we had higher participation responding to the
TC's questions is encouraging.  Hopefully this trend will continue as the numbers
are more meaningful as we have more years of data for comparison.

It is also encouraging to see the numbers moving in the desired direction for
a number of the questions that we are asking.  The responses to how/when users are
upgrading their OpenStack clouds seems to suggest that the efforts of the TC and
the community as a whole have had a positive impact on the user experience, or at
least their upgrade habits.  The overall improvement in user engagement, participating
in the community is also encouraging.  The data suggests that the OpenStack
community continues to be a consistently active one.

All-in-all, the TC is pleased with the continued responses we are getting and
would like to continue to collect this data for future analysis.

Additional Resources
--------------------

The `OpenStack Survey Report
<https://www.openstack.org/analytics>`_ also provides
a graphical overview of the OpenStack Survey
results.
