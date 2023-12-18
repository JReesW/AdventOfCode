from numpy import array
import re


with open("addenda/input18.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


dirs = {
    'L': array([-1, 0]),
    'R': array([1, 0]),
    'U': array([0, -1]),
    'D': array([0, 1]),
    '0': (1, 0),
    '1': (0, 1),
    '2': (-1, 0),
    '3': (0, -1)
}


def alternating(grid, first, last, row):
    if 0 < row < len(grid) - 1:
        return ((grid[row + 1][first] == '#' and grid[row - 1][last] == '#') or
                (grid[row - 1][first] == '#' and grid[row + 1][last] == '#'))
    return False


def part1():
    # basically the same ray tracing thingamajig as in day 10
    mn_w, mn_h = 0, 0
    mx_w, mx_h = 0, 0
    pos = array([0, 0])

    for line in lines:
        d, n, _ = line.split(' ')
        n = int(n)
        pos += dirs[d] * n

        mn_w = min(mn_w, pos[0])
        mn_h = min(mn_h, pos[1])
        mx_w = max(mx_w, pos[0])
        mx_h = max(mx_h, pos[1])

    grid = [['.' for _ in range(mx_w - mn_w + 1)] for _ in range(mx_h - mn_h + 1)]
    pos = array([mn_w * -1, mn_h * -1])
    grid[pos[1]][pos[0]] = '#'

    for line in lines:
        d, n, _ = line.split(' ')

        for _ in range(int(n)):
            pos += dirs[d]
            grid[pos[1]][pos[0]] = '#'

    total = 0
    for y, row in enumerate(grid):
        row_text = ''.join(row)
        starts = [m.start() for m in re.finditer("#+", row_text) if alternating(grid, m.start(), m.end() - 1, y)]

        for x, c in enumerate(row):
            if c == '#':
                total += 1
            else:
                left = [s for s in starts if s < x]
                right = [s for s in starts if s > x]

                if (len(left) % 2 == 1 and right) or (len(right) % 2 == 1 and left):
                    total += 1
                    grid[y][x] = 'o'

    return total


def part2():
    # new method, which is just better in every imaginable way
    # not rewriting part 1 because I'm sorta proud of it
    x_pos = 0
    area = 1

    for line in lines:
        _, _, col = line.split(' ')
        n = int(col[2:7], 16)
        x, y = dirs[col[7]]
        x_pos += x * n
        area += (y * n) * x_pos + (n / 2)

    return int(area)


print(part1())
print(part2())
