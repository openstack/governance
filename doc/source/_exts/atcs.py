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

"""Show information about extra ATCs managed in this repo.
"""

import operator
import re

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives import tables
from docutils.utils import SystemMessagePropagation
from sphinx.util import logging

import projects

LOG = logging.getLogger(__name__)


class ExtraATCsTable(tables.Table):
    """List the extra ATCs for the given project.
    """

    HEADERS = ('Full Name', 'Email', 'Expires In')
    HEADER_MAP = {
        'Full Name': 'name',
        'Email': 'email',
        'Expires In': 'expires-in',
    }

    option_spec = {'class': directives.class_option,
                   'name': directives.unchanged,
                   'project': directives.unchanged,
                   }

    def run(self):
        project = self.options.get('project')
        if not project:
            error = self.state_machine.reporter.error(
                'No project set for extra-atcs table',
                nodes.literal_block(self.block_text, self.block_text),
                line=self.lineno)
            return [error]

        # Handle the width settings and title
        try:
            col_widths = self.get_column_widths(len(self.HEADERS))
            title, messages = self.make_title()
        except SystemMessagePropagation as detail:
            return [detail.args[0]]
        except Exception as err:
            error = self.state_machine.reporter.error(
                'Error processing memberstable directive:\n%s' % err,
                nodes.literal_block(self.block_text, self.block_text),
                line=self.lineno,
            )
            return [error]

        all_teams = projects.get_project_data()
        try:
            team_data = all_teams[project]
        except KeyError:
            raise ValueError('No project %r in projects.yaml' % (project,))
        project_members = team_data.get('extra-atcs', [])

        # If we have no extra ATCs, skip building the table.
        if not project_members:
            return []

        # Sort the project_members by name
        project_members = sorted(
            project_members,
            key=operator.itemgetter('name'),
        )

        table_node = self.build_table(project_members, col_widths)
        table_node['classes'] += self.options.get('class', [])
        self.add_name(table_node)

        if title:
            table_node.insert(0, title)

        return [table_node] + messages

    def build_table(self, project_members, col_widths):
        table = nodes.table()

        # Set up the column specifications
        # based on the widths.
        tgroup = nodes.tgroup(cols=len(col_widths))
        table += tgroup
        tgroup.extend(nodes.colspec(colwidth=col_width)
                      for col_width in col_widths)

        # Set the headers
        thead = nodes.thead()
        tgroup += thead
        row_node = nodes.row()
        thead += row_node
        row_node.extend(
            nodes.entry(h, nodes.paragraph(text=h))
            for h in self.HEADERS
        )

        # The body of the table is made up of rows.
        # Each row contains a series of entries,
        # and each entry contains a paragraph of text.
        tbody = nodes.tbody()
        tgroup += tbody
        rows = []
        for row in project_members:
            trow = nodes.row()
            # Iterate over the headers in the same order every time.
            for h in self.HEADERS:
                # Get the cell value from the row data, replacing None
                # in re match group with empty string.
                cell = row.get(self.HEADER_MAP[h]) or ''
                entry = nodes.entry()
                para = nodes.paragraph(text=str(cell))
                entry += para
                trow += entry
            rows.append(trow)
        tbody.extend(rows)

        return table


_PATTERN = re.compile(r'(?P<project>.+):\s+(?P<name>.+)\s\((?P<email>.+)\)\s\[(?P<expires_in>.*)\]')


def setup(app):
    LOG.info('loading atcs extension')
    app.add_directive('extraatcstable', ExtraATCsTable)
