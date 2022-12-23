import re


with open("addenda/input22.txt", 'r') as file:
    lines = file.readlines()


directions = [
    (1, 0),   # right
    (0, 1),   # down
    (-1, 0),  # left
    (0, -1)   # up
]


def parse_input():
    grid = {}
    commands = None

    for y, line in enumerate(lines):
        line = line.rstrip()
        if '.' in line or '#' in line:
            for x, c in enumerate(line):
                if c in {'.', '#'}:
                    grid[(x + 1, y + 1)] = c
        elif len(line) < 3:
            pass
        else:
            commands = [n if n in {'L', 'R'} else int(n) for n in re.findall(r"\d+|[LR]", line)]

    return grid, commands


def part1():
    grid, commands = parse_input()

    pos = list(sorted([k for k in grid if k[1] == 1]))[0]
    direction = 0

    for command in commands:
        if command == 'L':
            direction = (direction - 1) % 4
        elif command == 'R':
            direction = (direction + 1) % 4
        else:
            for _ in range(command):
                new_pos = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])
                if new_pos not in grid:
                    minmax = (min, max)[direction // 2]
                    i = (direction + 1) % 2
                    new_pos = minmax([g for g in grid if g[i] == pos[i]])

                if grid[new_pos] == '.':
                    pos = new_pos

    return pos[1] * 1000 + pos[0] * 4 + direction


permitted_dirs_example = {
    0: {10, 12, 13},
    1: {5, 6, 7, 8},
    2: {1, 4, 9},
    3: {0, 2, 3, 11}
}


connections_example = {
    # red top-left
    tuple((i, 5) for i in range(5, 9)): tuple(((9, i), 0) for i in range(1, 5)),
    tuple((9, i) for i in range(1, 5)): tuple(((i, 5), 1) for i in range(5, 9)),

    # green top-left
    tuple((i, 5) for i in range(1, 5)): tuple(((i, 1), 1) for i in range(12, 8, -1)),
    tuple((i, 1) for i in range(12, 8, -1)): tuple(((i, 5), 1) for i in range(1, 5)),

    # blue bottom-left
    tuple((1, i) for i in range(5, 9)): tuple(((i, 12), 3) for i in range(13, 17)),
    tuple((i, 12) for i in range(13, 17)): tuple(((1, i), 0) for i in range(5, 9)),

    # green bottom-left
    tuple((i, 8) for i in range(1, 5)): tuple(((i, 12), 3) for i in range(12, 8, -1)),
    tuple((i, 12) for i in range(12, 8, -1)): tuple(((i, 8), 3) for i in range(1, 5)),

    # red bottom-left
    tuple((i, 8) for i in range(5, 9)): tuple(((9, i), 0) for i in range(12, 8, -1)),
    tuple((9, i) for i in range(12, 8, -1)): tuple(((i, 8), 3) for i in range(5, 9)),

    # red right
    tuple((12, i) for i in range(5, 9)): tuple(((i, 9), 1) for i in range(16, 12, -1)),
    tuple((i, 9) for i in range(16, 12, -1)): tuple(((12, i), 2) for i in range(5, 9)),

    # blue right
    tuple((12, i) for i in range(1, 5)): tuple(((16, i), 2) for i in range(12, 8, -1)),
    tuple((16, i) for i in range(12, 8, -1)): tuple(((12, i), 2) for i in range(1, 5)),
}


permitted_dirs = {
    0: {2, 4, 10, 11},
    1: {3, 5, 12},
    2: {1, 6, 7, 8},
    3: {0, 9, 13}
}


connections = {
    # red top-left
    tuple((i, 101) for i in range(1, 51)): tuple(((51, i), 0) for i in range(51, 101)),  # 0
    tuple((51, i) for i in range(51, 101)): tuple(((i, 101), 1) for i in range(1, 51)),  # 1

    # red top-right
    tuple((100, i) for i in range(51, 101)): tuple(((i, 50), 3) for i in range(101, 151)),  # 2
    tuple((i, 50) for i in range(101, 151)): tuple(((100, i), 2) for i in range(51, 101)),  # 3

    # red bottom
    tuple((50, i) for i in range(151, 201)): tuple(((i, 150), 3) for i in range(51, 101)),  # 4
    tuple((i, 150) for i in range(51, 101)): tuple(((50, i), 2) for i in range(151, 201)),  # 5

    # blue left
    tuple((1, i) for i in range(101, 151)): tuple(((51, i), 0) for i in range(50, 0, -1)),  # 6
    tuple((51, i) for i in range(50, 0, -1)): tuple(((1, i), 0) for i in range(101, 151)),  # 7

    # green left
    tuple((1, i) for i in range(151, 201)): tuple(((i, 1), 1) for i in range(51, 101)),  # 8
    tuple((i, 1) for i in range(51, 101)): tuple(((1, i), 0) for i in range(151, 201)),  # 9

    # blue right
    tuple((100, i) for i in range(101, 151)): tuple(((150, i), 2) for i in range(50, 0, -1)),  # 10
    tuple((150, i) for i in range(50, 0, -1)): tuple(((100, i), 2) for i in range(101, 151)),  # 11

    # green right
    tuple((i, 200) for i in range(1, 51)): tuple(((i, 1), 1) for i in range(101, 151)),  # 12
    tuple((i, 1) for i in range(101, 151)): tuple(((i, 200), 3) for i in range(1, 51)),  # 13

}


def part2():
    grid, commands = parse_input()

    pos = list(sorted([k for k in grid if k[1] == 1]))[0]
    direction = 0

    for command in commands:
        if command == 'L':
            direction = (direction - 1) % 4
        elif command == 'R':
            direction = (direction + 1) % 4
        else:
            for _ in range(command):
                new_pos = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])
                new_dir = direction
                if new_pos not in grid:
                    for i, conn in enumerate(connections):
                        if i in permitted_dirs[direction]:
                            if pos in conn:
                                new_pos, new_dir = connections[conn][conn.index(pos)]

                if grid[new_pos] == '.':
                    pos = new_pos
                    direction = new_dir

    return pos[1] * 1000 + pos[0] * 4 + direction


print(part1())
print(part2())
