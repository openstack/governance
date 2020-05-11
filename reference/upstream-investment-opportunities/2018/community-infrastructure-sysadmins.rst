Community Infrastructure Sysadmins
==================================

Description
-----------

The Infrastructure team is responsible for designing,
building and maintaining the systems that are used in the day to day
operation of the OpenStack project as a whole; this includes
development, testing, and collaboration tools. All of the software
it runs is open source, and under public configuration management so
that everyone in the community has the opportunity to participate.
One very effective way to get involved in OpenStack, gaining a deep
understanding of and visibility within the community, is by helping
operate this infrastructure. Attrition due to shifts in employment
or availability of personal time impacts the team's ability to
support the community effectively, and so there is a constant need
for new contributors who can commit to investing sufficient effort
to overcome the steep learning curve associated with these varied
technologies.

Because our community is global, its support needs span most
timezones. Unfortunately, the bulk of long-term contributors to
Infrastructure are concentrated in the Americas and so this leaves
APAC and EMEA community members with far fewer options for immediate
assistance with urgent issues. Gaining more contributors who are
active during those times (whether they live in those parts of the
World or not) would provide a substantial benefit to the community.
This is not necessarily as easy as it sounds because it's harder to
get as much overlap with the current bulk of the team for shadowing
and knowledge transfer, but there are still some existing team
members in those timezones who can help mitigate that somewhat.

In particular, the team seeks developers and systems administrators
with a background both in maintaining Unix/Linux servers and free
software, and places heavy emphasis on systems automation and
configuration management (primarily Ansible and Puppet at the
moment). Everything possible goes through code review, and gets
extensively documented and communicated with the rest of the
community over IRC and mailing lists. Server resources are donated
by companies operating OpenStack services so there is
substantial opportunity both for people who have experience in those
technologies as well as anyone wishing to gain more familiarity with
them.

Value
-----

Reusability
~~~~~~~~~~~

The infrastructure team leverages resources donated from companies operating
OpenStack services. The community uses the software it produces as a tool for
testing it. Every day, contributors submit thousands of patches for review.
Infrastructure tools deploy each patch and test it against thousands of tests
and scenarios. This volume provides an opportunity to improve the software we
write by giving us first-hand experience with issues at scale. The benefit of
fixing these issues for the OpenStack CI system is two-fold:

1. It makes the test platform more stable and robust
2. Products or services benefits from the fix being applied upstream

Don't Repeat Yourself or Your Testing (DRY)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The culture built around extensive testing in OpenStack makes it easier for us
to trust patches proposed for review. We've integrated this culture into our
review process. Duplicating a social and technical CI system of this size takes
incredible amounts of time, people, and patience. Bolstering the CI system we
already have in place allows you to focus on testing that is specific to your
product or service.

Immediate Feedback
~~~~~~~~~~~~~~~~~~~

The OpenStack CI system is the backbone of feedback for contributors and
operators. Users get this feedback early, ideally before the patch lands.
Ensuring early feedback through a robust CI system and testing means fewer
surprises down the road when you attempt to integrate your product into a new
release or deploy a new version of a service.

Contact
-------

Join the #openstack-infra channel on the Freenode IRC network or reach out
through the openstack-infra mailing lists on lists.openstack.org if you would
like to get involved. It’s a rewarding chance to learn and help others, but
most of all it’s fun! The Technical Committee sponsor for this initiative is
Jeremy Stanley (fungi).
