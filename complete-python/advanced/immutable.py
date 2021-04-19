print('\n# Example 1')

friends_last_seen = {
    'Alice': 10,
    'Bob': 20,
    'Charlie': 30
}

# Print the physical address of the "friends_last_seen" dictionary
print(id(friends_last_seen))

friends_last_seen = {
    'Alice': 10,
    'Bob': 20,
    'Charlie': 30
}

# Doing it again assigns a different address
print(id(friends_last_seen))

friends_last_seen['Alice'] = 'ages'

# Id does not change now, since a dictionary is a mutable data type
print(id(friends_last_seen))

# Immutable data types
# Integers
# Floats
# Strings
# Tuples

# With lists, ID does not change
print('\n# Example 2')
people = ['Alice', 'Bob']
print(id(people))
people.append('Charlie')
print(id(people))

print('\n# Example 3')

friends_last_seen = {
    'Alice': 10,
    'Bob': 20,
    'Charlie': 30
}


def see_friend(friends, name):
    """
    Complex data types, like "friends" argument here, are passed by reference
    """
    print('Inside 1   ', id(friends))
    print('Inside 2   ', friends is friends_last_seen)
    friends[name] = 0


print('Outside 1', id(friends_last_seen))
see_friend(friends_last_seen, 'Alice')

# Same as "Outside 1" since see_friends is passed a reference
print('Outside 2', id(friends_last_seen))


print('\n# Example 3')
age = 30
def increase_age(curr_age):
    curr_age += 1
print(id(age))
increase_age(age)
print(id(age))

print('\n# Example 4')
primes = [2, 3, 5]
print(id(primes))

primes += [7, 11] # Equivalent to primes.__iadd__([7, 11])
print(id(primes)) # This has identical ID

primes = primes + [7, 11]
print(id(primes)) # This changes ID