nums = [0, 1, 2, 3, 4]

doubled = [num * 2 for num in nums]

# # Equivalent
# doubled = []
# for num in nums:
#   doubled.append(num * 2)

print(doubled)

letters = ['a', 'b', 'c']
uppercase_letters = [letter.upper() for letter in letters];
print(uppercase_letters)

friend = input('Enter a friend name: ')
friends = ['Alice', 'Bob', 'Charlie']
friends_search = [name.lower() for name in friends]

if friend.lower() in friends_search:
  print(f'{friend.title()} is in your friends\' list')
else:
  print(f'Sorry, {friend.title()} is not your friend, yet')


# With conditionals
ages = [22, 35, 27, 21, 20]
odds = [f'Age is {age}' for age in ages if age % 2 == 1]
print(odds)

# Multiple conditionals
friends = ['Alice', 'Bob', 'Charlie', 'Darlene']
guests = ['Alice', 'Charlie', 'Eric']

friends_at_party = [
    name.title() for name in guests if name.lower() in [
        friend.lower() for friend in friends
    ]
]

print(friends_at_party)
