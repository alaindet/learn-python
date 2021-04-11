COLUMN_SEPARATOR = ','
ROW_SEPARATOR = '\n'

friends = []
csv_content = []

with open('friends.csv', 'r') as csv_file:
    csv_content = csv_file.read()

# Safer alternative 
# lines = [ line for line in csv_content.split(ROW_SEPARATOR) if line != '' ]

lines = csv_content.split(ROW_SEPARATOR)[:-1]
headers_line = lines[0]
content_lines = lines[1:]

headers = headers_line.split(COLUMN_SEPARATOR)
content = [ line.split(COLUMN_SEPARATOR) for line in content_lines ]

for row in content:
    friend = {}
    for header, column in zip(headers, row):
        friend[header] = column
    friends.append(friend)

print(friends)
