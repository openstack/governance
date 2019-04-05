==========================================
 2019-03-22 Namespace Unofficial Projects
==========================================

As OpenStack has evolved, the infrastructure program hosting OpenStack code
has also evolved into its own program called OpenDev. As OpenDev prepares to
move git hosting to new URLs and new backends, OpenStack has an opportunity
to revisit previous choices about how projects are namespaced.

Previously, OpenStack had a concept of "stackforge" to host unofficial
projects. Eventually, the TC :ref:`retired the stackforge name
<20160119_stackforge_resolution>` and git namespace in order to simplify the
logistics of moving projects from unofficial to official, and the "openstack"
git namespace became a place for all projects hosted on OpenStack's git
infrastructure.

As the growth of OpenStack has slowed and processes have improved, the need
to streamline the process of making a project official has decreased.
Additionally, a single namespace has caused confusion in the community about
which projects are official and which are unofficial.

It's become clear that OpenStack should use this opportunity to go back to the
old model of a separate namespace for unofficial projects. When the git
repositories are moved to the new OpenDev infrastructure, a new namespace
called "unknown" will be created, and all unofficial projects currently
hosted in the OpenStack infrastructure will be re-located there. All official
projects will remain in the "openstack" namespace. This includes projects
which are currently in the "openstack-dev" and "openstack-infra" namespaces
which are not moving to another namespace (e.g. "opendev").

Unofficial projects moved to the "unknown" namespace are encouraged to find
a home in an existing namespace other than "openstack", or to create a new
namespace for themselves.
