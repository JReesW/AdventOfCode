import time
import numpy as np


with open("addenda/input14.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def get_weight(grid):
    weight = 0

    for col in grid:
        for i, c in enumerate(col):
            if c == 'O':
                weight += len(col) - i

    return weight


def move(grid):
    for col in grid:
        rocks = [n for n, c in enumerate(col) if c == '#']
        boulders = []

        for y, c in enumerate(col):
            if c == 'O':
                above = [r for r in rocks + boulders if r < y]
                if above:
                    boulders.append(max(above) + 1)
                else:
                    boulders.append(0)

        col[col == 'O'] = '.'
        np.put(col, boulders, 'O')

    return grid


def part1():
    grid = np.array([np.array(list(line)) for line in lines]).T

    return get_weight(move(grid))


def part2():
    grid = np.array([np.array(list(line)) for line in lines]).T

    seen = {}
    i = 0
    while True:
        flat = ''.join(grid.flat)
        if flat in seen:
            break
        seen[flat] = i

        for _ in range(4):
            grid = np.rot90(move(grid))

        i += 1

    first = seen[''.join(grid.flat)]
    cycle_len = i - first
    needed_mod = (1_000_000_000 - first) % cycle_len

    while (i - first) % cycle_len != needed_mod:
        for _ in range(4):
            grid = np.rot90(move(grid))

        i += 1

    return get_weight(grid)


print(part1())
print(part2())
