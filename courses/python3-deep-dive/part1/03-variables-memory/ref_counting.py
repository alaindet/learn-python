import ctypes

def ref_count(address: int):
    return ctypes.c_long.from_address(address).value

a = [1, 2, 3]

# print(id(a)) # 2557998780672

print(ref_count(id(a))) # 1

# getrefcount always shows references count + 1 (itself)
# import sys
# print(sys.getrefcount(a)) # 2

b = a
print(ref_count(id(a))) # 2

c = a
print(ref_count(id(a))) # 3

# The ref counting goes back to 2 since b is not referencing a anymore
b = 3
print(ref_count(id(a))) # 2

# The ref counting goes back to 1 since c is not referencing a anymore
c = 10
print(ref_count(id(a))) # 1

# WATCH THIS
a_id = id(a)

# Here, ref counting for "a" goes down to zero and the garbage collector frees
# the address of the variable "a"
a = None

# Ref counting
print(ref_count(a_id)) # 0