..
  This work is licensed under a Creative Commons Attribution 3.0
  Unported License.
  http://creativecommons.org/licenses/by/3.0/legalcode

..
  This template should be in ReSTructured text. Please do not delete
  any of the sections in this template.  If you have nothing to say
  for a whole section, just write: "None". For help with syntax, see
  http://sphinx-doc.org/rest.html To test out your formatting, see
  http://www.tele3.cz/jbar/rest/rest.html

.. Modify the next line to replace <proposed-tag-name> with the tag
   name, then remove this comment.

.. _`tag-<proposed-tag-name>`:

========================================================================
proposed-tag-name (should match the tags/proposed-tag-name.rst filename)
========================================================================

..
  Tag names can contain a prefix that represents the category of tag.
  Category prefixes should end in a colon (:). Category prefixes as
  well as tag names should follow a lowercased-hyphen-separated
  style. Examples: 'release:coordinated' or 'docs:api-reference-complete'

Introduction paragraph -- a short summary of what this tag will mean.


Application to current deliverables
===================================

As part of the application you need to go through the exercise of applying
the proposed tag to at least some subset of the current deliverables or teams
(depending on whether the tag applies to teams or deliverables). This
will serve as an example of how the tag should be applied in the real world.
You may also submit (as a subsequent change) the corresponding governance
change to immediately apply the proposed tag to deliverables or teams.

.. tagged-projects:: <tag name>


Rationale
=========

The detailed reason why the OpenStack ecosystem benefits from having this tag
defined.


Requirements
============

* A list of requirements for granting the tag to an existing project.
* All the criteria should be objective and predictable.
* If a tag requires another tag, this should be mentioned here.


Tag application process
=======================

Details of the process to follow to maintain the tag. Are additions/removals
regularly reviewed, or are they considered only upon request ? Which group
is involved, and at which frequency ?

The process may include requiring feedback from specific groups, delegation
of tag maintenance from the TC, minimum delays between application and tag
grant, timeframes where granting or removing the tag is appropriate, etc.

If the grant process is different from the removal process, this should also
be mentioned here.

By default, you can use the following process:

Anyone may propose adding or removing this tag to a set of projects by
proposing a change to the openstack/governance repository. The change is
reviewed by the Technical Committee and approved using standard resolution
approval rules, including discussion at at least one Technical Committee
public IRC meeting.


Deprecation
===========

Some tags may have a deprecation period (where a project retains the tag but
only until a certain announced date). If the proposed tag has a deprecation
period, its duration (and any other specific rules) should be listed here.
