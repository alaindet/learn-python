# TODO: Refactor with context manager approach?

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f'Copying text data from {from_file} to {to_file}')

from_file_object = open(from_file)
from_file_data = from_file_object.read()

to_file_exists = exists(to_file)
print(f'Output file already exists?: {to_file_exists}')

from_file_weight = len(from_file_data)
print(f'Input file weight: {from_file_weight} bytes')


print(f'Press RETURN to write output file, or CTRL+C to abort')
input()

to_file_object = open(to_file, 'w')
to_file_object.write(from_file_data)

print(f'Data from {from_file} to {to_file} written')

from_file_object.close()
to_file_object.close()
