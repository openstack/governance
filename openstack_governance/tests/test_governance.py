# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslotest import base

from openstack_governance import governance
from openstack_governance import yamlutils


_team_data_yaml = """
Release Management:
  ptl:
    name: Doug Hellmann
    irc: dhellmann
    email: doug@doughellmann.com
  irc-channel: openstack-release
  mission: >
    Coordinating the release of OpenStack deliverables, by defining the
    overall development cycle, release models, publication processes,
    versioning rules and tools, then enabling project teams to produce
    their own releases.
  url: https://wiki.openstack.org/wiki/Release_Management
  tags:
    - team:diverse-affiliation
  deliverables:
    release-schedule-generator:
      repos:
        - openstack/release-schedule-generator
    release-test:
      repos:
        - openstack/release-test
    release-tools:
      repos:
        - openstack-infra/release-tools
    releases:
      repos:
        - openstack/releases
    reno:
      repos:
        - openstack/reno
      docs:
        contributor: https://docs.openstack.org/developer/reno/
    specs-cookiecutter:
      repos:
        - openstack-dev/specs-cookiecutter
"""

TEAM_DATA = yamlutils.loads(_team_data_yaml)


class TestGetRepoOwner(base.BaseTestCase):

    def setUp(self):
        super().setUp()
        self.gov = governance.Governance(TEAM_DATA)

    def test_repo_exists(self):
        owner = self.gov.get_repo_owner(
            'openstack/releases',
        )
        self.assertEqual('Release Management', owner)

    def test_no_such_repo(self):
        self.assertRaises(
            ValueError,
            self.gov.get_repo_owner,
            'openstack/no-such-repo',
        )


class TestGetRepositories(base.BaseTestCase):

    def setUp(self):
        super().setUp()
        self.gov = governance.Governance(TEAM_DATA)

    def test_by_team(self):
        repos = self.gov.get_repositories(
            team_name='Release Management',
        )
        self.assertEqual(
            sorted(['openstack/release-schedule-generator',
                    'openstack/release-test',
                    'openstack-infra/release-tools',
                    'openstack/releases',
                    'openstack/reno',
                    'openstack-dev/specs-cookiecutter']),
            sorted(r.name for r in repos),
        )

    def test_by_deliverable(self):
        repos = self.gov.get_repositories(
            deliverable_name='release-tools',
        )
        self.assertEqual(
            ['openstack-infra/release-tools'],
            [r.name for r in repos],
        )

    def test_tag_negative(self):
        repos = self.gov.get_repositories(
            tags=['team:single-vendor'],
        )
        self.assertEqual([], list(repos))

    def test_tags_positive(self):
        repos = self.gov.get_repositories(
            tags=['team:diverse-affiliation'],
        )
        self.assertEqual(
            sorted(['openstack/release-schedule-generator',
                    'openstack/release-test',
                    'openstack-infra/release-tools',
                    'openstack/releases',
                    'openstack/reno',
                    'openstack-dev/specs-cookiecutter']),
            sorted(r.name for r in repos),
        )
