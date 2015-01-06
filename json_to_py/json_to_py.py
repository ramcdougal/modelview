cell_template = """# converted by json_to_py from {json_file}

class {class_name}:
    def __init__(self, name=None, x=0, y=0, z=0):
        '''Instantiate {class_name}.
        
        Parameters:
            x, y, z -- position offset
            name -- a name for the cell (used for the cell= argument of Section)
            
        Note: if name is not specified, self is used instead
        '''
        self._x, self._y, self._z = x, y, z
        self._name = name if name is not None else self

        self._setup_morphology()
        self._setup_mechanisms()

    def _setup_morphology(self):
        self._create_sections()
        self._setup_nseg()
        self._connect_sections()
    
    def _setup_mechanisms(self):
        {mechanism_code}
    
    def _create_sections(self):
        from neuron import h
        {section_code}
    
    def _connect_sections(self):
        {connection_code}
    
    def _setup_nseg(self):
        {nseg_code}

if __name__ == '__main__':
    # if this file is run directly, create one instance
    # NB: this won't do anything interesting by itself and is best used with
    #     NEURON's GUI tools
    
    cell = {class_name}(name='neuron')
"""

def json_to_py(json_file, py_file, cell_num=0):
    import json
    with open(json_file) as f:
        data = json.load(f)
    
    def unknown_modelview_version():
        import warnings
        warnings.warn('Unknown modelview version; will attempt to generate Python anyways, but this process might be inaccurate.')
    
    def parse_assert(condition):
        if not condition:
            raise Exception('Unable to parse ModelView json.')
    
    if data['modelview_version'] != 0: unknown_modelview_version()
    
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
    
    def get_section_names(seg_names):
        sec_names = set()
        sec_arrays = {}
        for seg in seg_names:
            sec_name = seg.split('(')[0]
            if '[' in sec_name:
                parts = sec_name.split('[')
                sec_array = parts[0]
                index = int(parts[1].split(']')[0])
                sec_arrays[sec_array] = max(index + 1, sec_arrays.get(sec_array, 0))
            else:
               sec_names.add(sec_name)

        return sec_names, sec_arrays
    
    sec_names, sec_arrays = get_section_names(seg_names)

    # the name of the NEURON class we will build
    class_name = data['short_title'].replace(' ', '_').replace('.', '')
    
    # used for separating lines in class methods
    separator = '        '
    
    # code for constructing the sections and section arrays
    # we sort to ensure consistency
    sec_names = sorted(sec_names)
    # start with those that aren't arrays
    section_code = separator.join('self.{sec} = h.Section(cell=self._name, name="{sec}")\n'.format(sec=sec) for sec in sec_names)
    # now the arrays
    section_code += ''.join(separator + 'self.{array} = [h.Section(cell=self._name, name="{array}[%d]" % i) for i in xrange({length})]\n'.format(array=array_name, length=sec_arrays[array_name]) for array_name in sorted(sec_arrays.keys()))
    # remove any leading or trailing whitespace
    section_code = section_code.strip()
    
        
    
    
    mechanism_code = 'pass'
    connection_code = 'pass'
    nseg_code = 'pass'
    
    with open(py_file, 'w') as f:
        f.write(cell_template.format(json_file=json_file,
                                     class_name=class_name,
                                     mechanism_code=mechanism_code,
                                     nseg_code=nseg_code,
                                     section_code=section_code,
                                     connection_code=connection_code
        ))
    
    print sec_names
    print sec_arrays
    print class_name

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


