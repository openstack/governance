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

import os
import sys

import requests
import yaml

import base

s = requests.session()


def get_core_reviews_by_company(group):
    # reviews by individual
    reviews = s.get('http://stackalytics.com/api/'
                           '1.0/stats/engineers?metric=marks'
                           '&project_type=all&module=%s' % group).json()
    companies = {}
    for eng in reviews['stats']:
        if eng['core'] != 'master':
            continue
        company = s.get('http://stackalytics.com/api/1.0/'
                               'stats/companies?metric=marks&'
                               'module=%s&user_id=%s&project_type=all'
                               % (group, eng['id'])).json()['stats'][0]['id']
        companies.setdefault(company, {'reviewers': 0, 'reviews': 0})
        companies[company]['reviews'] += eng['metric']
        companies[company]['reviewers'] += 1
    return companies


def get_diversity(project):
    # commits by company
    group = "%s-group" % project.lower()
    commits = s.get('http://stackalytics.com/api/'
                           '1.0/stats/companies?metric=commits'
                           '&project_type=all&module=%s' % group).json()
    # reviews by company
    reviews = s.get('http://stackalytics.com/api/'
                           '1.0/stats/companies?metric=marks'
                           '&project_type=all&module=%s' % group).json()
    core_reviews_by_company = get_core_reviews_by_company(group)
    commits_total = sum([company['metric'] for company in commits['stats']])
    commits_top = float(commits['stats'][0]['metric']) / commits_total * 100
    commits_top2 = ((float(commits['stats'][0]['metric']) +
                    float(commits['stats'][1]['metric']))
                    / commits_total * 100)
    reviews_total = sum([company['metric'] for company in reviews['stats']])
    reviews_top = float(reviews['stats'][0]['metric']) / reviews_total * 100
    reviews_top2 = ((float(reviews['stats'][0]['metric']) +
                    float(reviews['stats'][1]['metric']))
                    / reviews_total * 100)
    core_review_values = [company['reviews'] for company in
                          core_reviews_by_company.itervalues()]
    core_review_values.sort(reverse=True)
    core_reviews_total = sum(core_review_values)
    core_reviews_top = (float(core_review_values[0]) /
                        core_reviews_total * 100)
    core_reviews_top2 = ((float(core_review_values[0]) +
                         float(core_review_values[1])) /
                         core_reviews_total * 100)
    core_reviewers_values = [company['reviewers'] for company in
                             core_reviews_by_company.itervalues()]
    core_reviewers_values.sort(reverse=True)
    core_reviewers_total = sum(core_reviewers_values)
    core_reviewers_top = (float(core_reviewers_values[0]) /
                          core_reviewers_total * 100)
    core_reviewers_top2 = ((float(core_reviewers_values[0]) +
                           float(core_reviewers_values[1])) /
                           core_reviewers_total * 100)
    print '%-18s (%.2f%% | %.2f%% | %.2f%% | %.2f%%)' % (
        project, commits_top, reviews_top, core_reviews_top,
        core_reviewers_top)
    print '%-18s (%.2f%% | %.2f%% | %.2f%% | %.2f%%)' % (
        '', commits_top2, reviews_top2, core_reviews_top2,
        core_reviewers_top2)
    is_diverse = (commits_top <= 50 and reviews_top <= 50 and
                  core_reviews_top <= 50 and core_reviewers_top <= 50 and
                  commits_top2 <= 80 and reviews_top2 <= 80 and
                  core_reviews_top2 <= 80 and core_reviewers_top2 <= 80)
    return is_diverse


class ValidateDiversity(base.ValidatorBase):

    @staticmethod
    def validate(team):
        """Return True of team should contain the tag 'team:diverse-affiliation'"""
        return get_diversity(team)

    @staticmethod
    def get_tag_name():
        return "team:diverse-affiliation"


def main():
    print '<Team> (top commit % | top review % | top core review % | ' \
        'top core reviewer %)'
    print '       (top 2 commit % | top 2 review % | top 2 core review % | ' \
        'top 2 core reviewer %)'
    filename = os.path.abspath('reference/projects.yaml')
    with open(filename, 'r') as f:
        projects = yaml.load(f.read())
    for project in projects:
        get_diversity(project)


if __name__ == '__main__':
    sys.exit(main())
