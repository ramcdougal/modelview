#!/usr/bin/python
# sprinkle_json_gen.py
# copy the json_generator.py into the top level folders and run them,
# finally move all the accessionnum.json files into the 
# (senselab)modeldb/modelview folder

import os, stat
import shutil

nrn_version_folder = "7.4" # in the current folder a folder containing all the expanded models

# copy the json_generator.py's

# first read in the map.txt

map={} # will take accession num key, value is folder name

map_file=open("map.txt",'r')
map_lines = map_file.readlines() # there are currently 388 lines so reasonable to read whole file in
for line in map_lines:
  map_line_list = line[:-1].split(" ") # :-1 removes \n at end, split puts accessionnum in first element, dir if any in next
  if len(map_line_list[1])>1: # if there is a non null folder (more than "\n") associated with the accessionnum
    map[map_line_list[0]] = map_line_list[1]

# now sprinkle the generators
failed_path_list = []
for accession, folder in map.items():
  # accession left out: don't use relative_path = nrn_version_folder+"/"+accession+"/"+folder+"/"+folder
  relative_path = nrn_version_folder+"/"+folder+"/"+folder
  try:
    stuff = os.listdir(relative_path)
    shutil.copy("../../modelview/json_generator/json_generator.py", relative_path) # do the sprinkle
  except:
    stuff = ''
    failed_path_list.append(relative_path)

print("The following paths likely had a problem (perhaps there was nothing there):")
print(failed_path_list)

# finally start all the generators 
#
# to develop code try to start just one
# place a start_time.txt and stop_time.txt in the folder of 
# the real start and stop times.

from timeout_command import timeout_command

skip_over=['64261', '147461','149739']

# also add to skip_over all the files for which a accessionnum.json already exists

import glob
prev_json_files = glob.glob('7.4/*/*/*.json')
json_accessions = []
for json_file in prev_json_files:
  omit_ext=json_file[:-5]
  skip_over.append(omit_ext.split("/")[-1])

for accessionnum, folder in map.items():
  if accessionnum in skip_over:
    print("**** skipping over accessionnum "+accessionnum+", folder: ",folder)
    continue
  # accession left out: relative_path = nrn_version_folder+"/"+folder+"/"+folder
  relative_path = nrn_version_folder+"/"+folder+"/"+folder
  if relative_path in failed_path_list:
    print("**** Not even trying to run this failed path: "+relative_path)
  else:
    # accessionnum = "143604"
    # folder = "singleDendrite"
    # relative_path = "7.4/"+folder+"/"+folder
    # cmd_filename = "./modelview_"+accessionnum+".sh"
    cmd_filename = "./modelview_"+accessionnum+".sh"
    modelviewshell_file = open(cmd_filename,"w")
    modelviewshell_file.write("#!/bin/bash\n")
    modelviewshell_file.write("cd "+relative_path+" && python json_generator.py "+accessionnum+"\n")
    modelviewshell_file.close()
    st = os.stat(cmd_filename)
    os.chmod(cmd_filename, st.st_mode | stat.S_IEXEC)
    cmd_list = [cmd_filename]
    print("Initiating command: "+repr(cmd_list))
    timeout_command(cmd_list,600,relative_path)

print("done")

