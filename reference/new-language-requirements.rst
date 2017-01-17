.. NOTE(flaper87): This document sets the bar high on purpose. The idea is to
   list all the possible things that may be needed/useful when adding a new
   language and reduce it. I'd like this cleaning process to happen during the
   review of the document. Therefore, before it lands.

=================================================================
 Requirements for language additions to the OpenStack Ecosystem
=================================================================

Adding new programming languages in OpenStack is possible by following the
process described below. Every new language addition goes through careful
consideration on both, technical and community, aspects. When considering a new
programming language addition, the community must consider whether this language
may or may not fragment the community, what the impact is on the infrastructure
team and systems, how this language impacts the release model, etc.

Innovation is highly encouraged. However, teams experimenting with new languages
should keep under consideration the points mentioned above and the process
explained in this document. New programming languages in OpenStack are added
under specific circumstances where the existing, already accepted, languages
have been proven to not meet the technical requirements and the concerns
at the point evaluation.

.. NOTE(flaper87): Is the 2-steps process good or just too complex? I like it
   because it allows for separating discussions (which was a problem in previous
   proposals) and it also allows for organizing the work. Teams should not worry
   about doing any of the up-front work until phase 1 is over. Once phase1 is
   passed, teams can work on addressing the requirements and move their projects
   forward in parallel.

   Other processes that would allow for some separation like the one I mentioned
   above are worth evaluating too.

The process for adding a new language consists of two separate steps that
require some work up-front. The first step involves the analysis of the need for
a new language and the second one the support for the new language in the
OpenStack ecosystem.

After reviewing and agreeing on the need for a new language, the team driving
this effort should start working on the second phase. The needs of a new
language should not be questioned during the evaluation of the second phase,
unless the team working on it decides the language is not needed anymore.

Step 1: Use case analysis
#########################

The TC will evaluate the use case for the new proposed language in this phase.
Members of the community interested in this addition are expected to have
started a discussion on the mailing list before presenting the request to the
TC. It's encouraged to let the mailing list discussion mature before it's
brought to the TC.

The discussion should evolve around the needs of the language, the technical
difficulties at hand and the reasons why existing languages are not good enough
for the task. Adding a new language should not be the norm and it comes with a
cost, as explained earlier in this document. Projects should strive for
consuming the existing languages in the ecosystem.

Once the discussion has matured, the request should be brought up to the TC for
further discussion, evaluation and voting in the form of :ref:`resolutions`.

Step 2: Requirements evaluation
###############################

If the need of a new language is agreed on, the members interested in it are
expected to work with the rest of the community on meeting the following minimum
requirements:

Setup the CI pipelines for the new language
-------------------------------------------

Work with the infrastructure team on setting up CI pipelines for projects using
the new language. The following tasks should be addressed as part of this work:

* CI jobs for lint checkers
* CI jobs for unit tests
* CI templates for functional tests
* CI jobs for documentation builds
* Ensure the jobs for meeting the :doc:`project-testing-interface`
  requirements exist.
* subunit-formatted output from tests
* Provide a mechanism for pre-caching and/or mirroring dependencies in the gate
* Provide plugins for DevStack to help creating QA and development environments

Define how the deliverables are distributed
-------------------------------------------

Work with the release team to define the release processes for projects using
the new programming language. These processes should answer the following
questions:

* Should the deliverables be shipped in binary format? or is the source code
  enough?
* How can the release of the new deliverables be automated?
* Where should the deliverables be published? Is there a PyPi equivalent for the
  new language?

Define how stable maintenance will work
---------------------------------------

Work with the stable team to define the maintenance processes for stable
branches. These processes should address the following requirements:

* Backport policies (if new policies are needed)
* CI jobs for stable branches
* Identify main contacts for stable branches and jobs maintenance

Define how internationalization will work
-----------------------------------------

Work with the i18n team to define the translation processes for projects using
the new language. These processes should address the following requirements:

* Provide tools and jobs for importing and exporting translations

Define how documentation will work
----------------------------------

Work with the documentation team to define the processes for generating,
publishing and maintaining the documentation for projects using the new
language. All projects should use Sphinx for their project documentation and
follow the api-ref_ standards for their API documentation, should they need one.
The use of language specific tools for other type of documentation (developer's)
is fine.

* Provide tools and jobs for generating documentation
* Adopt OpenStack's themes and documentation standards.

.. _api-ref: http://developer.openstack.org/api-guide/quick-start/index.html

Define how dependencies will be managed
---------------------------------------

Work with the infrastructure and requirements team to define a process for
managing dependencies for the new language similar to the existing
`requirements` process used for Python dependencies. This process should
describe:

* How the dependencies for the new language are consumed
* How the dependencies for the new language can be managed, pinned, etc,
  if necessary
* How the dependencies' license will be tracked and reviewed
* How testing-specific dependencies can be managed
* How to track reproducible builds

Define a way to share code/libraries for projects using the language
--------------------------------------------------------------------

Work with the Oslo team to define the processes for sharing common code among
projects using the new language. These processes should answer the following
questions:

* What team owns the shared code? Should this code fall under the Oslo team
  umbrella?
* How are the produced libraries going to be delivered?
* How are the produced libraries going to be consumed?

Guarantee compatible functionality for the base common libraries
----------------------------------------------------------------

Most OpenStack projects rely on a set of base common libraries that provide a
seamless experience to operators and users of OpenStack. The team proposing a
new language must provide a compatible behavior with these libraries either by
developing a counterpart version of the library in the language or proving that
the language itself (or any existing library) is capable of guaranteeing
compatibility.

The following libraries have an impact on the operator's and user's experience,
therefore their behavior is considered critical and it must be guaranteed by any
new language:

* oslo.config
* oslo.log

Once the above requirements have been addressed, a final resolution should be
brought up to the TC. This resolution will mark the language as an official
language in the ecosystem. OpenStack projects consuming this language can be
released from this moment on.
