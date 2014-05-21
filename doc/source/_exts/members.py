"""Build a table of the current members of the TC.
"""

import re

from docutils import nodes
from docutils.parsers.rst.directives.tables import Table
from docutils.parsers.rst import directives

# Full name (IRC nickname) [expires in] {role}
_PATTERN = re.compile('(?P<name>.*)\s+\((?P<irc>.*)\)\s+\[(?P<date>.*)\](\s+\{(?P<role>.*)\})?')


def _parse_members_file(app, filename):
    """Load the members file and return each row as a dictionary.
    """
    with open(filename, 'r') as f:
        for linum, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            m = _PATTERN.match(line)
            if not m:
                app.warning('Could not parse line %d of %s: %r' %
                            (linum, filename, line))
                continue
            yield m.groupdict()


class MembersTable(Table):
    """Insert the members table using the referenced file as source.
    """

    HEADERS = ('Full Name', 'IRC Nickname', 'Term Expires', 'Role')
    HEADER_MAP = {
        'Full Name': 'name',
        'IRC Nickname': 'irc',
        'Term Expires': 'date',
        'Role': 'role',
    }

    option_spec = {'class': directives.class_option,
                   'name': directives.unchanged,
                   'datafile': directives.unchanged,
                   }

    has_content = False

    def run(self):
        env = self.state.document.settings.env
        app = env.app
        config = app.config

        # The required argument to the directive is the name of the
        # file to parse.
        datafile = self.options.get('datafile')
        if not datafile:
            error = self.state_machine.reporter.error(
                'No filename in membertable directive',
                nodes.literal_block(self.block_text, self.block_text),
                line=self.lineno)
            return [error]

        # Handle the width settings and title
        try:
            col_widths = self.get_column_widths(len(self.HEADERS))
            title, messages = self.make_title()
        except SystemMessagePropagation, detail:
            return [detail.args[0]]
        except Exception, err:
            error = self.state_machine.reporter.error(
                'Error processing memberstable directive:\n%s' % err,
                nodes.literal_block(self.block_text, self.block_text),
                line=self.lineno,
                )
            return [error]

        # Now find the real path to the file, relative to where we are.
        rel_filename, filename = env.relfn2path(datafile)

        # Build the table node using the parsed file
        data_iter = _parse_members_file(app, filename)
        table_node = self.build_table(
            data_iter,
            col_widths,
        )
        table_node['classes'] += self.options.get('class', [])
        self.add_name(table_node)

        if title:
            table_node.insert(0, title)

        return [table_node] + messages

    def build_table(self, table_data, col_widths):
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
        for row in table_data:
            trow = nodes.row()
            # Iterate over the headers in the same order every time.
            for h in self.HEADERS:
                # Get the cell value from the row data, replacing None
                # in re match group with empty string.
                cell = row.get(self.HEADER_MAP[h]) or ''
                entry = nodes.entry()
                para = nodes.paragraph(text=unicode(cell))
                entry += para
                trow += entry
            rows.append(trow)
        tbody.extend(rows)

        return table

def setup(app):
    app.info('loading members extension')
    app.add_directive('memberstable', MembersTable)
