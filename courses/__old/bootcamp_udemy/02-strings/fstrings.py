fname = 'Mario'
lname = 'Rossi'
color = 'Yellow'

print('Hello ' + fname + ' ' + lname + ', it seems ' + color + ' is your favorite color')
print(f'Hello {fname} {lname}, it seems {color} is your favorite color') # Equivalent

# Expressions too!
# Note: type casting the expression to string is implicit
print(f'2 x 5 = {2 * 5}')

# Formatting the expression
# The :.2f part is the formatting suffix
# Formatting also takes care of rounding for floats
# Formatters mimic what you tipically do with printf() in C and C-like languages
print(f'10 / 6 = {10 / 6:.2f}') # 10 / 6 = 1.67

