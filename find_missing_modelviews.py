from urllib.request import urlopen
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup, Comment

# get list of neuron models
neuron_models = []
neuron_models_html = urlopen('http://senselab.med.yale.edu/modeldb/ModelList.asp?id=1882').read()
neuron_models_soup = BeautifulSoup(neuron_models_html, 'html5lib')
for link in neuron_models_soup.find_all('a'):
    href = link.get('href')
    if href is not None and 'ShowModel.asp?model=' in href:
        model_id = int(href.split('=')[1])
        neuron_models.append(model_id)

neuron_models.sort()

def does_modelview_exist(model_id):
    try:
        urlopen('http://senselab.med.yale.edu/modeldb/modelview/%d.json' % model_id)
    except urllib.error.HTTPError:
        return False
    return True

has_modelview = []
no_modelview = []

for model in neuron_models:
    if does_modelview_exist(model):
        has_modelview.append(model)
    else:
        no_modelview.append(model)


print('modelview exists for:')
print(has_modelview)
print()
print('modelview does not exist for:')
print(no_modelview)

