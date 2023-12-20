from math import inf
from collections import defaultdict


with open("addenda/input17.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]

    width = len(lines[0])
    height = len(lines)


LEFT = (-1, 0)
UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)


ORTHOGONAL = {
    LEFT: (UP, DOWN),
    RIGHT: (UP, DOWN),
    UP: (LEFT, RIGHT),
    DOWN: (LEFT, RIGHT)
}


def get_options(tile):
    pos, dir, n = tile
    options = []

    if n < 2:
        dx, dy = pos[0] + dir[0], pos[1] + dir[1]
        if 0 <= dx < width and 0 <= dy < height:
            options.append(((dx, dy), dir, n + 1))

    for d in ORTHOGONAL[dir]:
        dx, dy = pos[0] + d[0], pos[1] + d[1]
        if 0 <= dx < width and 0 <= dy < height:
            options.append(((dx, dy), d, 0))

    return options


def get_ultra_options(tile):
    pos, dir, n = tile
    options = []

    if n < 9:
        dx, dy = pos[0] + dir[0], pos[1] + dir[1]
        if 0 <= dx < width and 0 <= dy < height:
            options.append(((dx, dy), dir, n + 1))

    if n >= 3:
        for d in ORTHOGONAL[dir]:
            dx, dy = pos[0] + d[0], pos[1] + d[1]
            if 0 <= dx < width and 0 <= dy < height:
                options.append(((dx, dy), d, 0))

    return options


def dijkstra(options_func, mx, end_func=lambda _: True):
    grid = [[int(c) for c in line] for line in lines]

    visited = defaultdict(lambda: inf)
    options = [
        ((0, 0), DOWN, mx),
        ((0, 0), LEFT, mx),
    ]
    for option in options:
        visited[option] = 0

    for option in options:
        for new_option in options_func(option):
            (x, y), _, _ = new_option
            if (n := visited[option] + grid[y][x]) < visited[new_option]:
                visited[new_option] = n
                options.append(new_option)

    return min([visited[option] for option in options if (height - 1, width - 1) in option and end_func(option)])


def part1():
    return dijkstra(get_options, 2)


def part2():
    return dijkstra(get_ultra_options, 9, lambda o: o[2] >= 3)


print(part1())
print(part2())
