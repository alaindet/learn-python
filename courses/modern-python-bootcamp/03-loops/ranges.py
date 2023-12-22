# Ranges are objects of class 'range'
# Range objects are iterables, that's why they work with the 'for' keyword
print(range(1, 3), type(range(1, 3))) # range(1, 3) <class 'range'>

# Ranges (one argument: to, from is implicitly 0)
# Prints: 0, 1, 2, 3, 4
for x in range(5):
    print(f'One arg: {x}')

# Ranges (two arguments: from, to)
for x in range(10, 15):
    print(f'Two args: {x}')

# Range (three arguments: from, to, step)
for x in range(0, 10, 2):
    print(f'Three args: {x}')

# Range with a negative step (prints all numbers between 10 and 1)
for x in range(10, 0, -1):
    print(f'{x}...')
print('Happy new year!') 

# Turn a range object in a simple list
r = range(10)