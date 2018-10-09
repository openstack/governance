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
import textwrap

from openstack_governance import _wiki
from openstack_governance import members
from openstack_governance import projects


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--member-file',
        default='reference/members',
        help='location of members file, (%(default)s)',
    )
    parser.add_argument(
        '--projects-file',
        default='reference/projects.yaml',
        help='location of projects.yaml, (%(default)s)',
    )
    args = parser.parse_args()

    member_nics = [
        m['irc']
        for m in members.parse_members_file(args.member_file)
    ]

    project_data = projects.load_project_file(args.projects_file)
    project_names = list(project_data.keys())

    num_teams = len(project_names)
    assignments_per = num_teams // (len(member_nics) // 2)

    print('TEAMS', num_teams)
    print('TC   ', len(member_nics))
    print('PER  ', assignments_per)

    # Determine how many assignments everyone has by reading the wiki
    # page.

    project_to_liaisons = _wiki.get_liaison_data()

    member_counts = collections.Counter({
        nic: 0
        for nic in member_nics
    })
    for team, liaisons in project_to_liaisons.items():
        for member in liaisons:
            member_counts.update({member: 1})

    print('\nAlready assigned:')
    for member, count in sorted(member_counts.items()):
        print('{:12}: {}'.format(member, count))

    choices = []
    for member, count in sorted(member_counts.items()):
        choices.extend([member] * (assignments_per - count))

    # Make sure we have a list in order that isn't assigning the same
    # person to a team twice.
    print()
    for team, liaisons in project_to_liaisons.items():
        while len(liaisons) < 2:
            random.shuffle(choices)
            next_choice = choices.pop()
            while next_choice in liaisons:
                choices.insert(0, next_choice)
                next_choice = choices.pop()
            print('assigning {} to {}'.format(next_choice, team))
            liaisons.append(next_choice)

    print(textwrap.dedent('''
    === Project Teams ===

    {| class="wikitable"
    |-
    ! Group !! TC members'''))

    for team, liaisons in project_to_liaisons.items():
        print('|-\n| {} || {}'.format(team, ', '.join(liaisons)))

    print('|}\n')

if __name__ == '__main__':
    main()
