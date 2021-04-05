# is_learning = True

# while is_learning:
#   print('Learning...')
#   ask = input('Are you still learning? ')
#   is_learning = ask == 'yes'
#   if not is_learning:
#     print('You finally mastered it')

people = ['Alice', 'Bob', 'Charlie']

for person in people:
    print(person)

indices = [0, 1, 2, 3, 4]

for _ in indices:
    print('I will repeat 5 times')

for _ in range(5):
    print('I will repeat 5 times again')

start = 2
stop = 20
step = 3
for index in range(start, stop, step):
    print(index)

students = [
    {'name': 'Alice', 'grade': 92},
    {'name': 'Bob', 'grade': 90}
]

for student in students:
    name = student['name']
    grade = student['grade']
    print(f'{name} has a grade of {grade}')

people = {
    'Alice': 20,
    'Bob': 30,
    'Charlie': 40
}

for name, age in people.items():
    print(f'{name} is {age} years old')
    if name == 'Bob':
        break
    else:
        continue

cars = ['ok', 'ok', 'ok', 'ok', 'ko', 'ok', 'ok']
no_faulty_cars = ['ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok']

for status in no_faulty_cars:
    if status == 'ko':
        print('Stopping the production')
        break
    print(f'The car is {status}')
else:
    print('No break was encountered')
