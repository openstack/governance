====================================================
Community Infrastructure Maintainer for ELK Services
====================================================

Summary
-------

The OpenStack community is seeking developers and system
administrators with a background in maintaining Unix/Linux servers and
free software to join the Infrastructure team (TaCT SIG now).  This
team is responsible for designing, building and maintaining the
systems that are used in the day to day operation of the OpenStack
project as a whole.

There is a critical need for infrastructure team members for maintaining
Logstash, Elasticsearch, Elastic-recheck services. These services
(collectively called ELK) + elastic-recheck service which automate
the identification of most critical failures. These services are used by
upstream community development in day to day software development
and testing. This helps the community to deliver the stable code. To know
more details about the criticality of these services in upstream development
please refer to `this ML thread <http://lists.openstack.org/pipermail/openstack-discuss/2021-May/022439.html>`_

Business Case
-------------

Sponsorship of a team member is a way to visibly help build and
maintain the development, collaboration, and testing tools used by the
third most active open source project in the world without having to
donate hardware.  Team members interact with contributors across all
the OpenStack projects as well as with the OpenStack service providers
who supply resources for OpenStack CI systems.

Sponsors of infrastructure team members have a "seat at the table" as
decisions are made about how to improve and scale OpenStack
infrastructure going forwards.

Sponsors gain in-house expertise and experience building large-scale,
adaptive software development infrastructure with open-source tools
and public configuration management.  There is no better way to gain
exposure to, and expertise with, leading-edge CI/CD in advance of
potential deployment at home, than to place someone on the team
deploying one of the world's most scaled out instances of the `Zuul
project`_.

The software developed, skills involved, and open community practices
learned can have high value downstream in a sponsor's own enterprises
and software products.

.. _`Zuul project`: https://zuul-ci.org

Technical Details
-----------------

The OpenStack community team pushes a lot of code changes and to test it
thoroughly, each code change runs a lot of jobs in CI in an integrated way
with a different set of configurations. All of the tests make sure that
OpenStack as a whole stack works and is stable software when delivered at
the end. This complete process involves a lot of tooling and their maintenance.

The infrastructure team is responsible for designing, building and maintaining
the systems that are used in the day to day operation of the OpenStack project
as a whole; this includes development, testing, and collaboration tools. All of
the software it runs is open source, and under public configuration management
so that everyone in the community has the opportunity to participate. One very
effective way to get involved in OpenStack and gain a deep understanding and
visibility within the community is by helping operate this infrastructure.

A few of the tools which are critical for day to day upstream development are
Logstash, Elasticsearch, Kibana (ELK as short) and Elastic-recheck and because
there is no maintainer, they are being `proposed for retirement
<http://lists.openstack.org/pipermail/openstack-discuss/2021-May/022439.html>`_.

In particular, the team seeks developers and systems administrators
with a background both in maintaining Unix/Linux servers and free
software, to maintain the ELK services. Everything possible goes through code
review, and gets extensively documented and communicated with the rest of the
community over IRC and mailing lists. Server resources are donated
by companies operating OpenStack services so there is
substantial opportunity both for people who have experience in those
technologies as well as anyone wishing to gain more familiarity with
them.

Value
~~~~~

The infrastructure team leverages resources donated from companies operating
OpenStack services. The community uses the software it produces as a tool for
testing it. Every day, contributors submit thousands of patches for review.
Infrastructure tools deploy each patch and test it against thousands of tests
and scenarios. This volume provides an opportunity to improve the software we
write by giving us first-hand experience with issues at scale. The benefit of
fixing these issues for the OpenStack CI system is two-fold:

1. It makes the test platform more stable and robust
2. Products or services benefit from the fixes being applied upstream

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
release or deploy a new version of a service. Without the ELK services, it will
be very difficult to debug a failure and to deliver the stable code.

Contact
-------

Join the OpenStack Infra IRC channel (``openstack-infra`` on `OFTC
<https://www.oftc.net>`_) or reach out through the openstack-discuss
mail list at list.openstack.org if you would like to get involved.
