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

import json
import urllib

import requests

import base

# Specify stable branch to look for. Some repos contain stable branches
# but not for the most recent release.
# TODO(jogo): figure out to stop hard coding this.
latest_stable_branch = "kilo"


class ValidateStableBranches(base.ValidatorBase):

    @staticmethod
    def has_stable_branch(repo):
        response = requests.get(
            'https://review.openstack.org:443/projects/%s/branches' %
            urllib.quote_plus(repo))
        # strip off first few chars because 'the JSON response body starts with
        # a magic prefix line that must be stripped before feeding the rest of
        # the response body to a JSON parser'
        # https://review.openstack.org/Documentation/rest-api.html
        branches = json.loads(response.text[4:])
        for branch in branches:
            if branch['ref'].startswith("refs/heads/stable/%s" %
                                        latest_stable_branch):
                return True
        return False

    @staticmethod
    def validate(repo):
        """Return True of team should contain the tag get_tag_name()"""
        return ValidateStableBranches.has_stable_branch(repo)

    @staticmethod
    def get_tag_name():
        return "release:has-stable-branches"
