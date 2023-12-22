a = 1
b = 2

print(a == b) # False
print(a != b) # True
print(a > b)  # False
print(a >= b) # False
print(a < b)  # True
print(a <= b) # True

print('a' < 'b') # True (Comparison happens on alphabetical order)

name = 'Alice'
age = 20
is_sad = False

if (
    (name == 'Alice' or name == 'Bob')
    and age > 18
    and not is_sad
):
    print(f'Hi, {name}!')

print(True and False) # False
print(True or False) # True
print(not False) # True