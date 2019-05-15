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

.. _`tag-status:maintenance-mode`:

=======================
status:maintenance-mode
=======================

The status:maintenance-mode tag is a project team level tag.

There are situations the project team or the TC wish to indicate that
a project team is in a period of low activity (which we call
'maintenance-mode'). This is accomplished by applying the
status:maintenance-mode tag to the project team.

Application to current teams
============================

.. tagged-projects:: status:maintenance-mode


Rationale
=========

From time to time, and for any number of reasons, a project team
enters a period where there is reduced activity and contribution.

When a project team, or the Technical Committee determine that a
project team is in such a transient state, the 'maintenance-mode' tag
can be applied to it. The application of the tag signals to all that
the project team is in this mode, and they can set their expectations
on activity accordingly.

The following section (Requirements) describes the requirements for a
the tag to be applied.

Requirements
============

The tag can be applied by the Technical Committee or the project team,
the project team has entered a transient period of low activity.

It is important to understand that this is intended to be for a
transient period of low activity, one that can be exited if there are
additional active contributors who are able to contribute actively to
the project team.

* the project team has an appointed, and responsive release liaison
* the project team has an appointed, and responsive liaison to the
  security team
* the project team will meet the release goals, and take the necessary
  actions required to cause a release to be available as part of the
  regular OpenStack release schedule
* the project team will fix and release fixes to security issues
  raised by the VMT
* the project team will keep their project in line with the global
  requirements list

When a project team is in maintenance-mode, the following are
explicitly not guaranteed.

* the project team does not guarantee the review and merging of
  non-critical bug fixes
* the project team does not guarantee the implementation and delivery
  of new features and functionality
* the project team makes no commitments to respond to queries on the
  project's IRC channel or on the mailing list
* the project team makes no commitments to hold its regularly
  scheduled meetings.

Tag application process
=======================

This tag is applied either by the Technical Committee or the project
team (voluntarily).

The application of the tag requires a change to be submitted to the
governance repository. The change should include a justification for
why the tag should be applied or removed.

The change is reviewed by the Technical Committee and discussed with
the project team. It should be approved using standard resolution
approval rules, including discussion at at least one Technical
Committee public IRC meeting.

Deprecation
===========

The Technical Committee may from time to time review project teams
that are in maintenance-mode to consider other actions (such as making
the project unofficial) as they feel is appropriate.
