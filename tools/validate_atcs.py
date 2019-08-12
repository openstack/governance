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
from datetime import datetime
import json
import logging

import requests
import yaml

LOG = logging.getLogger()


# The OpenStack foundation member directory lookup API endpoint
MEMBER_LOOKUP_URL = 'https://openstackid-resources.openstack.org/'


def lookup_member(email):
    "A requests wrapper to querying the OSF member directory API"
    # URL pattern for querying foundation members by E-mail address
    LOG.debug('looking up %s', email)
    raw = requester(
        MEMBER_LOOKUP_URL + '/api/public/v1/members',
        params={
            'filter[]': [
                'group_slug==foundation-members',
                'email==' + email,
            ],
            'expand': 'all_affiliations',
        },
        headers={'Accept': 'application/json'},
    )
    decoded = decode_json(raw)
    try:
        return decoded['data'][0]
    except (KeyError, IndexError):
        return None


def requester(url, params={}, headers={}):
    """A requests wrapper to consistently retry HTTPS queries

    :param url: The URL to get.
    :type url: str
    :param params: Additional parameters to provide.
    :type params: dict(str, str)
    :param headers: Additional headers to set.
    :type params: dict(str, str)

    """
    # Try up to 3 times
    retry = requests.Session()
    retry.mount("https://", requests.adapters.HTTPAdapter(max_retries=3))
    return retry.get(url=url, params=params, headers=headers)


def decode_json(raw):
    """Trap JSON decoding failures and provide more detailed errors

    Remove ')]}' XSS prefix from data if it is present, then decode it
    as JSON and return the results.

    :param raw: Response text from API
    :type raw: str

    """

    # Gerrit's REST API prepends a JSON-breaker to avoid XSS vulnerabilities
    if raw.text.startswith(")]}'"):
        trimmed = raw.text[4:]
    else:
        trimmed = raw.text

    # Try to decode and bail with much detail if it fails
    try:
        decoded = json.loads(trimmed)
    except Exception:
        LOG.error(
            '\nrequest returned %s error to query:\n\n    %s\n'
            '\nwith detail:\n\n    %s\n',
            raw, raw.url, trimmed)
        raise
    return decoded


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--projects',
        default='./reference/projects.yaml',
        help='projects.yaml file path (%(default)s)',
    )
    args = parser.parse_args()

    # Quiet the urllib3 module output coming out of requests.
    logging.getLogger('urllib3').setLevel(logging.WARNING)

    logging.basicConfig()

    with open(args.projects, 'r', encoding='utf-8') as f:
        projects = yaml.safe_load(f.read())

    exit_code = 0

    for project_name, project_data in sorted(projects.items()):
        atcs = project_data.get('extra-atcs', [])
        for atc in atcs:
            try:
                member = lookup_member(atc['email'])
            except Exception as e:
                print('ERROR: {}: Could not validate ATC {}: {}'.format(
                    project_name, atc, e))
            else:
                if not member:
                    # NOTE(mnaser): The ATC membership checks were not
                    #               enforced for all ATCs expiring before
                    #               January 2020.  This should be removed
                    #               after January 2020.
                    expires = datetime.strptime(atc['expires-in'], "%B %Y")
                    if expires <= datetime(2020, 1, 1):
                        msg = 'Skipping {} from validation'.format(atc)
                    else:
                        msg = 'Unable to find membership: {}'.format(atc)
                        exit_code = 1

                    print('{}: {}'.format(project_name, msg))

    return exit_code


if __name__ == '__main__':
    import sys
    sys.exit(main())
