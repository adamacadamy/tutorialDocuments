
# Lesson: Reading, Writing, and Converting JSON, YAML, and CSV in Python

# 1. Handling JSON Files
# JSON (JavaScript Object Notation) is a popular data format. Python provides the json module to work with JSON data.

import json

# Reading JSON
with open('data.json', 'r') as file:
    data = json.load(file)  # Load JSON data into a Python dictionary
    print(data)

# Writing JSON
data_to_write = {'name': 'John', 'age': 30, 'city': 'New York'}
with open('output.json', 'w') as file:
    json.dump(data_to_write, file, indent=4)  # Write dictionary data to a JSON file with indentation

# 2. Handling YAML Files
# YAML (YAML Ain't Markup Language) is a human-readable data format. You'll need the PyYAML library to work with YAML files.
# Install PyYAML with 'pip install pyyaml'.

import yaml

# Reading YAML
with open('data.yml', 'r') as file:
    data = yaml.safe_load(file)  # Load YAML data into a Python dictionary
    print(data)

# Writing YAML
data_to_write = {'name': 'John', 'age': 30, 'city': 'New York'}
with open('output.yml', 'w') as file:
    yaml.dump(data_to_write, file)  # Write dictionary data to a YAML file

# 3. Handling CSV Files
# CSV (Comma-Separated Values) is a common format for tabular data. Python provides the csv module to work with CSV files.

import csv

# Reading CSV
with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)  # Print each row from the CSV file

# Writing CSV
data_to_write = [
    ['Name', 'Age', 'City'],
    ['John', '30', 'New York'],
    ['Jane', '25', 'London']
]
with open('output.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data_to_write)  # Write the list of rows to the CSV file

# 4. Converting Between JSON, YAML, and CSV
# You can convert between these formats by first reading the data into Python dictionaries or lists and then writing them to the desired format.

# JSON to YAML
with open('data.json', 'r') as json_file:
    data = json.load(json_file)  # Load JSON data

with open('output.yml', 'w') as yaml_file:
    yaml.dump(data, yaml_file)  # Write data to YAML file

# YAML to JSON
with open('data.yml', 'r') as yaml_file:
    data = yaml.safe_load(yaml_file)  # Load YAML data

with open('output.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)  # Write data to JSON file

# CSV to JSON
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    rows = list(csv_reader)  # Convert CSV rows to a list of dictionaries

with open('output.json', 'w') as json_file:
    json.dump(rows, json_file, indent=4)  # Write the list of dictionaries to a JSON file

# JSON to CSV
with open('data.json', 'r') as json_file:
    data = json.load(json_file)  # Load JSON data

with open('output.csv', 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())  # Create a CSV writer with field names from JSON
    csv_writer.writeheader()
    csv_writer.writerows(data)  # Write JSON data to CSV file

# This lesson covers reading, writing, and converting between JSON, YAML, and CSV files. 
# The key idea is to read data into Python structures and then write them out to another format as needed.
