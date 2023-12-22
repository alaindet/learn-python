file = open('data.txt', 'r')
file_content = file.read()
print(f'File content: {file_content}')
file.close()

new_content = input('Enter a name to write to file: ')

# 'w' mode overwrites the file content
file_to_write = open('data.txt', 'w')

file_to_write.write(new_content)
file_to_write.close()
