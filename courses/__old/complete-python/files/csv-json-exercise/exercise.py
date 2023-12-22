"""
This is a CSV to JSON converter. It assumes the CSV file is called "data", it
exists and it is valid. Outputs an equivalent "data.json" file in the same folder
"""

import csv
import json

INPUT_FILE = 'data.csv'
OUTPUT_FILE = 'data.json'

data = []

with open(INPUT_FILE, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for line in reader:
        data.append(line)

with open(OUTPUT_FILE, 'w') as json_file:
    json.dump(data, json_file)

print(f'Input CSV file "{INPUT_FILE}" converted to JSON file "{OUTPUT_FILE}"')
