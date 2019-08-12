#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Verify that all data files match the schema."""

import argparse
import pkgutil

import jsonschema

from openstack_governance import yamltools


_yaml = yamltools.YAML()

_PROJECTS_SCHEMA = _yaml.load(
    pkgutil.get_data('openstack_governance',
                     'projects_schema.yaml').decode('utf-8')
)


def main():
    parser = argparse.ArgumentParser()
    parser.parse_args()

    errors = []

    with open('reference/projects.yaml', 'r', encoding='utf-8') as f:
        all_projects = _yaml.load(f.read())

    validator = jsonschema.Draft4Validator(_PROJECTS_SCHEMA)

    errors = False
    for e in validator.iter_errors(all_projects):
        errors = True
        print(e)

    return 1 if errors else 0
