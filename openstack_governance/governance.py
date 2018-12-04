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

"""Work with the governance repository.
"""

import logging
import os.path
import weakref

from openstack_governance import _yamlutils

import requests

LOG = logging.getLogger(__name__)
REPO_URL_BASE = "http://git.openstack.org/cgit/openstack/governance/plain"


def get_tags_for_deliverable(team_data, team, name):
    "Return the tags for the deliverable owned by the team."
    if team not in team_data:
        return set()
    team_info = team_data[team]
    dinfo = team_info['deliverables'].get(name)
    if not dinfo:
        return set()
    return set(dinfo.get('tags', [])).union(set(team_info.get('tags', [])))


class Team(object):

    def __init__(self, name, data):
        self.name = name
        self.data = data
        # Protectively initialize the ptl data structure in case part
        # of it is missing from the project list, then replace any
        # values we do have from that data.
        self.ptl = {
            'name': 'MISSING',
            'irc': 'MISSING',
        }
        self.ptl.update(data.get('ptl', {}))
        self.deliverables = {
            dn: Deliverable(dn, di, self)
            for dn, di in self.data.get('deliverables', {}).items()
        }

    @property
    def tags(self):
        return set(self.data.get('tags', []))

    @property
    def service(self):
        return self.data.get('service')

    @property
    def mission(self):
        return self.data.get('mission')


class Deliverable(object):
    def __init__(self, name, data, team):
        self.name = name
        self.data = data
        self.team = weakref.proxy(team)
        self.repositories = {
            rn: Repository(rn, self)
            for rn in self.data.get('repos', [])
        }

    @property
    def tags(self):
        return set(self.data.get('tags', [])).union(self.team.tags)


class Repository(object):
    def __init__(self, name, deliverable):
        self.name = name
        self.deliverable = weakref.proxy(deliverable)

    @property
    def tags(self):
        return self.deliverable.tags


class Governance(object):

    _projects_filename = 'reference/projects.yaml'
    _tc_repos_filename = 'reference/technical-committee-repos.yaml'
    _sigs_repos_filename = 'reference/sigs-repos.yaml'
    _wgs_repos_filename = 'reference/foundation-board-repos.yaml'

    def __init__(self, team_data, tc_data, sigs_data, wgs_data):
        self._team_data = team_data
        self._tc_data = tc_data
        self._sigs_data = sigs_data
        self._wgs_data = wgs_data

        team_data['Technical Committee'] = {
            'deliverables': {
                repo['repo'].partition('/')[-1]: {'repos': [repo['repo']]}
                for repo in tc_data['Technical Committee']
            }
        }
        for sig_name, sig_info in sigs_data.items():
            team_data['{} SIG'.format(sig_name)] = {
                'deliverables': {
                    repo['repo'].partition('/')[-1]: {'repos': [repo['repo']]}
                    for repo in sig_info
                }
            }
        for wg_name, wg_info in wgs_data.items():
            team_data[wg_name] = {
                'deliverables': {
                    repo['repo'].partition('/')[-1]: {'repos': [repo['repo']]}
                    for repo in wg_info
                }
            }

        self._teams = [Team(n, i) for n, i in self._team_data.items()]

    @classmethod
    def from_local_repo(cls, repo_dir='.'):
        team_filename = os.path.join(repo_dir, cls._projects_filename)
        team_data = _yamlutils.load_from_file(team_filename)

        tc_filename = os.path.join(repo_dir, cls._tc_repos_filename)
        tc_data = _yamlutils.load_from_file(tc_filename)

        sigs_filename = os.path.join(repo_dir, cls._sigs_repos_filename)
        sigs_data = _yamlutils.load_from_file(sigs_filename)

        wgs_filename = os.path.join(repo_dir, cls._wgs_repos_filename)
        wgs_data = _yamlutils.load_from_file(wgs_filename)

        return cls(team_data, tc_data, sigs_data, wgs_data)

    @classmethod
    def from_remote_repo(cls, repo_url_base=REPO_URL_BASE):
        team_url = REPO_URL_BASE + '/reference/projects.yaml'
        LOG.debug('fetching team data from %s', team_url)
        r = requests.get(team_url)
        team_data = _yamlutils.loads(r.text)

        tc_url = REPO_URL_BASE + '/reference/technical-committee-repos.yaml'
        LOG.debug('fetching TC data from %s', tc_url)
        r = requests.get(tc_url)
        tc_data = _yamlutils.loads(r.text)

        sigs_url = REPO_URL_BASE + '/reference/sigs-repos.yaml'
        LOG.debug('fetching SIGs data from %s', sigs_url)
        r = requests.get(sigs_url)
        sigs_data = _yamlutils.loads(r.text)

        wgs_url = REPO_URL_BASE + '/reference/foundation-board-repos.yaml'
        LOG.debug('fetching WGs data from %s', wgs_url)
        r = requests.get(wgs_url)
        wgs_data = _yamlutils.loads(r.text)

        return cls(team_data, tc_data, sigs_data, wgs_data)

    def get_team(self, name):
        for team in self._teams:
            if team.name == name:
                return team
        raise ValueError('No team {!r} found'.format(name))

    def get_repo_owner(self, repo_name):
        """Return the name of the team that owns the repository.

        :param repo_name: Long name of the repository, such as 'openstack/nova'.

        """
        for team, info in self._team_data.items():
            for dname, dinfo in info.get('deliverables', {}).items():
                if repo_name in dinfo.get('repos', []):
                    return team
        raise ValueError('Repository %s not found in governance list' % repo_name)

    def get_repositories(self, team_name=None, deliverable_name=None,
                         tags=[]):
        """Return a sequence of repositories, possibly filtered.

        :param team_name: The name of the team owning the repositories. Can be
            None. For Example: team_name='adjutant' or team_name='security SIG'
            or team_name='Technical Committee'
        :para deliverable_name: The name of the deliverable to which all
           repos should belong.
        :param tags: The names of any tags the repositories should
            have. Can be empty.

        """
        if tags:
            tags = set(tags)

        if team_name:
            teams = [self.get_team(team_name)]
        else:
            teams = self._teams

        for team in teams:
            if deliverable_name and deliverable_name not in team.deliverables:
                continue
            if deliverable_name:
                deliverables = [team.deliverables[deliverable_name]]
            else:
                deliverables = team.deliverables.values()
            for deliverable in deliverables:
                for repository in deliverable.repositories.values():
                    if tags and not tags.issubset(repository.tags):
                        continue
                    yield repository
