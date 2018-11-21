# All Rights Reserved.
#
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

import yaml
import yamlordereddictloader


def loads(blob):
    """Load a yaml blob and retain key ordering."""
    # This does use load, which is unsafe, but should be ok
    # for what we are loading here in this program; we should
    # be able to fix that in the future (if it matters).
    return yaml.load(blob, Loader=yamlordereddictloader.Loader)


def load_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return loads(f.read())
