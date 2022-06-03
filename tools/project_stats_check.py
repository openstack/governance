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
import sys
from urllib import request
import yaml


TOP_X_OWNER = 10
# Zuul builds fetch size per query
BUILDSET_FETCH_SIZE = 500


class BaseQuery:
    def __init__(self, base_url, query_separator='&', verbose=False):
        self.verbose = verbose
        self.query_separator = query_separator
        if base_url.endswith('/'):
            self.base_url = base_url
        else:
            self.base_url = base_url + '/'

    def query(self, api, conditions=None):
        url = self.base_url + api
        if conditions:
            url += '?' + (self.query_separator.join(conditions))
        if self.verbose:
            print("Request on url %s" % url)
        result = request.urlopen(url)
        result = yaml.safe_load(result.read())
        if self.verbose:
            print(result)
        return result


class Zuul(BaseQuery):
    def get_project_buildsets(self, repos, fetch_size, branch='master', tenant='openstack'):
        # project={repos}&pipeline=gate&limit=500&branch=master

        conditions = ['pipeline=gate',
                      'limit='+str(fetch_size),
                      'branch=' + branch]
        for repo in repos:
            # count all repos in one set
            conditions.append('project=' + repo)
        return self.query(api='api/tenant/%s/buildsets' % tenant, conditions=conditions)

    def fetch_repo_buildset_success_rate(self, buildsets):
        success = {}
        not_success = {}
        for buildset in buildsets:
            if type(buildset) != dict:
                if self.verbose:
                    print("Buildset %s is not a dict. Skipping." % buildset)
                continue
            project = buildset['project']
            result = buildset['result']
            if result == 'SUCCESS':
                if project in success:
                    success[project] += 1
                else:
                    success[project] = 1
            else:
                if project in not_success:
                    not_success[project] += 1
                else:
                    not_success[project] = 1
        success_rates = {}
        all_projects = set(success).union(set(not_success))
        for project in all_projects:
            success_rates[project] = format(
                success.get(project, 0)/(
                    success.get(project, 0) + not_success.get(project, 0)
                )*100, '.0f') + '%'
        return success_rates


class Gerrit(BaseQuery):
    def query(self, api, conditions=None):
        url = self.base_url + api
        if conditions:
            # Set no-limit=1 to fetch larger amount of patches
            url += '?no-limit=1&q=' + (self.query_separator.join(conditions))
        if self.verbose:
            print("Request on url %s" % url)
        result = request.urlopen(url)
        if self.verbose:
            print(result)

        # The first line contains random chars like `'b\')]}\\\'`
        # Consider it as a bug and directly access second line from result
        result = yaml.safe_load(result.readlines()[1])
        if self.verbose:
            print(result)
        return result

    def get_project_query_list(self, repos):
        projects = []
        repoSize = len(repos)
        for i in range(repoSize):
            repo = repos[i]
            if i == 0:
                projects += ['(project:' + repo, 'OR']
            elif i == repoSize - 1:
                projects.append('project:' + repo + ')')
            else:
                projects += ['project:' + repo, 'OR']
        return projects

    def get_total_valid(self, repos, within, branch='master'):
        # q=(status:open+OR+status:merged)+project:{repo}+
        # NOT+label:Workflow<=-1+label:Verified>=1+NOT+age:{within}day

        conditions = ['(status:open', 'OR', 'status:merged)',
                      'NOT', 'label:Workflow<=-1',
                      'label:Verified>=1',
                      'branch:' + branch,
                      'NOT', 'age:' + str(within) + 'day']
        conditions += self.get_project_query_list(repos)
        return self.query(api='changes/', conditions=conditions)

    def get_total_not_review(self, repos, within, branch='master'):
        # q=status:open+project:{repos}+label:Code-Review=0+
        # NOT+label:Workflow<=-1+label:Verified>=1+NOT+age:{within}day

        conditions = ['status:open',
                      'NOT', 'label:Workflow<=-1',
                      'label:Verified>=1',
                      'label:Code-Review=0',
                      'branch:' + branch,
                      'NOT', 'age:' + str(within) + 'day']
        conditions += self.get_project_query_list(repos)
        return self.query(api='changes/', conditions=conditions)

    def get_total_merged(self, repos, within, branch='master'):
        # q=status:merged+project:{repos}+NOT+age:{within}day

        conditions = ['status:merged',
                      'branch:' + branch,
                      'NOT', 'age:' + str(within) + 'day']
        conditions += self.get_project_query_list(repos)
        return self.query(api='changes/', conditions=conditions)

    def count_owners(self, patches, limit=-1):
        owners = {}
        patchCount = len(patches)
        for p in patches:
            owner = p.get('owner', {}).get('_account_id', 0)
            if owner in owners:
                owners[owner] += 1
            else:
                owners[owner] = 1
        sorted_owners = sorted(
            owners.items(), reverse=True, key=lambda item: item[1])
        results = {}
        for owner, count in sorted_owners:
            owner = self.get_account_name(owner)
            if limit != -1 and len(results) >= limit:
                break
            results[owner] = format(
                (count / patchCount) * 100, '.2f') + '%'
        return results

    def get_account_name(self, account_id):
        # Profile will looks like: {"_account_id":22816,
        # "name":"OpenStack Release Bot",
        # "email":"infra-root@openstack.org","username":"release"}
        profile = self.query(api=('accounts/%s' % account_id))
        return profile.get('name', account_id)


def validate_gerrit_data(repos, count_days, branch, verbose):
    gerrit = Gerrit(
        base_url='https://review.opendev.org/', query_separator='+',
        verbose=verbose)
    print(" Validating Gerrit...")
    total_valid_patches = gerrit.get_total_valid(
        repos, within=count_days, branch=branch)

    if not total_valid_patches:
        print(" * There are no any patches proposed within "
              "%s days" % count_days)
        return

    not_reviewed_patches = gerrit.get_total_not_review(
        repos, within=count_days, branch=branch)
    merged_patches = gerrit.get_total_merged(
        repos, within=count_days, branch=branch)
    unreview_rate = (
        len(not_reviewed_patches)/len(total_valid_patches))*100//1
    merged_rate = (
        len(merged_patches)/len(total_valid_patches))*100//1
    owners_rates = gerrit.count_owners(
        patches=total_valid_patches, limit=10)

    print(" *", "There are",
          "%s ready for" % len(total_valid_patches),
          "review patches generated within %s days" % count_days)
    print(" *", "There are",
          "%s not reviewed" % len(not_reviewed_patches),
          "patches generated within %s days" % count_days)
    print(" *", "There are %s merged" % len(merged_patches),
          "patches generated within %s days" % count_days)
    print(" *", "Unreviewed patch rate for",
          "patches generated within",
          "%s days is %s" % (count_days, unreview_rate), '%')
    print(" *", "Merged patch rate for patches generated within",
          "%s days is %s" % (count_days, merged_rate), '%')
    print(" * ", "Here's top %s owner for patches" % TOP_X_OWNER,
          "generated within",
          "%s days (Name/Account_ID: Percentage):" % count_days)
    for owner, rate in owners_rates.items():
        print('    - ', owner, ': ', rate)


def validate_zuul_data(repos, branch, verbose):
    zuul = Zuul(base_url="https://zuul.opendev.org/", verbose=verbose)
    print(" Validate Zuul...")
    print(" Set buildsets fetch size to",
          "%s" % BUILDSET_FETCH_SIZE)
    gate_builds = zuul.get_project_buildsets(
        repos, fetch_size=BUILDSET_FETCH_SIZE, branch=branch)
    repo_success_rates = zuul.fetch_repo_buildset_success_rate(
        gate_builds)
    for repo, rate in repo_success_rates.items():
        print(" * Repo: %s gate job builds success" % repo,
              "rate: %s" % rate)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--file',
        default='./reference/projects.yaml',
        help='projects.yaml file path (%(default)s)',
    )
    parser.add_argument(
        '-p', '--projects',
        help='projects to analyze. Separate with comma',
    )
    parser.add_argument(
        '-d', '--days',
        default='180',
        help='Days to count gerrit patches generated since (%(default)s)',
    )
    parser.add_argument(
        '-b', '--branch',
        default='master',
        help='Branch to analyze on projects (%(default)s)',
    )
    parser.add_argument(
        '-z', '--skip-zuul',
        action='store_true',
        help='Skip Zuul analysis (%(default)s)',
    )
    parser.add_argument(
        '-g', '--skip-gerrit',
        action='store_true',
        help='Skip Gerrit analysis (%(default)s)',
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Show debug information',
    )
    args = parser.parse_args()
    with open(args.file, 'r', encoding='utf-8') as f:
        projects = yaml.safe_load(f.read())

    project_scope = args.projects.split(',') if (
        args.projects is not None) else list(projects.keys())
    count_days = args.days

    def get_repos(project):
        '''Get repositories in project'''
        repos = []
        defn = projects.get(project, {})
        deliverables = defn.get('deliverables', {})
        for key, deliverable in deliverables.items():
            repos += deliverable.get('repos', '')
        return repos

    all_branch = args.branch.split(',')
    for branch in all_branch:
        if not (branch.startswith('master') or branch.startswith('stable/')):
            print('Invalid branch %s' % branch)
            sys.exit(1)
    for project in project_scope:
        print('*' * 50)
        if project not in projects:
            print('Invalid project %s' % project)
            continue
        print("Start Project %s analysis..." % project)
        repos = get_repos(project)
        print(" Includes repositories: %s" % repos)
        for branch in all_branch:
            print(" Start analysis branch %s..." % branch)
            if not args.skip_gerrit:
                validate_gerrit_data(repos, count_days, branch, args.verbose)

            if not args.skip_zuul:
                validate_zuul_data(repos, branch, args.verbose)

        print('*'*50)


if __name__ == '__main__':
    main()
