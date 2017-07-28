======================================================================
 2017-06-13 Document current level of community database support
======================================================================

Over the years, OpenStack's ecosystem and developer community grew
around MySQL (as defined in [#f2]_). Emerging from the OpenStack
User Survey 2017 [#f1]_ there is a trend visible that most production
deployments today settle on MySQL as the configured database backend.

Although the OpenStack User Survey is non-authoritative, its reported
bias (> 10 to 1 for MySQL [#f2]_ vs. PostgreSQL [#f3]_) is also
mirrored in openstack-operator mailing list posts, ask.openstack.org
posts, and content during operator meetups. In contrast, production
deployments using PostgreSQL appear to be less popular ([#f4]_).

The OpenStack community is generally offering wide ranges of options
to the users. For DBMS we advocate the use of abstraction layers
like for example oslo.db and SQLAlchemy to avoid a lock-in on a
specific database implementation.

Still the development community could design and develop individual
features with specific backends in mind. Even if portability issues
are caught during code review and various levels of automated QA,
there is still impact on the community like documentation and other
cost of handling peculiarities of each DBMS like best practices
for each implementation choice.

Therefore, we should clearly state that currently in the OpenStack
community there is a bias towards MySQL [#f2]_ over other
databases like for example PostgreSQL.

As a set of concrete steps we should do the following:

- The OpenStack documentation should be updated to document the
  community preference::

    .. warning::

       While OpenStack can be used with many SQL DBMS, please
       be aware that the upstream OpenStack developer community
       is so far focusing on the MySQL family of databases
       as a backend and tests OpenStack against the version of
       MySQL provided with Operating System distributions.

       If you exclusively rely on the OpenStack upstream
       community and not on an OpenStack vendor for support of your
       OpenStack installation you are proceeding at your own
       risk by choosing a different DBMS backend.

- We should state to the OpenStack Foundation that there needs
  to be a way for distributors to report back aggregate data about
  their users, who are not self reporting to the survey. The upstream
  community does not have infinite resources, and is legitimately
  trying to make hard and informed decisions about things not to do.
  Because there is no mandatory registration of clouds, the best
  information we can get is via the User Survey and what vendors
  decide to share.

In the future we may want to make stronger statements, but the
important thing is being clear to users that PostgreSQL is currently
not first class supported upstream and there isn't any
coordinated effort to change that.

This should not exclude vendors claiming support for other DBMS choices
for their customers. However, for users bypassing vendors and
going straight to upstream, the current reality of OpenStack
enablement needs to be clear.


.. rubric:: Footnotes

.. [#f1] April 2017 User Survey
         https://www.openstack.org/assets/survey/April2017SurveyReport.pdf
.. [#f2] The term MySQL is used as a reference to the MySQL database and
         the close variants MariaDB and Galera.
.. [#f3] The term PostgreSQL is used as a reference to the PostgreSQL
         database and close derivatives.
.. [#f4] As of the Boston Forum (May 2017) known users of PostgreSQL
         are:

         - SUSE: investigating migrating to Galera
         - Huawei: not actually PostgreSQL, but an internal db based on pg.
         - Windriver
         - SAP: consuming OpenStack directly, not via vendor. They
           did not respond to the user survey, so their usage is not
           recorded there.
