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

"""Do dirty things with wikis.
"""

import collections
import itertools

import mwclient


def get_page_section(page_content, section_start):
    "Return iterable of lines making up a section of a wiki page."
    lines = page_content.splitlines()
    lines = itertools.dropwhile(
        lambda x: x != section_start,
        lines,
    )
    next(lines)  # skip the start_section line
    lines = itertools.takewhile(
        lambda x: not x.startswith('='),  # another section or subsection
        lines,
    )
    return lines


def get_wiki_table(section_content):
    """Return iterable of dicts making up rows of a wiki table.

    Assumes there is only one table per section.

    """
    lines = itertools.dropwhile(
        lambda x: x != '{| class="wikitable"',
        section_content,
    )
    headings = []
    items = []
    for line in lines:
        if line == '|-':
            continue
        elif line.startswith('!'):
            headings = [h.strip() for h in line.lstrip('!').split('!!')]
        elif line in ['}', '|}']:
            # end of table
            break
        elif line.startswith('|'):
            items.extend(i.strip() for i in line.lstrip('|').split('||'))

        if len(items) == len(headings):
            row = {
                h: i
                for (h, i) in zip(headings, items)
            }
            yield row
            items = []


def get_wiki_page(name):
    "Return the text of a wiki page as a string."
    site = mwclient.Site('wiki.openstack.org')
    page = site.Pages[name]
    return page.text()


def get_liaison_data():
    "Return team -> liaisons mapping"
    project_to_liaisons = collections.OrderedDict()
    wiki_page = get_wiki_page('OpenStack_health_tracker')
    section = get_page_section(wiki_page, '=== Project Teams ===')
    table = get_wiki_table(section)

    for row in table:
        if not row:
            continue
        liaisons = [
            m.strip()
            for m in row['TC members'].split(',')
            if m.strip()
        ]
        project_to_liaisons[row['Group']] = liaisons

    return project_to_liaisons
