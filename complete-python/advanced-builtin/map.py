people = ['Alice', 'Bob', 'Charlie', 'Darlene', 'Eric', 'Francis']

# Using map
for name in map(lambda name: name.lower(), people):
    print(name)

# Alternative 1: with generator comprehension
names1_generator = (name.lower() for name in people)
names1 = tuple(names1_generator)
print(names1)



# Example with a class
class User:
    def __init__(self, username, password):
        self.username
        self.password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])

users = (
    {'username': 'alice', 'password': 'very-secure'},
    {'username': 'bob', 'password': 'super-safe'}
)

# They do the same thing
user_instances1 = [User.from_dict(user) for user in users]
user_instances2 = map(User.from_dict, users)
