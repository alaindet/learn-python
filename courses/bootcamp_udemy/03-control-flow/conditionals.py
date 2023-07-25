balance = 100.0
price = 60.0

def balance_repr(balance: float) -> str:
    return f'Balance: {balance:.2f}$'

def buy(balance: float, price: float) -> float:
    if balance < price:
        # TODO: Raise error!
        print('Insufficient funds!')
    else:
        print(f'You spent {price:.2f}$')
        balance -= price

    return balance

# Start
print(balance_repr(balance))

# Buy 1
balance = buy(balance, price)
print(balance_repr(balance))

# Buy 2 (insufficient funds)
balance = buy(balance, price)
print(balance_repr(balance))

proceed_prompt = 'Continue? Type "yes" or "no": '
proceed_input = input(proceed_prompt)
proceed_input = proceed_input.replace(' ', '').strip().lower()

if proceed_input == 'yes':
    print('You typed "yes"')
elif proceed_input == 'no':
    print('You typed "no"')
else:
    print('You typed an invalid answer')