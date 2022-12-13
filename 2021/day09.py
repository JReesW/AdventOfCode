# cheap, I know... sue me
from skimage.morphology import flood_fill
import numpy as np
from collections import defaultdict


with open("addenda/input09.txt", 'r') as file:
    lines = file.readlines()


def part1():
    grid = [[int(c) for c in line.strip()] for line in lines]
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            low = True
            p = grid[y][x]
            if y > 0 and grid[y-1][x] <= p\
                    or y < len(grid) - 1 and grid[y+1][x] <= p\
                    or x > 0 and grid[y][x-1] <= p\
                    or x < len(grid[0]) - 1 and grid[y][x+1] <= p:
                low = False
            if low:
                total += p + 1
    return total


def part2():
    grid = np.array([[-1 if c == '9' else 0 for c in line.strip()] for line in lines])
    cur = 1
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y, x] == 0:
                grid = flood_fill(grid, (y, x), cur, connectivity=1)
                cur += 1

    counts = defaultdict(lambda: 0)
    for row in grid:
        for n in row:
            if n > 0:
                counts[n] += 1
    a, b, c = sorted([c for c in counts.values()], reverse=True)[:3]
    return a * b * c


print(part1())
print(part2())
