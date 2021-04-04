import mylib

mylib.apples()
print(mylib.tangerine)

instance = mylib.MyLib()
instance.apples()
print(instance.tangerine)


# The syntax below explicits a new-style class
# Which is default in Python3 and optional in Python2
# It means "class Song is inheriting from object", which is
# the base class from which any class is extended
#
# class Song(object):

class Song:

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self, name = 'INSERT_NAME_HERE'):
        print(f'This song is for {name}')
        for line in self.lyrics:
            print(line)


happy_birthday = Song([
    'Happy birthday to you',
    'And I sure',
    'You know the rest'
])

bulls_on_parade = Song([
    'The rally around the family',
    'With pockets full of shells'
])

happy_birthday.sing_me_a_song('Alain')
bulls_on_parade.sing_me_a_song('John')
