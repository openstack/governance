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

"""Report on the current list of projects.
"""

import yaml

from docutils import nodes
from docutils.parsers import rst
from docutils.statemachine import ViewList
from sphinx.util.nodes import nested_parse_with_titles

import projects


def _team_to_rst(name, info):
    yield '.. _project-%s:' % projects.slugify(name)
    yield ''
    yield '=' * len(name)
    yield name.title()
    yield '=' * len(name)
    yield ''
    yield ':Home Page: ' + info.get('url', '')
    yield ':PTL: ' + info.get('ptl', '')
    service = info.get('service')
    if service:
        yield ':Service: ' + service
    yield ''
    mission = info.get('mission', '').rstrip()
    if mission:
        yield mission
        yield ''
    for project in info.get('projects', []):
        tags = [
            ':ref:`tag-%s`' % t['name']
            for t in project.get('tags', [])
        ]
        if tags:
            tag_references = '(%s)' % ', '.join(tags)
        else:
            tag_references = ''
        yield '- :repo:`%s` %s' % (project['repo'], tag_references)
    yield ''
    yield '.. extraatcstable:: :ref:`Extra ATCs <atc>`'
    yield '   :project: %s' % name
    yield ''


def _write_team_pages(app):
    all_teams = projects.get_project_data()
    files = []
    for team, info in all_teams.items():
        slug = projects.slugify(team)
        filename = 'reference/projects/%s.rst' % slug
        app.info('generating team page for %s' % team)
        with open(filename, 'w') as f:
            f.write('\n'.join(_team_to_rst(team, info)))
        files.append(filename)
    return files


class TeamsListDirective(rst.Directive):

    has_content = False

    def run(self):
        env = self.state.document.settings.env
        app = env.app

        all_teams = projects.get_project_data()

        # Build the view of the data to be parsed for rendering.
        result = ViewList()
        for team_name in sorted(all_teams.keys()):
            team_info = all_teams[team_name]
            for line in _team_to_rst(team_name, team_info):
                result.append(line, '<' + __name__ + '>')

        # Parse what we have into a new section.
        node = nodes.section()
        node.document = self.state.document
        nested_parse_with_titles(self.state, result, node)

        return node.children


def setup(app):
    app.info('loading teams extension')
    app.add_directive('teamslist', TeamsListDirective)
    _write_team_pages(app)
