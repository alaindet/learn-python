accounts = {
    'checking': 1958.00,
    'savings': 3695.00,
}


def add_balance(amount: float, name: str='checking') -> float:
    """
    Function to update the balance of an account and return new balance
    Non-default arguments CANNOT follow default arguments
    """
    accounts[name] += amount
    return accounts[name]

add_balance(500.00, 'savings')
add_balance(500.00)
print(accounts['savings'])
print(accounts['checking'])

# # BAAAAD IDEA
# # Mutable default arguments
# def create_account(name: str, holder: str, account_holders: list = []):
#     account_holders.append(holder)
#     return {
#         'name': name,
#         'main_account_holder': holder,
#         'account_holders': account_holders,
#     }


# a1 = create_account('checking', 'Alice')
# a2 = create_account('savings', 'Bob')

# print(a2) # Has a mutable default argument (account_holders)


# Argument unpacking
transactions = [
    (-180.67, 'checking'),
    (-220.00, 'checking'),
    (200, 'savings'),
    (-15.99, 'checking'),
    (-57.00, 'checking'),
    (300, 'savings')
]

for transaction in transactions:

    # Argument unpacking
    add_balance(*transaction)

    # # Alternative 1: named arguments
    # add_balance(amount=transaction[0], name=transaction[1])

    # # Alternative 1b: named arguments does not need an order
    # add_balance(name=transaction[1], amount=transaction[0])

    # # Alternative 2: tuple unpacking
    # amount, name = transaction
    # add_balance(amount, name)

print(accounts)


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'User (username: {self.username})'


# Dictionary unpacking
## Unpack a dictionary's keys to named arguments of a function
## Order of keys and arguments does not matter here
users = [
    {'username': 'Alice', 'password': '1234'},
    {'username': 'Bob', 'password': '5678'},
]
user_instances = [User(**user) for user in users]
print(user_instances)

# Tuple unpacking
## Equivalent to the example above, but using tuples
users = [
    ('Alice', '1234'),
    ('Bob', '5678'),
]
user_instances = [User(*user) for user in users]
print(user_instances)
