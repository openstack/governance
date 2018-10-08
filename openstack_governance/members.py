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

import logging
import re

LOG = logging.getLogger(__name__)

# Full name (IRC) <E-mail> [expires in] {role}
_PATTERN = re.compile('(?P<name>.*)\s+\((?P<irc>.*)\)\s+\<(?P<email>.*)\>\s+\[(?P<date>.*)\](\s+\{(?P<role>.*)\})?')


def parse_members_file(filename):
    """Load the members file and return each row as a dictionary.
    """
    with open(filename, 'r') as f:
        for linum, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            m = _PATTERN.match(line)
            if not m:
                LOG.warning('Could not parse line %d of %s: %r' %
                            (linum, filename, line))
                continue
            yield m.groupdict()
