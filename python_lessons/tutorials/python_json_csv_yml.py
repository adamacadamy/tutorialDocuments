""" 
 1. built in libraries
 2. external libraries
    has to be installed using pip or other python library fetchers
"""

import json # is built in library no need to install
import yaml # is external library you need to install with `pip install pyyaml`
import csv

with open('data.json', 'r') as file:
    data = json.load(file)
    print(type(data))
    print(data)
    
print("------------------------------")  

json_data_to_write = {'name': 'John', 'Age': 30, 'city': 'New York'}
with open('new_data.json', 'w') as file:
    json.dump(json_data_to_write, file)
    
print("------------------------------")  
    
    
with open('data.yml', 'r') as file:
    data = yaml.safe_load(file)
    print(data)
    
print("------------------------------")  

data_to_write = {'name': 'John', 'age': 30, 'city': 'New York'}
with open('new_data.yml', 'w') as file:
    yaml.dump(data_to_write, file)
    
print("------------------------------")  

with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    print(list(csv_reader))
    for row in csv_reader:
        print(row)
    
print("------------------------------")  

csv_data_to_write = [
    ['Name', 'Age', 'City'],
    ['John', '30', 'New York'],
    ['Jane', '25', 'London']
]
        
with open('new_data.csv', 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(csv_data_to_write)
    
    
print("------------------------------")  

with open('new_data.json', 'r') as file:
    data = json.load(file)

print(data) 
with open('json_to_yml.yml', 'w') as file:
    yaml.dump(data, file)

# csv , json , yaml

data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
]

with open('json_to_csv.csv', 'w') as file:
    
    """ 
    data = {'name': 'John', 'Age': 30, 'city': 'New York'}
    header = list(data.keys()) # ['name', 'age', 'city']
    rows =  ['John', 30, 'New York']

    """ 
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)