# The reason why "a" and "b" have the same reference, is because the CPython runtime
# creates and caches number objects (in old versions, from -6 to 256), for performance
# given how how much these numbers are user
a = 999999
b = 999999
print(a is b) # True

# Python interns strings and creates singleton instances to speed up string
# comparisons. By default, strings getting interned are identifiers and many 
# other that could be used as identifiers or constants

# It is possible to manually intern strings to optimize the runtime for memory
# if you know those interned strings get compared many times
# Ex.: interning frequent words in the english literature when processing texts

# Manually interning strings, however, is discouraged
import sys

a = sys.intern('the quick brown fox')
b = sys.intern('the quick brown fox')

print('a == b', a == b) # True
print('a is b', a is b) # True --> This is WAY FASTER