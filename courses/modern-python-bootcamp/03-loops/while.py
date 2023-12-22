# This causes havoc if you don't break it
# while True:
    # This runs forever!

n = 0

while True:
    n += 1
    if n == 5:
        break

print('Pfiuuu! We made it out of the infinite while. N =', n)

# This exits only with the correct answer
while True:
    answer = input('What is the answer? > ')
    if answer == '42':
        print('You are correct!')
        break
    print('Uh oh, looks like you\'re not a Hitchhiker, try again!')

# Keep asking the user for an integer number
while True:
    user_input = input('Enter a valid integer > ')
    try:
        i = int(user_input)
        print('You entered an integer:', i)
        break
    except ValueError:
        print('Invalid input passed:', user_input)