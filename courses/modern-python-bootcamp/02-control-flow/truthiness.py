n = 42

# The == operator compares a and b for equal value => EQUALITY
# The "is" operator checks if a and b are THE SAME object in memory => IDENTITY
# The "is" operator is much strictier than ==, so == is recommended

print(n is 42) # This is True, but == is recommended
print(n == 42)

# Natural "falsy" values are
# - Empty objects
# - Empty strings
# - None constant
# - False constant
# - Zero
falsy_values = [{}, '', None, False, 0]
truthy_values = [1, 'hello', True]

for val in falsy_values + truthy_values:
    if val:
        print(f'{val} is truthy')
    else:
        print(f'{val} is falsy')