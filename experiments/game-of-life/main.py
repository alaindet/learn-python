from math import sqrt
import time
import random
import os
from typing import List


PULSAR_EXAMPLE = """
.................
.....x.....x.....
.....x.....x.....
.....xx...xx.....
.................
.xxx..xx.xx..xxx.
...x.x.x.x.x.x...
.....xx...xx.....
.................
.....xx...xx.....
...x.x.x.x.x.x...
.xxx..xx.xx..xxx.
.................
.....xx...xx.....
.....x.....x.....
.....x.....x.....
.................
"""

GLIDER_EXAMPLE = """
..x.............
...x............
.xxx............
................
................
................
................
................
................
................
................
................
................
................
................
................
"""


def clear_output() -> None:
    """Clears the terminal output"""
    os.system('cls' if os.name == 'nt' else 'clear')


def chunks(elements, n):
    """Splits a list into multiple same-sized lists (the last one can be smaller)"""
    n = max(1, n)
    return [elements[i:i+n] for i in range(0, len(elements), n)]


class GameState:
    """The game board is assumed to be a square"""

    def __init__(self, cells: List[bool], size: int, alive: str, dead: str):
        self.cells = cells
        self.size = size
        self.alive = alive
        self.dead = dead

    def serialize(self) -> str:
        """Creates a serialized state as string from the current state"""
        rows = chunks(self.cells, self.size)
        return '\n'.join([self._serialize_row(row) for row in rows])

    def _serialize_row(self, row: List[bool]) -> str:
        return ''.join([self.alive if cell else self.dead for cell in row])

    @classmethod
    def deserialize(cls, serialized: str, alive: str, dead: str):
        """Creates a board from a serialized string state"""
        state: List[bool] = []

        for char in serialized.strip():
            if char == alive:
                state.append(True)
            elif char == dead:
                state.append(False)

        # The board must be squared!
        size = int(sqrt(len(state)))

        return cls(state, size, alive, dead)

    @classmethod
    def create_random(cls, size: int, alive: str, dead: str):
        """Creates a board with a random distribution of alive and dead cells"""
        cells = [random.getrandbits(1) for i in range(size * size)]
        return cls(cells, size, alive=alive, dead=dead)

    @classmethod
    def create_empty(cls, size: int, alive: str, dead: str):
        """Creates an empty board"""
        cells = [False for i in range(size * size)]
        return GameState(cells, size, alive=alive, dead=dead)


def get_neighbors_indices(size: int, index: int) -> List[int]:
    """
    Calculates valid indices of neighbors excluding outbound indices when
    the cell is on the grid's edge. Here, t=top, tl=top left, b = bottom, etc.
    """

    t = index - size
    tl, tr = t - 1, t + 1
    b = index + size
    bl, br = b - 1, b + 1
    l, r = index - 1, index + 1

    last_index = (size * size) - 1
    empty = -1

    # On the left edge
    if index % size == 0:
        tl, l, bl = empty, empty, empty

    # On the right edge
    if (index + 1) % size == 0:
        tr, r, br = empty, empty, empty

    # On the top edge
    if t < 0:
        tl, t, tr = empty, empty, empty

    # On the bottom edge
    if b > last_index:
        bl, b, br = empty, empty, empty

    indices = [tl, t, tr, r, br, b, bl, l]
    return [index for index in indices if index != empty]


def count_neighbors(state: GameState, index: int) -> int:
    """Counts the number of alive neighbors of a given cell"""
    count = 0
    for index in get_neighbors_indices(state.size, index):
        if state.cells[index]:
            count += 1
    return count


def next_cell_state(state: GameState, index: int) -> bool:
    """
    Calculates the next cell state based on the neighbor cells
    Rules are:
    - A live cell stays alive with 2 or 3 neighbors
    - A live cell dies if neighbors are either < 2 or > 3
    - A dead cell comes alive with exactly 3 neighbors
    """
    is_alive = state.cells[index]
    neighbors = count_neighbors(state, index)
    return neighbors == 3 or (neighbors == 2 and is_alive)


def calculate_next_state(state: GameState) -> GameState:
    """Calculates the next state based on the current one"""
    cells = [next_cell_state(state, i) for i, _ in enumerate(state.cells)]
    return GameState(cells, size=state.size, alive=state.alive, dead=state.dead)


def game_of_life(
    *,
    generations: int,
    total_time: int,
    state: GameState,
) -> None:

    interval = total_time / generations

    clear_output()
    print(f'Generation #0 / {generations}')
    print(state.serialize())
    time.sleep(interval)

    for gen in range(generations):
        state = calculate_next_state(state)
        clear_output()
        print(f'Generation #{gen+1} / {generations}')
        print(state.serialize())
        time.sleep(interval)


def game_of_life_random_state(**kwargs) -> None:

    state = GameState.create_random(
        size=kwargs['size'],
        alive=kwargs['alive'],
        dead=kwargs['dead'],
    )

    game_of_life(
        generations=kwargs['generations'],
        total_time=kwargs['total_time'],
        state=state
    )


def game_of_life_from_state(**kwargs) -> None:
    game_of_life(**kwargs)


def main() -> None:
    # game_of_life_random_state(
    #     generations=100,
    #     size=30,
    #     total_time=15,
    #     alive=' @ ',
    #     dead=' · ',
    # )

    serialized = PULSAR_EXAMPLE
    # serialized = GLIDER_EXAMPLE
    state = GameState.deserialize(serialized=serialized, alive='x', dead='.')
    state.alive = ' @ '
    state.dead = ' · '

    game_of_life_from_state(
        generations=100,
        total_time=15,
        state=state,
    )


if __name__ == '__main__':
    main()
