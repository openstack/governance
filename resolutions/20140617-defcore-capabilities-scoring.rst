=========================================
 2014-06-17 DefCore Capabilities Scoring
=========================================

The DefCore team has put together a scorecard_ combining many criteria
to evaluate which capabilities_ of OpenStack should be considered
core. They have asked the TC to help fill in the "Aligns with
Technical Direction" section, replacing the score in each cell with
either ``0`` (for "not needed") or ``1`` (for "required").

The table below includes the three columns from the "Aligns with
Technical Direction" of the original scorecard:

TC Future Direction

  Does the Technical Committee plan to continue supporting this
  feature?

Complete

  Is the feature currently implemented and fully
  working?

Stable

  Is the API for the feature stable enough to support over a long
  period?

..
  The table below reproduces the "Aligns with Technical Direction"
  section of the spreadsheet as it stands on 2014-06-17, based on
  ``defcore.csv``.  A follow-up changeset will modify this resolution
  to reflect the scores of the TC (separate patches will make it
  easier to discuss the changes from the original values).

  The ``0.5`` values are placeholders for the "undecided" scores the
  DefCore committee needs us to resolve.

  The other ``1`` and ``0`` scores were decided by the DefCore
  committee, but as these are technical questions they are also up for
  review. We should focus on filling in the missing values first, and
  may want a second pass to update the other values.

  The blank fields are for capabilities that won't be included based
  on other criteria, so we can score them but don't have to during
  this pass.

===== ================================= ===================== ========== ========
  Row Candidate Capabilities             TC Future Direction   Complete   Stable
===== ================================= ===================== ========== ========
    4 compute-servers                             1               1         1
    5 volume                                      1               1         1
    6 compute-volume                              1               1         1
    7 compute-quotas                              1               1         1
    8 compute-flavors                             1               1         1
    9 images-v1                                   1               1         1
   10 compute-auth                                1               1         1
   11 images-v2                                   1               1         1
   12 objectstore-object                          1               1         1
   13 compute-keypairs                            1               1         1
   14 compute-servers-metadata                    1               1         1
   15 objectstore-container                       1               1         1
   16 volume-snapshots                            1               1         1
   17 compute-images                              0               1         1
   18 compute-floating-ips                        1               1         1
   19 compute-instance-actions                    1               1         1
   20 compute-security-groups                     1               1         1
   21 compute-image-metadata                      0               1         1
   22 objectstore-container-quota                 1               1         1
   23 compute-virtual-interfaces                  1               1         0
   24 objectstore-container-acl                   0               1         1
   25 objectstore-acct-services                   0               1         1
   26 objectstore-container-staticweb             0               1         1
   27 <identity-non-admin-roles>                  1               1         0
   28 compute-usage                               0               1         1
   29 compute-limits                              1               1         1
   30 networks-extensions                         1               1         1
   31 networks-l2                                 1               0         0
   32 compute-ext-disk-config                     0               1         0
   33 networks-l3                                 1               0         0
   34 compute-live-migration                      1               0         0
   35 compute-servers-personality                 0               1         1
   36 networks-floating-ips                       1               0         0
   37 networks-security-groups                    1               0         0
   38 networks-lbaas                              1               0         0
   39 orch-stacks                                 0               0         0
   40 compute-multiple-create                     1               1         1
   41 networks-vpn                                1               0         0
   42 compute-attach-interface                    0               0         0
   43 networks-quotas                             1               0         0
   44 compute-auth-v3                             1               0         0
   45 compute-volume-proxy                        0
   46 compute-volume-ebs                          0
   47 compute-console-log                         1               0         0
   48 identity-admin-v3-roles                     1               0         0
   49 identity-admin-v3-endpoints                 1               0         0
   50 identity-admin-v3-credentials               1               0         0
   51 identity-admin-v3-domains                   1               0         0
   52 identity-admin-v3-policies                  1               0         0
   53 identity-admin-v3-users                     1               0         0
   54 identity-admin-v3-services                  1               0         0
   55 identity-admin-v3-tokens                    1               0         0
   56 identity-admin-v3-projects                  1               0         0
   57 volume-multi-backend                        1               1         1
   58 identity-admin-users                        0               1         1
   59 identity-admin-roles                        1               1         1
   60 compute-admin-aggregates                    1               1         1
   61 objectstore-quotas                          1               1         1
   62 compute-admin-servers-pause                 1               1         1
   63 compute-admin-servers-suspend               1               1         1
   64 identity-admin-tenants                      0               1         0
   65 compute-admin-avail-zone                    0               1         1
   66 identity-admin-services                     1               1         1
   67 volume-extra-specs                          1               1         1
   68 compute-admin-flavors                       1               1         1
   69 compute-admin-server                        1               1         1
   70 compute-admin-services                      1               1         1
   71 compute-admin-fixed-ips                     1               0         1
   72 compute-admin-quota                         1               1         1
   73 compute-admin-hypervisor                    1               1         1
   74 compute-admin-hosts                         1               1         1
===== ================================= ===================== ========== ========

.. _scorecard: https://docs.google.com/a/dreamhost.com/spreadsheet/ccc?key=0Av62KoL8f9kAdFo4V1ZLUFM0OHlrRnFpQUkxSHJ5QWc&usp=drive_web#gid=6

.. _capabilities: https://github.com/stackforge/refstack/tree/master/defcore/havana
