a = [1, 2, 3]
b = [1, 2, 3]

# Test for equality
print(a == b) # True

# Here, a and b are "equal" even though they occupy two different positions
# in memory

# Test for identity
print(a is b) # False

# The "is" operator tests for identity, so it assures a and b point to the same
# position in memory. Hence, "a is b" is False, since a and b are equal but
# *DO NOT* point to the same position in memory

c = b
print(b is c) # True

# Here, we assigned the value of b to the new variable c, so they *ARE* identical
# since they point to the same position in memory

# Quirk: simple literal values test True for identity since they are
# constant objects in memory
d = 42
e = 42
print(d is e) # True