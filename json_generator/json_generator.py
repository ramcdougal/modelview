from neuron import h
import numpy
import json

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

def cell_tree(root):
    secs = secs_with_root(root)
    return [{'text': sec_seg(secs)}]

# summary
summary = {
    'text': sec_seg(list(h.allsec()))
}

# real cells
# TODO: action: display all cells
real_cells = {
    'text': '%d real cells' % len(root_sections)
}
if root_sections:
    real_cells['children'] = []
    for root in root_sections:
        # TODO: action: when clicking on a specific cell, display just that one
        real_cells['children'].append({'text': 'root %s' % root.name(), 'children': cell_tree(root)})

# TODO: this
artificial_cells = {'text': '0 artificial cells'}

# TODO: generate this automatically
references = {
    'text': 'References',
    'children': [
        {
            'text': 'Paper: <a href="http://dx.doi.org/10.1023/B:JCNS.0000004837.81595.b0">doi:10.1023/B:JCNS.0000004837.81595.b0</a>'
        },
        {
            'text': '<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=32992">ModelDB Entry</a>'
        }
    ]
}	  

blank_line = {'text': ''}

# linear mechanisms
linear_mechs = h.List('LinearMechanism')
linear_mechs = {'text': '%d LinearMechanism objects' % linear_mechs.count()}

# TODO: generate this automatically by analyzing modeldb
mech_xref = {
    'hd': ' (I-h, <a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=32992&file=\\synchro-ca1\\h.mod">h.mod</a>)',
    'kad': ' (K-A, <a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=32992&file=\\synchro-ca1\\kadist.mod">kadist.mod</a>)',
    'kap': ' (K-A, <a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=32992&file=\\synchro-ca1\\kaprox.mod">kaprox.mod</a>)',
    'kdr': ' (K-dr, <a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=32992&file=\\synchro-ca1\\kdrca1.mod">kdrca1.mod</a>)',
    'na3': ' (Na, <a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=32992&file=\\synchro-ca1\\na3n.mod">na3n.mod</a>)',
    'nax': ' (Na, <a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=32992&file=\\synchro-ca1\\naxn.mod">naxn.mod</a>)',
    'ds': ' (<a href="http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=32992&file=\\synchro-ca1\\distr.mod">distr.mod</a>)'
}

# mechanisms in use
mechs = []
h("""
objref mt
json_var = 0
strdef mname
""")
h.mt = h.MechanismType(0)
for i in xrange(int(h.mt.count()) - 1):
    h.mt.select(i)
    h('mt.selected(mname)')
    mechs.append({'text': h.mname + mech_xref.get(h.mname, '')})
mech_in_use = {'text': '%d mechanisms in use' % len(mechs), 'children': mechs}

# density mechanisms
density_mechanisms = {
    'text': 'Density Mechanisms',
    'children': [
        mech_in_use
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

# TODO: this
kschan_defs = {
    'text': 'KSChan definitions for density mechanisms'
}




data = {
    'neuron': [{'title': 'root: ' + root.name(), 'morphology': morph_per_root(root)} for root in root_sections],
    'title': 'CA1 pyramidal neuron: effects of Ih on distal inputs (Migliore et al 2004)',
    'short_title': 'Migliore et al 2004',
    'tree': [
            summary,
            blank_line,
            real_cells,
            artificial_cells,
            netcons,
            linear_mechs,
            blank_line,
            density_mechanisms,
            kschan_defs,
            blank_line,
            references              
        ]
}


with open('modelview.json', 'w') as f:
    f.write('modelview_data = ' + json.dumps(data))
    
    
    
