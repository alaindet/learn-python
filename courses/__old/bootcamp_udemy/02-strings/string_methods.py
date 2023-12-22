# This displays all the methods for strings
print(dir(str))
# Currently prints 81 methods!

# This displays an help about the given method
help(str.replace)
# replace(self, old, new, count=-1, /)
#     Return a copy with all occurrences of substring old replaced by new.
#     
#       count
#         Maximum number of occurrences to replace.
#         -1 (the default value) means replace all occurrences.
#     
#     If the optional argument count is given, only the first count occurrences are
#     replaced.

word = 'Hello'
# Note that .upper and .lower create a copy
print(word.upper(), word.lower(), word) # HELLO hello Hello

s = 'This is a String'
print(s.upper()) # THIS IS A STRING
print(s.lower()) # this is a string
print('  192.168.1.1      '.strip()) # 192.168.1.1
print('$$Hello$$$$'.strip('$')) # Hello
print(s.replace('String', 'word')) # This is a word
print(s.count('s')) # 2
print(s.lower().count('s')) # 3
# vvv By default, splits uses whitespace characters as split boundaries
print(s.split()) # ['This', 'is', 'a', 'String']
print('192.168.1.1'.split('.')) # ['192', '168', '1', '1']
print('@'.join(['a', 'b', 'c'])) # a@b@c
# vvv Returns the first index of the first appearance
print('aa bb cc aa bb cc'.find('bb')) # 3
print('abcdef'.find('xx')) # -1
print('c' in 'abcdef') # True
print('x' not in 'abcdef') # True