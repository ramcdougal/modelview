from neuron import h
import numpy
import json

h.load_file("mview.hoc")

mview = h.ModelView(1)

items = []
def navigate(hlist):
    items = []
    i=0
    for ho in hlist:
        item = {'text': ho.s.lstrip(' *')}
        if ho.children:
            item['children'] = navigate(ho.children)
        items.append(item)
    return items

# TODO: build these in instead of scraping from classic ModelView
classic_rows = navigate(mview.display.top)
nsegs = {}
for row in classic_rows:
    words = row['text'].split()
    # NOTE: the row contains all its children in the same format as in the JSON
    if len(words) == 3 and words[1] == 'LinearMechanism':
        linear_mechanisms = row
    if len(words) == 3 and words[1] == 'artificial':
        artificial_cells = row
    if len(words) == 3 and words[1] == 'real' and words[2] == 'cells':
        for root in row['children']:
            root_name = root['text'][5:]
            nsegs[root_name] = root['children'][1]
    if row['text'] == 'Density Mechanisms':
        for child_row in row['children']:
            if child_row['text'] == 'Global parameters for density mechanisms':
                global_param_for_density = child_row
            if child_row['text'] == 'KSChan definitions for density mechanisms':
                kschan_defs = child_row
            if child_row['text'] == 'Homogeneous Parameters':
                # TODO: colorize
                homogeneous_parameters = child_row
            if child_row['text'] == 'Heterogeneous Parameters':
                # TODO: colorize
                heterogeneous_parameters = child_row

print nsegs

def get_pts_between(x, y, z, d, arc, lo, hi):
    left_x = numpy.interp(lo, arc, x, left=x[0], right=x[-1])
    left_y = numpy.interp(lo, arc, y, left=y[0], right=y[-1])
    left_z = numpy.interp(lo, arc, z, left=z[0], right=z[-1])
    left_d = numpy.interp(lo, arc, d, left=d[0], right=d[-1])
    right_x = numpy.interp(hi, arc, x, left=x[0], right=x[-1])
    right_y = numpy.interp(hi, arc, y, left=y[0], right=y[-1])
    right_z = numpy.interp(hi, arc, z, left=z[0], right=z[-1])
    right_d = numpy.interp(hi, arc, d, left=x[0], right=d[-1])
    in_between = [[x0, y0, z0, d0] for (x0, y0, z0, d0, a0) in zip(x, y, z, d, arc) if lo < a0 < hi]
    return [[left_x, left_y, left_z, left_d]] + in_between + [[right_x, right_y, right_z, right_d]]

def get_root(sec):
    return h.SectionRef(sec=sec).root().sec

root_sections = []
for sec in h.allsec():
    if not h.SectionRef(sec).has_parent():
        root_sections.append(sec)

# TODO: generate this automatically by analyzing modeldb or, better, the model files
mech_xref = {
    'hd': ' (I-h, <a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=32992&file=\\synchro-ca1\\h.mod">h.mod</a>)',
    'kad': ' (K-A, <a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=32992&file=\\synchro-ca1\\kadist.mod">kadist.mod</a>)',
    'kap': ' (K-A, <a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=32992&file=\\synchro-ca1\\kaprox.mod">kaprox.mod</a>)',
    'kdr': ' (K-dr, <a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=32992&file=\\synchro-ca1\\kdrca1.mod">kdrca1.mod</a>)',
    'na3': ' (Na, <a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=32992&file=\\synchro-ca1\\na3n.mod">na3n.mod</a>)',
    'nax': ' (Na, <a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=32992&file=\\synchro-ca1\\naxn.mod">naxn.mod</a>)',
    'ds': ' (<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=32992&file=\\synchro-ca1\\distr.mod">distr.mod</a>)'
}

# get all mech names
mech_names = []
h("""
objref mt
json_var = 0
strdef mname
""")
h.mt = h.MechanismType(0)
for i in xrange(int(h.mt.count())):
    h.mt.select(i)
    h('mt.selected(mname)')
    mech_names.append(h.mname)

# get all point process names
pointprocess_names = []
h.mt = h.MechanismType(1)
for i in xrange(int(h.mt.count())):
    h.mt.select(i)
    h('mt.selected(mname)')
    pointprocess_names.append(h.mname)

print 'pointprocess_names: ', pointprocess_names

# get the names of mechanism parameters (range_vars)
range_vars = {}
for mech in mech_names:
    h.mt = h.MechanismStandard(mech)
    range_vars[mech] = []
    suffix = '_' + mech
    lensuffix = len(suffix)
    for i in xrange(int(h.mt.count())):
        h('mt.name(mname, %d)' % i)
        mname = h.mname
        if mname[-lensuffix :] == suffix:
            mname = mname[: -lensuffix]
        range_vars[mech].append(mname)
    if not range_vars[mech]: del range_vars[mech]
print 'range_vars:', range_vars


def mechs_present(secs):
    result = []
    for name in mech_names:
        for sec in secs:
            if hasattr(sec(0.5), name):
                result.append(name)
                break
    return ['Ra', 'cm'] + result

def two_char_hex(n):
    s = hex(int(n))[-2 :]
    if s[0] == 'x':
        s = '0' + s[1]
    return s

def hex_rgb(r, g, b):
    """expects r, g, b between 0 and 1"""
    return '#' + two_char_hex(r * 255) + two_char_hex(g * 255) + two_char_hex(b * 255)

def values_to_colors(values):
    non_nan = [v for v in values if not numpy.isnan(v)]
    if len(non_nan) == 0:
        return ['black'] * len(values)
    lo = min(non_nan)
    hi = max(non_nan)
    length = float(hi - lo)
    if lo == hi:
        return ['black' if numpy.isnan(v) else 'red' for v in values]
    else:
        values = numpy.array([(v - lo) / length for v in values])
        # gradient from blue (lo) to red (hi)
        return [(hex_rgb(v, 0, 1 - v) if not numpy.isnan(v) else 'black') for v in values]

def morph_per_root(root):
    morph = []
    h.define_shape()
    for sec in secs_with_root(root):
        n3d = int(h.n3d(sec=sec))
        x = [h.x3d(i, sec=sec) for i in xrange(n3d)]
        y = [h.y3d(i, sec=sec) for i in xrange(n3d)]
        z = [h.z3d(i, sec=sec) for i in xrange(n3d)]
        d = [h.diam3d(i, sec=sec) for i in xrange(n3d)]
        arc = [h.arc3d(i, sec=sec) for i in xrange(n3d)]
        length = sec.L
        half_dx = 0.5 / sec.nseg
        for seg in sec:
            morph.append(get_pts_between(x, y, z, d, arc, (seg.x - half_dx) * length, (seg.x + half_dx) * length))
    return morph

def secs_with_root(root):
    return [sec for sec in h.allsec() if get_root(sec) == root]

def sec_seg(secs):
    if len(secs) == 1:
        num_secs = '1 section'
    else:
        num_secs = '%d sections' % len(secs)
    num_segs = sum(sec.nseg for sec in secs)
    if num_segs == 1:
        num_segs = '1 segment'
    else:
        num_segs = '%d segments' % num_segs
    return '%s; %s' % (num_secs, num_segs)

def set_action_to_all(tree, action):
    for row in tree:
        row['action'] = action
        if 'children' in row:
            set_action_to_all(row['children'], action)

def nseg_analysis(secs, cell_id, root_name):
    dx_max = 0
    for sec in secs:
        if sec.L / sec.nseg > dx_max:
            dx_max = sec.L / sec.nseg
            dx_max_loc = sec
    result = nsegs[root_name]
    set_action_to_all([result], [{'kind': 'neuronviewer', 'id': cell_id}])
    if result['text'] == '1 distinct values of nseg':
        result['text'] = '1 distinct value of nseg'
    result['children'][0]['action'] = [{'kind': 'neuronviewer', 'id': cell_id, 'colors': colorize_if_sec(secs, dx_max_loc)}]
    return result
    """
    dx_max = 0
    for sec in secs:
        if sec.L / sec.nseg > dx_max:
            dx_max = sec.L / sec.nseg
            dx_max_loc = sec
        nsegs[sec.nseg] = 0
    return {
        'text': '%d distinct value%s of nseg' % (len(nsegs.values()), 's' if len(nsegs.values()) != 1 else ''),
        'action': [{'kind': 'neuronviewer', 'id': cell_id}],
        'children': [
            {
                'text': 'Longest dx is %g at %s with nseg=%d' % (dx_max, dx_max_loc.name(), dx_max_loc.nseg),
                'action': [{'kind': 'neuronviewer', 'id': cell_id, 'colors': colorize_if_sec(secs, dx_max_loc)}]
            }
        ]
    }
    """

def colorize_by_mech_value(secs, mech, name):
    values = []
    for sec in secs:
        try:
            v = getattr(getattr(sec(0.5), mech), name)
            for seg in sec:
                values.append(getattr(getattr(seg, mech), name))
        except:    
            if not hasattr(sec(0.5), mech):
                values += [numpy.nan] * sec.nseg
    return values_to_colors(values)

def flot_by_distance_from_root(root, mech, name, secs):
    # measure distance from the midpt of the root
    h.distance(0, 0.5, sec=root)
    data = []
    for sec in secs:
        try:
            v = getattr(getattr(sec(0.5), mech), name)
            for seg in sec:
                data.append([h.distance(1, seg.x, sec=sec), getattr(getattr(seg, mech), name)])
        except:
            pass
    return [{
        'data': data,
        'color': 'black',
        'points': {'show': True}
    }]


def cell_mech_analysis(secs, cell_id):
    mps = mechs_present(secs)
    mechs = [name + mech_xref.get(name, '') for name in mps]
    children = []
    for mech_text, mech in zip(mechs, mps):
        child = {
            'text': mech_text,
            'action': [
                {
                    'kind': 'neuronviewer',
                    'colors': colorize_if_mech_present(secs, mech),
                    'id': cell_id
                }
            ]
        }
        if mech in range_vars:
            child_parts = []
            for name in range_vars[mech]:
                flotchart = flot_by_distance_from_root(root_sections[cell_id], mech, name, secs)
                child_parts.append({
                    'text': name,
                    'action': [
                        {'kind': 'neuronviewer', 'id': cell_id, 'colors': colorize_by_mech_value(secs, mech, name)},
                        {
                            'kind': 'flot',
                            'data': flotchart,
                            'xaxes': [{'axisLabel': 'Distance from root', 'labelcolor': 'black'}],
                            'yaxes': [{'axisLabel': '%s.%s' % (mech, name), 'labelcolor': 'black'}]
                        }
                    ]
                })
            child['children'] = child_parts
        children.append(child)
    return {
        'text': '%d inserted mechanisms' % len(mechs),
        'action': [{'kind': 'neuronviewer', 'id': cell_id}],
        'children': children
    }

def colorize_if_sec(secs, match_sec):
    result = []
    for sec in secs:
        result += ['red' if sec == match_sec else 'black'] * int(sec.nseg)
    return result

def colorize_if_mech_present(secs, mech):
    result = []
    for sec in secs:
        if hasattr(sec, mech) or hasattr(sec(0.5), mech):
            result += ['red'] * sec.nseg
        else:
            result += ['black'] * sec.nseg
    return result

def cell_tree(root):
    cell_id = root_sections.index(root)
    secs = secs_with_root(root)
    return [
        {
            'text': sec_seg(secs),
            'action': [{'kind': 'neuronviewer', 'id': cell_id}]
        },
        nseg_analysis(secs, cell_id, root.name()),
        cell_mech_analysis(secs, cell_id)
    ]

# summary
summary = {
    'text': sec_seg(list(h.allsec()))
}

# real cells
# TODO: action: display all cells
real_cells = {
    'text': '%d real cell%s' % (len(root_sections), 's' if len(root_sections) != 1 else ''),
    'action': [
        {
            'kind': 'neuronviewer',
            'id': i
        } for i in xrange(len(root_sections))
    ]
}
if root_sections:
    real_cells['children'] = []
    for cell_id, root in enumerate(root_sections):
        # TODO: action: when clicking on a specific cell, display just that one
        real_cells['children'].append({'text': 'root %s' % root.name(), 'children': cell_tree(root), 'action': [{'kind': 'neuronviewer', 'id': cell_id}]})

# TODO: generate this automatically
references = {
    'text': 'References',
    'children': [
        {
            'text': 'Paper: <a href="http://dx.doi.org/10.1023/B:JCNS.0000004837.81595.b0">doi:10.1023/B:JCNS.0000004837.81595.b0</a>',
            'noop': True
        },
        {
            'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=32992">ModelDB Entry</a>',
            'noop': True
        }
    ],
    'noop': True    
}	  

blank_line = {'text': ''}

# mechanisms in use
mechs = [{'text': name + mech_xref.get(name, '')} for name in mechs_present(list(h.allsec()))]
mech_in_use = {'text': '%d mechanisms in use' % len(mechs), 'children': mechs}

# density mechanisms
density_mechanisms = {
    'text': 'Density Mechanisms',
    'children': [
        mech_in_use,
        homogeneous_parameters,
        heterogeneous_parameters,
        global_param_for_density,
        kschan_defs
    ]
}

def process_values(name, values):
    if len(values) == 1:
        # TODO: plot location
        return {'text': '%s = %g' % (name, values[0])}
    else:
        # TODO: plot location, plot values as a function of distance to root
        return {
            'text': '%d values for %s from %g to %g' % (len(values), name, min(values), max(values)),
            'children': [{'text': v} for v in values]
        }

# NetCon (based on ncview.hoc)
netcon_list = h.List('NetCon')
netcons = {'text': '%d NetCon objects' % netcon_list.count()}
if netcon_list.count():
    weights = []
    delays = []
    threshold = []
    # TODO: talk to Michael about why this doesn't work in pure python
    for i in xrange(int(netcon_list.count())):
        h.mt = netcon_list.object(i)
        h('json_var = mt.weight')
        weights.append(h.json_var)
        h('json_var = mt.delay')
        delays.append(h.json_var)
        h('json_var = mt.threshold')
        threshold.append(h.json_var)
    weights = sorted(set(weights))
    delays = sorted(set(delays))
    threshold = sorted(set(threshold))
    netcons['children'] = [
        process_values('weight', weights),
        process_values('delay', delays),
        process_values('threshold', threshold)
    ]


# TODO: generate this by scanning modeldb. we already have this information
# TODO: actually use an include; do not store directly in the main json
components = {
    'text': '10 files shared with other ModelDB models',
    'children': [
        {
            'text': 'h.mod',
            'children': [
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=150288&file=\\KimEtAl2013\\h.mod">A 1000 cell network model for Lateral Amygdala (Kim et al. 2013)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=71312&file=\\xiaoshenli\\h.mod">CA1 pyramidal neuron synaptic integration (Li and Ascoli 2006, 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=106551&file=\\nc-mri\\h.mod">CA1 pyramidal neuron: calculation of MRI signals (Cassara et al. 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=44050&file=\\gaspiriniEtAl2004\\h.mod">CA1 pyramidal neuron: dendritic spike initiation (Gasparini et al 2004)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=138205&file=\\Schizophr\\h.mod">CA1 pyramidal neuron: schizophrenic behavior (Migliore et al. 2011)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=55035&file=\\obliques\\h.mod">CA1 pyramidal neuron: signal propagation in oblique dendrites (Migliore et al 2005)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=87535&file=\\magical7\\h.mod">CA1 pyramidal neurons: binding properties and the magical number 7 (Migliore et al. 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=144976&file=\\alzheimer\\h.mod">CA1 pyramidal neurons: effects of Alzheimer (Culmone and Migliore 2012)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=146376&file=\\reduction1.0\\h.mod">Ca1 pyramidal neuron: reduction model (Marasco et al. 2012)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=119283&file=\\FerranteEtAl2008\\h.mod">Computational neuropharmacology of CA1 pyramidal neuron (Ferrante et al. 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=146509&file=\\Branch_Point_Tapering\\h.mod">Functional impact of dendritic branch point morphology (Ferrante et al., 2013)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=97874&file=\\NQS_with_example\\modeldb\\h.mod">Neural Query System NQS Data-Mining From Within the NEURON Simulator (Lytton 2006)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=148644&file=\\ParekhAscoli2013\\h.mod">Neuronal morphology goes digital ... (Parekh & Ascoli 2013)'}
            ]
        },
        {
            'text': 'kadist.mod',
            'children': [
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=150288&file=\\KimEtAl2013\\kadist.mod">A 1000 cell network model for Lateral Amygdala (Kim et al. 2013)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=137259&file=\\ca3-synresp\\kadist.mod">A model of unitary responses from A/C and PP synapses in CA3 pyramidal cells (Baker et al. 2010)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=2796&file=\\ca1\\kadist.mod">CA1 pyramidal neuron (Migliore et al 1999)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=71312&file=\\xiaoshenli\\kadist.mod">CA1 pyramidal neuron synaptic integration (Li and Ascoli 2006, 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=106551&file=\\nc-mri\\kadist.mod">CA1 pyramidal neuron: calculation of MRI signals (Cassara et al. 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=7386&file=\\boosting\\kadist.mod">CA1 pyramidal neuron: conditional boosting of dendritic APs (Watanabe et al 2002)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=44050&file=\\gaspiriniEtAl2004\\kadist.mod">CA1 pyramidal neuron: dendritic spike initiation (Gasparini et al 2004)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=9769&file=\\lamotrigine\\kadist.mod">CA1 pyramidal neuron: effects of Lamotrigine on dendritic excitability (Poolos et al 2002)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=148094&file=\\kv72-R213QW-mutations\\kadist.mod">CA1 pyramidal neuron: effects of R213Q and R312W Kv7.2 mutations (Miceli et al. 2013)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=112546&file=\\km\\kadist.mod">CA1 pyramidal neuron: functional significance of axonal Kv7 channels (Shah et al. 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=126776&file=\\rebound\\kadist.mod">CA1 pyramidal neuron: rebound spiking (Ascoli et al.2010)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=138205&file=\\Schizophr\\kadist.mod">CA1 pyramidal neuron: schizophrenic behavior (Migliore et al. 2011)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=55035&file=\\obliques\\kadist.mod">CA1 pyramidal neuron: signal propagation in oblique dendrites (Migliore et al 2005)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=87535&file=\\magical7\\kadist.mod">CA1 pyramidal neurons: binding properties and the magical number 7 (Migliore et al. 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=144392&file=\\modeldb\\kadist.mod">CA1 pyramidal neurons: effects of Kv7 (M-) channels on synaptic integration (Shah et al. 2011)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=118986&file=\\mutant\\kadist.mod">CA1 pyramidal neurons: effects of a Kv7.2 mutation (Miceli et al. 2009)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=146376&file=\\reduction1.0\\kadist.mod">Ca1 pyramidal neuron: reduction model (Marasco et al. 2012)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=150551&file=\\AshhadNarayanan2013\\kadist.mod">Calcium waves and mGluR-dependent synaptic plasticity in CA1 pyr. neurons (Ashhad & Narayanan 2013)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=119283&file=\\FerranteEtAl2008\\kadist.mod">Computational neuropharmacology of CA1 pyramidal neuron (Ferrante et al. 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=146509&file=\\Branch_Point_Tapering\\kadist.mod">Functional impact of dendritic branch point morphology (Ferrante et al., 2013)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=97874&file=\\NQS_with_example\\modeldb\\kadist.mod">Neural Query System NQS Data-Mining From Within the NEURON Simulator (Lytton 2006)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=148644&file=\\ParekhAscoli2013\\kadist.mod">Neuronal morphology goes digital ... (Parekh & Ascoli 2013)</a>'}]            
        },
        {
            'text': 'kaprox.mod',
            'children': [
            {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=2796&file=\\ca1\\kaprox.mod">CA1 pyramidal neuron (Migliore et al 1999)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=71312&file=\\xiaoshenli\\kaprox.mod">CA1 pyramidal neuron synaptic integration (Li and Ascoli 2006, 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=106551&file=\\nc-mri\\kaprox.mod">CA1 pyramidal neuron: calculation of MRI signals (Cassara et al. 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=7386&file=\\boosting\\kaprox.mod">CA1 pyramidal neuron: conditional boosting of dendritic APs (Watanabe et al 2002)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=44050&file=\\gaspiriniEtAl2004\\kaprox.mod">CA1 pyramidal neuron: dendritic spike initiation (Gasparini et al 2004)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=9769&file=\\lamotrigine\\kaprox.mod">CA1 pyramidal neuron: effects of Lamotrigine on dendritic excitability (Poolos et al 2002)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=148094&file=\\kv72-R213QW-mutations\\kaprox.mod">CA1 pyramidal neuron: effects of R213Q and R312W Kv7.2 mutations (Miceli et al. 2013)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=112546&file=\\km\\kaprox.mod">CA1 pyramidal neuron: functional significance of axonal Kv7 channels (Shah et al. 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=19696&file=\\sc-pp\\kaprox.mod">CA1 pyramidal neuron: integration of subthreshold inputs from PP and SC (Migliore 2003)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=126776&file=\\rebound\\kaprox.mod">CA1 pyramidal neuron: rebound spiking (Ascoli et al.2010)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=138205&file=\\Schizophr\\kaprox.mod">CA1 pyramidal neuron: schizophrenic behavior (Migliore et al. 2011)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=55035&file=\\obliques\\kaprox.mod">CA1 pyramidal neuron: signal propagation in oblique dendrites (Migliore et al 2005)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=87535&file=\\magical7\\kaprox.mod">CA1 pyramidal neurons: binding properties and the magical number 7 (Migliore et al. 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=144976&file=\\alzheimer\\kaprox.mod">CA1 pyramidal neurons: effects of Alzheimer (Culmone and Migliore 2012)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=144392&file=\\modeldb\\kaprox.mod">CA1 pyramidal neurons: effects of Kv7 (M-) channels on synaptic integration (Shah et al. 2011)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=118986&file=\\mutant\\kaprox.mod">CA1 pyramidal neurons: effects of a Kv7.2 mutation (Miceli et al. 2009)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=146376&file=\\reduction1.0\\kaprox.mod">Ca1 pyramidal neuron: reduction model (Marasco et al. 2012)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=150551&file=\\AshhadNarayanan2013\\kaprox.mod">Calcium waves and mGluR-dependent synaptic plasticity in CA1 pyr. neurons (Ashhad & Narayanan 2013)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=119283&file=\\FerranteEtAl2008\\kaprox.mod">Computational neuropharmacology of CA1 pyramidal neuron (Ferrante et al. 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=3167&file=\\timing\\kaprox.mod">Estimation and Production of Time Intervals (Migliore et al 2001)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=117207&file=\\acker_antic\\Model\\kaprox.mod">Excitability of PFC Basal Dendrites (Acker and Antic 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=146509&file=\\Branch_Point_Tapering\\kaprox.mod">Functional impact of dendritic branch point morphology (Ferrante et al., 2013)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=97874&file=\\NQS_with_example\\modeldb\\kaprox.mod">Neural Query System NQS Data-Mining From Within the NEURON Simulator (Lytton 2006)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=148644&file=\\ParekhAscoli2013\\kaprox.mod">Neuronal morphology goes digital ... (Parekh & Ascoli 2013)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=145672&file=\\Fineberg_et_al_2012\\migliore_kaprox.mod">Neurophysiological impact of inactivation pathways in A-type K+ channels (Fineberg et al 2012)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=121259&file=\\bogaard2009\\kaprox.mod">Small world networks of Type I and Type II Excitable Neurons (Bogaard et al. 2009)</a>'}]
        },
        {
            'text': 'kdrca1.mod',
            'children': [
            {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=2796&file=\\ca1\\kdrca1.mod">CA1 pyramidal neuron (Migliore et al 1999)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=71312&file=\\xiaoshenli\\kdrca1.mod">CA1 pyramidal neuron synaptic integration (Li and Ascoli 2006, 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=106551&file=\\nc-mri\\kdrca1.mod">CA1 pyramidal neuron: calculation of MRI signals (Cassara et al. 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=7386&file=\\boosting\\kdrca1.mod">CA1 pyramidal neuron: conditional boosting of dendritic APs (Watanabe et al 2002)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=9769&file=\\lamotrigine\\kdrca1.mod">CA1 pyramidal neuron: effects of Lamotrigine on dendritic excitability (Poolos et al 2002)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=148094&file=\\kv72-R213QW-mutations\\kdrca1.mod">CA1 pyramidal neuron: effects of R213Q and R312W Kv7.2 mutations (Miceli et al. 2013)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=112546&file=\\km\\kdrca1.mod">CA1 pyramidal neuron: functional significance of axonal Kv7 channels (Shah et al. 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=19696&file=\\sc-pp\\kdrca1.mod">CA1 pyramidal neuron: integration of subthreshold inputs from PP and SC (Migliore 2003)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=126776&file=\\rebound\\kdrca1.mod">CA1 pyramidal neuron: rebound spiking (Ascoli et al.2010)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=138205&file=\\Schizophr\\kdrca1.mod">CA1 pyramidal neuron: schizophrenic behavior (Migliore et al. 2011)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=55035&file=\\obliques\\kdrca1.mod">CA1 pyramidal neuron: signal propagation in oblique dendrites (Migliore et al 2005)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=87535&file=\\magical7\\kdrca1.mod">CA1 pyramidal neurons: binding properties and the magical number 7 (Migliore et al. 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=144976&file=\\alzheimer\\kdrca1.mod">CA1 pyramidal neurons: effects of Alzheimer (Culmone and Migliore 2012)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=144392&file=\\modeldb\\kdrca1.mod">CA1 pyramidal neurons: effects of Kv7 (M-) channels on synaptic integration (Shah et al. 2011)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=118986&file=\\mutant\\kdrca1.mod">CA1 pyramidal neurons: effects of a Kv7.2 mutation (Miceli et al. 2009)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=146376&file=\\reduction1.0\\kdrca1.mod">Ca1 pyramidal neuron: reduction model (Marasco et al. 2012)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=119283&file=\\FerranteEtAl2008\\kdrca1.mod">Computational neuropharmacology of CA1 pyramidal neuron (Ferrante et al. 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=3167&file=\\timing\\kdrca1.mod">Estimation and Production of Time Intervals (Migliore et al 2001)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=146509&file=\\Branch_Point_Tapering\\kdrca1.mod">Functional impact of dendritic branch point morphology (Ferrante et al., 2013)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=148644&file=\\ParekhAscoli2013\\kdrca1.mod">Neuronal morphology goes digital ... (Parekh & Ascoli 2013)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=145672&file=\\Fineberg_et_al_2012\\migliore_kdrca1.mod">Neurophysiological impact of inactivation pathways in A-type K+ channels (Fineberg et al 2012)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=121259&file=\\bogaard2009\\kdrca1.mod">Small world networks of Type I and Type II Excitable Neurons (Bogaard et al. 2009)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=64212&file=\\VNO\\kdr.mod">Vomeronasal sensory neuron (Shimazaki et al 2006)</a>'}]
        },
        {
            'text': 'na3n.mod',
            'children': [{'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=71312&file=\\xiaoshenli\\na3n.mod">CA1 pyramidal neuron synaptic integration (Li and Ascoli 2006, 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=106551&file=\\nc-mri\\na3n.mod">CA1 pyramidal neuron: calculation of MRI signals (Cassara et al. 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=119283&file=\\FerranteEtAl2008\\na3n.mod">Computational neuropharmacology of CA1 pyramidal neuron (Ferrante et al. 2008)</a>'}]
        },
        {
            'text': 'naxn.mod',
            'children': [{'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=71312&file=\\xiaoshenli\\naxn.mod">CA1 pyramidal neuron synaptic integration (Li and Ascoli 2006, 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=106551&file=\\nc-mri\\naxn.mod">CA1 pyramidal neuron: calculation of MRI signals (Cassara et al. 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=44050&file=\\gaspiriniEtAl2004\\naxn.mod">CA1 pyramidal neuron: dendritic spike initiation (Gasparini et al 2004)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=101629&file=\\ca3b\\naxn.mod">CA3 pyramidal neuron: firing properties (Hemond et al. 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=119283&file=\\FerranteEtAl2008\\naxn.mod">Computational neuropharmacology of CA1 pyramidal neuron (Ferrante et al. 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=97874&file=\\NQS_with_example\\modeldb\\naxn.mod">Neural Query System NQS Data-Mining From Within the NEURON Simulator (Lytton 2006)</a>'}]
        },
        {
            'text': 'netstimm.mod',
            'children': [{'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=119283&file=\\FerranteEtAl2008\\netstimm.mod">Computational neuropharmacology of CA1 pyramidal neuron (Ferrante et al. 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=146509&file=\\Branch_Point_Tapering\\netstimm.mod">Functional impact of dendritic branch point morphology (Ferrante et al., 2013)</a>'}]
        },
        {
            'text': 'distr.mod',
            'children': [{'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=71312&file=\\xiaoshenli\\distr.mod">CA1 pyramidal neuron synaptic integration (Li and Ascoli 2006, 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=144541&file=\\Ih_current\\distr.mod">CA1 pyramidal neuron: Ih current (Migliore et al. 2012)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=106551&file=\\nc-mri\\distr.mod">CA1 pyramidal neuron: calculation of MRI signals (Cassara et al. 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=138205&file=\\Schizophr\\distr.mod">CA1 pyramidal neuron: schizophrenic behavior (Migliore et al. 2011)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=55035&file=\\obliques\\distr.mod">CA1 pyramidal neuron: signal propagation in oblique dendrites (Migliore et al 2005)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=144976&file=\\alzheimer\\distr.mod">CA1 pyramidal neurons: effects of Alzheimer (Culmone and Migliore 2012)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=101629&file=\\ca3b\\distr.mod">CA3 pyramidal neuron: firing properties (Hemond et al. 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=146376&file=\\reduction1.0\\distr.mod">Ca1 pyramidal neuron: reduction model (Marasco et al. 2012)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=118098&file=\\ca3-summ\\distr.mod">Ca3 pyramidal neuron: membrane response near rest (Hemond et al. 2009)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=119283&file=\\FerranteEtAl2008\\distr.mod">Computational neuropharmacology of CA1 pyramidal neuron (Ferrante et al. 2008)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=146509&file=\\Branch_Point_Tapering\\distr.mod">Functional impact of dendritic branch point morphology (Ferrante et al., 2013)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=7659&file=\\window\\distr.mod">Modulation of temporal integration window (Migliore, Shepherd 2002)</a>'},
                {'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=148644&file=\\ParekhAscoli2013\\distr.mod">Neuronal morphology goes digital ... (Parekh & Ascoli 2013)</a>'}]
        },
        {
            'text': 'n128su.hoc',
            'children': [{'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=119283&file=\\FerranteEtAl2008\\n128su.hoc">Computational neuropharmacology of CA1 pyramidal neuron (Ferrante et al. 2008)</a>'}]
        },
        {
            'text': 'n128su.ses',
            'children': [{
                'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=119283&file=\\FerranteEtAl2008\\n128su.ses">Computational neuropharmacology of CA1 pyramidal neuron (Ferrante et al. 2008)</a>'}]
        }
    ]
}

# make all of the components noop
def make_noop(tree):
    for row in tree:
        row['noop'] = True
        if 'children' in row:
            make_noop(row['children'])
make_noop([components])


data = {
    'neuron': [{'title': 'root: ' + root.name(), 'morphology': morph_per_root(root)} for root in root_sections],
    'title': 'CA1 pyramidal neuron: effects of Ih on distal inputs (Migliore et al 2004)',
    'short_title': 'Migliore et al 2004',
    'neuronviewer': range(len(root_sections)),
    'tree': [
            summary,
            blank_line,
            real_cells,
            artificial_cells,
            netcons,
            linear_mechanisms,
            blank_line,
            density_mechanisms,
            blank_line,
            components,
            blank_line,
            references              
        ]
}


with open('modelview.json', 'w') as f:
    f.write(json.dumps(data))
    
    
    
