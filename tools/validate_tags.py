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

""" validate tag applications in projects.yaml

Validate the application of tags that can be pragmatically applied.

Note: Does not automatically update projects.yaml since doing so can reformat
and reorder projects.yaml

"""

import stable
import teamstats

import requests
import yaml

import os
import sys
import urllib

# List of modules to validate team based tags
team_validators = [
    teamstats.ValidateDiversity,
]

# List of modules to validate repository based tags
repo_validators = [
    stable.ValidateStableBranches,
]


def main():
    filename = os.path.abspath('reference/projects.yaml')
    with open(filename, 'r') as f:
        teams = yaml.load(f.read())
    for team in teams:
        # Check team based tags
        for validator in team_validators:
            validate(team, teams[team], validator)
        # Check deliverable based tags
        for name, deliverable in teams[team]['deliverables'].items():
            for repo in deliverable['repos']:
                if not repo_exists(repo):
                    continue
                for validator in repo_validators:
                    validate(repo, deliverable, validator)


def validate(name, data, validator):
    tag_name = validator.get_tag_name()
    contains_tag = any([tag_name == tag for tag in
                        data.get('tags', [])])
    if validator.validate(name):
        # should contain tag
        if not contains_tag:
            print_tag_missing(name, tag_name)
    else:
        # should not contain tag
        if contains_tag:
            print_bad_tag(name, tag_name)


def repo_exists(repo):
    """Sometimes the governance docs can get out of sync with repo names."""
    response = requests.get(
        'https://review.openstack.org:443/projects/%s/' %
        urllib.quote_plus(repo))
    # strip off first few chars because 'the JSON response body starts with
    # a magic prefix line that must be stripped before feeding the rest of
    # the response body to a JSON parser'
    # https://review.openstack.org/Documentation/rest-api.html
    if response.status_code == 404:
        return False
    return True


def print_tag_missing(name, tag):
    print ("* %s should have the tag '%s'" % (name, tag))


def print_bad_tag(name, tag):
    print ("* %s should not have the tag '%s'" % (name, tag))

if __name__ == '__main__':
    sys.exit(main())
