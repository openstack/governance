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

"""
Generate badges for the projects
"""

import os

from itertools import chain
from itertools import zip_longest
from PIL import ImageFont
from sphinx.util import logging

import projects

LOG = logging.getLogger(__name__)

PADDING = 8
BASE_TAGS_URL = 'https://governance.openstack.org/tc/reference/tags/'
COLOR_SCHEME = {
    "brightgreen": "#4c1",
    "green": "#97CA00",
    "yellow": "#dfb317",
    "yellowgreen": "#a4a61d",
    "orange": "#fe7d37",
    "red": "#e05d44",
    "blue": "#007ec6",
    "grey": "#555",
    "lightgrey": "#9f9f9f",
}

SVG_ROOT = """<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg contentScriptType="text/ecmascript" zoomAndPan="magnify" contentStyleType="text/css"
 height="{height}" width="{width}" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg"
 version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink">
  <title id="os:gov:badges:title">
    This is a container for a set of OpenStack badges indicating the status and
    features of this project and its repository
  </title>
{svg}
</svg>
"""
FLAT_BADGE_TEMPLATE = """<svg id="{left_text}:{right_text}" width="{width}" height="20" x="{svg_x}" y="{svg_y}">
<title>{left_text}:{right_text}</title>
<a target="_blank" xlink:href="{link}">
  <linearGradient id="smooth:{left_text}:{right_text}" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>

  <mask id="round:{left_text}:{right_text}">
    <rect width="{width}" height="20" rx="3" fill="#fff"/>
  </mask>

  <g mask="url(#round:{left_text}:{right_text})">
    <rect width="{left_width}" height="20" fill="#555"/>
    <rect x="{left_width}" width="{right_width}" height="20" fill="{color}"/>
    <rect width="{width}" height="20" fill="url(#smooth:{left_text}:{right_text})"/>
  </g>

  <g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11">
    <text x="{left_x}" y="15" fill="#010101" fill-opacity=".3">{left_text}</text>
    <text x="{left_x}" y="14">{left_text}</text>
    <text x="{right_x}" y="15" fill="#010101" fill-opacity=".3">{right_text}</text>
    <text x="{right_x}" y="14">{right_text}</text>
  </g>
</a>
</svg>
"""


def _generate_badge(left_text, right_text, link=None, colorscheme='brightgreen'):

    font = ImageFont.truetype('DejaVuSans.ttf', 11)
    left_width = font.getsize(left_text)[0] + PADDING
    right_width = font.getsize(right_text)[0] + PADDING
    width = left_width + right_width

    data = {
        'link': link or '',
        'svg_x': 0,
        'svg_y': 0,
        'color': COLOR_SCHEME[colorscheme],
        'width': width,
        'left_width': left_width,
        'left_text': left_text,
        'left_x': left_width / 2,
        'right_width': right_width,
        'right_text': right_text,
        'right_x': left_width + right_width / 2 - 1,
    }

    return data


def _generate_tag_badges(tags):
    badges = []

    badges.append(_generate_badge('project', 'official'))

    for tag in tags:
        # NOTE(flaper87): will submit other patches to make these
        # tags consistent with the rest.
        if tag in ['starter-kit:compute', 'tc-approved-release']:
            group, tname = 'tc', tag
        else:
            group, tname = tag.split(':')

        link = BASE_TAGS_URL + '%s.html' % tag.replace(':', '_')
        badges.append(_generate_badge(group, tname, link, colorscheme='blue'))
    return badges


def _organize_badges(badges):
    sbadges = sorted(badges, key=lambda badge: badge['width'])

    # NOTE(flaper87): 4 is the number of columns
    ziped = list(zip_longest(*(iter(sbadges),) * 4))

    result = []
    for y, group in enumerate(ziped):
        result.append([])
        col_x = 0
        for x, badge in enumerate(group):
            # NOTE(flaper87): zip_longest fills the
            # empty slots with None. We don't care about
            # those.
            if badge is None:
                break

            width_badge = ziped[-1][x]
            if width_badge is None:
                if len(ziped) > 1:
                    width_badge = ziped[-2][x]
                else:
                    width_badge = badge

            badge['height'] = 20
            badge['svg_y'] = (20 + 4) * y

            # NOTE(flaper87): 3 is just an extra padding in case there are two badges
            # with the same width in the same row
            badge['svg_x'] = col_x
            col_x += width_badge['width'] + 3
            result[y].append(badge)
    return result


def _to_svg(badges):
    for badge in badges:
        yield FLAT_BADGE_TEMPLATE.format(**badge)


def _generate_teams_badges(app, exception=None):
    LOG.info('Generating team badges')
    all_teams = projects.get_project_data()
    files = []

    badges_dir = os.path.join(app.outdir, 'badges')
    if not os.path.exists(badges_dir):
        os.mkdir(badges_dir)

    filename = os.path.join(badges_dir, 'project-unofficial.svg')
    svg_data = _generate_badge('project', 'unofficial', colorscheme='red')
    svg = FLAT_BADGE_TEMPLATE.format(**svg_data)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(SVG_ROOT.format(height=20, width=106, svg=svg))
    files.append(filename)

    for team, info in all_teams.items():
        LOG.info('generating team badge for %s' % team)

        for name, deliverable in info['deliverables'].items():
            tags = info.get('tags', []) + deliverable.get('tags', [])
            badges = _organize_badges(_generate_tag_badges(tags))
            svg = '\n'.join(_to_svg(chain(*badges)))

            root_width = max([bdg_row[-1]['width'] + bdg_row[-1]['svg_x']
                              for bdg_row in badges])
            root_height = badges[-1][0]['svg_y'] + badges[-1][0]['height']

            for repo in deliverable.get('repos', []):
                repo_name = repo.split('/')[1]
                filename = os.path.join(badges_dir, '%s.svg' % projects.slugify(repo_name))
                with open(filename, 'w') as f:
                    f.write(SVG_ROOT.format(height=root_height, width=root_width, svg=svg))
                files.append(filename)

    return files


def setup(app):
    LOG.info('loading badges extension')
    app.connect('build-finished', _generate_teams_badges)
