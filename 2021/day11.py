import numpy as np


with open("addenda/test.txt", 'r') as file:
    lines = file.readlines()


def part1():
    grid = np.array([np.array([int(c) for c in line.strip()]) for line in lines])

    flashes = 0
    for i in range(100):
        grid += np.full(grid.shape, 1)
        grid %= 10
        print(i, 100 - np.count_nonzero(grid))
        flashes += 100 - np.count_nonzero(grid)

    return flashes


def part2():
    pass


print(part1())
print(part2())
