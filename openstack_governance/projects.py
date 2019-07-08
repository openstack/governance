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


from openstack_governance import yamltools


def load_project_file(filename='reference/projects.yaml'):
    yaml = yamltools.YAML()
    with open(filename, 'r', encoding='utf-8') as f:
        return yaml.load(f)


def write_project_file(data, filename='reference/projects.yaml'):
    yaml = yamltools.YAML()
    with open(filename, 'w', encoding='utf-8') as f:
        yaml.dump(data, f)
