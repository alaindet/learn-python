friends = ['Rolf', 'Bob', 'Jen', 'Anne']
time_since_seen = [3, 7, 15, 11]

# long_time_no_see = {
#     friends[i]: time_since_seen[i]
#     for i in range(len(friends))
#     if time_since_seen[i] > 5
# }

long_time_no_see = dict(zip(friends, time_since_seen))

print(long_time_no_see)
