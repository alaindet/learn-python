# Print out numbers from 1 to 100 (including 100).
# But, instead of printing multiples of 3, print "Fizz"
# Instead of printing multiples of 5, print "Buzz"
# Instead of printing multiples of both 3 and 5, print "FizzBuzz".

for number in range(1, 101):
    output = ''
    if number % 3 == 0:
        output += 'Fizz'
    if number % 5 == 0:
        output += 'Buzz'
    if len(output):
        print(output)
        continue
    print(number)
