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

import datetime
import os.path
import subprocess

from sphinx.util import logging

LOG = logging.getLogger('page_context')

_projects_last_updated = datetime.datetime.now()
_projects_last_updated_set = False


def _get_last_updated_file(src_file):
    if not os.path.exists(src_file):
        return None
    try:
        last_updated_t = subprocess.check_output(
            [
                'git', 'log', '-n1', '--format=%ad',
                '--date=format:%Y-%m-%d %H:%M:%S',
                '--', src_file,
            ]
        ).decode('utf-8').strip()
    except subprocess.CalledProcessError as err:
        LOG.info('[governance] Could not get modification time of %s: %s',
                 src_file, err)
    else:
        if last_updated_t:
            try:
                return datetime.datetime.strptime(last_updated_t,
                                                  '%Y-%m-%d %H:%M:%S')
            except ValueError:
                LOG.info('[governance] Could not parse modification time of '
                         '%s: %r',
                         src_file, last_updated_t)
    return None


def html_page_context(app, pagename, templatename, context, doctree):
    # Use the last modified date from git instead of applying a single
    # value to the entire site.
    global _projects_last_updated
    global _projects_last_updated_set

    # Note: openstackdocstheme now handles this, so we only need to do our own
    # evaluation for generated reference pages.
    if pagename.startswith('reference/projects/'):
        if not _projects_last_updated_set:
            last_updated = _get_last_updated_file('reference/projects.yaml')
            if last_updated:
                LOG.info('[governance] Last updated for reference/'
                         'projects.yaml is %s', last_updated)
                _projects_last_updated = last_updated
                _projects_last_updated_set = True

        context['last_updated'] = _projects_last_updated


def setup(app):
    LOG.info('[governance] connecting html-page-context event handler')
    app.connect('html-page-context', html_page_context)
    return {
        'parallel_read_safe': True,
    }
