"""\
List methods
https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
"""

list1 = [1, 2, 3]
list1.append(4)
print(list1)  # [1, 2, 3, 4]

list2 = [5, 6]
list1.extend(list2)
print(list1)  # [1, 2, 3, 4, 5, 6]

# Insert a value in the middle of the list
list2.insert(1, 10)

# This DOES NOT raise an error, it appends to the end instead
out_of_bound_index = len(list2) + 42
list2.insert(out_of_bound_index, 11)
print(list2)

# This searches and removes a value and IT DOES raise an error if no value is found
try:
    list2.remove(11)  # This works
    list2.remove(123)  # This fails
except ValueError:
    print('a ValueError was raised')

try:
    list3 = [1, 2, 3]
    list3.pop(1)  # Remove at given index
    print(list3)  # Prints [1, 3]
    list3.pop()  # Remove from end
    list3.pop()  # This fails as it's an empty list already
except IndexError:
    print('an IndexError was raised')

list4 = [1, 2, 3, 4]
list4.clear()
print(list4)  # []

try:
    list5 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    print(list5.index('c'))  # 2
    print(list5.index('d', 2, 5))  # Restricts the search to a slice, prints 3
    print(list5.index('z'))  # Fails
except ValueError:
    print('a ValueError was raised')

print(['a', 'b', 'c', 'd', 'a', 'a', 'd'].count('a'))  # Prints 3
print([11, 22, 33, 44, 55].count(42))  # Prints 0

list6 = [22, 44, 33, 11, 32]
list6.sort()
print(list6)  # Prints [11, 22, 32, 33, 44]

list7 = [3, 1, 2]
list7.reverse()
print(list7)  # Prints [2, 1, 3]
