import csv

with open('friends.csv', 'r') as file:
    reader = csv.DictReader(file)
    for line in reader:
        print('\n===\n')
        for key in line.keys():
            print(f'{key}: {line[key]}')
    print('\n===\n')
