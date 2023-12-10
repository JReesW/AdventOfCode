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
    'J': ((0, -1), (-1, 0)),  # left or up
    'F': ((0, 1), (1, 0)),  # right or down
    'L': ((0, 1), (-1, 0))  # right or up
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
    for mover in movers:
        dist_grid[mover[0]][mover[1]] = 1

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

    new_lines = []
    for row, drow in zip(grid, dist_grid):
        line = ""
        for c, d in zip(row, drow):
            if d is None:
                line += '\033[91m' + '.' + '\033[0m'
            else:
                line += '\033[92m' + c + '\033[0m'
        new_lines.append(
            line.replace('7', '┐')
            .replace('F', '┌')
            .replace('J', '┘')
            .replace('L', '└')
            .replace('-', '─')
            .replace('|', '│')
        )

    for line in new_lines:
        print(line)

    """
    And now, seeing as I didn't solve it algorithmically, it's time to do it by hand ;)
    I took a screenshot of the output (making sure there was no line-spacing between lines)
    Put the screenshot in paint.net and flooded the inside part with a single color.
    Then you can see all red . characters that are surrounded by the flooding color.
    Count those by hand and there's your answer lmao
    """

    return "Have fun! ;)"


print(part1())
print(part2())
