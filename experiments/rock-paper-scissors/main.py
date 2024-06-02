from contextlib import contextmanager
from enum import Enum
from random import randint
from typing import Callable, Optional


class Log:
    """Utility class for colored logging output."""
    _sequence = {
        'blue': '\033[94m',
        'green': '\033[92m',
        'red': '\033[91m',
        'bold': '\033[1m',
        'end': '\033[0m',
    }

    @classmethod
    def red(cls, message: str) -> None:
        cls._print(message, cls._sequence['red'])

    @classmethod
    def green(cls, message: str) -> None:
        cls._print(message, cls._sequence['green'])

    @classmethod
    def blue(cls, message: str) -> None:
        cls._print(message, cls._sequence['blue'])

    @classmethod
    def bold(cls, message: str) -> None:
        cls._print(message, cls._sequence['bold'])

    @classmethod
    def title(cls, title: str) -> str:
        return '\n'.join([title, '=' * len(title)])

    @classmethod
    def _print(cls, message: str, color: str) -> None:
        end = cls._sequence['end']
        print(f'{color}{message}{end}')


class InvalidInputException(Exception):
    """Exception raised for invalid input."""
    pass


class QuitGameException(Exception):
    """Exception raised to quit the game."""
    pass


class Shape(Enum):
    ROCK = 'r'
    PAPER = 'p'
    SCISSORS = 's'

    @classmethod
    def display(cls, shape: Optional[str]) -> str:
        match shape:
            case cls.ROCK:
                return 'Rock'
            case cls.PAPER:
                return 'Paper'
            case cls.SCISSORS:
                return 'Scissors'
            case _:
                return '(None)'


class Player:
    def __init__(self, name: str, logger: Callable[[str], None]):
        self.name = name
        self.score = 0
        self.logger = logger
        self.last_move: Optional[Shape] = None

    def log_last_move(self) -> None:
        last_move = Shape.display(self.last_move)
        self.logger(f'{self.name} played: {last_move}')

    def log_win(self) -> None:
        self.logger(f'[OUTCOME] {self.name} won!')

    def log_score(self) -> None:
        self.logger(f'{self.name} score = {self.score}')

    def ask_move(self) -> None:
        self.last_move = self._read_move()

    def _read_move(self) -> Shape:
        while True:
            print('\nType a letter to select a shape (r=Rock, p=Paper, s=Scissors).')
            print('Type q to quit')

            try:
                user_input = input('> ').lower()

                if user_input == 'q':
                    raise QuitGameException()

                if user_input not in [shape.value for shape in Shape]:
                    raise InvalidInputException()

                return Shape(user_input)

            except InvalidInputException:
                print('ERROR: Invalid input. Try again')

    def random_move(self) -> None:
        """Assign a random move to the player."""
        n = randint(1, 3)
        match n:
            case 1:
                self.last_move = Shape.ROCK
            case 2:
                self.last_move = Shape.PAPER
            case 3:
                self.last_move = Shape.SCISSORS


def check_winner(player1: Player, player2: Player) -> Optional[Player]:
    """Determine the winner between two players."""
    p1, p2 = player1.last_move, player2.last_move

    if p1 == p2:
        return None

    if (
        (p1 == Shape.ROCK and p2 == Shape.SCISSORS) or
        (p1 == Shape.PAPER and p2 == Shape.ROCK) or
        (p1 == Shape.SCISSORS and p2 == Shape.PAPER)
    ):
        return player1

    return player2


@contextmanager
def game_context():
    Log.bold('\n' + Log.title('Rock Paper Scissors'))
    try:
        yield
    except (KeyboardInterrupt, QuitGameException):
        print('You quit the game')
    finally:
        print('\nIt was nice playing with you. Bye!')


def turns():
    """Generator function to track game turns."""
    turn_number = 1
    while True:
        yield turn_number
        turn_number += 1


def main() -> None:
    """Main function to start the game."""
    with game_context():
        player1 = Player('User', Log.blue)
        player2 = Player('CPU', Log.green)
        draws = 0

        for turn in turns():
            Log.bold('\n' + Log.title(f'Turn #{turn}'))

            player1.ask_move()
            player1.log_last_move()

            player2.random_move()
            player2.log_last_move()

            print('――――――')
            winner = check_winner(player1, player2)
            if winner:
                winner.score += 1
                winner.log_win()
            else:
                Log.bold('[OUTCOME]: Draw!')
                draws += 1
            print('――――――')

            player1.log_score()
            player2.log_score()
            print(f'Draws = {draws}')


if __name__ == '__main__':
    main()
