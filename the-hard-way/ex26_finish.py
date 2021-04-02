from sys import argv

script, filename = argv

age = input('How old are you? > ')
height = input('How tall are you? (cm) > ')
weight = input('How much do you weight? (kg) > ')
print(f"So, you're {age} old, {height} cm tall and {weight} kg heavy.")
txt = open(filename)
print("Here's your file {filename}:")
print(txt.read())
print('Type the filename again:')
file_again = input('> ')
txt_again = open(file_again)
print(txt_again.read())

print("Let's practice everything.")
print("You'd need to know 'bout escapes  with \\ that do \n newlines and \t tabs.")

poem = """
\tThe lovely world\n
with logic so firmly planted\n
cannot discern the needs of love\n
nor comprehend passion from intuition\n
and requires an explanation\n
where there is none.
"""

print('--------------')
print(poem)
print('--------------')


five = 10 - 2 + 3 - 6
print(f'This should be five: {five}')

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars * 100
    return [jelly_beans, jars, crates]


start_point = 10000
jelly_beans, jars, crates = secret_formula(start_point)

print("With a starting point of: {}".format(start_point))
print(f"We'd have {jelly_beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)

print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

people = 20
cats = 30
dogs = 15


if people < cats:
    print ('Too many cats! The world is doomed!')

if people > cats:
    print('Not many cats! The world is saved!')

if people < dogs:
    print('The world is drooled on!')

if people > dogs:
    print('The world is dry!')

dogs += 5

if people >= dogs:
    print('People are greater than or equal to dogs')

if people <= dogs:
    print('People are less than or equal to dogs')

if people == dogs:
    print('People are equal to dogs')
