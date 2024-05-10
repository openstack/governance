=====================================
Analysis of 2023 User Survey Feedback
=====================================

Introduction
------------

This is an analysis of the results from the 2023 User Survey in comparison to
the `2022 results  <https://governance.openstack.org/tc/user_survey/analysis-2022.html>`_.
As with the previous analysis, the analysis will  be performed on a per-question
basis with an over-all summary at the end.

How do you upgrade your version of OpenStack?
---------------------------------------------

+---------------------------------------------------------------+-------+-------------------------+
| Response                                                      | Users | Percentage of Responses |
+---------------------------------------------------------------+-------+-------------------------+
| Skip/fast-forward releases                                    |   65  |           35            |
+---------------------------------------------------------------+-------+-------------------------+
| Upgrade all coordinated releases (once every 6 months)        |   50  |           27            |
+---------------------------------------------------------------+-------+-------------------------+
| Not upgrade                                                   |   44  |           24            |
+---------------------------------------------------------------+-------+-------------------------+
| Deploy regularly from the master branch                       |   9   |           5             |
+---------------------------------------------------------------+-------+-------------------------+
| Deploy all intermediary releases and all coordinated releases |   18  |           10            |
+---------------------------------------------------------------+-------+-------------------------+

Total number of responses was 186 this year and it is again lower than in the
previous years: 272 in 2021 survey and 249 in 2022.
Results in this year's survey are similar to the 2022 survey. Differences are
mostly in the "Upgrade all coordinated releases (once every 6 months)" and
"Deploy all intermediary releases and all coordinated releases" answers. Number
of users who are upgrading every 6 months decreased by 3% and number of users
who are deploying all intermediary releases and all coordinated releases
increased by 6% - from 4 to 10%. This may be positive sign that users trust
more our intermediary releases.


Once on a given release, do you use stable branches for bug-fix upgrades?
-------------------------------------------------------------------------

+-------------------------------------------------------------+-------+-------------------------+
| Response                                                    | Users | Percentage of Responses |
+-------------------------------------------------------------+-------+-------------------------+
| I do not do bugfix upgrades                                 |   27  |           15            |
+-------------------------------------------------------------+-------+-------------------------+
| Yes, backporting specific fixes                             |   27  |           15            |
+-------------------------------------------------------------+-------+-------------------------+
| Yes, deploying every commit on the stable branch            |   13  |            7            |
+-------------------------------------------------------------+-------+-------------------------+
| Yes, upgrading at various points in time depending on fixes |   63  |           36            |
+-------------------------------------------------------------+-------+-------------------------+
| Yes, using only official point releases                     |   46  |           26            |
+-------------------------------------------------------------+-------+-------------------------+

Number of responses for that question was also lower this year (176) comparing
with previous years: 249 in 2022 and 272 in 2021.
Most of the responses this year are very similar to the responses from previous
years. The biggest difference is that 6% less users this year declared that they
are backporting specific fixes (15% in 2023 vs. 21% in 2022) and at the same
time 6% more users declared upgrading at various points in time (36% vs. 30%).
This may be also positive sign that our community is doing good job with
maintenance of stable branches and backporting needed fixes.


To which projects does your organization contribute maintenance resources such as patches for bug and reviews on master or stable branches?
-------------------------------------------------------------------------------------------------------------------------------------------

About 48% of users who provided info about projects they use participated also
in this question. This is slightly higher than in 2022 (44%). In absolute
numbers it was 85 users who participated in this question this year.
There is one change in the TOP 5 projects on that list.
`Ironic <https://wiki.openstack.org/wiki/Ironic>`_ which was in the TOP 5 in
2022 is now replaced on the 5th position by the `Kolla
<https://wiki.openstack.org/wiki/Kolla>`_ (come back to the TOP 5 after 1 year)
and `Octavia <https://wiki.openstack.org/wiki/Octavia>`_.

+----------+--------------+----------------------+
| Project  | Contributors | Contributors in 2022 |
+----------+--------------+----------------------+
| Nova     |      38      |          63          |
+----------+--------------+----------------------+
| Neutron  |      33      |          53          |
+----------+--------------+----------------------+
| Keystone |      22      |          30          |
+----------+--------------+----------------------+
| Cinder   |      21      |          31          |
+----------+--------------+----------------------+
| Octavia  |      19      |          21          |
+----------+--------------+----------------------+
| Kolla    |      19      |          18          |
+----------+--------------+----------------------+

One thing which can be dangerous is the fact that overall number of users who
declared contributions to most of the projects dropped significantly this year.
This year we continue the analysis of how many of responders who reported they
used a project also contribute to it.
To get this information we considered the number of
users who reported that they were using the project in production.
Note that we did not count users who indicated that they were just
testing a service or who indicated that they had the service
installed as part of a Proof of Concept. So the number of users that are using
any given service may be notably larger than indicated in the results below.
Here are the results of that investigation.

+-------------------+--------------+-------+-----------------+----------------------+
| Project           | Contributors | Users | % Participation | 2022 % Participation |
+-------------------+--------------+-------+-----------------+----------------------+
| AODH              | 5            | 22    | 23              | 11                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Barbican          | 5            | 66    | 8               | 12                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Blazar            | 3            | 5     | 60              | 60                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Ceilometer        | 14           | 75    | 26              | 13                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Cinder            | 21           | 213   | 13              | 15                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Cloudkitty        | 5            | 12    | 63              | 42                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Congress*         | -            | 2     | 0               | 0                    |
+-------------------+--------------+-------+-----------------+----------------------+
| Cyborg            | 1            | 7     | 25              | 29                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Designate         | 13           | 53    | 27              | 26                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Dragonflow*       | -            | 3     | 0               | -                    |
+-------------------+--------------+-------+-----------------+----------------------+
| Freezer           | -            | 2     | 0               | 0                    |
+-------------------+--------------+-------+-----------------+----------------------+
| Glance            | 18           | 218   | 10              | 10                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Heat              | 8            | 154   | 7               | 10                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Horizon           | 18           | 199   | 11              | 9                    |
+-------------------+--------------+-------+-----------------+----------------------+
| Ironic            | 12           | 64    | 24              | 39                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Karbor*           | 1            | 4     | 25              | -                    |
+-------------------+--------------+-------+-----------------+----------------------+
| Keystone          | 22           | 226   | 13              | 13                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Kolla             | 19           | 59    | 42              | 31                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Kuryr             | 3            | 5     | 50              | 40                   |
+-------------------+--------------+-------+-----------------+----------------------+
| LOCI              | 1            | 6     | 20              | 50                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Magnum            | 9            | 50    | 26              | 20                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Masakari          | 4            | 8     | 27              | 63                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Manila            | 10           | 36    | 28              | 28                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Mistral           | 2            | 16    | 10              | 38                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Monasca           | 1            | 5     | 13              | 0                    |
+-------------------+--------------+-------+-----------------+----------------------+
| Murano            | -            | 8     | 0               | 13                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Neutron           | 33           | 216   | 20              | 25                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Nova              | 38           | 217   | 21              | 29                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Octavia           | 19           | 112   | 23              | 19                   |
+-------------------+--------------+-------+-----------------+----------------------+
| OpenStack-Ansible | 14           | 58    | 40              | 40                   |
+-------------------+--------------+-------+-----------------+----------------------+
| OpenStack-Helm    | 4            | 8     | 50              | 50                   |
+-------------------+--------------+-------+-----------------+----------------------+
| OpenStack Client  | 6            | 179   | 4               | 11                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Panko*            | 2            | 10    | 29              | 0                    |
+-------------------+--------------+-------+-----------------+----------------------+
| Qinling*          | -            | 0     | 0               | 0                    |
+-------------------+--------------+-------+-----------------+----------------------+
| Rally             | 2            | 41    | 5               | 13                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Sahara            | 1            | 5     | 20              | 50                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Searchlight*      | -            | 1     | 0               | 0                    |
+-------------------+--------------+-------+-----------------+----------------------+
| Senlin            | 4            | 4     | 50              | 100                  |
+-------------------+--------------+-------+-----------------+----------------------+
| Solum             | -            | 0     | 0               | 0                    |
+-------------------+--------------+-------+-----------------+----------------------+
| Storlets          | -            | 0     | 0               | 0                    |
+-------------------+--------------+-------+-----------------+----------------------+
| Swift             | 9            | 90    | 12              | 20                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Tacker            | 1            | 3     | 33              | 100                  |
+-------------------+--------------+-------+-----------------+----------------------+
| Tricircle*        | -            | 1     | 0               | 100                  |
+-------------------+--------------+-------+-----------------+----------------------+
| TripleO*          | 4            | 23    | 18              | 13                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Trove             | 4            | 10    | 40              | 67                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Venus             | -            | 2     | 0               | -                    |
+-------------------+--------------+-------+-----------------+----------------------+
| Vitrage           | -            | 2     | 0               | 100                  |
+-------------------+--------------+-------+-----------------+----------------------+
| Watcher           | -            | 3     | 0               | 67                   |
+-------------------+--------------+-------+-----------------+----------------------+
| Zaqar             | 1            | 6     | 17              | 0                    |
+-------------------+--------------+-------+-----------------+----------------------+
| Zun               | 1            | 6     | 17              | 0                    |
+-------------------+--------------+-------+-----------------+----------------------+

* project already retired

Still the same projects as in 2022 have 0 declared contributors. One project
(Monasca) which didn't had any contributors in 2022 now have one declared
contributor.
Most of the projects with higest number of users experienced drop in the
participation level. Project with the biggest drop in number of contributors is
OpenstackClient which contributors dropped from 19 in 2022 to only 6 in 2023
(11% in 2022 vs. 4% in 2023).


How do members of your organization contribute to OpenStack?
------------------------------------------------------------

+----------------------------------------------+-------+-------------------------+
| Response                                     | Users | Percentage of Responses |
+----------------------------------------------+-------+-------------------------+
| Bug reports                                  |  132  |           89            |
+----------------------------------------------+-------+-------------------------+
| Bug fixes on master                          |   59  |           40            |
+----------------------------------------------+-------+-------------------------+
| Participate in Forum sessions at the Summit  |   47  |           32            |
+----------------------------------------------+-------+-------------------------+
| Participate in PTG sessions                  |   38  |           26            |
+----------------------------------------------+-------+-------------------------+
| Documentation improvement                    |   35  |           23            |
+----------------------------------------------+-------+-------------------------+
| Backporting bug fixes to stable branches     |   33  |           22            |
+----------------------------------------------+-------+-------------------------+
| Participate in Ops meetups                   |   29  |           19            |
+----------------------------------------------+-------+-------------------------+
| Feature development                          |   27  |           18            |
+----------------------------------------------+-------+-------------------------+
| Code review on master                        |   25  |           17            |
+----------------------------------------------+-------+-------------------------+
| Sponsor in-person events                     |   25  |           17            |
+----------------------------------------------+-------+-------------------------+
| Code review on stable branches               |   20  |           13            |
+----------------------------------------------+-------+-------------------------+
| Feature design review                        |   17  |           11            |
+----------------------------------------------+-------+-------------------------+
| Contribute resources to run CI jobs upstream |   4   |           3             |
+----------------------------------------------+-------+-------------------------+
| Host third-party CI jobs downstream          |   2   |           1             |
+----------------------------------------------+-------+-------------------------+

This year, similarly to 2022, most popular form of contributions was by
reporting bugs and it even increased compared to last year (89% vs 84%).
There is one significant difference in this year's responses to that question as
number of contributors who are fixing bugs on master branch increased from 43
users in 2022 to 59 this year. But in terms of percentage it was almost the same
(40% in 2023 vs. 39% in 2022). There is also significant drop in number of
contributors who are improving our documentation - 35 users (23%) in 2023
compared to 47 users (42%) in 2022.
Other change worth to mention is drop in number of users who host third-party
CI - 7 users in 2022 compared to just 2 in 2023.


What prevents you or your organization from contributing more maintenance resources, or makes contributing difficult?
---------------------------------------------------------------------------------------------------------------------

There were 76 users who responded to tha question which is less than in 2022
survey where there were 101 responses.

+--------------------------------------------------+-------+-------------------------+
| Response                                         | Users | Percentage of Responses |
+--------------------------------------------------+-------+-------------------------+
| Lack of resources                                |   41  |           54            |
+--------------------------------------------------+-------+-------------------------+
| Lack of skills                                   |    8  |           11            |
+--------------------------------------------------+-------+-------------------------+
| Difficult process                                |    6  |            8            |
+--------------------------------------------------+-------+-------------------------+
| Legal / community issues                         |    5  |            7            |
+--------------------------------------------------+-------+-------------------------+
| Paying vendor for support                        |    4  |            5            |
+--------------------------------------------------+-------+-------------------------+
| Slow review process / Lack of maintainers        |    3  |            4            |
+--------------------------------------------------+-------+-------------------------+
| No need to contribute as it just works as needed |    3  |            4            |
+--------------------------------------------------+-------+-------------------------+
| Specific changes, rejected by the community      |    1  |            1            |
+--------------------------------------------------+-------+-------------------------+
| Security                                         |    1  |            1            |
+--------------------------------------------------+-------+-------------------------+
| Moving to Kubernetes platform                    |    1  |            1            |
+--------------------------------------------------+-------+-------------------------+
| Low number of customers                          |    1  |            1            |
+--------------------------------------------------+-------+-------------------------+
| Limited upside to commercial return              |    1  |            1            |
+--------------------------------------------------+-------+-------------------------+
| Time zone (AWST) crossover                       |    1  |            1            |
+--------------------------------------------------+-------+-------------------------+

The most common reasons which prevents organizations from contributing did not
change this year comparing to the previous one. It's still lack of resources
(both time and people), lack of skills in the team and difficult process. In
that last category from the Top 3 there are included things like (but not only):

* not easy to satify the testing in the CI environment,
* unusual and cumbersome process with gerrit,
* different communictation tools used by various projects,

One new category of the responses this year is about some legal and "community
related" issues. Some examples of the responses included there are below:

+--------------------------------------------------------------------------+
| The fear of helping the competition                                      |
+--------------------------------------------------------------------------+
| No reason to contribute                                                  |
+--------------------------------------------------------------------------+
| we have customers to serve and our time is not dedicated for open source |
| projects                                                                 |
+--------------------------------------------------------------------------+
| Legal understanding                                                      |
+--------------------------------------------------------------------------+

Those are complete responses from the user survey and in some cases it may be
really hard to understand exactly what does it mean but generally responses like
those about having no reason to contribute or fear of helping competition may
sounds a bit alarming for our community.

Other ways users participate:
-----------------------------

The same as in the 2022 user survey there were no users responses to this
question this year.

How are you consuming OpenStack:
--------------------------------

This is one of the new questions added by the TC to the 2023 survey. There were
168 responses to this question.
Most of the users are using OpenStack directly from the Git repositories or from
one of the 2 biggest vendors (Canonical and Red Hat) but other channels like
pypi or packages provided by Debian are also quite popular.

+---------------+-------+-------------------------+
| Response      | Users | Percentage of Responses |
+---------------+-------+-------------------------+
| Git           |   57  |            34           |
+---------------+-------+-------------------------+
| Canonical     |   55  |            33           |
+---------------+-------+-------------------------+
| RHOSP         |   40  |            24           |
+---------------+-------+-------------------------+
| pypi packages |   30  |            18           |
+---------------+-------+-------------------------+
| Other Distros |   23  |            14           |
+---------------+-------+-------------------------+
| Debian        |   19  |            11           |
+---------------+-------+-------------------------+

If using other distros, please specify:
---------------------------------------

This is one of the new questions added by the TC to the 2023 survey. There were
23 responses to this question.
There is no one, most popular option here. Users are using various ways to
consume OpenStack deliverables, from upstream products like Kolla or OpenStack
Ansible, through the packages provided by various distros (Oracle Linux,
RockyLinux) or OpenStack distributions (like RDO) to the packages build on their
own.

+---------------------------------------------------------------------------+-------+-------------------------+
| Response                                                                  | Users | Percentage of Responses |
+---------------------------------------------------------------------------+-------+-------------------------+
| Kolla                                                                     |   6   |            24           |
+---------------------------------------------------------------------------+-------+-------------------------+
| RockyLinux + PACKSTACK                                                    |   1   |            4            |
+---------------------------------------------------------------------------+-------+-------------------------+
| Tripleo from the public repositories                                      |   1   |            4            |
+---------------------------------------------------------------------------+-------+-------------------------+
| community                                                                 |   1   |            4            |
+---------------------------------------------------------------------------+-------+-------------------------+
| RDO                                                                       |   3   |            13           |
+---------------------------------------------------------------------------+-------+-------------------------+
| build our own deb packages                                                |   1   |            4            |
+---------------------------------------------------------------------------+-------+-------------------------+
| VIO                                                                       |   1   |            4            |
+---------------------------------------------------------------------------+-------+-------------------------+
| CentOS                                                                    |   2   |            8            |
+---------------------------------------------------------------------------+-------+-------------------------+
| StackHPC                                                                  |   1   |            4            |
+---------------------------------------------------------------------------+-------+-------------------------+
| DS OpenStack                                                              |   1   |            4            |
+---------------------------------------------------------------------------+-------+-------------------------+
| Mirantis MOSK (via debs in container images)                              |   1   |            4            |
+---------------------------------------------------------------------------+-------+-------------------------+
| Ubuntu- Oracle Linux                                                      |   1   |            4            |
+---------------------------------------------------------------------------+-------+-------------------------+
| Oracle Linux                                                              |   1   |            4            |
+---------------------------------------------------------------------------+-------+-------------------------+
| k8s- loci                                                                 |   1   |            4            |
+---------------------------------------------------------------------------+-------+-------------------------+
| We have in-house deployment/installation based on Ubuntu and Kayobe.      |   1   |            4            |
+---------------------------------------------------------------------------+-------+-------------------------+

How do your users interact with OpenStack:
------------------------------------------

This is one of the new questions added by the TC to the 2023 survey. There were
181 responses to this question.
Replies to this question shows clearly that there are 2 main ways how users
interacts with Openstack: using CLI - we think this is the unified "OpenStack
Client" but the question doesn't mention any specific CLI tool, and Horizon
dashboard. This aligns with responses to one of the questions above about
projects used by users where both OpenstackClient and Horizon are declared to be
used by many users.
We can contrast the responses to this question with the one about the OpenStack
projects used, and the contributions made by the respondant. Doing this would
reveal that these widely used interface projects lack sufficient user
contributions. This indicates that we should encourage a higher user investment
in the development of these interfaces.

+---------------------------+-------+-------------------------+
| Response                  | Users | Percentage of Responses |
+---------------------------+-------+-------------------------+
| CLI                       |  153  |            85           |
+---------------------------+-------+-------------------------+
| Horizon                   |  147  |            81           |
+---------------------------+-------+-------------------------+
| Internally developed tool |   42  |            23           |
+---------------------------+-------+-------------------------+
| Other                     |   33  |            18           |
+---------------------------+-------+-------------------------+
| Skyline                   |   12  |            7            |
+---------------------------+-------+-------------------------+

Participation in UI is lacking in maintenance. Do you contribute in UI maintenance:
-----------------------------------------------------------------------------------

This is one of the new questions added by the TC to the 2023 survey. There were
131 responses to this question.
Replies to this question only confirm what community saw in past release cycles,
that most of users don't contribute to our UI products at all. This is aligned
with the question about projects contributors level which is described above and
where projects like OpenStack Client are declared to be used by a lot of users
but only few declare contributing to its development.
Our communtity should focus more on those UI projects as it is clear that they
are very important for users but lack contributors.

+----------+-------+-------------------------+
| Response | Users | Percentage of Responses |
+----------+-------+-------------------------+
| Yes      |   12  |            9            |
+----------+-------+-------------------------+
| No       |  119  |            91           |
+----------+-------+-------------------------+

If not, then what is the primary reason:
----------------------------------------

This is one of the new questions added by the TC to the 2023 survey. There were
120 responses to this question.
Replies to this questions are also aligned with more general question about
reasons which prevents organizations to contribute to the OpenStack. Most
popular answer is lack of resources/skills.

+----------------------------------+-------+-------------------------+
| Response                         | Users | Percentage of Responses |
+----------------------------------+-------+-------------------------+
| Other                            |   8   |            7            |
+----------------------------------+-------+-------------------------+
| Because of resources- skill      |  100  |            83           |
+----------------------------------+-------+-------------------------+
| Happy with current functionality |   22  |            18           |
+----------------------------------+-------+-------------------------+

If other, please specify:
-------------------------

This is one of the new questions added by the TC to the 2023 survey. There were
8 responses to this question.
This one is open question and responses provided by users are all different.
Below is list of all complete responses.

+-----------------------------------------------------------------------------+
| Response                                                                    |
+-----------------------------------------------------------------------------+
| getting started                                                             |
+-----------------------------------------------------------------------------+
| we already contribute to a lot of other OpenStack projects                  |
+-----------------------------------------------------------------------------+
| Third party UI                                                              |
+-----------------------------------------------------------------------------+
| Man- no Idea how to even get started- and then there's no time.             |
+-----------------------------------------------------------------------------+
| Our team's end users are now getting used to Horizon. As time goes forward- |
| there may be needs that we can upstream.                                    |
+-----------------------------------------------------------------------------+
| Don't have the bandwidth yet to contribute.                                 |
+-----------------------------------------------------------------------------+
| Not considered                                                              |
+-----------------------------------------------------------------------------+
| The team has other priorities                                               |
+-----------------------------------------------------------------------------+

What library, if any, are you using to interface with OpenStack:
----------------------------------------------------------------

This is one of the new questions added by the TC to the 2023 survey. There were
36 responses to this question.
Most popular option is official OpenStack SDK project.

+--------------+-------+-------------------------+
| Response     | Users | Percentage of Responses |
+--------------+-------+-------------------------+
| openstacksdk |   33  |            92           |
+--------------+-------+-------------------------+
| gophercloud  |   8   |            22           |
+--------------+-------+-------------------------+
| Other        |   3   |            8            |
+--------------+-------+-------------------------+
| fog          |   1   |            3            |
+--------------+-------+-------------------------+

If other, please specifiy:
--------------------------

This is one of the new questions added by the TC to the 2023 survey. There were
2 responses to this question.
As this one is open question and responses provided by users are all different
below is list of all complete responses.

+------------------------------------------------------------+
| Response                                                   |
+------------------------------------------------------------+
| Custom built control panel instead of Horizon              |
+------------------------------------------------------------+
| Our own platform that connects to the API of our clusters. |
+------------------------------------------------------------+

What software or services in your cloud environment are enabled by OpenStack and OpenStack provisioned resources, for example: Kubernetes:
------------------------------------------------------------------------------------------------------------------------------------------

This is one of the new questions added by the TC to the 2023 survey. There were
52 responses to this question.
Kubernetes is by far the most popular service to be used in the cloud declared
by the OpenStack users. Other popular services are things like Database as a
Service, Web servers, Virtual Private Servers (VPS).

+-------------------------+-------+-------------------------+
| Response                | Users | Percentage of Responses |
+-------------------------+-------+-------------------------+
| Kubernetes              |  42   |            81           |
+-------------------------+-------+-------------------------+
| Cloudfoundry            |   1   |             2           |
+-------------------------+-------+-------------------------+
| FaaS                    |   1   |             2           |
+-------------------------+-------+-------------------------+
| DBaaS                   |   6   |            12           |
+-------------------------+-------+-------------------------+
| OpenStack               |   3   |             6           |
+-------------------------+-------+-------------------------+
| Openshift               |   2   |             4           |
+-------------------------+-------+-------------------------+
| Web servers             |   4   |             8           |
+-------------------------+-------+-------------------------+
| IaaS                    |   1   |             2           |
+-------------------------+-------+-------------------------+
| CDN                     |   1   |             2           |
+-------------------------+-------+-------------------------+
| Jenkins                 |   2   |             4           |
+-------------------------+-------+-------------------------+
| Artifactory             |   2   |             4           |
+-------------------------+-------+-------------------------+
| Gerrit                  |   2   |             4           |
+-------------------------+-------+-------------------------+
| Nextcloud               |   2   |             4           |
+-------------------------+-------+-------------------------+
| Apache Cloudera         |   1   |             2           |
+-------------------------+-------+-------------------------+
| Grafana                 |   1   |             2           |
+-------------------------+-------+-------------------------+
| Terraform               |   1   |             2           |
+-------------------------+-------+-------------------------+
| VPS                     |   3   |             6           |
+-------------------------+-------+-------------------------+
| SaaS                    |   1   |             2           |
+-------------------------+-------+-------------------------+
| Slurm                   |   4   |             8           |
+-------------------------+-------+-------------------------+
| Backups                 |   1   |             2           |
+-------------------------+-------+-------------------------+
| Key Value store         |   1   |             2           |
+-------------------------+-------+-------------------------+
| VNF                     |   4   |             8           |
+-------------------------+-------+-------------------------+
| Azimuth                 |   1   |             2           |
+-------------------------+-------+-------------------------+
| Jupyter                 |   2   |             4           |
+-------------------------+-------+-------------------------+
| Uniview                 |   1   |             2           |
+-------------------------+-------+-------------------------+
| Aiven                   |   1   |             2           |
+-------------------------+-------+-------------------------+
| Machine Learning        |   1   |             2           |
+-------------------------+-------+-------------------------+
| Gitlab                  |   1   |             2           |
+-------------------------+-------+-------------------------+
| Rocket.Chat             |   1   |             2           |
+-------------------------+-------+-------------------------+
| Jitsii Meet             |   1   |             2           |
+-------------------------+-------+-------------------------+
| Netbox                  |   1   |             2           |
+-------------------------+-------+-------------------------+
| Hashicorp Vault         |   1   |             2           |
+-------------------------+-------+-------------------------+
| Zammad                  |   1   |             2           |
+-------------------------+-------+-------------------------+
| BIND9                   |   1   |             2           |
+-------------------------+-------+-------------------------+
| Blockchain as a Service |   1   |             2           |
+-------------------------+-------+-------------------------+
| StarlingX               |   1   |             2           |
+-------------------------+-------+-------------------------+

Summary
-------

Unfortunately number of the responses to the survey this year decreased again
comparing to the 2022 survey.
Bad sign may be decreasing number of users who declare that they
contribute to the OpenStack projects. It is also confirmed by question
specifically related to the UI projects where only 9% of users declared that
they contribute to that kind of projects.
Very positive thing is that there are no new projects with
declared 0 contributors and number of projects in such state decreased by 1 as
Monasca has at least 1 user that is also a contributor.
It seems that things like, how users are upgrading OpenStack, what stable
releases they are using or how people are contributing to the OpenStack in
general is still stable.
In the 2023 survey TC added couple of new questions about how users are
consuming OpenStack, how they interact with the OpenStack and what cloud
services are used on top of the OpenStack infrastructure. Those
questions show clearly that users are mostly using official OpenStack projects
to interact with OpenStack (OpenStack client, SDK, Horizon) and that the most
popular tool installed on top of the OpenStack is Kubernetes.


Additional Resources
--------------------

The `OpenStack Survey Report
<https://www.openstack.org/analytics>`_ also provides
a graphical overview of the OpenStack Survey
results.
