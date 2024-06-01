from contextlib import contextmanager
from enum import StrEnum
from random import randint
from typing import Optional


class Log:
    """Thanks to https://stackoverflow.com/a/287944/5653974"""
    _sequence = {
        'blue': '\033[94m',
        'green': '\033[92m',
        'red': '\033[91m',
        'bold': '\033[1m',
        'end': '\033[0m',
    }

    @classmethod
    def red(self, message: str) -> None:
        self._print(message, self._sequence['red'])

    @classmethod
    def green(self, message: str) -> None:
        self._print(message, self._sequence['green'])

    @classmethod
    def blue(self, message: str) -> None:
        self._print(message, self._sequence['blue'])

    @classmethod
    def bold(self, message: str) -> None:
        self._print(message, self._sequence['bold'])

    @classmethod
    def title(self, title: str) -> str:
        return '\n'.join([title, '=' * len(title)])

    @classmethod
    def _print(self, message: str, color: str) -> None:
        end = self._sequence['end']
        print(f'{color}{message}{end}')


class InvalidInputException(Exception):
    pass


class QuitGameException(Exception):
    pass


class Shape(StrEnum):
    Rock = 'r'
    Paper = 'p'
    Scissors = 's'

    @classmethod
    def display(self, shape: Optional[str]) -> str:
        match shape:
            case self.Rock:
                return 'Rock'
            case self.Paper:
                return 'Paper'
            case self.Scissors:
                return 'Scissors'
            case _:
                return '(None)'


class Player:
    name: str
    score = 0
    last_move: Optional[Shape] = None

    def __init__(self, name: str):
        self.name = name

    def display(self) -> str:
        return f'{self.name} = {self.score}'

    def display_move(self) -> str:
        return Shape.display(self.last_move)

    def ask_move(self) -> None:
        self.last_move = self._read_move()

    def _read_move(self) -> Shape:
        while True:
            print('\n'.join([
                'Type a letter to select a shape (r=Rock, p=Paper, s=Scissors).',
                'Type q to quit',
            ]))

            try:
                user_input = input('> ').lower()

                if user_input in ['q', 'quit']:
                    raise QuitGameException()

                if user_input not in Shape:
                    raise InvalidInputException()

                return Shape(user_input)

            except (InvalidInputException, ValueError):
                print('ERROR: Invalid input. Try again')

    def random_move(self) -> Shape:
        """TODO: Improve"""
        n = randint(1, 3)
        match n:
            case 1:
                self.last_move = Shape.Rock
            case 2:
                self.last_move = Shape.Paper
            case 3:
                self.last_move = Shape.Scissors


def check_winner(player1: Player, player2: Player) -> Optional[Player]:

    p1 = player1.last_move
    p2 = player2.last_move

    if p1 == p2:
        return None

    if (
        (p1 == Shape.Rock and p2 == Shape.Scissors) or
        (p1 == Shape.Paper and p2 == Shape.Rock) or
        (p1 == Shape.Scissors and p2 == Shape.Paper)
    ):
        return player1

    return player2


@contextmanager
def game_context():
    Log.bold('\n' + Log.title('Rock Paper Scissors'))

    try:
        yield
    except KeyboardInterrupt:
        pass
    except QuitGameException:
        print('You quit the game')
    finally:
        print('\nIt was nice playing with you. Bye!')


def turns():
    i = 1
    while True:
        yield i
        i += 1


def main() -> None:
    with game_context():
        player1 = Player('User')
        player2 = Player('CPU')

        for turn in turns():

            Log.bold('\n' + Log.title(f'Turn #{turn}'))

            player1.ask_move()
            Log.blue(f'{player1.name} played: {player1.display_move()}')

            player2.random_move()
            Log.green(f'{player2.name} played: {player2.display_move()}')

            winner = check_winner(player1, player2)

            if winner:
                winner.score += 1
                logger = Log.blue if winner is player1 else Log.green
                logger(f'Outcome: {winner.name} won!')
            else:
                Log.bold('Outcome: Draw!')

            print(f'Score: {player1.display()}, {player2.display()}')


if __name__ == '__main__':
    main()
