#!/usr/bin/env python3
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import argparse
import os
import sys

import requests
import yaml

parser = argparse.ArgumentParser()
parser.add_argument(
    '-p', '--projects',
    default='./reference/projects.yaml',
    help='projects.yaml file path (%(default)s)',
)
parser.add_argument(
    '-g', '--gerrit',
    default=('http://git.openstack.org/cgit/openstack-infra/project-config/'
             'plain/gerrit/projects.yaml'),
    help=('URL for gerrit project list, ignored if --project-config is set or '
          'when running in Zuul'),
)
parser.add_argument(
    '-c', '--project-config',
    default=('/home/zuul/src/git.openstack.org/openstack-infra/project-config'),
    help='Local path of project-config',
)
args = parser.parse_args()

with open(args.projects, 'r', encoding='utf-8') as f:
    projects = yaml.safe_load(f.read())


if os.path.exists(args.project_config):
    projects_yaml = '%s/gerrit/projects.yaml' % args.project_config
    with open(projects_yaml) as gerrit_projects:
        gerrit_data = yaml.safe_load(gerrit_projects)
else:
    response = requests.get(args.gerrit)
    gerrit_data = yaml.safe_load(response.text)
gerrit_projects = set(
    entry.get('project')
    for entry in gerrit_data
)

errors = 0
for team_name, team_data in projects.items():
    deliverables = team_data.get('deliverables')
    for deliverable_name, deliverable_data in deliverables.items():
        for repo_name in deliverable_data.get('repos', []):
            if repo_name not in gerrit_projects:
                print('Unknown repository {} as part of {} in {}'.format(
                    repo_name, deliverable_name, team_name))
                errors += 1

sys.exit(1 if errors else 0)
