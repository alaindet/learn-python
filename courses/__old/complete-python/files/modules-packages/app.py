# # Method 1: Import everything
# import utils.filesystem_helpers
# filesystem_helpers.save_to_file('Alain', 'data.txt')
# print(filesystem_helpers.read_from_file('data.txt'))

# # Method 2: Import one thing at a time
# from utils.filesystem_helpers import save_to_file, read_from_file
# save_to_file('Alain', 'data.txt')
# print(read_from_file('data.txt'))
