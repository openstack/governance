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

from openstack_governance import _yamlutils
from openstack_governance import governance


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

_tc_data_yaml = """
---
# List of repositories owned by the technical committee
Technical Committee:
  - repo: openstack/governance
  - repo: openstack/project-team-guide
"""

_sigs_data_yaml = """
---
# List of repositories owned by SIGs
meta:
  - repo: openstack/governance-sigs
api:
  - repo: openstack/api-sig
"""

_wgs_data_yaml = """
---
# List of repositories owned by Foundation board and subcommittes
Interop Working Group:
  - repo: openstack/interop
  - repo: openstack/refstack-client
  - repo: openstack/refstack
  - repo: openstack/python-tempestconf
"""

TEAM_DATA = _yamlutils.loads(_team_data_yaml)
TC_DATA = _yamlutils.loads(_tc_data_yaml)
SIGS_DATA = _yamlutils.loads(_sigs_data_yaml)
WGS_DATA = _yamlutils.loads(_wgs_data_yaml)


class TestGetRepoOwner(base.BaseTestCase):

    def setUp(self):
        super().setUp()
        self.gov = governance.Governance(TEAM_DATA, TC_DATA, SIGS_DATA, WGS_DATA)

    def test_repo_exists(self):
        owner = self.gov.get_repo_owner(
            'openstack/releases',
        )
        self.assertEqual('Release Management', owner)

    def test_repo_exists_tc(self):
        owner = self.gov.get_repo_owner(
            'openstack/governance',
        )
        self.assertEqual('Technical Committee', owner)

    def test_no_such_repo(self):
        self.assertRaises(
            ValueError,
            self.gov.get_repo_owner,
            'openstack/no-such-repo',
        )


class TestLocalRepo(base.BaseTestCase):

    def test_create(self):
        gov = governance.Governance.from_local_repo()
        repos = gov.get_repositories(
            team_name='Technical Committee',
        )
        repo_names = set(r.name for r in repos)
        self.assertIn('openstack/governance', repo_names)


class TestGetRepositories(base.BaseTestCase):

    def setUp(self):
        super().setUp()
        self.gov = governance.Governance(TEAM_DATA, TC_DATA, SIGS_DATA, WGS_DATA)

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

    def test_by_team_tc(self):
        repos = self.gov.get_repositories(
            team_name='Technical Committee',
        )
        self.assertEqual(
            sorted(['openstack/governance',
                    'openstack/project-team-guide']),
            sorted(r.name for r in repos),
        )

    def test_by_team_sig(self):
        repos = self.gov.get_repositories(
            team_name='meta SIG',
        )
        self.assertEqual(
            sorted(['openstack/governance-sigs']),
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


class TestGetTeam(base.BaseTestCase):

    def setUp(self):
        super().setUp()
        self.gov = governance.Governance(TEAM_DATA, TC_DATA, SIGS_DATA, WGS_DATA)

    def test_found(self):
        team = self.gov.get_team('meta SIG')
        self.assertEqual('meta SIG', team.name)

    def test_not_found(self):
        self.assertRaises(
            ValueError,
            self.gov.get_team,
            'No Such Team',
        )


class TestTeamProperties(base.BaseTestCase):

    def setUp(self):
        super().setUp()
        self.team_with = governance.Team(
            'test',
            {'service': 'service name',
             'mission': 'mission statement'},
        )
        self.team_without = governance.Team(
            'test',
            {},
        )

    def test_service(self):
        self.assertEqual('service name', self.team_with.service)
        self.assertIsNone(self.team_without.service)

    def test_mission(self):
        self.assertEqual('mission statement', self.team_with.mission)
        self.assertIsNone(self.team_without.mission)
