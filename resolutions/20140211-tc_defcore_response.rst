=============================
 2014-02-11 DefCore Response
=============================

This resolution is the draft of an email from the TC to the Board DefCore
committee on the issue of identifying "required sections" of code.

---

The Technical Committee thanks the Board for requesting our assistance in
defining the requirements for usage of the OpenStack trademark [1] in
defining "core" components of OpenStack [2]. This is an important and
complicated issue, so the Technical Committee feels that it needs to be solved
in stages. In order to improve the engagement of the Technical Committee on
this issue, we have selected Michael Still as our representative to the
"DefCore" subcommittee, with Anne Gentle as his backup.

The Technical Committee understands that the end goal of the Board is to
define criteria that can be used to define who shall be granted a license to
use the OpenStack trademark. We understand that these criteria will be
defined per OpenStack release, and that there is therefore scope to
incrementally refine the requirements over time.

Designating areas of codes where a private implementation can be substituted
for the mainline code [3] is time consuming, but otherwise a technical and
objective answer. However, deciding which, amongst those areas, constitute a
required use is more subjective and depends on the stakeholders we want to
best serve.

The Technical Committee warns that we are unlikely to reach a consensus
position in a time that is reasonable for the Icehouse release. Additionally,
we believe we would have the following further policy questions for the board:

* how granular and specific does the board want this to be? How do we handle
  drift in the code over time from operations such as refactoring? How do we
  identify designated sections -- both line numbers and cryptographic hashes
  of the lines of code have been proposed, but both methods are flawed.

* how limiting should it be? For example, are backports from master of fixes or
  features to the designated areas allowed?

* many parts of OpenStack are pluggable in ways that do not replace designated
  sections and are not alternate implementations of a plugin interface - for
  example you can add new WSGI middlewares or scheduler filters - how much of
  this extensibility does the board wish to allow?

* altering libraries (3rd party, or part of OpenStack itself) can have as much
  impact on behaviour as altering OpenStack services itself. Is there a desire
  to address this?

* at some point, these sorts of requirements, and the desire to force people
  to engage upstream, seem confusingly at conflict with our "business friendly"
  choice of a permissive license (i.e. the Apache License vs, say, the AGPL).
  How does the board reconcile the use of an extremely permissive software
  license with an extremely restrictive trademark license?

There are a variety of stake holders in this discussion, and it is hard to
balance the requirements of those stake holders in the requirements definition
process.

The Technical Committee sees the stake holders as:

* end users -- end users care about interoperability of deployed OpenStack
  clouds. This interoperability is best measured by API testing, with
  tempest being a likely vehicle to drive such testing.

* deployers -- organizations deploying OpenStack in their datacenters want
  confidence that their OpenStack distribution is providing code that will be
  supported long term by the OpenStack community. Privately implemented
  features increase the risk to these deployments as they are reliant on a set
  of developers that is smaller than the entire OpenStack community.

* distributors -- distributors need the ability to differentiate their
  products, but they also need to be able to entice deployers away from other
  distributors. This compatibility of different distributions is one of the
  competitive advantages of OpenStack, and should be protected by our
  trademark policy. Therefore, we do not believe that private features are the
  right way for distributors to differentiate their products.

* developers -- the OpenStack development community is also an important part
  of the OpenStack ecosystem, and should be considered in this process. We
  feel that encouraging distributors and other employers of developers to
  engage with the upstream community is of value, and that the preference is
  for all code to end up going through our development process instead of
  being held in private.

We understand that the DefCore committee is intending the "defined sections of
code" requirement as a way of protecting deployers and developers from private
patches being held by distributors on critical sections of the OpenStack code.

However, addressing the needs of all of these stake holders is not possible
in the time available in the Icehouse release. Therefore, we would like to
suggest a focus on ensuring that end users have a good experience with Icehouse
being the priority at this time. The Technical Committee encourages the
DefCore committee to therefore focus on defining the set of API tests that a
compliant OpenStack should pass for this release. We can then iterate in future
releases to extend the requirements for trademark licensing to cover the
needs of additional stake holder groups. The Technical Committee suggests that
tempest is the right vehicle to implement these interoperability tests.

It is felt by the Technical Committee that whilst API testing is a good first
step, it should not be sufficient to remove the requirement that:

    "[distributors] include the entirety of the OpenStack [..] code from
    either of the latest two releases and associated milestones" [4]

This requirement should remain until the further issues outlined in this
response can be addressed.

In summary, the Technical Committee proposes a focus on black box API
interoperability testing for the Icehouse release, with a plan to iterate the
requirements for future releases.

---

1:   http://eavesdrop.openstack.org/meetings/tc/2014/tc.2014-02-04-20.02.log.html#l-332

    <joshuamckenty> we need the PTLs to decide what code sections are designated sections
    <joshuamckenty> nova might make the "conductor" a designated section
    <joshuamckenty> capabilities don't have to be implemented with the same code unless that code is a designated section
    <joshuamckenty> e.g., neutron plugins

  https://wiki.openstack.org/wiki/Governance/CoreDefinition

2: https://wiki.openstack.org/wiki/Governance/CoreDefinition (section 4)

3: http://lists.openstack.org/pipermail/openstack-dev/2014-February/026413.html

4: http://lists.openstack.org/pipermail/openstack-dev/2014-February/026559.html
