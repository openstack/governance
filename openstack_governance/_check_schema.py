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
import os
import pkgutil

import jsonschema

from openstack_governance import yamltools

_yaml = yamltools.YAML()


def main():
    parser = argparse.ArgumentParser()
    parser.parse_args()

    for data_file, schema_file in (
        ('members.yaml', 'members.yaml'),
        ('projects.yaml', 'projects.yaml'),
        ('sigs-repos.yaml', 'repos.yaml'),
        ('technical-committee-repos.yaml', 'repos.yaml'),
        (os.path.join('sigs', 'archived-sigs.yaml'), 'sigs.yaml'),
        (os.path.join('sigs', 'completed-sigs.yaml'), 'sigs.yaml'),
        (os.path.join('sigs', 'sigs.yaml'), 'sigs.yaml'),
    ):
        pkg_schema = pkgutil.get_data(
            'openstack_governance', os.path.join('schemas', schema_file)
        )
        schema = _yaml.load(pkg_schema.decode())
        validator = jsonschema.Draft202012Validator(schema)

        with open(f'reference/{data_file}', 'r', encoding='utf-8') as f:
            data = _yaml.load(f.read())

        errors = False
        for e in validator.iter_errors(data):
            errors = True
            print(e)

    return 1 if errors else 0
