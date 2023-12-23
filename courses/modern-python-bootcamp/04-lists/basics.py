# A list of the same type
scores = [8, 6, 7, 10, 9, 4, 6]
students = ['Alice', 'Bob', 'Charlie', 'Damon', 'Ester', 'Fleur', 'Gaston']

# A list of different types
info = [
    'John',
    'Doe',
    30,
    {'favorite_color': 'blue'},
    ['Fred', 'Joanne', 'Daliah'],
]

# Indexing
print(scores[0], scores[-1])  # 8 6
print(info[0], info[-1][0])  # 'John' 'Fred'

# Comparison
friends = info[-1]
print('Joanne' in friends)  # True

# Casually looping over a list
for info_item in info:
    print(info_item)

# Looping with index
for index, student in enumerate(students, start=1):
    print(f'{index}) {student}')

# Looping at the same time
for student, score in zip(students, scores):
    print(f'{student} scored {score:02}/10')

# Looping with a while (not recommended)
i = 0
while i < len(scores):
    print(scores[i])
    i += 1
