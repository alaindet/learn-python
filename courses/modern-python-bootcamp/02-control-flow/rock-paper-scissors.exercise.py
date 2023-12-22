from random import choice
from typing import Union

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
RPS = [ROCK, PAPER, SCISSORS]

PLAYER1_WINS = -1
PLAYER2_WINS = 1
DRAW = 0

human_score = 0
computer_score = 0

def get_random_move() -> Union[ROCK, PAPER, SCISSORS]:
    return choice(RPS)

def normalize_move(move: str) -> Union[ROCK, PAPER, SCISSORS]:
    move_lower = move.lower()
    if move_lower in RPS:
        return move_lower
    elif move == 'r':
        return ROCK
    elif move == 'p':
        return PAPER
    elif move == 's':
        return SCISSORS
    else:
        raise ValueError

def read_move() -> Union[ROCK, PAPER, SCISSORS]:
    while True:
        try:
            move_input = input('Enter a move > ')
            return normalize_move(move_input)
        except ValueError:
            print('Invalid move entered, try again.')
            print('Valid moves are "rock", "r", "paper", "p", "scissors", "s"')
            print('\n')

def check_move(
    player1: Union[ROCK, PAPER, SCISSORS],
    player2: Union[ROCK, PAPER, SCISSORS],
) -> Union[PLAYER1_WINS, PLAYER2_WINS, DRAW]:
    
    if player1 == player2:
        return DRAW
    
    if (
        (player1 == ROCK and player2 == SCISSORS)
        or (player1 == PAPER and player2 == ROCK)
        or (player1 == SCISSORS and player2 == PAPER)
    ):
        return PLAYER1_WINS

    return PLAYER2_WINS

def rock_paper_scissors() -> None:

    global human_score, computer_score

    print('\nLet\'s play Rock-Paper-Scissors!\n')

    while True:
        human_move = read_move()
        computer_move = get_random_move()
        result = check_move(human_move, computer_move)
        outcome = ''

        if result == PLAYER1_WINS:
            outcome = 'Human wins!'
            human_score += 1
        elif result == PLAYER2_WINS:
            outcome = 'Computer wins!'
            computer_score += 1
        else:
            outcome = 'Draw!'

        print(f'[Human] {human_move} VS [Computer] {computer_move} => {outcome}')
        print(f'[Scores] Human: {human_score}, Computer: {computer_score}')
        print('\n')

rock_paper_scissors() # <-- Start here!