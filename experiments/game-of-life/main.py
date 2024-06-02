import time
import random
import os
from typing import List


ALIVE = ' @ '
DEAD = ' · '

GameState = List[bool]


def clear_output() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def chunks(elements, n):
    n = max(1, n)
    return [elements[i:i+n] for i in range(0, len(elements), n)]


def print_state(state: GameState, size=20) -> None:
    for chunk in chunks(state, size):
        print(''.join([ALIVE if cell else DEAD for cell in chunk]))


def calculate_next_state(state: GameState, size=20) -> GameState:
    """TODO"""
    return state


def get_random_state(grid_size: int) -> GameState:
    state: GameState = []
    for i in range(grid_size * grid_size):
        state.append(random.getrandbits(1))
    return state


def print_generation(generation: int, state: GameState, size: int) -> None:
    clear_output()
    print(f'Generation #{generation}')
    print_state(state, size)
    time.sleep(0.5)


def game_of_life(*, generations=10, size=20, t=10, state: GameState) -> None:

    interval = t/generations

    print_generation(0, state, size)
    time.sleep(interval)

    for gen in range(1, generations):
        state = calculate_next_state(state, size)
        print_generation(gen, state, size)
        time.sleep(interval)


def game_of_life_random_state(**kwargs) -> None:
    state = get_random_state(kwargs['size'])
    input = {**kwargs, 'state': state}
    game_of_life(**input)


def main() -> None:
    game_of_life_random_state(generations=10, size=20, t=10)


if __name__ == '__main__':
    main()
