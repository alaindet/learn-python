adders = []
for n in range(1, 4):
    adders.append(lambda x: x + n)

# They all print 13!
# This is because n is bound at each iteration but it *evaluated* when called
# n is a variable that gets re-assigned for each iteration
for adder in adders:
    print(adder(10))

# A better way
better_adders = []
for n in range(1, 4):
    def adder(n):
        return lambda x: x + n
    better_adders.append(adder(n))

for better_adder in better_adders:
    print(better_adder(10)) # Prints 11, 12, 13...


def create_incrementer(initial_value: int, step: int):
    """Notice "step" is an argument, not a declared variable in here"""
    value = initial_value

    def incrementer():
        nonlocal value
        value += step
        return value
    
    return incrementer

inc = create_incrementer(10, 5)
print(inc()) # 15
print(inc()) # 20
print(inc()) # 25
print(inc()) # 30
