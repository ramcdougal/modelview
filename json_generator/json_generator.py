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
real_cells = {
    'text': '%d real cells' % len(root_sections)
}
if root_sections:
    real_cells['children'] = []
    for root in root_sections:
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

data = {
    'neuron': [{'title': 'root: ' + root.name(), 'morphology': morph_per_root(root)} for root in root_sections],
    'title': 'CA1 pyramidal neuron: effects of Ih on distal inputs (Migliore et al 2004)',
    'short_title': 'Migliore et al 2004',
    'tree': [
            summary,
            blank_line,
            real_cells,
            artificial_cells,
            references              
        ]
}


with open('modelview.json', 'w') as f:
    f.write('modelview_data = ' + json.dumps(data))
    
    
    
