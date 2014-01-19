import sys
import os
import urllib2
from run_protocols import protocol

p = sys.argv[1]
id = int(p.split('_')[0])

protocol = protocol[p]

#
# download the zip file
#
zip_file = urllib2.urlopen('http://senselab.med.yale.edu/ModelDB/eavBinDown.asp?o=%d&a=23&mime=application/zip' % id).read()
with open('zipfile.zip', 'wb') as f:
    f.write(zip_file)


#
# compile the model mechanisms
#
assert(protocol['compile'][0][: 3] == 'cd ')
dir_name = protocol['compile'][0][3:]
os.system('unzip zipfile.zip')
os.system('cp json_generator.py %s/' % dir_name)
os.chdir(dir_name)

for command in protocol['compile']:
    os.system(command)

#
# load the model into NEURON
#
assert(len(protocol['launch']) == 1)
assert(protocol['launch'][0] == 'nrngui -python')

# this import has to be done after the mod files have been compiled
from neuron import h

#
# act as if we're going to run it, but generate the json and exit when the
# first fadvance occurs
#
def generate_json(*args, **kwargs):
    if h.t <= 0: return
    # json_generator expects to be run from the terminal, so update sys.argv
    sys.argv = ['json_generator.py', id, 'norun', p]
    import json_generator
    os.system('cp *.json ..')
    os.chdir('..')
    os.remove('zipfile.zip')
    os.system('rm -fr %s' % dir_name)
    sys.exit()
    
for i, command in enumerate(protocol['run']):
    if i == len(protocol['run']) - 1:
        h.CVode().extra_scatter_gather(0, generate_json)
    exec(command)

print 'WARNING: Never actually did an fadvance.'
print '         Attempting to generate JSON anyways.'
h.t = 1
generate_json()
