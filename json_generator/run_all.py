import os
from run_protocols import protocol
import filecmp
import json

with open('stochastic_list.txt', 'w') as f:
    pass

failed_list = []

for key in protocol:
    os.system('python go.py %s' % key)
    os.system('mv %s.json %s.old' % (key, key))
    os.system('python go.py %s' % key)
    
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
    print 'some modelviews failed:'
    print failed_list
else:
    print 'all modelviews generated successfully'
