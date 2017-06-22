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

import yaml


parser = argparse.ArgumentParser()
parser.add_argument(
    '-p', '--projects',
    default='./reference/projects.yaml',
    help='projects.yaml file path (%(default)s)',
)
format_grp = parser.add_mutually_exclusive_group()
format_grp.add_argument(
    '-f', '--full',
    action='store_const',
    const='full',
    dest='mode',
    default='full',
    help='show all details (default)',
)
format_grp.add_argument(
    '-e', '--email',
    action='store_const',
    const='email',
    dest='mode',
    help='show only email addresses',
)
format_grp.add_argument(
    '-i', '--irc',
    action='store_const',
    const='irc',
    dest='mode',
    help='show only IRC nics',
)
format_grp.add_argument(
    '-c', '--csv',
    action='store_const',
    const='csv',
    dest='mode',
    help='all data, comma separated',
)
args = parser.parse_args()


with open(args.projects, 'r', encoding='utf-8') as f:
    projects = yaml.safe_load(f.read())

fmt_str = {
    'full': '{name}\t{irc}\t{email}\t{project_name}',
    'irc': '{irc}',
    'email': '{email}',
    'csv': '"{name}","{irc}","{email}","{project_name}"',
}[args.mode]

for project_name, project_data in projects.items():
    ptl = project_data['ptl']
    print(fmt_str.format(project_name=project_name, **ptl))
