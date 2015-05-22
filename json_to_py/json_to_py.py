"""
Convert ModelDB's ModelView JSON to Python runnable with NEURON.

Robert A. McDougal
January 2015

Note: This script necessarily makes a number of assumptions on how to interpret
      the JSON. No guarantees are made about the "inversion."

Some known assumptions/limitations:
- If endpoints occupy the same point, they are assumed to be connected
- all ion mechanisms are assumed to be inserted by mod files
- connections to the root are assumed to occur at either end; I'm not sure how common this is in practice, but it's true for e.g. 87284... more recently generated modelviews (with a parents attribute for each neuron) do not have this limitation
- all connections to the child are assumed to occur at child(0)
- point processes are ignored (usually no big deal because these are often for synaptic connections/other input)
- linear mechanisms, kschan mechanisms are ignored
"""

cell_template = """# converted by json_to_py from {json_file}

class {class_name}:
    def __init__(self, name=None, x=0, y=0, z=0):
        '''Instantiate {class_name}.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, self is used instead
        '''
        self._x, self._y, self._z = x, y, z
        self._name = name
        self._setup_morphology()
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "{class_name}_instance"

    def _set_section_morphology(self, sec, xyzdiams):
        '''sets the shape and position for a section, shifting it by the offset position'''
        from neuron import h
        h.pt3dclear(sec=sec)
        for pt in xyzdiams:
            x, y, z, diam = pt
            h.pt3dadd(x + self._x, y + self._y, z + self._z, diam, sec=sec)
            
    def _setup_morphology(self):
        self._create_sections()
        self._shape_sections()
        self._connect_sections()
    
    def _insert_mechanisms(self):
        {mechanism_code}
    
    def _set_mechanism_parameters(self):
        {parameter_code}
    
    def _create_sections(self):
        from neuron import h
        {section_code}
    
    def _shape_sections(self):
        {shape_code}
    
    def _connect_sections(self):
        {connection_code}
    
    def _discretize_model(self):
        {nseg_code}

if __name__ == '__main__':
    # if this file is run directly, create one instance
    # NB: this won't do anything interesting by itself and is best used with
    #     NEURON's GUI tools
    
    from neuron import h, gui
    {temperature_code}
    cell = {class_name}(name='neuron')
"""

def json_to_py(json_file, py_file, cell_num=0):
    import json
    import collections
    import itertools
    with open(json_file) as f:
        data = json.load(f)
    
    def unknown_modelview_version():
        import warnings
        warnings.warn('Unknown modelview version; will attempt to generate Python anyways, but this process might be inaccurate.')
    
    def parse_assert(condition):
        if not condition:
            raise Exception('Unable to parse ModelView json.')
    
    if data['modelview_version'] != 0: unknown_modelview_version()
    
    # read temperature
    temperature_code = None
    for row in data['tree']:
        if 'text' in row and 'Temperature:' in row['text']:
            if row['text'] == 'Temperature: unmodeled':
                temperature_code = ''
            else:
                temperature_code = 'h.celsius = %g' % float(row['text'].split(':')[1].split('&deg;C')[0])
    parse_assert(temperature_code is not None)
    
    cell_line_split = data['tree'][2]['text'].split()
    parse_assert(len(cell_line_split) == 4 and cell_line_split[2] == 'with' and cell_line_split[3] == 'morphology')
    num_cells = int(cell_line_split[0])
    if num_cells <= cell_num:
        raise Exception('Attempted to extract cell number %d, but there are only %d in the json.' % (cell_num, num_cells))

    parse_assert(len(data['tree'][2]['children']) == num_cells)
    parse_assert(len(data['neuron']) == num_cells)
    
    neuron = data['neuron'][cell_num]
    morphology = neuron['morphology']
    seg_names = neuron['seg_names']
    neuron_properties = data['tree'][2]['children'][cell_num]
    
    root_node_line = neuron_properties['text'].split()
    parse_assert(len(root_node_line) == 2 and root_node_line[0] == 'root')
    
    root_node = root_node_line[1]
    
    inserted_mechanisms = neuron_properties['children'][2]
    inserted_mechanisms_line = inserted_mechanisms['text'].split()
    parse_assert(len(inserted_mechanisms_line) == 3 and inserted_mechanisms_line[1] == 'inserted' and inserted_mechanisms_line[2] == 'mechanisms')
    inserted_mechanisms = inserted_mechanisms['children']
    
    # TODO: use the strategy used for constant_parameters for inserted_mechanisms (i.e. don't hardcode position)
    constant_parameters = [child for child in neuron_properties['children'] if 'subsets with constant parameters' in child['text']]
    parse_assert(len(constant_parameters) <= 1)
    if constant_parameters:
        constant_parameters = constant_parameters[0]['children']

    unique_parameters = [child for child in neuron_properties['children'] if 'sections with unique parameters' in child['text']]
    parse_assert(len(unique_parameters) <= 1)
    if unique_parameters:
        unique_parameters = unique_parameters[0]['children']
    
    # get maps of sec names, segment indices, positions, endpoints, etc
    sec_names = set()
    sec_arrays = {}
    index_lookup = {}
    section_indices = {}
    section_positions = {}
    positions = []
    ends0 = {}
    ends1 = {}
    for i, seg in enumerate(seg_names):
        index_lookup[seg] = i
        parts = seg.split('(')
        position = float(parts[1].split(')')[0])
        positions.append(position)
        sec_name = parts[0]
        if position == 0:
            ends0[sec_name] = morphology[i][0][0 : 3]
        elif position == 1:
            ends1[sec_name] = morphology[i][0][0 : 3]
        else:
            if sec_name not in section_indices:
                section_indices[sec_name] = [i]
                section_positions[sec_name] = [position]
            else:
                section_indices[sec_name].append(i)
                section_positions[sec_name].append(position)
                parse_assert(position == max(section_positions[sec_name]))
        if '[' in sec_name:
            parts = sec_name.split('[')
            sec_array = parts[0]
            index = int(parts[1].split(']')[0])
            sec_arrays[sec_array] = max(index + 1, sec_arrays.get(sec_array, 0))
        else:
           sec_names.add(sec_name)

    num_secs = len(section_indices)

    # the name of the NEURON class we will build
    class_name = data['short_title'].replace(' ', '_').replace('.', '')
    
    # used for separating lines in class methods
    separator = '        '
    
    # code for constructing the sections and section arrays
    # we sort to ensure consistency
    sec_names = sorted(sec_names)
    # start with those that aren't arrays
    section_code = separator.join('self.{sec} = h.Section(cell=self, name="{sec}")\n'.format(sec=sec) for sec in sec_names)
    # now the arrays
    section_code += ''.join(separator + 'self.{array} = [h.Section(cell=self, name="{array}[%d]" % i) for i in xrange({length})]\n'.format(array=array_name, length=sec_arrays[array_name]) for array_name in sorted(sec_arrays.keys()))
    # remove any leading or trailing whitespace
    section_code = section_code.strip()
    
    # code for identifying the shape of sections
    shape_code = ''
    for sec in sorted(section_indices.keys()):
        indices = section_indices[sec]
        pts = list(itertools.chain.from_iterable(morphology[i] for i in indices))
        shape_code += separator + ('self._set_section_morphology(self.%s, %r)\n' % (sec, pts)) 
    # remove any leading or trailing white space
    shape_code = shape_code.strip()
    
    # code for identifying nseg
    nseg_code = separator.join('self.{sec}.nseg = {nseg}\n'.format(sec=sec, nseg=len(section_indices[sec])) for sec in sec_names)
    for array_name in sorted(sec_arrays.keys()):
        length = sec_arrays[array_name]
        distinct_nseg = set(len(section_indices['%s[%d]' % (array_name, i)]) for i in xrange(length))
        for nseg in distinct_nseg:
            nseg_code += separator + 'for i in %r:\n' % ([i for i in xrange(length) if len(section_indices['%s[%d]' % (array_name, i)]) == nseg])
            nseg_code += separator + '    self.%s[i].nseg = %d\n' % (array_name, nseg)
        
    nseg_code = nseg_code.strip()
    
    # code for identifying mechanisms
    # TODO: clean this up so that there's no need to assign sec_lists to
    #       variables; just insert everything that exists in exactly that
    #       sec_list in one pass
    mechanism_code = 'from neuron import h\n'
    sec_lists = {}
    for mechanism in inserted_mechanisms:
        # skip the mechanisms that are present by default
        mechanism_name = mechanism['text'].split()[0]
        if mechanism_name in ('Ra', 'cm'): continue
        # skip the ion mechanisms that are (usually) inserted by mod files
        if mechanism_name[-4:] == '_ion': continue
        mechanism_secs = sorted(set(seg_names[i].split('(')[0] for i in mechanism['action'][0]['highlight']))
        if mechanism_secs:
            if len(mechanism_secs) == num_secs:
                mechanism_code += separator + 'for sec in h.allsec():\n'
            else:
                sec_list = '[%s]' % ', '.join('self.%s' % sec for sec in mechanism_secs)
                if sec_list not in sec_lists:
                    sec_lists[sec_list] = len(sec_lists)
                    mechanism_code += separator + 'sec_list%d = %s\n' % (len(sec_lists) - 1, sec_list)
                sec_list = 'sec_list%d' % sec_lists[sec_list]
                mechanism_code += separator + 'for sec in %s:\n' % sec_list
            mechanism_code += separator + '    sec.insert("%s")\n' % mechanism_name
    mechanism_code = mechanism_code.strip()
    
    # code for supporting constant parameters
    parameter_code = ''
    for parm_subset in constant_parameters:
        secs = sorted(set(seg_names[i].split('(')[0] for i in parm_subset['action'][0]['highlight']))
        sec_list = '[%s]' % ', '.join('self.%s' % sec for sec in secs)
        parameter_code += separator + 'for sec in %s:\n' % sec_list
        for child in parm_subset['children']:
            parameter_code += separator + '    sec.' + child['text'] + '\n'
    
    connection_code = ''
    if 'parents' not in neuron:
        # code for locating shared endpoints (and hence: connections)

        connection_pts = collections.defaultdict(list)
        for name, coords in ends0.iteritems():
            connection_pts[tuple(coords)].append(name + '(0)')
        for name, coords in ends1.iteritems():
            connection_pts[tuple(coords)].append(name + '(1)')
        # ensure the root node is connected to the rest of the tree (well... this guarantees it's connected to something; it doesn't guarantee it's connected to everything)
        root_ends = [tuple(ends0[root_node]), tuple(ends1[root_node])]
        parse_assert(len(connection_pts[root_ends[0]]) + len(connection_pts[root_ends[1]]) > 2)
        # now write the connection code
        for connection_pt in sorted(connection_pts.keys()):
            nodes = connection_pts[connection_pt]
            if len(nodes) < 2: continue
            parent = [node for node in nodes if '(1)' in node] + [node for node in nodes if node == root_node + '(0)']
            parse_assert(len(parent) == 1)
            parent = parent[0]
            for node in sorted(nodes):
                if node != parent:
                    connection_code += '%sself.%s.connect(self.%s, 0)\n' % (separator, node.split('(')[0], parent)
    else:
        for sec, parent in zip(neuron['secs'], neuron['parents']):
            if parent is not None:
                connection_code += '%sself.%s.connect(self.%s)\n' % (separator, sec, parent)
    connection_code = connection_code.strip()        
    
    # code for supporting the unique parameters
    for sec_data in unique_parameters:
        sec = sec_data['text']
        for child in sec_data['children']:
            param_rule = child['text']
            rhs = param_rule.split('=')[1].strip()
            if ' ' in rhs:
                lhs = param_rule.split('=')[0].strip()
                # specified on a per-segment basis
                parameter_code += separator + 'for seg, value in zip(self.%s, [%s]):\n' % (sec.strip(), ', '.join(rhs.split()))
                parameter_code += separator + '    seg.%s = value\n' % lhs
            else:
                # constant for the whole section
                parameter_code += separator + 'self.' + sec.strip() + '.' + param_rule + '\n'
    parameter_code = parameter_code.strip()
    
    with open(py_file, 'w') as f:
        f.write(cell_template.format(json_file=json_file,
                                     class_name=class_name,
                                     mechanism_code=mechanism_code,
                                     nseg_code=nseg_code,
                                     section_code=section_code,
                                     connection_code=connection_code,
                                     shape_code=shape_code,
                                     parameter_code=parameter_code,
                                     temperature_code=temperature_code
        ))


if __name__ == '__main__':
    import sys
    if len(sys.argv) not in (3, 4):
        print 'Usage: python %s FILENAME.JSON FILENAME.PY [CELL#]' % sys.argv[0]

    json_file = sys.argv[1]
    py_file = sys.argv[2]
    if len(sys.argv) > 3:
        cell_num = int(sys.argv[3])
    else:
        cell_num = 0
    json_to_py(json_file, py_file, cell_num=cell_num)


