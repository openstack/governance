=============================================================================
 Engineer to Adapt the Current Zanata Translations Infrastructure to Weblate
=============================================================================

Summary
-------

The OpenStack community is seeking an engineer with system administrator skills
(or a system administrator with engineering skills) to adapt the current
translations infrastructure that connects gerrit/zuul to a self-hosted Zanata
server, to connect instead to a third-party hosted Weblate server.

Business Case
-------------

The official language of OpenStack is United States English (en-us).
End-user-facing strings in both the web UI and in responses from the OpenStack
APIs appear by default in en-us.  This can be a barrier to non-native English
readers who would otherwise like to use an OpenStack cloud.  Sponsoring an
engineer to adapt the current translations infrastructure from Zanata to
Weblate is a way to visibly demonstrate your commitment to the OpenStack
community and investment in support for its translation to other languages.


Technical Details
-----------------

There are two Zuul CI jobs that exist today: upstream-translation-update and
propose-translation-update [0].

upstream-translation-update operates in a source repository and generates a
gettext .pot translations file for that repo then uploads those to Zanata
[1]. This is the piece that takes information from the git repos and puts it in
Zanata so that translators know what needs to be translated.

propose-translation-update operates in a source repository and fetches .po
files containing translated strings for various languages and synchronizes them
into the git repositories then pushes the result to Gerrit for review [2].

Unfortunately, the end result here is some `spaghetti code
<https://wikipedia.org/wiki/Spaghetti_code>`_.  A possibly incomplete list of
bits that come into play here: [3][4][5]. Much of this isn't actually Zanata
specific and can be reused. We suspect that the bulk of the work in switching
to Weblate is updating these scripts [1][2] to talk to Weblate. Additionally,
reorganizing things to be more centralized and easier to maintain would be
helpful.

Another approach would be to build new jobs from scratch copying what is useful
from the old Zanata stuff. Then we can run both sets of jobs in parallel as
part of the transition ; this also has the upside of allowing you to refactor
from the start.

[0] https://opendev.org/openstack/project-config/src/commit/b5e236a37ece2a31959142b282cb24186439921e/zuul.d/jobs.yaml#L1168-L1223

[1] https://opendev.org/openstack/openstack-zuul-jobs/src/commit/ab0fad7f5878961884394a4c552256947a106fdc/roles/prepare-zanata-client/files/upstream_translation_update.sh
(Note the extract_messages_* functions that are called; these create .pot files for various types of sources.)

[2] https://opendev.org/openstack/openstack-zuul-jobs/src/commit/ab0fad7f5878961884394a4c552256947a106fdc/roles/prepare-zanata-client/files/propose_translation_update.sh

[3] https://opendev.org/openstack/project-config/src/commit/b5e236a37ece2a31959142b282cb24186439921e/playbooks/translation/

[4] https://opendev.org/openstack/project-config/src/commit/b5e236a37ece2a31959142b282cb24186439921e/roles/copy-proposal-common-scripts

[5] https://opendev.org/openstack/openstack-zuul-jobs/src/commit/ab0fad7f5878961884394a4c552256947a106fdc/roles/prepare-zanata-client/

Contact
-------

Join the OpenStack Internationalization (``#openstack-i18n``) or TC
(``#openstack-tc``) channel on `OFTC <https://www.oftc.net/>`_ to get
more information.

You can also reach out through the `OpenStack Community Mailing List
<mailto:openstack-discuss@lists.openstack.org>`_ if you would like to get
involved.  Include ``[i18n]`` in your email's subject line.
