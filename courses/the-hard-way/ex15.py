from sys import argv

script, filename = argv
txt = open(filename)

print(f'Here is your file {filename}: ')
print('\n===\n')
print(txt.read())
print('===\n')
print('Type the filename again: ')
file_again = input('> ')
txt_again = open(file_again)
print('\n===\n')
print(txt_again.read())
print('===\n')
