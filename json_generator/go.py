import sys
import os
import urllib2
from run_protocols import protocol

p = sys.argv[1]
id = int(p.split('_')[0])

protocol = protocol[p]

zip_file = urllib2.urlopen('http://senselab.med.yale.edu/ModelDB/eavBinDown.asp?o=%d&a=23&mime=application/zip' % id).read()
with open('zipfile.zip', 'wb') as f:
    f.write(zip_file)

assert(protocol['compile'][0][: 3] == 'cd ')
dir_name = protocol['compile'][0][3:]
os.system('unzip zipfile.zip')
os.system('cp json_generator.py %s/' % dir_name)
os.chdir(dir_name)

for command in protocol['compile']:
    os.system(command)

assert(len(protocol['launch']) == 1)
assert(protocol['launch'][0][:15] == 'nrngui -python ')
load_file = protocol['launch'][0][15:]

# this import has to be done after the mod files have been compiled
from neuron import h
h.load_file(load_file)

# TODO: add hook for fadvance that execfiles json_generator

for command in protocol['run']:
    exec(command)

os.system('cp *.json ..')
os.chdir('..')
os.remove('zipfile.zip')
os.system('rm -fr %s' % dir_name)
