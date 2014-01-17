import sys
import os
from run_protocols import protocol
from neuron import h

p = sys.argv[1]
id = int(p.split('_')[0])

protocol = protocol[p]

# TODO: this won't work because wget doesn't get the zip file name

os.system('wget "http://senselab.med.yale.edu/ModelDB/eavBinDown.asp?o=%d&a=23&mime=application/zip"' % id)

assert(protocol['compile'][0][: 3] == 'cd ')
dir_name = protocol['compile'][0][3:]
os.system('unzip %s.zip' % dir_name)
os.system('cp json_generator.py %s/' % dir_name)
os.system('cd %s' % dir_name)

for command in protocol['compile']:
    os.system(command)

assert(len(protocol['launch']) == 1)
assert(protocol['launch'][0][:15] == 'nrngui -python ')
load_file = protocol['launch'][15:]
h.load_file(load_file)

# TODO: add hook for fadvance that execfiles json_generator

for command in protocol['run']:
    exec(command)

os.system('cp *.json ..')

os.system('cd ..')
os.system('rm -f %s.zip' % dir_name)
os.system('rm -fr %s' % dir_name)
