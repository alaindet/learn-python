# Sets do not have order and cannot have duplicates
# They are used for quick comparisons

art_friends = {'Alice', 'Bob'}
science_friends = {'Charlie', 'Darlene'}

art_friends.add('Charlie')
art_friends.remove('Bob')
# print(art_friends)

set1 = {'Alice', 'Bob', 'Charlie'}
set2 = {'Anne', 'Charlie'}

exclusive_in_set1 = set1.difference(set2)
# print(exclusive_in_set1)

exclusive_in_set2 = set2.difference(set1)
# print(exclusive_in_set2)

not_in_both = set1.symmetric_difference(set2)
# print(not_in_both)

intersection = set1.intersection(set2)
# print(intersection)

everyone = set1.union(set2)
# print(everyone)
