# Set comprehension
friends = ['Rolf', 'ruth', 'charlie', 'Jen']
guests = ['jose', 'Bob', 'Rolf', 'Charlie', 'michael']

friends_ = {friend.lower() for friend in friends}
guests_ = {guest.lower() for guest in guests}
present_friends = {name.title() for name in friends_.intersection(guests_)}
print(present_friends)


# Dictionary comprehension
friends = ['Rolf', 'Bob', 'Jen', 'Anne']
time_since_seen = [3, 7, 15, 11]

long_time_no_see = {
  friends[i]: time_since_seen[i]
  for i in range(len(friends))
  if time_since_seen[i] > 5
}
print(long_time_no_see)
