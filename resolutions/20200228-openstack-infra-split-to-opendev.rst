=============================================
 2020-02-28 OpenStack-Infra split to OpenDev
=============================================

The OpenStack infrastructure team has slowly changed its role to becoming
a team which provides resources to more than the OpenStack project, operating
many services under the OpenDev name.  Due to this, it makes sense for the
OpenStack infrastructure team to be split into two subsets (which are initially
intersecting): the OpenDev team (which runs the core infrastructure as the
provider in this case) and the OpenStack Infrastructure team (which runs the
tenant for "OpenStack" within OpenDev).

This move will help open up the ecosystem, which the infrastructure team has
built, out to projects beyond OpenStack.  This hopefully should help the
growth of the team and introduce a seperation of responsibility between
the core infrastructure (OpenDev) team and the OpenStack infrastructure
team.

With this change, the OpenDev and OpenStack infrastructure teams will continue
to work together to help improve the infrastructure that developers inside the
OpenStack community use on a daily basis.  It should hopefully attract more
users (which can perhaps mean more donated resources and potentially more
contributors down the line).

The current donated resources, which are being provided to the OpenStack
project, would continue to be operated by the new OpenDev team and continue
to be provided to the OpenStack project.

Background
----------

The OpenStack infrastructure team currently helps deliver and manage the
infrastructure which was being used by the overall community for the past
few years.  This infrastructure includes things like Gerrit, Zuul, Etherpad,
Wiki, Gitea and many other services which are used on a daily basis by the
developer community.  The infrastructure team also manages all of the donated
resources by cloud providers who seek to provide build resources for projects
within OpenStack.

As the OpenStack foundation started adopting other projects, many of them
needed a home to run their open software development and took advantage of the
massive existing ecosystem that the OpenStack infrastructure team built-out
over time.  Therefore, this put us in a state where the OpenStack
infrastructure team was helping facilitate resources for more than OpenStack.

Over time, it made sense to start looking at ways of helping projects start
becoming tenants within the big OpenStack infrastructure system and OpenDev
was formed as a primary team, community and environment to help deliver
these resources for projects.  In addition, every project would be managing
its own tenant in this case.
