=====================================
 Technical Committee Vision for 2019
=====================================

It's March of 2019 and we are getting ready for the upcoming Forum at
the OpenStack Summit. The OpenStack community has evolved quite a bit
over the last couple of years. Where do we even begin?

We have finally released our 4th Constellation for OpenStack,
available at https://orion.openstack.org. This new way of looking at
OpenStack reference architectures has successfully given people
concrete approaches to get started with OpenStack. Users have been
excited that not only do these constellations come with a dedicated
website explaining which set of projects make up this constellation,
but they have dedicated documentation for each one as well. A custom
install guide, an operators guide for the constellation in question, a
consolidated API reference for the environment, as well as a
validation script based on tempest that helps determine if the
environment is fully configured interoperable with other similar
constellation deployments completes the picture. Many of the
deployment tools are now providing high level macros to install a
specific constellations, which gives users a great way to see
different configurations of OpenStack without getting lost.

Constellations have become the new standard way to start exploring
OpenStack. For more advanced users, the project navigator helps
connect the dots from constellations into which projects to
contribute. The old confusion about git namespaces is a thing of the
past, given how convenient and user friendly these new views
are. Users have definitely reported via the user survey a higher ease
of initial understanding of OpenStack. This Constellation based view
has helped shape the overall project map. As we have been going
through and building these constellations we found several components
that did not fit well. We removed components that either overlapped
with work in adjacent communities or were not consistent with the
OpenStack mission. Other projects were refactored to clarify their
scope as they were placed on the map.

While the Constellation view has helped understand some prebuilt
patterns with OpenStack that are successful, it has also demonstrated
that there is more than one way to remix these components into
interesting architectures. Having multiple deeply worked examples has
helped clarify that OpenStack components can work well in many
configurations and use cases. As a result, new use cases are now
easier to envision and has led to the use of individual OpenStack
components in other deployments.

At the most recent OpenStack summit, three users gave presentations
about using single or minimal components of OpenStack, including using
Keystone for authenticating services not related to OpenStack at
all. Everyone was really thrilled by that as the landscape of
technology does not begin and end with OpenStack. This happened
because we started thinking differently about adjacent
Communities. The TC identified OpenStack services that would be of
value in new use cases and scenarios in conjunction with other
communities and ensured that they can be run as projects independent
of others. We have done the heavy lifting that makes it easy to
integrate Keystone into projects written in Go, Nodejs, or Java, so
that new projects starting off can easily start with a multi-tenancy
user/project story. It also makes it seamless for users to combine
services from OpenStack, and all these other communities in their
composite applications. The users love not having to hard code
credentials from different services throughout their environment.

We have learned a lot from adjacent communities in the process, and
have made some substantial changes to the way we do things based on
these collaborations. The TC is proactive in reaching out to
communities with overlapping interests including consumers of
OpenStack as well as components which play a critical role in
deployment of a OpenStack Solution. In addition, we have also been
able been able to share some of our hard learned lessons and success
stories to help them on their journey. We now have a very repeatable
system for engaging with new communities, sharing some of our past
insights, and helping where we can, while being respectful of how
every community has their own culture and needs as they grow. The 5-10
groups we have formed close partnerships with are continuously asked
for feedback to ensure their satisfaction with our partnership. Our
partnerships focus on this quality of partnership, rather than
quantity of groups we interact with, so the appropriate amount of
resources can be focused on success. It is a regular occurrence that
TC members are or have been committers within these other communities.

The outreach included both technical and non-technical aspects. Since
the OpenStack ecosystem is mature and has excellent systems and
processes in place for dealing with governance, vulnerabilities,
continuous integration infrastructure, leadership development, etc.,
the TC shares the best practices with other newly forming communities
to help bootstrap them. On the technical side, the TC worked closely
with leadership teams of the other communities to find opportunities
to share code as services, libraries, reduce scope and complexity of
some projects to remove duplicated effort. This has empowered
contributors to easily move between OpenStack and other communities
and develop synergies to benefit everyone. The TC worked with the
OpenStack Infrastructure, Quality Assurance, and similar teams to make
sure there is a common understanding of how to deal with new language
ecosystems, new projects that will need continuous integration,
mirroring needs, and works to expand available resources as well as
ensure that there is no undue impact on limited resources.

Reaching out to so many other communities, and sharing lessons between
us, really confirmed for all of us how critical diversity is to the
future of OpenStack. There are so many good ideas out there, and so
many people that are motivated to help move the conversation
forward. The diverse community also drives a lot of empathy in our
contributors. It has been much easier to understand and empathize with
the wide range of challenges and problems people are trying to solve
with OpenStack when we have so many different perspectives in our
community. Diversity, on many axes, is now a key value in OpenStack
itself, and we have seen our contributor base get measurably more
diverse in each of the last three releases.

More than 50% of the contributors to the most recent OpenStack release
identified strongly as an OpenStack user or operator. This has helped
grow different patterns and culture of contributions, that are more
focused on near term needs of the operators in the field. It has also
brought much more sympathy to the needs of part time contributors who
can't complete a perfect patch to get it accepted. A small organic
team of shepherds have been taking the drive-by contributions and
working them into the system, either by taking over the patches or by
applying follow-up changes. The new bot that converts github pull
requests to gerrit change-sets, instead of discarding them, imported
several patches in each of the last three months.

The TC itself has changed in the process. We now regularly have people
from the operator community and user committee both on the TC and
assisting with many of the TC initiated efforts. The TC now looks much
more like our contributor base. The TC membership now includes several
women and representatives from APAC and European countries. These
changes did not happen overnight, or by accident. We now have very
heavy emphasis on mentoring in the community, with multiple different
efforts underway. There is the new OpenStack Ladder program, inspired
by the Drupal Ladder program, has aimed to bring more traditional
users and operators into the contributor space and ensure that they
don’t feel overwhelmed getting their first patch in.

For members of the community that are already engaged, we have built
into our ladder program a specific mentoring program around
inter-project work. This is not only technical mentoring, but focuses
on the skills needed to interface with multiple communities, and work
to build consensus across sometimes large cultural boundaries. We have
10 mentors and over 50 participants in this program, who are spending
more than 40% of their OpenStack time focused on efforts spanning two
or more projects. This has not only given OpenStack a unified user and
operator experience, but this spanning of project communities has made
our community feel more whole as well.

With more community members having successes in inter-project work, it
is now commonplace for popup teams to form around these kind of
efforts, often lead by members of the mentoring program. They will
engage with key members from different project teams within OpenStack,
or projects in other communities, or both. Members of the user and and
operators communities are often a part of these popup teams. People
find it exciting and energizing to dive into such crucial work early
in their OpenStack engagement. Success breeds success, and as the
velocity of this work has increased we have seen a renewed investment
from member companies to keep accelerating this work.

Much of the work done by these inter-project teams has come from the
improved feedback loop between user, operators and developers. Indeed
this feedback, coupled with the increase in diversity of
contributions, makes it hard to distinguish between users, operators
and developers. One visible success story has been the TC curated Top
10 hit list. It has brought renewed focus on some of the hard problems
we need to go after in the near term. It is now commonplace that key
features that identified in the Top 10 hit list get completed in a
single cycle. Not only does it easily express some of the most
important work that we need to get done as a community, but the
process of creating it made us all understand OpenStack that much
more.

When TC members and other community leaders started taking deep dives
into projects they normally don’t contribute to, there was a ton of
enlightenment. Old prejudices took a backseat as we walked a mile in
each other’s shoes. This new understanding is part of why hierarchical
quotas are now implemented and working in many services, and are now
getting tested in the field. We expect most of the OpenStack projects,
as well as a number of non OpenStack projects in adjacent communities
to have this supported over the next year.

Over the past year, the TC has proudly celebrated the good work done
by those who stepped up to lead and work on crucial work in the
community. It has been particularly satisfying to see the breadth of
talent now involved in the technical leadership of the OpenStack
community. More companies are investing longer term contributors to
the OpenStack project, because they can see a clearer path for value
delivery to their products and services delivered using OpenStack. We
now have between 50 and 100 contributors with significant commits to
two or more Projects every release cycle. Importantly, we have
retained 75% of those contributors over the last three
releases. Moreover, 50% of these contributors are part time, yet still
able to get actively involved in critical inter-project work. And we
regularly see those folks that leave our community become leaders and
mentors in other Open Source projects in the ecosystem. We have grown
not just OpenStack, but Open Source as a whole, and that is something
we can all be proud of.
