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

_default_last_updated = datetime.datetime.now()


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
            except ValueError as err:
                LOG.info('[governance] Could not parse modification time of '
                         '%s: %r',
                         src_file, last_updated_t)
    return None


def _get_last_updated(app, pagename):
    last_updated = None
    full_src_file = app.builder.env.doc2path(pagename)

    candidates = []

    # Strip the prefix from the filename so the git command recognizes
    # the file as part of the current repository.
    src_file = full_src_file[len(app.builder.env.srcdir):].lstrip('/')
    candidates.append(src_file)

    if not os.path.exists(src_file):
        # Some of the files are in doc/source and some are not. Some
        # of the ones that are not are symlinked. If we can't find the
        # file after stripping the full prefix, try looking for it in
        # doc/source explicitly.
        candidates.append(os.path.join('doc/source', src_file))

    if pagename.startswith('reference/projects/'):
        # If the file is in the reference/projects directory, it may
        # be an auto-generated project page. In that case, use the
        # YAML file as the source of the last_updated timestamp.
        candidates.append('reference/projects.yaml')

    for filename in candidates:
        last_updated = _get_last_updated_file(filename)
        if last_updated:
            LOG.info('[governance] Last updated for %s is %s',
                     pagename, last_updated)
            return last_updated
    LOG.info('[governance] could not determine last_updated for %r',
             pagename)
    return _default_last_updated


def html_page_context(app, pagename, templatename, context, doctree):
    # Use the last modified date from git instead of applying a single
    # value to the entire site.
    context['last_updated'] = _get_last_updated(app, pagename)


def setup(app):
    LOG.info('[governance] connecting html-page-context event handler')
    app.connect('html-page-context', html_page_context)
    return {
        'parallel_read_safe': True,
    }
