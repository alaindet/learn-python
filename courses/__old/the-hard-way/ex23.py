from sys import argv

script, input_encoding, error = argv
encoding = 'utf-8'


def print_line(line, encoding, errors):
    sanitized_line = line.strip()
    raw_bytes = sanitized_line.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    print(raw_bytes, '<===>', cooked_string)


def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


languages = open('ex23.txt', encoding=encoding)
main(languages, input_encoding, error)
