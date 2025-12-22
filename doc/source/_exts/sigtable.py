#!/usr/bin/env python

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

"""Build a table of the current teams"""

import yaml

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.tables import Table
from sphinx.util import logging

LOG = logging.getLogger(__name__)


class SIGTable(Table):
    """Insert the members table using the referenced file as source.
    """
    HEADERS = ('Name', 'Status', 'Chairs', 'Scope')
    WIDTHS = [15, 15, 40, 80]

    option_spec = {'class': directives.class_option,
                   'name': directives.unchanged,
                   'datafile': directives.unchanged,
                   'reposfile': directives.unchanged,
                   }

    def run(self):
        env = self.state.document.settings.env

        # The required argument to the directive is the name of the
        # file to parse.
        datafile = self.options.get('datafile')
        if not datafile:
            error = self.state_machine.reporter.error(
                'No filename in sigtable directive',
                nodes.literal_block(self.block_text, self.block_text),
                line=self.lineno)
            return [error]

        # Now find the real path to the file, relative to where we are.
        _, filename = env.relfn2path(datafile)

        LOG.info('loading sigtable')
        LOG.info('reading %s' % filename)
        with open(filename, 'r', encoding='utf-8') as f:
            _teams_yaml = yaml.safe_load(f.read())

        # Load repos data if reposfile is provided
        _repos_yaml = {}
        reposfile = self.options.get('reposfile')
        if reposfile:
            _, repos_filename = env.relfn2path(reposfile)
            LOG.info('reading repos from %s' % repos_filename)
            with open(repos_filename, 'r', encoding='utf-8') as f:
                _repos_yaml = yaml.safe_load(f.read())

        # Adjust headers and widths if repos are included
        headers = list(self.HEADERS)
        widths = list(self.WIDTHS)
        if _repos_yaml:
            headers.append('Repositories')
            widths.append(60)

        table = nodes.table()

        # Set up the column specifications
        # based on the widths.
        tgroup = nodes.tgroup(cols=len(headers))
        table += tgroup
        tgroup.extend(nodes.colspec(colwidth=col_width)
                      for col_width in widths)

        # Set the headers
        thead = nodes.thead()
        tgroup += thead
        row_node = nodes.row()
        thead += row_node
        row_node.extend(
            nodes.entry(h, nodes.paragraph(text=h))
            for h in headers
        )

        # The body of the table is made up of rows.
        # Each row contains a series of entries,
        # and each entry contains a paragraph of text.
        tbody = nodes.tbody()
        tgroup += tbody
        rows = []

        all_teams = _teams_yaml
        if not all_teams:
            return []
        for team in sorted(all_teams.keys()):
            trow = nodes.row()
            # Iterate over the headers in the same order every time.
            for h in headers:
                if h.lower() == "name":
                    cell = "<a href=\"%s\">%s</a>" % (all_teams[team]['url'],
                                                      team)
                    entry = nodes.entry()
                    para = nodes.raw('', cell, format='html')
                elif h.lower() == "status":
                    s = all_teams[team]['status'].lower()
                    cell = ('<a href="https://governance.openstack.org/sigs/'
                            'reference/sig-guideline.html#%s">%s</a>'
                            ) % (s, s)
                    entry = nodes.entry()
                    para = nodes.raw('', cell, format='html')
                elif h.lower() == "chairs":
                    chairs = []
                    for chair in all_teams[team]['chairs']:
                        chairs.append("%s (%s, <br /> %s) <br /> <br />" % (chair['name'], chair['irc'], chair['email']))
                    cell = "".join(chairs)
                    entry = nodes.entry()
                    para = nodes.raw('', cell, format='html')
                elif h.lower() == "repositories":
                    # Add repositories column if available
                    repos = []
                    if team in _repos_yaml:
                        for repo_item in _repos_yaml[team]:
                            repo = repo_item['repo']
                            repos.append('<a href="https://opendev.org/%s">%s</a>' % (repo, repo))
                    cell = '<br />'.join(repos) if repos else ''
                    entry = nodes.entry()
                    para = nodes.raw('', cell, format='html')
                else:
                    # Get the cell value from the row data, replacing None
                    # in re match group with empty string.
                    cell = all_teams[team][h.lower()] or ''
                    entry = nodes.entry()
                    para = nodes.paragraph(text=str(cell))
                entry += para
                trow += entry
            rows.append(trow)
        tbody.extend(rows)

        # Build the table node
        table['classes'] += self.options.get('class', [])
        self.add_name(table)

        return [table]


class RetiredSIGTable(SIGTable):

    HEADERS = ('Name', 'Status', 'Chairs', 'Scope', 'Reason')
    WIDTHS = [15, 15, 40, 60, 60]


def setup(app):
    app.add_directive('sigtable', SIGTable)
    app.add_directive('retired-sigtable', RetiredSIGTable)
