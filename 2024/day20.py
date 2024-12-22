from collections import defaultdict

with open("addenda/input20.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
diagonals = [(1, -1), (1, 1), (-1, 1), (-1, -1)]


def prep():
    grid = []
    start = None
    for y, line in enumerate(lines):
        grid.append([])
        for x, c in enumerate(line):
            if c == 'S':
                start = (x, y)
            grid[-1].append('.' if c in 'SE' else c)

    checks = [start]
    grid[start[1]][start[0]] = 0
    while checks:
        check = checks.pop(0)
        for d in directions:
            new_check = check[0] + d[0], check[1] + d[1]
            if grid[new_check[1]][new_check[0]] == '.':
                grid[new_check[1]][new_check[0]] = grid[check[1]][check[0]] + 1
                checks.append(new_check)

    return grid


def part1():
    grid = prep()

    saves = defaultdict(lambda: 0)
    _directions = [(a * 2, b * 2) for a, b in directions]
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if type(c) == int:
                for d in _directions + diagonals:
                    nx, ny = x + d[0], y + d[1]
                    if 0 <= nx < len(line) and 0 <= ny < len(grid) and type(grid[ny][nx]) == int:
                        if grid[ny][nx] > grid[y][x]:
                            save = grid[ny][nx] - grid[y][x] - 2
                            if save > 0:
                                saves[save] += 1

    return sum([saves[save] for save in saves if save >= 100])


def part2():
    grid = prep()
    path = {}
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if type(c) == int:
                path[(x, y)] = grid[y][x]

    saves = defaultdict(lambda: 0)

    for (ax, ay), ap in path.items():
        for (bx, by), bp in path.items():
            if bp > ap:
                dis = abs(ax - bx) + abs(ay - by)  # taxicab
                if dis <= 20:
                    save = bp - ap - dis
                    if save > 0:
                        saves[save] += 1

    return sum([saves[save] for save in saves if save >= 100])


print(part1())
print(part2())
