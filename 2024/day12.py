from collections import defaultdict
from itertools import groupby

with open("addenda/input12.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
add = lambda a, b: (a[0] + b[0], a[1] + b[1])
in_bounds = lambda a: 0 <= a[0] < len(lines[0]) and 0 <= a[1] < len(lines)


def prep():
    grid = []
    for line in lines:
        grid.append([])
        for c in line:
            grid[-1].append(c)

    checked = {}
    i = 0
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if (x, y) not in checked:
                i += 1
                checked[(x, y)] = (grid[y][x], i)
                flood = [add((x, y), d) for d in directions]
                flood = [f for f in flood if in_bounds(f) and grid[f[1]][f[0]] == grid[y][x] and f not in checked]
                while flood:
                    f = flood.pop(0)
                    checked[f] = (grid[y][x], i)
                    _flood = [add(f, d) for d in directions]
                    _flood = [f for f in _flood if
                              in_bounds(f) and grid[f[1]][f[0]] == grid[y][x] and f not in checked and f not in flood]
                    flood += _flood

    return grid, checked


def part1():
    grid, checked = prep()

    area = defaultdict(lambda: 0)
    perimeter = defaultdict(lambda: 0)
    for coords, (c, i) in checked.items():
        area[f"{c}{i}"] += 1
        border = [add(coords, d) for d in directions]
        perimeter[f"{c}{i}"] += len([b for b in border if not in_bounds(b) or grid[b[1]][b[0]] != c])

    return sum([area[k] * perimeter[k] for k in area])


def part2():
    grid, checked = prep()

    area = defaultdict(lambda: 0)
    h_sides = defaultdict(lambda: [])
    v_sides = defaultdict(lambda: [])
    for (x, y), (c, i) in checked.items():
        area[f"{c}{i}"] += 1
        for dx, dy in directions[::2]:
            ax, ay = add((x, y), (dx, dy))
            if not in_bounds((ax, ay)) or grid[ay][ax] != c:
                h_sides[f"{c}{i}"].append((x, y + (dy / 10)))
        for dx, dy in directions[1::2]:
            ax, ay = add((x, y), (dx, dy))
            if not in_bounds((ax, ay)) or grid[ay][ax] != c:
                v_sides[f"{c}{i}"].append((x + (dx / 10), y))

    sides = defaultdict(lambda: 0)
    for k, ls in h_sides.items():
        for _, g in groupby(sorted(ls, key=lambda t: t[1]), key=lambda t: t[1]):
            g = sorted(list(g))
            s = 1
            for (a, _), (b, _) in zip(g, g[1:]):
                if abs(a - b) > 1:
                    s += 1
            sides[k] += s
    for k, ls in v_sides.items():
        for _, g in groupby(sorted(ls, key=lambda t: t[0]), key=lambda t: t[0]):
            g = sorted(list(g))
            s = 1
            for (_, a), (_, b) in zip(g, g[1:]):
                if abs(a - b) > 1:
                    s += 1
            sides[k] += s

    return sum([area[k] * sides[k] for k in area])


print(part1())
print(part2())
