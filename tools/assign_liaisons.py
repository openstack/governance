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
import collections
import random

from openstack_governance import members
from openstack_governance import projects


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--member-file',
        default='reference/members.yaml',
        help='location of members file, (%(default)s)',
    )
    parser.add_argument(
        '--projects-file',
        default='reference/projects.yaml',
        help='location of projects.yaml, (%(default)s)',
    )
    parser.add_argument(
        '--replace-all',
        action='store_true',
        help='Replace all assigned liaisons (%(default)s)',
    )
    parser.add_argument(
        '--remove-all',
        action='store_true',
        help='Remove all assigned liaisons (%(default)s)',
    )
    args = parser.parse_args()

    member_nics = [
        m['irc']
        for m in members.parse_members_file(args.member_file)
    ]

    project_data = projects.load_project_file(args.projects_file)

    num_teams = len(project_data)
    assignments_per = num_teams // (len(member_nics) // 2)

    member_counts = collections.Counter({
        nic: 0
        for nic in member_nics
    })

    if not args.replace_all:
        for _, team in project_data.items():
            proj_liaisons = team.get('liaisons', {})
            for member in proj_liaisons.get('tc_members', []):
                member_counts.update({member: 1})

    choices = []
    for member, count in sorted(member_counts.items()):
        choices.extend([member] * (assignments_per - count))
    # Make sure we have a list in order that isn't assigning the same
    # person to a team twice.

    for name, team in project_data.items():
        proj_liaisons = team.get('liaisons', {})
        liaisons = proj_liaisons.get('tc_members', [])
        if args.remove_all:
            team['liaisons']['tc_members'] = []
            continue
        if args.replace_all:
            liaisons = []
        while len(liaisons) < 2:
            random.shuffle(choices)
            next_choice = choices.pop()
            while next_choice in liaisons:
                choices.insert(0, next_choice)
                next_choice = choices.pop()
            liaisons.append(next_choice)
        team['liaisons']['tc_members'] = liaisons

    projects.write_project_file(project_data, args.projects_file)


if __name__ == '__main__':
    main()
