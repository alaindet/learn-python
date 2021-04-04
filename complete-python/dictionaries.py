people_age = {
  'Alice': 20,
  'Bob': 30,
  'Charlie': 40
}

# print(people_age['Alice'])

# Add/override a key
people_age['Darlene'] = 45

friends = (
  { 'name': 'Alice', 'age': 20 },
  { 'name': 'Bob', 'age': 30 },
  { 'name': 'Charlie', 'age': 40 }
)

print(friends[1]['name'])

some_data = [
  ('Alice', 20),
  ('Bob', 30),
  ('Charlie', 40)
]

some_dict = dict(some_data)

print(some_dict)
