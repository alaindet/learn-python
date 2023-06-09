import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(range(22), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)

winning_player = { 'name': None, 'numbers_count': 0 }
for player in players:
    lucky_numbers = lottery_numbers.intersection(player['numbers'])
    luck_numbers_count = len(lucky_numbers)
    if luck_numbers_count > winning_player['numbers_count']:
        winning_player['name'] = player['name']
        winning_player['numbers_count'] = luck_numbers_count

if winning_player['name'] == None:
    print('No one won')
    exit()

name = winning_player['name']
prize = 100 ** winning_player['numbers_count']
print(f'{name} won {prize}')
