""" 
 1. built in libraries
 2. external libraries
    has to be installed using pip or other python library fetchers
"""

import json # is built in library no need to install
import yaml # is external library you need to install with `pip install pyyaml`
import csv

""" 
r = read
w = write
"""
with open('data.json', 'r') as data_json_file: 
    data = json.load(data_json_file)
    print(data)
    print(type(data))


print("------------------------------") 
 
json_data_to_write = [
    
    {'name': 'John', 'Age': 30, 'city': 'New York'},
    {'name': 'Adam', 'Age': 30, 'city': 'Berlin'}
]

""" 
w checks if there is a file already if there is none it creates one
"""
with open('new_data.json', 'w') as  new_data_json_file:
    json.dump(json_data_to_write, new_data_json_file)
    
print("------------------------------") 

with open('data.yml', 'r') as data_yml_file:
    data = yaml.safe_load(data_yml_file)
    print(data)

yaml_data_to_write = [
    
    {'name': 'John', 'Age': 30, 'city': 'New York'},
    {'name': 'Adam', 'Age': 30, 'city': 'Berlin'}
]

print("------------------------------") 

with open('new_data.yml', 'w') as nw_data_yml_file:
    yaml.dump(yaml_data_to_write, nw_data_yml_file)
    
print("------------------------------") 

with open('data.csv', 'r') as data_csv_file:
    print(data_csv_file.read())
    csv_reader = csv.reader(data_csv_file)
    print(list(csv_reader))
    for row in csv_reader:
        print(row)
    
csv_data_to_write = [
    ['Name', 'Age', 'City'],
    ['John', '30', 'New York'],
    ['Jane', '25', 'London']
]

with open('new_data.csv', 'w') as new_data_csv_file:
    csv_writer = csv.writer(new_data_csv_file)
    csv_writer.writerows(csv_data_to_write)
    
print("------------------------------") 
data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
]

with open('json_to_csv.csv', 'w') as json_to_csv_file:
    # fieldnames = list(data[0].keys())
    fieldnames = ['name', 'age', 'city']
    print(fieldnames)
    writer = csv.DictWriter(json_to_csv_file, fieldnames)
    writer.writeheader()
    writer.writerows(data)