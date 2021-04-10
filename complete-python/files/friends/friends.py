from textwrap import dedent
from re import sub
from random import random

INPUT_FILE = 'friends.txt'
OUTPUT_FILE = 'nearby_friends.txt'

friends = []
nearby_friends = []

with open(INPUT_FILE, 'r') as friends_file:
    friends = friends_file.read().split('\n')[:-1]

for friend in friends:
    if (random() > 0.5):
        nearby_friends.append(friend)

nearby_friends_content = '\n'.join(nearby_friends) + '\n'

with open(OUTPUT_FILE, 'w') as nearby_friends_file:
    nearby_friends_file.write(nearby_friends_content)
