blockchain = []
blockchain_seed = [1]


def get_user_input(question='Enter your transaction amount: '):
    """
    Returns the user input

    Parameters
    ----------
    question : str
        The question the user sees
    """
    return float(input(question))


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=blockchain_seed):
    blockchain.append([last_transaction, transaction_amount])


tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(tx_amount)
add_value(tx_amount, get_last_blockchain_value())

tx_amount = get_user_input()
add_value(tx_amount)
add_value(tx_amount, get_last_blockchain_value())

for block in blockchain:
    print('Outputting block')
    print(block)
