# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
#
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.

"""
A tool that will translate a projects.yaml file into a visualized graph.

Usage: universe_dot.py <projects-file> <output-file> just-project? ...

To run make sure pydot (or pydot2) is installed, as well as six and pyyaml.

After these are installed run this like:

$ python tools/universe_dot.py reference/projects.yaml \
  ironic_universe.dot ironic;

$ neato -Tsvg ironic_universe.dot > ironic_universe.svg

Then open ironic_universe.svg in your favorite web browser.

Or to create the whole openstack universe.

$ python tools/universe_dot.py reference/projects.yaml os_universe.dot

$ neato -Tsvg os_universe.dot > os_universe.svg

Then open os_universe.svg in your favorite web browser.
"""

import sys
import time

import pydot
import six
import yaml

if len(sys.argv) == 1:
    print(__doc__.strip())
    sys.exit(1)


projects_file = sys.argv[1]
output_dot_file = sys.argv[2]
just_projects = set(sys.argv[3:])

print("Reading projects from '%s'" % projects_file)
with open(projects_file, 'rb') as fh:
    projects = yaml.safe_load(fh)
    project_names = sorted(six.iterkeys(projects))
    if just_projects:
        print("Restricting to just %s projects" % list(just_projects))
        for project_name in list(project_names):
            if project_name not in just_projects:
                project_names.remove(project_name)
    project_names = tuple(project_names)

graph_nodes = {}
start = time.time()
print("Constructing nodes.")
print("Please wait...")
deliverable_node_attrs = {
    'fontsize': '11',
}
project_node_attrs = {
    'fontsize': '11',
    'shape': 'diamond',
}
node_count = 0
edges_needed = 0
for project_name in project_names:
    node = pydot.Node(name=project_name, **project_node_attrs)
    node_count += 1
    graph_nodes[project_name] = node
    deliverables = projects[project_name].get('deliverables', [])
    deliverable_names = sorted(six.iterkeys(deliverables))
    for deliverable_name in deliverable_names:
        edges_needed += 1
        node_path = "%s/%s" % (project_name, deliverable_name)
        if deliverable_name == project_name:
            # Avoid creating a self-link, since its actually not, avoid
            # this by creating a node with a hidden name, and a label that
            # is its actual name...
            node_deliverable_node_attrs = dict(deliverable_node_attrs)
            node_deliverable_node_attrs['name'] = '__%s' % deliverable_name
            node_deliverable_node_attrs['label'] = deliverable_name
        else:
            node_deliverable_node_attrs = dict(deliverable_node_attrs)
            node_deliverable_node_attrs['name'] = deliverable_name
        node = pydot.Node(**node_deliverable_node_attrs)
        graph_nodes[node_path] = node
        node_count += 1

print("Inserting %s nodes and %s edges into"
      " a new graph." % (node_count, edges_needed))
print("Please wait...")
if just_projects:
    nice_names = [name.title() for name in sorted(just_projects)]
    graph_name = '%s Universe' % (" and ".join(nice_names))
else:
    graph_name = 'OpenStack Universe'
graph_kwargs = {
    'rankdir': 'LR',
    'nodesep': '0.25',
    'overlap': 'false',
    'ranksep': '0.5',
    'splines': 'true',
    'ordering': 'in',
    'graph_name': graph_name,
}
graph = pydot.Graph(**graph_kwargs)
for project_name in project_names:
    print("  Inserting nodes for '%s'" % project_name)
    node = graph_nodes[project_name]
    graph.add_node(node)
    deliverables = projects[project_name].get('deliverables', [])
    deliverable_names = sorted(six.iterkeys(deliverables))
    for deliverable_name in deliverable_names:
        print("    Inserting node for '%s'" % deliverable_name)
        node_path = "%s/%s" % (project_name, deliverable_name)
        deliverable_node = graph_nodes[node_path]
        graph.add_node(deliverable_node)
        print("    Inserting edge for '%s' -> '%s'"
              % (project_name, deliverable_name))
        graph.add_edge(pydot.Edge(node, deliverable_node,
                                  style='dotted'))
end = time.time()
print("Finished in %0.2f seconds" % (end - start))

print("Writing graph to '%s'" % output_dot_file)
with open(output_dot_file, "wb") as fh:
    fh.write(graph.to_string())
