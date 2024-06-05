def create_adders():
    adders = []
    for n in range(1, 3):
        adders.append(lambda x: x + n)
    return adders


adders = create_adders()

# This does not work as intended, the cell is the same, but it should be different!

# (<cell at 0x00000239871CF490: int object at 0x00007FF9E54B5DE0>,)
print(adders[0].__closure__)
print(adders[0].__code__.co_freevars)  # ('n',)

# (<cell at 0x00000239871CF490: int object at 0x00007FF9E54B5DE0>,)
print(adders[1].__closure__)
print(adders[1].__code__.co_freevars)  # ('n',)


def create_better_adders():
    adders = []
    for n in range(1, 3):
        adders.append(lambda x, y=n: x + y)
    return adders


# Note:
# y=n above in the code means the default value of y is n and is calculated
# upon DEFINITION of the lambda (inside the loop)
# Also, n is just used to initial the default value, but there' no reference to
# it inside the lambda and so there's no closure (check the .__closure__ below)
better_adders = create_better_adders()
print(better_adders[0].__closure__)  # None
print(better_adders[0].__code__.co_freevars)  # ()

print(better_adders[1].__closure__)  # None
print(better_adders[1].__code__.co_freevars)  # ()
