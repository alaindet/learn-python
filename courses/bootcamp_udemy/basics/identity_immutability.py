a = 42
b = a
print(
    'b is reference to a: ',
    a is b, # True
    id(a) == id(b), # Equivalent (True)
)

a, b = 69, 69
print(
    'a and b have the same literal value: ',
    a is b, # True
    id(a) == id(b), # Equivalent (True)
)

a, b = 10, 20
print(
    'a and b have different literal value: ',
    a is b, # False
    id(a) == id(b), # Equivalent (False)
)

# Changing immutable values re-assigns them
a = 1
print(id(a)) # 140730738533160
a += 1
print(id(a)) # 140730738533192 (it's different!)

# This is a mutable type
nums = [1, 2, 3]
print(id(nums)) # 2627520396032
nums.append(4)
print(id(nums)) # 2627520396032 (it's the same!)

nums2 = nums.copy()
print(id(nums2)) # 2485951359040 (it's different!)
print(nums == nums2) # True (compares values?)
print(nums is nums2) # False (compares addresses)

print({ 'name': 'a' } == { 'name': 'a' }) # True
print({ 'name': 'a' } is { 'name': 'a' }) # False
