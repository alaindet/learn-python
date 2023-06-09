things_str = 'Apples Oranges Crows Telephone Light Sugar'
box = ['Song', 'Frisbee', 'Banana', 'Corn']

things = things_str.split(' ')

while len(things) != 10:
  next_thing = box.pop()
  things.append(next_thing)
  print(f'There are {len(things)} items now')

print(things[1])
print(things[-1])
print(things.pop())
print(' '.join(things))
print('#'.join(things[3:5]))
