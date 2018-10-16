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

"""Load the projects.yaml file.
"""

import copy
import os.path

from openstack_governance import projects
from sphinx.util import logging

LOG = logging.getLogger(__name__)

_projects_yaml = {}


def get_project_data():
    """Return a copy of the project data."""
    return copy.deepcopy(_projects_yaml)


def slugify(name):
    """Convert name to slug form for references."""
    return name.lower().replace(' ', '-')


def setup(app):
    global _projects_yaml

    filename = os.path.abspath('reference/projects.yaml')
    LOG.info('reading %s' % filename)
    _projects_yaml = projects.load_project_file(filename)
