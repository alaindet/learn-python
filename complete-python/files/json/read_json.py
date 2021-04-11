import json

content = None

with open('friends.json', 'r') as file:
    content = json.load(file)

print(content['friends'][0])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

with open('cars.json', 'w') as file:
    json.dump({'cars': cars}, file)
