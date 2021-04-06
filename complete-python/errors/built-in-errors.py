# IndexError
# Thrown when accessing a non-existing index in a list
friends = ['Foo', 'Bar']
try:
    print(friends[2])
except IndexError:
    print('Catched IndexError')

# KeyError
# Thrown when accessing non-existing keys in dictionaries
grades = {'Alice': 85, 'Bob': 94}
try:
    print(grades['Charlie'])
except KeyError:
    print('Catched KeyError')

# NameError
# Thrown when using a non-existing variable
try:
    print(hello)
except NameError:
    print('Catched NameError')

# AttributeError
# Thrown when accessing a non-existing attribute of an instance
people = ['Alice', 'Bob', 'Charlie']
nearby = ['Bob', 'Darlene']
try:
    both = people.intersection(nearby)
except AttributeError:
    print('Catched AttributeError')

# NotImplementedError
try:
    class User:
        def __init__(self, username, password):
            self.username = username
            self.password = password

        def login(self):
            raise NotImplementedError('This is not implemented yet')

    user = User('Alain', '1234')
    user.login()
except NotImplementedError:
    print('Catched NotImplementedError')

# RuntimeError
# try:
#     # Not easy to trigger
#     # It is a base class
# except RuntimeError:
#     print('Catched RuntimeError')

# SyntaxError
# Thrown when syntax is wrong
# Cannot be catched: Fatal error
# try:
#     class User # <-- There's a missing :
#         def __init__(self, username, password):
#             self.username = username
#             self.password = password
# except SyntaxError:
#     print('Catched RuntimeError')

# IndentationError
# Thrown when indentation is wrong
# Cannot be catched: Fatal error
# try:
#     def hello():
#     return 'hello'
# except IndentationError:
#     print('Catched IndentationError')

# TabError
# Cannot be catched: Fatal error
# Thrown when using tabs instead of spaces

# TypeError
try:
    # You cannot add strings and numbers
    print('Answer' + 42)

    # This is fine
    # print('Answer' + str(42))
except TypeError:
    print('Catched TypeError')

# ValueError
# Only built-in functions raise this, usually
try:
    print(int('20.5'))
except ValueError:
    print('Catched ValueError')

# ImportError
# Usually happens on circular dependency imports
# try:
#     # Cannot be easily catched
# except:
#     print('Catched ImportError')


# DeprecationWarning
try:
    class User:

        def __init__(self, username, password):
            self.username = username
            self.password = password

        @staticmethod
        def old_register(username, password):
            raise DeprecationWarning('User#old_register is deprecated')

        @staticmethod
        def new_register(username, password):
            # Do something...
            pass

    User.old_register('Alain', '1234')

except DeprecationWarning:
    print('catched DeprecationWarning')
