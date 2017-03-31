import json
from pprint import pprint
data_file = open('files/equipments.json')
data = json.load(data_file)

pprint(data)


