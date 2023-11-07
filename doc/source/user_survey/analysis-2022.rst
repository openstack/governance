=====================================
Analysis of 2022 User Survey Feedback
=====================================

Introduction
------------

This is an analysis of the results from the 2022 User Survey in comparison to
the `2021 results  <https://governance.openstack.org/tc/user_survey/analysis-2021.html>`_.
As with the previous analysis, the analysis will  be performed on a per-question
basis with an over-all summary at the end.

How do you upgrade your version of OpenStack?
---------------------------------------------

+---------------------------------------------------------------+-------+-------------------------+
| Response                                                      | Users | Percentage of Responses |
+---------------------------------------------------------------+-------+-------------------------+
| Skip/fast-forward releases                                    |   84  |           34            |
+---------------------------------------------------------------+-------+-------------------------+
| Upgrade all coordinated releases (once every 6 months)        |   75  |           30            |
+---------------------------------------------------------------+-------+-------------------------+
| Not upgrade                                                   |   65  |           26            |
+---------------------------------------------------------------+-------+-------------------------+
| Deploy regularly from the master branch                       |   12  |           4             |
+---------------------------------------------------------------+-------+-------------------------+
| Deploy all intermediary releases and all coordinated releases |   12  |           4             |
+---------------------------------------------------------------+-------+-------------------------+

The total number of responses was slightly lower than in the 2021 survey - 272
in 2021 and 249 in 2022.
Results in this year's survey are almost the same as from last year. The only
differences are a small increase of users who do not do upgrades and in the same
time decrease amount of users who deploy all intermediary releases and all
coordinated releases. But as differences are small (2-3%) this doesn't show any
significant change.
It is very interesting how results of this question will change (or not) in next
year's survey, when SLURP releases will be available.

Once on a given release, do you use stable branches for bug-fix upgrades?
-------------------------------------------------------------------------

Number of responses for this question was a bit smaller than in 2021, similar
to the previous questions. There were 235 responses in 2022 compared to the 265
in the 2021 survey.

+-------------------------------------------------------------+-------+-------------------------+
| Response                                                    | Users | Percentage of Responses |
+-------------------------------------------------------------+-------+-------------------------+
| I do not do bugfix upgrades                                 |   39  |           17            |
+-------------------------------------------------------------+-------+-------------------------+
| Yes, backporting specific fixes                             |   50  |           21            |
+-------------------------------------------------------------+-------+-------------------------+
| Yes, deploying every commit on the stable branch            |   16  |            7            |
+-------------------------------------------------------------+-------+-------------------------+
| Yes, upgrading at various points in time depending on fixes |   71  |           30            |
+-------------------------------------------------------------+-------+-------------------------+
| Yes, using only official point releases                     |   59  |           25            |
+-------------------------------------------------------------+-------+-------------------------+

The responses for the question about stable branches updates are very consistent
with 2021 survey. There are no major changes in how results are distributed. The
only change is an increase in the number of users who are backporting specific
fixes (21% this year vs. 17% in 2021) and a decrease in the number of users who
are using only official point releases (25% this year vs. 30% in 2021). This
shows that there is a significant number of users who are backporting fixes
selectively on their own rather than waiting for official point releases which
will include required fixes.

To which projects does your organization contribute maintenance resources such as patches for bug and reviews on master or stable branches?
-------------------------------------------------------------------------------------------------------------------------------------------

Overall participation level for this questions is similar to the 2021 survey -
about 44% of users who provided information about used projects, participated
also in this question.
In the TOP 5 projects according to the number of contributors there is one
change - `Ironic <https://wiki.openstack.org/wiki/Ironic>`_ is now listed as
5th project with top number of contributors. It replaced `Kolla
<https://wiki.openstack.org/wiki/Kolla>`_ which was ranked 5th in the 2021
survey.
Majority of the projects (3/5) showed minor decrease in reported number of
contributors from 2021.

+----------+--------------+----------------------+
| Project  | Contributors | Contributors in 2021 |
+----------+--------------+----------------------+
| Nova     |      63      |          63          |
+----------+--------------+----------------------+
| Neutron  |      53      |          56          |
+----------+--------------+----------------------+
| Cinder   |      31      |          40          |
+----------+--------------+----------------------+
| Keystone |      30      |          34          |
+----------+--------------+----------------------+
| Ironic   |      25      |          23          |
+----------+--------------+----------------------+

After the first review of these results in the 2019 user survey,
the TC wanted to compare the number of respondents who reported they
used a project as compared to the number who reported that they contribute
to the project.
For the 2021 results review we have continued the analysis to see how many of
respondents who reported they used a project also contribute to the project.  In
2022 we have continued that but have also added the previous percentage of
participation for reference. To get this information we considered the number of
users who reported that they were using the project in production.
Note that we did not count users who indicated that they were just
testing a service or who indicated that they had the service
installed as part of a Proof of Concept. So the number of users that are using
any given service may be notably larger than indicated in the results below.
Here are the results of that investigation.

+-------------------+--------------+-------+-----------------+----------------------+
| Project           | Contributors | Users | % Participation | 2021 % Participation |
+-------------------+--------------+-------+-----------------+----------------------+
| AODH              | 3            | 28    | 11              | 9                    |
+-------------------+--------------+-------+-----------------+----------------------+
| Barbican          | 10           | 81    | 12              | 11                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Blazar            | 3            | 5     | 60              | 150                  |
+-------------------+--------------+-------+-----------------+----------------------+
| Ceilometer        | 10           | 75    | 13              | 12                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Cinder            | 31           | 213   | 15              | 19                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Cloudkitty        | 5            | 12    | 42              | 33                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Congress          | -            | 2     | 0               | -                    |
+-------------------+--------------+-------+-----------------+----------------------+
| Cyborg            | 2            | 7     | 29              | 75                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Designate         | 14           | 53    | 26              | 24                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Freezer           | -            | 2     | 0               | -                    |
+-------------------+--------------+-------+-----------------+----------------------+
| Glance            | 21           | 218   | 10              | 12                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Heat              | 16           | 154   | 10              | 8                    |
+-------------------+--------------+-------+-----------------+----------------------+
| Horizon           | 18           | 199   | 9               | 8                    |
+-------------------+--------------+-------+-----------------+----------------------+
| Ironic            | 25           | 64    | 39              | 35                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Keystone          | 30           | 226   | 13              | 15                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Kolla             | 18           | 59    | 31              | 49                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Kuryr             | 2            | 5     | 40              | 63                   |
+-------------------+--------------+-------+-----------------+----------------------+
| LOCI              | 3            | 6     | 50              | 43                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Magnum            | 10           | 50    | 20              | 42                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Masakari          | 5            | 8     | 63              | 14                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Manila            | 10           | 36    | 28              | 50                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Mistral           | 6            | 16    | 38              | 35                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Monasca           | -            | 5     | 0               | 12                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Murano            | 1            | 8     | 13              | 50                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Neutron           | 53           | 216   | 25              | 24                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Nova              | 63           | 217   | 29              | 27                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Octavia           | 21           | 112   | 19              | 29                   |
+-------------------+--------------+-------+-----------------+----------------------+
| OpenStack-Ansible | 23           | 58    | 40              | 46                   |
+-------------------+--------------+-------+-----------------+----------------------+
| OpenStack-Helm    | 4            | 8     | 50              | 36                   |
+-------------------+--------------+-------+-----------------+----------------------+
| OpenStack Client  | 19           | 179   | 11              | 11                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Panko             | -            | 10    | 0               | 43                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Qinling           | -            | 0     | 0               | -                    |
+-------------------+--------------+-------+-----------------+----------------------+
| Rally             | 5            | 38    | 13              | 14                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Sahara            | 1            | 2     | 50              | 50                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Searchlight       | -            | 1     | 0               | -                    |
+-------------------+--------------+-------+-----------------+----------------------+
| Senlin            | 4            | 4     | 100             | 80                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Solum             | -            | 0     | 0               | -                    |
+-------------------+--------------+-------+-----------------+----------------------+
| Storlets          | -            | 0     | 0               | -                    |
+-------------------+--------------+-------+-----------------+----------------------+
| Swift             | 18           | 90    | 20              | 19                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Tacker            | 1            | 1     | 100             | 33                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Tricircle         | 1            | 1     | 100             | -                    |
+-------------------+--------------+-------+-----------------+----------------------+
| TripleO           | 3            | 23    | 13              | 42                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Trove             | 6            | 9     | 67              | 29                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Vitrage           | 2            | 2     | 100             | -                    |
+-------------------+--------------+-------+-----------------+----------------------+
| Watcher           | 2            | 3     | 67              | 33                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Zaqar             | -            | 5     | 0               | 22                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Zun               | -            | 4     | 0               | 25                   |
+-------------------+--------------+-------+-----------------+----------------------+

There are few things worth to note regarding the list above.
Projects like: Monasca, Panko, Zaqar and Zun still have users who use it in the
Production but they lost all of their contributors.
Those projects joined the group of the projects with 0 declared contributors
which includes also: Congress, Freezer, Solum and Storlets.
Couple of projects like TripleO, Murano or Cyborg have experienced significant
drop in the participation level in 2022 comparing to the previous year.
The good thing to note is that none of the core projects like e.g. Cinder,
Keystone, Glance, Ironic, Neutron, Nova, Horizon, OpenStack Client have
experienced contributors drop.


How do members of your organization contribute to OpenStack?
------------------------------------------------------------

As with the other questions in the user survey, this question also saw an
decrease in responses. 111 users responded to it in this years' survey
comparing to the 173 users last year.

+----------------------------------------------+-------+-------------------------+
| Response                                     | Users | Percentage of Responses |
+----------------------------------------------+-------+-------------------------+
| Bug reports                                  |   93  |           84            |
+----------------------------------------------+-------+-------------------------+
| Documentation improvement                    |   47  |           42            |
+----------------------------------------------+-------+-------------------------+
| Participate in Forum sessions at the Summit  |   44  |           40            |
+----------------------------------------------+-------+-------------------------+
| Bug fixes on master                          |   43  |           39            |
+----------------------------------------------+-------+-------------------------+
| Participate in Ops meetups                   |   37  |           33            |
+----------------------------------------------+-------+-------------------------+
| Participate in PTG sessions                  |   30  |           27            |
+----------------------------------------------+-------+-------------------------+
| Code review on master                        |   27  |           24            |
+----------------------------------------------+-------+-------------------------+
| Backporting bug fixes to stable branches     |   25  |           23            |
+----------------------------------------------+-------+-------------------------+
| Sponsor in-person events                     |   24  |           22            |
+----------------------------------------------+-------+-------------------------+
| Code review on stable branches               |   24  |           22            |
+----------------------------------------------+-------+-------------------------+
| Feature development                          |   23  |           21            |
+----------------------------------------------+-------+-------------------------+
| Feature design review                        |   14  |           13            |
+----------------------------------------------+-------+-------------------------+
| Contribute resources to run CI jobs upstream |   8   |           7             |
+----------------------------------------------+-------+-------------------------+
| Host third-party CI jobs downstream          |   7   |           6             |
+----------------------------------------------+-------+-------------------------+
| Other                                        |   1   |           1             |
+----------------------------------------------+-------+-------------------------+

Similarly to the last year results, most people declare that they report bugs
as their way of contribution to the OpenStack project.
Very good thing to note is the fact that "Documentation improvement" response
have got significant increase of the users (47 users this year vs. 39 in the
2021).
From the other hand different ways of the participation in the events decreased
significantly. One of the potential reasons for that for the in person events
may be effect of the overall global economic situation where many companies have
experienced budget difficulties and are looking for a ways how to save some
money. Other potential reasons for that may be for example:

* health concern,
* environmental concerns,
* political issues.

This is just a speculation as there was no question about this in the survey.
If we want to know more details about what prevents people from participating in
the in person events, We should consider adding new question to the next user
survey.


What prevents you or your organization from contributing more maintenance resources, or makes contributing difficult?
---------------------------------------------------------------------------------------------------------------------

There were 101 users who provided response for this question in the 2022 survey.
It is a decrease of the number of responses comparing to the 2021 where 131
users answers to this question.

+--------------------------------------------------+-------+-------------------------+
| Response                                         | Users | Percentage of Responses |
+--------------------------------------------------+-------+-------------------------+
| Lack of resources                                |   54  |           53            |
+--------------------------------------------------+-------+-------------------------+
| Lack of skills                                   |   14  |           14            |
+--------------------------------------------------+-------+-------------------------+
| Bug tracker tool is not intuitive                |   11  |           11            |
+--------------------------------------------------+-------+-------------------------+
| Inconvient way of receiving patches              |   11  |           11            |
+--------------------------------------------------+-------+-------------------------+
| Difficult process                                |    8  |            8            |
+--------------------------------------------------+-------+-------------------------+
| Business decission                               |    3  |            3            |
+--------------------------------------------------+-------+-------------------------+
| Using too old OpenStack version                  |    3  |            3            |
+--------------------------------------------------+-------+-------------------------+
| No need to contribute as it just works as needed |    3  |            3            |
+--------------------------------------------------+-------+-------------------------+
| Paying vendor for support                        |    2  |            2            |
+--------------------------------------------------+-------+-------------------------+
| Specific changes, rejected by the community      |    2  |            2            |
+--------------------------------------------------+-------+-------------------------+
| Language barrier                                 |    2  |            2            |
+--------------------------------------------------+-------+-------------------------+
| Security; Private Network                        |    1  |            1            |
+--------------------------------------------------+-------+-------------------------+
| Company focus shifted to other projects          |    1  |            1            |
+--------------------------------------------------+-------+-------------------------+
| Difficult to get started                         |    1  |            1            |
+--------------------------------------------------+-------+-------------------------+

The most common reason which prevents organizations from contributing is lack of
resources.
The second from the top, also repeated many times was lack of skills. There was
also one user who responded that it's "difficult to start" with them
which could actually be included in the same category.

There was 8 people who replied that the main reason which stops it from
contributing is generally "difficult process". It's worth to look deeper into
this category of replies and see in detail what were the answers there:

+--------------------------------------------------------------------------------+
| Most problems we encounter are in the gaps between projects which means        |
| neither project team will take responsibility and review/help out.             |
| "Drive by" patches from deployers are often one liners and attract -1          |
| reviews on the basis of "theres no testing of this whole area in               |
| devstack- so this is -1".                                                      |
| Operators have little or no interest in devstack and and not in a position     |
| to fix it's technical debt.                                                    |
+--------------------------------------------------------------------------------+
| Some projects have major lead times between patch contributions and reviews,   |
| with many picky reviews on non-critical areas.                                 |
| Thus we are not able to contribute significantly to Nova for example,          |
| unless needed because the staff get frustrated with the lack of progress       |
| and are on short contracts.                                                    |
+--------------------------------------------------------------------------------+
| Cumbersome upstream review processes make contributing fixes a time and thus   |
| cost intensive undertaking - this is the reason none of our drivers was ever   |
| tried to put to upstream but rather made public ourselfes.                     |
+--------------------------------------------------------------------------------+
| Internal struggle with OS policies.                                            |
+--------------------------------------------------------------------------------+
| scope creep in bugfixes/regressions (i.e. "please make your re-added feature   |
| which fixes a regression generally usable for ipv4 and ipv6" when the original |
| solution- which was implemented upstream- didn't implement ipv6 at all)        |
+--------------------------------------------------------------------------------+
| The time to have a fix "production ready" for upstream.                        |
+--------------------------------------------------------------------------------+
| The onboarding and contribution process is pretty high-bar (custom             |
| infrastructure compared to e.g. gitlab.com/github.com, gerrit workflow is      |
| unfamiliar to many); Oftentimes the issues we encounter are already fixed      |
| upstream.                                                                      |
+--------------------------------------------------------------------------------+

From above replies it seems that main reason why users see our process as
difficult is generally review process and requirement for high quality patches,
with good testing coverage when many operators just wants to have their issue
fixed fast.

Other interesting point is 3 users who replied that they don't need to
contribute as OpenStack works for them as expected.


Other ways users participate:
-----------------------------

There were no users responses to this question this year. It's very similar to
what was in the 2021 survey where we had just 2 responses to the same question.

Summary
-------

Unfortunately we noticed decrease of the overall number of users responding to
the TC questions in 2022 user survey comparing to the 2021 survey. The good
thing is that there is still a significant number of responses so we can get
a lot of useful information from it.
After 2021 survey numbers in most cases are very similar in the 2022 survey.
It seems that things like, how users are upgrading OpenStack, what maintenance
releases they are using or how people are contributing to the OpenStack in
general is stable.

The fact that there is still increasing number of projects with lack of
contributors is alarming and TC should probably thing more about actions
possible to take to address it.


Additional Resources
--------------------

The `OpenStack Survey Report
<https://www.openstack.org/analytics>`_ also provides
a graphical overview of the OpenStack Survey
results.
