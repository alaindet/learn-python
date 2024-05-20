"""
Peephole optimizations refer to code optimizations the Python compiler does to
make the runtime faster by analyzing the code and pre-calculating something
"""

import string
import time

def fn():
    a = 24 * 60
    b = (1, 2) * 5
    c = 'abc' * 3
    d = 'ab' * 20
    e = 'long string ' * 3
    f = ['a', 'b'] * 3

# This prints the compiled "constants" that the compiler computed based on code
print(fn.__code__.co_consts)
# It prints
# (None, 1440, (1, 2, 1, 2, 1, 2, 1, 2, 1, 2), 'abcabcabc',
#    'abababababababababababababababababababab', 'long string long string long string ',
#    'a', 'b', 3)

# Here, all variables inside the "fn" function scope got computed as constants by
# the Python compiler

print(string.ascii_letters) # defghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

char_list = list(string.ascii_letters)
print(char_list)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
#    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
#    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
#    'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

char_tuple = tuple(string.ascii_letters)
print(char_tuple)
# ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
#    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
#    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
#    'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

# NOTE: Sets are NOT ordered
char_set = set(string.ascii_letters)
print(char_set)
# {'n', 'q', 'W', 'k', 's', 'V', 'R', 'L', 'G', 'J', 'C', 'e', 'h', 'o', 'l',
#    'j', 'p', 'x', 'F', 'N', 'T', 'A', 'd', 'b', 'f', 'z', 'H', 'U', 'i', 'v',
#    'w', 'E', 'c', 'a', 'O', 'M', 'P', 'g', 'Q', 'S', 'D', 'I', 'y', 'r', 'B',
#    'Z', 'K', 't', 'u', 'Y', 'm', 'X'}

# This is very polymorphic as it works with multiple different data structures
# lists, tuples, dictionaries, sets
def membership_test(n, letters):
    for i in range(n):
        if 'z' in letters:
            pass

start = time.perf_counter()
membership_test(10_000_000, char_list)
end = time.perf_counter()
print('list: ', end - start) # list:  2.226990499999374

start = time.perf_counter()
membership_test(10_000_000, char_tuple)
end = time.perf_counter()
print('tuple: ', end - start) # tuple:  2.361669100006111

# Searching in a set is ~10x faster than searching in a list or tuple
start = time.perf_counter()
membership_test(10_000_000, char_set)
end = time.perf_counter()
print('set: ', end - start) # set:  0.26111819996731356