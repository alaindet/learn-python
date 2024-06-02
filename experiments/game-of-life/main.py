from textwrap import dedent
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


def get_state_from_string(state_string: str, alive: str, dead: str) -> GameState:
    state: List[bool] = []
    for char in state_string.strip():
        if char == alive:
            state.append(True)
        elif char == dead:
            state.append(False)
    return state


def get_random_state(size: int) -> GameState:
    return [random.getrandbits(1) for i in range(size * size)]


def get_empty_state(size: int) -> GameState:
    return [False for i in range(size * size)]


def get_neighbors_indices(size: int, index: int) -> List[int]:
    """Calculates valid indices of neighbors excluding outbound indices when
    the cell is on the grid's edge. Here, t=top, tl=top left, b = bottom, etc."""

    t = index - size
    tl, tr = t - 1, t + 1
    b = index + size
    bl, br = b - 1, b + 1
    l, r = index - 1, index + 1

    first_index = 0
    last_index = (size * size) - 1

    on_top_edge = t < first_index
    on_bottom_edge = b > last_index
    on_left_edge = index % size == 0
    on_right_edge = (index + 1) % size == 0
    invalid_index = -1

    if on_left_edge:
        tl, l, bl = invalid_index, invalid_index, invalid_index

    if on_right_edge:
        tr, r, br = invalid_index, invalid_index, invalid_index

    if on_top_edge:
        tl, t, tr = invalid_index, invalid_index, invalid_index

    if on_bottom_edge:
        bl, b, br = invalid_index, invalid_index, invalid_index

    indices = [tl, t, tr, r, br, b, bl, l]
    return [index for index in indices if index != invalid_index]


def count_neighbors(state: GameState, size: int, index: int) -> int:
    count = 0
    for index in get_neighbors_indices(size, index):
        if state[index]:
            count += 1
    return count


def next_cell_state(state: GameState, size: int, index: int) -> bool:
    is_alive = state[index]
    neighbors = count_neighbors(state, size, index)

    # A dead cell comes alive
    if not is_alive and neighbors == 3:
        return True

    # A live cell dies for underpopulation
    if neighbors < 2:
        return False

    # A live cell dies for overpopulation
    if neighbors > 3:
        return False

    # A live cell stays alive
    return True


def calculate_next_state(state: GameState, size=20) -> GameState:
    return [next_cell_state(state, size, i) for i, is_alive in enumerate(state)]


def print_generation(generation: int, state: GameState, size: int) -> None:
    clear_output()
    print(f'Generation #{generation}')
    print_state(state, size)


def game_of_life(*, generations=10, size=20, t=10, state: GameState) -> None:

    # print_generation(0, state, size)

    # state = calculate_next_state(state, size)
    # print_generation(1, state, size)

    # state = calculate_next_state(state, size)
    # print_generation(2, state, size)

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

    serialized_state = dedent("""
    ................
    ................
    ................
    ................
    ................
    .......xxx......
    ................
    .....x.....x....
    .....x.....x....
    .....x.....x....
    ................
    .......xxx......
    ................
    ................
    ................
    ................
    """)

    state = get_state_from_string(serialized_state, alive='x', dead='.')
    game_of_life(generations=20, size=16, t=1, state=state)


if __name__ == '__main__':
    main()
