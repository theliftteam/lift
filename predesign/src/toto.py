import json

with open('../data/data1.txt') as data_file:
    data = json.load(data_file)
    
print(data["root"]["dimensions"]["tank"]["radius"])