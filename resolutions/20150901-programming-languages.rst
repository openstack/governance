============================================
 2015-09-01 OpenStack Programming Languages
============================================

Every programming language is designed to solve a slightly different
problem space and comes with its own benefits. OpenStack started out
with only Python, a "batteries-included", operator-friendly, highly
readable and easy to learn language. Over time, we added bash and
JavaScript, which both address slightly different problem spaces where
Python was either suboptimal (system scripts) or not available (in-browser
execution). At the date of this resolution, the supported languages in
OpenStack are therefore: bash, javascript, python. However we should *not*
limit OpenStack service projects to these three programming languages in the
future, as it would either mean using suboptimal tools, not being able to
address specific problem spaces, or artificially excluding specific project
teams.

At the same time, we recognize that supporting more programming languages
comes with a community cost. Every added language needs to be properly
supported by cross-project efforts (like infrastructure, QA, release
management, vulnerability management, documentation...), efforts which
already struggle keeping up with the current set of languages (JavaScript
is still not totally supported by those). Every added language also further
fragments our community, and requires extra care to converge to our common
culture, which defines "are you OpenStack" in the context of the big tent.

Because we recognize these considerations, the OpenStack Technical Committee
will allow additional language support in OpenStack projects on a case-by-case
basis, carefully weighing the technical benefits of supporting the new
language against the community costs of supporting it.

We already recognize a number of standing exceptions to this rule:

* short-term experimentations in feature branches
* temporary legacy code, as long as the medium-term plan is to completely
  remove it
* downstream packaging, which uses the specific language of that particular
  trade (like Ruby Puppet recipes)
* project infrastructure configuration files, plug-ins or extensions, where
  the language is dictated by the tool being used or integrated
* downstream language SDKs, which obviously are implemented in the local idiom

The general idea is that this resolution applies to upstream OpenStack
services and libraries which are our main deliverables, not to downstream
integration projects or development infrastructure. The Technical Committee
will use common sense when considering those requests on a case-by-case basis.
