import re


with open("addenda/input10.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


class BreakOut(Exception):
    """"""


starting = {
    (0, 1): ['-', '7', 'J'],  # right
    (0, -1): ['-', 'F', 'L'],  # left
    (1, 0): ['|', 'J', 'L'],  # down
    (-1, 0): ['|', '7', 'F']  # up
}

dirs = {
    '-': ((0, -1), (0, 1)),  # left or right
    '|': ((-1, 0), (1, 0)),  # up or down
    '7': ((0, -1), (1, 0)),  # left or down
    'J': ((-1, 0), (0, -1)),  # left or up
    'F': ((0, 1), (1, 0)),  # right or down
    'L': ((-1, 0), (0, 1))  # right or up
}


def part1(p2=False):
    grid = [list(line) for line in lines]
    dist_grid = [[None for _ in row] for row in grid]

    start = None
    try:
        for y, row in enumerate(grid):
            for x, tile in enumerate(row):
                if tile == 'S':
                    start = (y, x)
                    dist_grid[y][x] = 0
                    raise BreakOut
    except BreakOut:
        pass

    movers = [(start[0] + y, start[1] + x) for (y, x), chars in starting.items() if grid[start[0] + y][start[1] + x] in chars]
    start_dirs = [(y, x) for (y, x), chars in starting.items() if grid[start[0] + y][start[1] + x] in chars]
    for mover in movers:
        dist_grid[mover[0]][mover[1]] = 1

    grid[start[0]][start[1]] = {v: k for k, v in dirs.items()}[tuple(sorted(start_dirs))]

    dist = 2
    try:
        while movers[0] != movers[1]:
            for i, mover in enumerate(movers):
                char = grid[mover[0]][mover[1]]
                for d in dirs[char]:
                    y, x = mover[0] + d[0], mover[1] + d[1]
                    if dist_grid[y][x] is None:
                        movers[i] = (y, x)
                        dist_grid[y][x] = dist
                        break
                else:
                    raise BreakOut
            dist += 1
    except BreakOut:
        if p2:
            return grid, dist_grid
        return dist


def part2():
    grid, dist_grid = part1(True)

    inside = 0
    for y, row in enumerate(dist_grid):
        line = "".join([(c if dist_grid[y][x] is not None else '.') for x, c in enumerate(grid[y])])
        swaps = list(re.finditer("L-*7|F-*J|\|", line))

        for x, c in enumerate(line):
            if c == '.':
                left = [swap for swap in swaps if swap.start() < x]
                inside += len(left) % 2

    return inside


print(part1())
print(part2())
