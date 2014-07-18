import urllib2
from bs4 import BeautifulSoup
from matplotlib import pyplot
import os

# in Ubuntu, can get this via: sudo apt-get install python-statsmodels
import statsmodels.api as sm

# load the list of models by simulator
all_models_html = urllib2.urlopen('http://senselab.med.yale.edu/modeldb/ListByModelName.asp?c=19&lin=-1').read()
all_models_soup = BeautifulSoup(all_models_html, 'html5lib')


def download_zip(model_id):
    zip_file = urllib2.urlopen('http://senselab.med.yale.edu/ModelDB/eavBinDown.asp?o=%d&a=23&mime=application/zip' % model_id).read()
    if zip_file == 'File not found!':
        # attribute 311 instead of 23 if an "alternate" version of the model
        zip_file = urllib2.urlopen('http://senselab.med.yale.edu/ModelDB/eavBinDown.asp?o=%d&a=311&mime=application/zip' % model_id).read()
        if zip_file == 'File not found!':
            raise Exception('no zip')
    with open('zipfile.zip', 'wb') as f:
        f.write(zip_file)

# download all the zips, collect the total number of files and the size of
# all files
table = all_models_soup.find_all('table')[1]
sizes = []
lengths = []
for link in table.find_all('a'):
    href = link.get('href')

    print link.text
    try:
        download_zip(int(href.split('=')[1]))
    except:
        # no zip (web link to model)
        lengths.append(0)
    else:
        os.system('zipinfo zipfile.zip > zipfile.txt')
        with open('zipfile.txt') as f:
            lines = [line.strip() for line in f]
        # remove header and trailing lines
        lines = lines[2 : -1]
        
        file_count = 0
        for line in lines:
            if line[-1] != '/':
                file_count += 1
                data = line.split()
                size = int(data[3])
                sizes.append(size)
        lengths.append(file_count)

    #if len(lengths) > 40: break

pyplot.figure()
ecdf = sm.distributions.ECDF(sizes)
x = sorted(set(sizes))
y = ecdf(x) * 100
pyplot.step(x, y, color='black', lw=3)
pyplot.xlabel('Upper Bound on File Size in Bytes')
pyplot.ylabel('Percent of Files in ModelDB')
pyplot.xscale('log')
pyplot.xlim(10, max(x))

pyplot.figure()
ecdf = sm.distributions.ECDF(lengths)
x = sorted(set(lengths))
y = ecdf(x) * 100
pyplot.step(x, y, color='black', lw=3)
pyplot.xlabel('Upper Bound on Number of Model Files')
pyplot.ylabel('Percent of Models in ModelDB')
pyplot.xscale('log')
pyplot.xlim(1, max(x))
pyplot.show()
