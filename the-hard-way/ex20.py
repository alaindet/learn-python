from sys import argv
from os.path import exists

script, input_file_path = argv
output_lines = []


def print_line(line_number, line_content):
    return f'#{line_number} {line_content}'


# TODO: Add error handling?
with open(input_file_path) as input_file:
    line_number = 1
    for line in input_file:
        output_line = print_line(line_number, line)
        output_lines.append(output_line)
        line_number += 1
    output = ''.join(output_lines)
    print(output)
