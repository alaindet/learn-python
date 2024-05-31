from contextlib import contextmanager
from enum import IntEnum
from random import choice as random_choice
from textwrap import dedent


class Shape(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3


QUIT_COMMANDS = {'q', 'Q', 'quit', 'QUIT'}


class QuitGameException(Exception):
    pass


def log(message: str) -> None:
    print(dedent(message))


def get_random_move() -> Shape:
    return random_choice(list(Shape))


def get_user_move() -> Shape:
    user_move: Shape | None = None

    while not user_move:
        log(
            """
            Select a shape:
            1. Rock
            2. Paper
            3. Scissors
            """
        )

        try:
            user_input = int(input('> '))

            if user_input in QUIT_COMMANDS:
                raise QuitGameException()

            if user_input in Shape:
                user_move = user_input

        except ValueError:
            print('Invalid input. Try again')

    return user_move


def intro() -> None:
    print('Rock Paper Scissors\n===================')


def outro() -> None:
    print('Bye')


@contextmanager
def game():
    intro()
    playing = True
    while playing:
        try:
            yield
        except QuitGameException:
            playing = False
    outro()


def main() -> None:
    playing = True
    while playing:

        try:
            user_move = get_user_move()
        except QuitGameException:
            playing = False
            outro()

        cpu_move = get_random_move()

        match user_move:
            case Shape.Rock:
                print('You typed rock')
            case Shape.Paper:
                print('You typed paper')
            case Shape.Scissors:
                print('You typed scissors')
            case _:
                print('Invalid input. Try again')


if __name__ == '__main__':
    main()
