==========================
Service and Project Naming
==========================

OpenStack projects must follow naming conventions for both the project team
and the service the team provides. Following are some guidelines for
reference to ensure consistency, reduce confusion, and enable documentation
clarity.

Project Naming Process
----------------------

The Technical Committee reviews the incoming project proposals through the
:repo:`openstack/governance` repository with an update to the
``doc/source/reference/projects.yaml`` file. TC members should review
the patches with these guidelines.

Project Name Guidelines
-----------------------

When seeking a project name refer to the `Legal Issues FAQ
<https://wiki.openstack.org/wiki/LegalIssuesFAQ>`_ on the OpenStack wiki.
Realize the team name will not become a trademark.

In documentation on `docs.openstack.org <http://docs.openstack.org>`_, project
names are consistently lowercase, such as nova and keystone. The documentation
also uses lowercase when referring to file names such as ``nova.conf``, and when
referring to the Command Line Interfaces (CLI) for those projects including
the ``openstack`` CLI command.

The history of this decision is that the documentation contributors wanted the
least amount of cognitive overhead when writing and reviewing. Learning rules
about case can be difficult across multiple projects with hundreds of
documentation contributors and thousands of changes and additions. Lowercase
for project names as a rule is then easiest to review and enforce at this scale
and growth pattern.

Service Name Guidelines
-----------------------

When naming the service that your project provides, please consider the use
of the service name in documentation for operators, administrators, end-users,
and developers consuming the service. The current convention is:

* Use service in documentation to further clarify what the project offers.
* Use an initial capital for all words in the service name, including the word
  after a hyphen.
* Do not use OpenStack in the name of the service. Certain other words may
  be reserved also due to trademark, but we have had examples of getting
  permission such as Puppet.

Examples of these guidelines in service names are: the Block Storage service
(cinder), the Object Storage service (swift), or the Bare Metal service
(ironic).

Review Guidelines
-----------------

Early in the OpenStack history, service names in
combination with the brand name "OpenStack," were thought to be legally
binding. However, as more services are added, the complexity of the names of
services has increased. So, while the names are considered proper nouns, naming
conventions do not indicate a legal right to the name.

If you have a question about legal use of the OpenStack name or logo, refer to
the `OpenStack Brand website <http://www.openstack.org/brand>`_. Refer to
`Documentation Conventions <http://docs.openstack.org/contributor-guide/writing-style/general-writing-guidelines.html>`_
and ask for guidance on the openstack-docs mailing
list if you have questions about using the names in context. As a final
arbitration or decision point, refer to the `IBM Style Guide <https://www.redbooks.ibm.com/Redbooks.nsf/ibmpressisbn/9780132101301?Open>`_
as it is the final decision point for spelling or usage of a term.

Developer documentation may refer to the project name, but end-user, operator,
administrator, and application developer documentation must refer to the
service name. When reviewing service names, consider the consumers of the
information.
