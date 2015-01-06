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
    
    print seg_names

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


