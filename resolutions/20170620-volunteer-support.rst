===========================================
 2017-06-20 Definition of Upstream Support
===========================================

Here we clarify what we mean by "upstream supports this feature" and
"upstream does not support this feature". We do that by looking at some of the
necessary conditions for "upstream support".

The upstream codebase is created and maintained by a community of volunteers.
As such, neither the TC, PTL or project teams are able to assign tasks to
contributors. In addition, its worth noting that many of those working on
upstream only spend part of their working week focused on upstream.

The Apache 2 license used by the community is clear about the lack of Warranty
and Liability. This document does not seek to contradict that.

Given all this, the term "upstream support" is more complicated than it
would first appear. It could be getting a reply to a mailing list post,
fixing a bug you reported, getting your code reviewed and merged, getting
help in IRC to debug a production issue or something else. In this document
we describe what needs to be in place to help provide some level of
"upstream support".

Implemented Upstream
====================

If something has not been implemented, it is sure not to work and
clearly can't be "supported" in any way.

We can ask these questions:

* Has someone implemented support for this upstream?
* Has this been implemented in an out-of-tree driver?
* Is the publicly available code for the out-of-tree driver useful when
  debugging problems in that driver?

Upstream can only be expected to support something that is implemented in the
upstream code base.

Continuously Tested
===================

When something is tested on every proposed patch, we quickly know if the
proposed patch will break the feature or deployment the tests are validating.
In addition, there are certain tests code must pass before the code can be
merged into master; we call these gating tests.

Should any patch break one of the above tests, that patch author needs to work
with the community to get the tests passing before their code will merge.
It seems reasonable to say deployments and features that have this level of
testing are, in some sense, "supported upstream".

When something is not tested, history has proven those features quickly stop
working. As such, something that is not tested, should be assumed to be
broken and not supported.

Full Upstream Participation
===========================

While having something implemented and continuously tested is required to
claim any level of "upstream support", there are many other aspects to having
a well maintained feature or driver.

The team maintaining the code must work in the open, for both bug fixes and
feature development. That allows for prompt replies about bugs you need
fixing. Even if the reply says it will not be fixed, its better than being
left in the dark about what is wrong. In a similar way, if you create a fix,
you would like that to be reviewed and included in future release in a timely
manner.

In a similar way, you want confidence that the feature/driver will continue to
work across upgrade. If those maintaining that feature or driver are actively
involved in upstream design discussions, it is much more likely what you rely
on will continue to work as the system evolves.

Deprecation
===========

In extreme cases, if a feature or driver can no longer be maintained, the
implementation must be removed.
Projects that are stable and widely deployed are expected to sign
up for the :ref:`tag-assert:follows-standard-deprecation`. This gives us a
controlled way to warn users about such features or drivers that are being
replaced or at risk of being removed.

OpenStack is a volunteer community. Should some parts of the codebase no
longer have anyone stepping up to maintain them, it would be unfair to not
warn our users of the risk this creates.
In particular, if there is no reliable testing of a particular part of the
code, or a particular deployment scenario, it is hard for the community to
keep that functioning as the upstream code evolves. Moreover, it is hard to
review bug fixes to those parts of the code, because there is no testing to
help prove the proposed fix improves the situation for all users of that
part of the code base.
In many cases, the best action is to remove the implementation from the
codebase, subject to the above deprecation process.

If we never removed features that are proving hard to support, there would be
many other problems for a much wider part of the community. People who try
the feature will find it broken, and assume that's normal for all OpenStack
features. In a similar ways, developers get complacent about parts of the
code that are known to have issues, and the overall quality will drop.

It is healthy to remove some features and simplify things as we move forward.
Over time it becomes clear that particular solutions turned out to be the
wrong way to do things, so its important to transition people to the better
solution. This helps existing users move to a single more stable code base,
and stops confusing new users that have to spend time working out which
option it the best one for them. Clearly this needs to be balanced against
maintaining API compatibility.

For clarity, deprecation is not a one way process. It is a process that has
many possible outcomes. Consider these points about deprecation:

* Upstream, it's often hard to know if anyone uses the feature, and if those
  people do exist, whether they really rely on that feature or use it because
  they didn't know there was a better way forward.
* We warn users there might be problems we don't know about, and we are no
  longer in a position to accept fixes.
* For new deployments, it signals that it is best to choose another way
  to solve your problem.
* Many times there is a different more preferred way to solve the problem,
  so users can switch to a different way of solving their problem.
* For people that really rely on the feature we are removing, this gives them
  a great opportunity to step up and help stop the feature from being removed
  by helping work out how best to maintain the feature upstream.
* Sometimes, after several attempts to get people to step up and maintain a
  feature, it keeps falling into disrepair. At this point, a new approach is
  likely needed to keep the feature working.

Downstream Support
==================

For the avoidance of doubt, because a technology choice is not supported
upstream, this does not mean it can't be supported downstream in a particular
OpenStack distribution or service offering.

However if you rely on something that is not supported upstream, you need to
consider the level of vendor lock-in / reliance you are willing to accept,
taking into account how disruptive a migration to something more widely
supported might be.

Many vendors offer an SLA and/or guarantee around addressing issues and
bugs you find in your deployment. In a similar way, you can pay some vendors
to get a specific feature added. Upstream does not do any of these things.
