import os
from run_protocols import protocol

# start with an empty file
with open('model_stats.csv', 'w') as f:
    pass

for key in protocol:
    os.system('python go_count_stats.py %s' % key)
