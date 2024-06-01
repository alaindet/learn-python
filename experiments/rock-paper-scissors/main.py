from contextlib import contextmanager
from enum import StrEnum
from random import randint
from typing import Optional


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
            print('Type a letter to select a shape (r=Rock, p=Paper, s=Scissors)')

            try:
                user_input = input('> ').lower()

                if user_input in ['q', 'quit']:
                    raise Exception('You quit the game')

                if user_input in Shape:
                    return Shape(user_input)

                else:
                    print('Invalid input. Try again')

            except ValueError:
                print('Invalid input. Try again')

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
    print('\nRock Paper Scissors\n===================')
    try:
        yield
    except KeyboardInterrupt:
        pass
    except Exception as err:
        print(err)
    finally:
        print('\nIt was nice playing with you. Bye!')


def turns():
    i = 1
    playing = True
    while playing:
        yield i
        i += 1


def main() -> None:
    with game_context():
        player1 = Player('User')
        player2 = Player('CPU')

        for turn in turns():

            print(f'\nTurn #{turn}')

            player1.ask_move()
            print(f'{player1.name} played: {player1.display_move()}')

            player2.random_move()
            print(f'{player2.name} played: {player2.display_move()}')

            winner = check_winner(player1, player2)

            if winner:
                winner.score += 1
                print(f'Outcome: {winner.name} won!')
            else:
                print('Outcome: Draw!')

            print(f'Score: {player1.display()}, {player2.display()}')


if __name__ == '__main__':
    main()
