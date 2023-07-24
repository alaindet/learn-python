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