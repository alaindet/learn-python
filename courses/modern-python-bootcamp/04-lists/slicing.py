"""\
Slicing means to extract a sublist from a list. Works on any sequence, like strings
"""

# Slicing creates a copy
# As you can see, slist is a slice of list but changing values on list later does
# not affect slist
list = [1, 2, 3, 4]
slist = list[:2]
print(list, slist)  # [1, 2, 3, 4] [1, 2]
list[0] = 99
print(list, slist)  # [99, 2, 3, 4] [1, 2]

# Slicing between two indices
# Includes element with index = 0, but does *NOT* include elements with index = 3
slist1 = list[0:3]  # It reads "from index 0 up to index 3"

# Omit start index (implicitly = 0)
slist2 = list[:3]  # Equivalent to list[0:3]

# Omit end index (implicitly len(list))
slist3 = list[1:]  # Equivalnet to list[1:len(list)]

# Omit all, used for shallow copying
slist4 = list[:]

# As you can see, [:] performs a shallow copy, since the dict literal inside the
# first list is the same for both lists!
person = {'name': 'Alain'}
list2 = [person]
slist5 = list2[:]
list2[0]['name'] = 'John'
print(slist5[0]['name'])  # Prints 'John'

# Slicing with a step
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = nums[::2]
print(evens)  # [0, 2, 4, 6, 8]
odds = nums[1::2]
print(odds)  # [1, 3, 5, 7, 9]

# Copy the slice from the end!
countdown = nums[::-1]
print(countdown)  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(nums[2::-1])
