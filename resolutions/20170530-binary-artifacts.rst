=================================================================
 2017-05-30 Guidelines for Managing Releases of Binary Artifacts
=================================================================

Until recently, the community has avoided releasing "binary" artifacts
such as compiled executables, operating system packages, or system
images. We have cited several reasons for the existing policy:

1. Binary executables, especially for languages that statically link,
   vendor, or aggregate dependencies, are harder to update if the code
   is subject to logical or security-related bugs.
2. System packages built in the community are not likely to be
   supported by the system vendors.
3. System and container images contain many different pieces of
   software, and therefore have an even greater risk of including
   faulty or malicious content.

Because the community did not have the resources to support the
inevitable use of binary artifacts in production deployments, we
focused on distributing OpenStack in source form by publishing source
archives to tarballs.openstack.org.  We have also published
developer-focused Python package formats such as sdists and wheels to
pypi.python.org because those formats are useful in our own CI
systems, and because it seemed clear, if only implicitly, that
consumers of the packages would understand they are not supported for
production use.

In contrast, the open source communities based around some of the
tools that we are adopting do release binary artifacts as a standard
practice. Container images and full system images are often published
to community-specific indexing services such as Docker Hub or
Vagrant's Atlas service. The results can then be consumed by anyone
familiar with the tools for searching those repositories. Binary
executables built from compiled languages such as Go are often made
available from project websites, as well.

Guidelines
==========

Although our community still does not have resources to support
production deployments, this shift in the common practices of other
communities is leading some of our teams to want to distribute binary
artifacts as well. This resolution describes some guidelines for doing
so, while mitigating the risks associated with someone inevitably
using the results in production.

* Users need to know what they are getting when they download
  artifacts, to enable them to know which artifacts are compatible
  with each other, with their infrastructure and to be able to find appropriate
  documentation. For this reason, the metadata for each artifact must
  clearly specify the name and version of the principal component it
  contains as well as the architecture for which it is built.
  For example, if an image contains the nova conductor from
  version 16.0.0, that information should be accessible, either
  through the name or through metadata associated with the image using
  whatever mechanism is common to the index or repository service
  where the image is published.

* Consumers of these artifacts need to be able to track bugs and
  security issues in components included in the artifacts. For this
  reason, all published binary artifacts must be accompanied by a
  manifest describing the versions of all components used to build it,
  whether they be the libraries used to build an executable or the
  system packages included in an image.

* The contents of binary artifacts "age" and become out of date as
  development work continues, either on the primary component or on
  dependencies built into the artifact. Consumers of these artifacts
  need to know whether they have a recent version, or if they are far
  out of date. For this reason, all binary artifacts should include
  metadata containing the date they were built, as well as the date
  they were published (if it is different).

* Users need to be able to reproduce environments, and developers need
  to be able to reproduce builds in order to investigate issues.
  Contributors to projects should not be expected to support or debug
  arbitrary versions packaged by someone else.  For these reasons,
  binary artifacts published to third-party registries should only be
  built from well-defined points in the history of an OpenStack
  project, identified with signed tags on the git repository. The inputs
  to recreate the build, including configuration files and build scripts,
  must be made available so that anyone can rebuild the image.

* We do not want the artifacts to be seen as owned by the community at
  large, if only a few people can actually address issues. For this
  reason, the metadata for binary artifacts must not say or imply that
  they are produced by "the OpenStack community." Specific team names
  should be used instead.

* Because only a subset of the community is producing and maintaining
  the artifacts, we need to ensure it is clear to consumers where to
  go if they do want help. For this reason, each artifact must be
  published with metadata, such as a bug tracker URL, describing where
  and how to seek help.

* Consumers of these artifacts need to understand the limits of the
  support they are likely to be able to receive. All of our official
  projects are released under the `Apache License
  <http://www.apache.org/licenses/LICENSE-2.0.html>`__, which includes
  a *Disclaimer of Warranty* stating that the software is provided
  without warranty and a *Limitation of Liability* saying that
  contributors are not liable for damages. It also, however, includes
  a clause allowing "redistributors" to offer additional levels of
  support. Teams must not indicate that they are offering support for
  any binary artifacts in a way that implies the warranty or liability
  for that support extends to the rest of the community.

References
==========

* This was discussed extensively in the openstack-dev mailing list
  thread `"do we want to be publishing binary container images?"
  <http://lists.openstack.org/pipermail/openstack-dev/2017-May/116677.html>`__
* There were at least 2 sessions at the Forum in Boston in 2017 to
  cover `"Methods and Projects for deploying OpenStack with
  Containers"
  <https://etherpad.openstack.org/p/boston-deploying-openstack-on-k8s>`__
  during which the topic was discussed.
