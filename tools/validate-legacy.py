#!/usr/bin/env python3

# Copyright 2020 VEXXHOST, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import sys

import requests
import yaml

FILES_URL = "https://opendev.org/api/v1/repos/{}/git/trees/master"
IGNORED_REPOS = [
    # NOTE(gmann): The below list represent the prefix of the old uncleaned
    # retired repositories. They are too many and not worth to cleanup now.
    # For more details, ref to https://etherpad.opendev.org/p/tc-retirement-cleanup
    'openstack/app-catalog',
    'openstack/congress-dashboard',
    'openstack/cue',
    'openstack/deb',
    'openstack/magnetodb',
    'openstack/openstack-chef-repo',
    'openstack/openstack-salt',
    'openstack/ossa',
    'openstack/python-appcatalogclient',
    'openstack/python-cueclient',
    'openstack/python-magnetodbclient',
    'openstack/refstack',
    'openstack/salt',
    'openstack/security-doc']

parser = argparse.ArgumentParser()
parser.add_argument(
    '-l', '--legacy-projects',
    default='./reference/legacy.yaml',
    help='legacy.yaml file path (%(default)s)'
)
args = parser.parse_args()

with open(args.legacy_projects, 'r', encoding='utf-8') as f:
    legacy_projects = yaml.safe_load(f.read())

errors = 0
for team_name, team_data in legacy_projects.items():
    # Check if the team has been retired or partially retired
    retired = True
    partially_retired = False
    if 'partial' in team_data:
        partially_retired = True
    if 'retired-on' not in team_data:
        retired = False
    # Check if team is not retired or partially retired but has entry in the
    # legacy project file.
    if not retired and not partially_retired:
        print('{} team has no retired-on date or missing partial retirement flag'.format(
            team_name
        ))
        errors += 1
        continue

    deliverables = team_data.get('deliverables')

    # Team has no deliverables, retired with no retired-on date
    if not deliverables:
        print('{} team has no deliverables with no retired-on date'.format(
            team_name
        ))
        errors += 1
        continue

    # In this case, team is not retired but has retired projects
    if partially_retired:
        for deliverable_name, deliverable_data in deliverables.items():
            # Retired-on date missing for a deliverable
            if 'retired-on' not in deliverable_data:
                print('{} is missing a retired-on date'.format(deliverable_name))
                errors += 1
                continue

    for deliverable_name, deliverable_data in deliverables.items():
        # Ensure that the repositories have no content.
        for repo in deliverable_data['repos']:
            repo_ignored = False
            for ir in IGNORED_REPOS:
                if repo.startswith(ir):
                    msg = '{} is an old repository and not worth do the cleanup, ignoring.'.format(repo)
                    print(msg)
                    repo_ignored = True
                    break
            if repo_ignored:
                continue
            if repo.startswith('opendev/'):
                msg = '{} not in openstack namespace, ignoring.'.format(repo)
                print(msg)
                continue

            url = FILES_URL.format(repo)
            files = requests.get(url).json()
            file_names = sorted([f['path'] for f in files['tree']])

            if file_names != ['.gitreview', 'README.rst']:
                msg = '{} is not properly retired, files: {}.'.format(
                    repo, file_names)
                print(msg)
                errors += 1
                continue


sys.exit(1 if errors else 0)
