import urllib2
from bs4 import BeautifulSoup
from matplotlib import pyplot

# load the list of models by simulator
all_models_html = urllib2.urlopen('http://senselab.med.yale.edu/modeldb/FindBySimulator.asp').read()
all_models_soup = BeautifulSoup(all_models_html, 'html5lib')

table = all_models_soup.find_all('table')[1]

# collect the numbers for each simulator
stats = {}
for i, row in enumerate(table.find_all('tr')[1:]):
    tds = row.find_all('td')
    stats[tds[0].text] = int(tds[-1].text)

def get_count(sim):
    return stats.get(sim, 0) + stats.get(sim + ' (web link to model)', 0)

sims = ('All Others', 'NEURON', 'MATLAB',  'C or C++ program', 'XPP','GENESIS',  'Python', 'Brian',  'FORTRAN')
val = [get_count(sim) for sim in sims]
pos = [i + 0.5 for i in xrange(len(sims))]

print val


# set all others
val[0] = sum(v for v in stats.values()) - sum(val)
pos[0] -= 0.5

pyplot.barh(pos, val, color='black', align='center')
pyplot.yticks(pos, sims)
pyplot.xlabel('Number of models in ModelDB')
pyplot.ylim(pos[0] - 0.5, pos[-1] + 0.5)
#pyplot.grid()
pyplot.show()
