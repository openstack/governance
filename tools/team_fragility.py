#!/usr/bin/env python

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


s = requests.session()


def fragility(team, series):
    org_metric = [{'team': team,
                   'type': 'no activity',
                   'value': 0,
                   'name': ''}]
    eng_metric = [{'team': team,
                   'type': 'no activity',
                   'value': 0,
                   'name': ''}]
    group = "%s-group" % team.lower()

    org_commits = s.get('http://stackalytics.com/api/'
                        '1.0/stats/companies?metric=commits&release=%s'
                        '&project_type=all&module=%s'
                        % (series, group)).json()
    total_commits = sum([company['metric']
                        for company in org_commits['stats']])

    if total_commits:
        # Entity with most commits
        if org_commits['stats'][0]['name'] == '*independent':
            # Skip "independent" if that is the largest org
            org_commits['stats'].pop(0)
        value = float(org_commits['stats'][0]['metric'] / total_commits * 100)
        org_metric.append({'team': team,
                           'type': 'org commit %',
                           'value': value,
                           'name': org_commits['stats'][0]['name']})

        # Core reviews
        reviews = s.get('http://stackalytics.com/api/'
                        '1.0/stats/engineers?metric=marks&release=%s'
                        '&project_type=all'
                        '&module=%s' % (series, group)).json()
        companies = {}
        engineers = []
        total_core_reviews = 0
        for eng in reviews['stats']:
            if eng['core'] != 'master':
                # Skip reviews for non-core reviewers
                continue
            engineers.append({'name': eng['name'], 'reviews': eng['metric']})
            total_core_reviews += eng['metric']

            # Identify company for that core reviewer
            for stat in s.get('http://stackalytics.com/api/1.0/stats/'
                              'companies?metric=marks&module=%s&user_id=%s&'
                              'project_type=all&release=%s' %
                              (group, eng['id'], series)).json()['stats']:
                company = stat['id']
                if company == '*independent':
                    continue

                if company not in companies:
                    companies[company] = 0

                companies[company] += stat['metric']

        if companies:
            # Organization with most core reviews
            most_core_reviews = max(companies, key=companies.get)
            v = float(companies[most_core_reviews] / total_core_reviews * 100)
            org_metric.append({'team': team,
                               'type': 'org core review %',
                               'value': v,
                               'name': most_core_reviews})

        if engineers:
            # Individual with most core reviews
            eng_most_core = max(engineers, key=lambda key: key['reviews'])
            v = float(eng_most_core['reviews'] / total_core_reviews * 100)
            eng_metric.append({'team': team,
                               'type': 'individual core review %',
                               'value': v,
                               'name': eng_most_core['name']})

        # Individual with most commits
        eng_commits = s.get('http://stackalytics.com/api/'
                            '1.0/stats/engineers?metric=commits&release=%s'
                            '&project_type=all&module=%s'
                            % (series, group)).json()

        value = float(eng_commits['stats'][0]['metric'] / total_commits * 100)
        eng_metric.append({'team': team,
                           'type': 'individual commit %',
                           'value': value,
                           'name': eng_commits['stats'][0]['name']})

    return (max(org_metric, key=lambda key: key['value']),
            max(eng_metric, key=lambda key: key['value']))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('series',
                        help='development cycle to consider')
    args = parser.parse_args()

    corpobus = []
    engbus = []

    filename = os.path.abspath('reference/projects.yaml')
    with open(filename, 'r') as f:
        projects = [k for k in yaml.safe_load(f.read())]
        projects.sort()

    for project in projects:
        if project not in ['OpenStackSDK', 'loci']:
            (org_fragility, eng_fragility) = fragility(project, args.series)
            corpobus.append(org_fragility)
            engbus.append(eng_fragility)

    print('============= Organizational diversity fragility =============')
    for busfactor in sorted(corpobus, key=lambda key: key['value'],
                            reverse=True):
        print('%-18s %.1f%% (%s, %s)' % (
              busfactor['team'], busfactor['value'],
              busfactor['name'], busfactor['type']))

    print('============= Individual fragility =============')
    for busfactor in sorted(engbus, key=lambda key: key['value'],
                            reverse=True):
        print('%-18s %.1f%% (%s, %s)' % (
              busfactor['team'], busfactor['value'],
              busfactor['name'], busfactor['type']))


if __name__ == '__main__':
    sys.exit(main())
