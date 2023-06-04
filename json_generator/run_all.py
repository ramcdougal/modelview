import os
from run_protocols import protocol
import filecmp
import json
import sys

if len(sys.argv) >= 2:
    # (soft) time_limit in seconds; hard time limit is 30s later
    time_limit = float(sys.argv[1])
else:
    time_limit = None

with open('stochastic_list.txt', 'w') as f:
    pass

failed_list = []

def attempt(key):
    if time_limit is None:
        os.system('python go.py %s' % key)
    else:
        os.system('timelimit -t%g -T30 python go.py %s' % (time_limit, key))


for key in protocol:
    attempt(key)
    os.system('mv %s.json %s.old' % (key, key))
    attempt(key)
    
    # if the two versions are not the same, then flag as stochastic
    try:
        if not filecmp.cmp('%s.json' % key, '%s.old' % key):
            with open('%s.old' % key) as f:
                data = json.loads(f.read())    
            data['stochastic'] = True
            with open('%s.json' % key, 'w') as f:
                f.write(json.dumps(data))
            with open('stochastic_list.txt', 'a') as f:
                f.write('%s\n' % key)
        os.remove('%s.old' % key)
    except OSError:
        failed_list.append(key)

if len(failed_list):
    print('some modelviews failed:')
    print(failed_list)
else:
    print('all modelviews generated successfully')
