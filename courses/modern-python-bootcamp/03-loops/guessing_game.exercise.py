from random import randint
from typing import Union

GUESS_GAME_MIN = 1
GUESS_GAME_MAX = 10

LOWER = -1
EXACT = 0
HIGHER = 1

def get_integer_input(message: str) -> int:
    while True:
        try:
            user_input = input(message + ' > ')
            n = int(user_input)
            return n
        except ValueError:
            print('Invalid input')

def guessing_game_check(to_be_guessed: int, picked: int) -> Union[LOWER, EXACT, HIGHER]:
    if picked < to_be_guessed:
        return LOWER
    if picked > to_be_guessed:
        return HIGHER
    return EXACT

def guessing_game() -> None:
    random_number = randint(GUESS_GAME_MIN, GUESS_GAME_MAX)
    message = f'Pick a number between {GUESS_GAME_MIN} and {GUESS_GAME_MAX}'
    attempts = 0
    
    while True:
        attempts += 1
        picked_number = get_integer_input(message)
        outcome = guessing_game_check(random_number, picked_number)

        if outcome == LOWER:
            print('Too low, go higher')
            continue

        if outcome == HIGHER:
            print('Too high, go lower')
            continue

        print(f'You guessed the number {random_number} in {attempts} attempts')
        return

def main() -> None:

    games = 0

    print('\nWelcome to Guess the Number!')
    print('============================')

    while True:
        games += 1
        print(f'\nGame #{games}')
        guessing_game()

if __name__ == '__main__':
    main()