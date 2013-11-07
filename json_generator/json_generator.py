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
    for sec in h.allsec():
        if get_root(sec) != root: continue
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

data = {'neuron': [{'title': 'root: ' + root.name(), 'morphology': morph_per_root(root)} for root in root_sections],
        'title': 'CA1 pyramidal neuron: effects of Ih on distal inputs (Migliore et al 2004)',
        'short_title': 'Migliore et al 2004',
        'tree': [
	            {
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
	        ]
	    }


with open('modelview.json', 'w') as f:
    f.write('modelview_data = ' + json.dumps(data))
    
    
    
