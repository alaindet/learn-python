set1 = {1, 2, 3}

set1.add(4)
set1.add(4)
set1.add(4)
print(set1)  # {1, 2, 3, 4}

try:
    set1.remove(3)
    set1.remove(3)  # This raises a KeyError
except KeyError:
    print('You tried to remove a non-existing value from set')
print(set1)  # {1, 2, 4}

set2 = set1.copy()
print(set1 == set2)  # True (equality)
print(set1 is set2)  # False (identity)

set2.clear()  # Remove all elements from set2

history_students = {'Alice', 'Bob', 'Charlie'}
math_students = {'Alan', 'Billy', 'Charlie'}
art_students = {'Sam', 'Rhonda'}

# Union
all_students = history_students | math_students
# Equivalent
# all_students = history_students.union(math_students)
print(all_students)  # {'Billy', 'Alan', 'Alice', 'Bob', 'Charlie'}

cross_students = history_students & math_students
# Equivalent
# cross_students = history_students.intersection(math_students)
print(cross_students)  # {'Charlie'}

# math students and art students are completely disjoint (no intersection)
print(math_students.isdisjoint(art_students))  # True

# .remove() and .discard() are almost the same, except .remove() raises a KeyError
# when the value is not found, while .discard() fails silently
art_students.discard('Sam')
art_students.discard('Nope')  # This fails silently
print(art_students)  # {'Rhonda'}

# Examples for all sets aliased operations
a = {1, 2, 3, 4, 5, 6}
b = {4, 5, 6, 7, 8, 9}

print(a | b) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(a & b) # {4, 5, 6}
print(a - b) # {1, 2, 3}
print(b - a) # {7, 8, 9}
print(a ^ b) # {1, 2, 3, 7, 8, 9}
