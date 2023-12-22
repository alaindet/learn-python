age = 42
name = 'The answer'

print(age == 42) # Outputs: True
print(age > 69) # Outputs: False
print(len(name) != 10) # Outputs: False

a_list = [1, 2, 3, 4] # A list
a_tuple = ('Dan', 42, 'London') # A tuple
a_set = {1, 2, 3} # A set
print(type(a_set)) # Outputs: <class 'set'>
a_frozen_set = frozenset({1, 2, 3}) # A frozen set
print(type(a_frozen_set)) # Outputs: <class 'frozenset'>
a_dict = { name: 'Dan', age: 42 } # A dictionary