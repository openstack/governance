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

from __future__ import print_function

import argparse
import os.path

import yaml

_section = '''
Planning Artifacts:

Completion Artifacts:
'''


def main():
    parser = argparse.ArgumentParser(
        'build the "Project Teams" section of a goal document',
    )
    parser.parse_args()

    print('Paste this output to the end of the goals file:\n')

    filename = os.path.abspath('reference/projects.yaml')
    with open(filename, 'r') as f:
        projects = [k for k in yaml.safe_load(f.read())]
    projects.sort(key=lambda x: x.lower())

    for p in projects:
        print(p)
        print('-' * len(p))
        print(_section)


if __name__ == '__main__':
    main()
