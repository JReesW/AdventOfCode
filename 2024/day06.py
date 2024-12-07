with open("addenda/input06.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def prep():
    guard = None
    grid = []

    for y, line in enumerate(lines):
        grid.append([])
        for x, col in enumerate(line):
            if col == '^':
                guard = x, y
                grid[y].append('X')
            else:
                grid[y].append(col)

    return guard, grid


def part1(p2=False):
    guard, grid = prep()
    d = 0
    visited = set()

    while 0 < guard[0] < len(grid[0]) - 1 and 0 < guard[1] < len(grid) - 1:
        res = guard[0] + directions[d][0], guard[1] + directions[d][1]
        if grid[res[1]][res[0]] == '#':
            d = (d + 1) % 4
        else:
            guard = res
        grid[guard[1]][guard[0]] = 'X'
        visited.add(guard)

    if p2:
        return visited
    return sum([row.count('X') for row in grid])


def part2():
    total = 0

    for x, y in part1(True):

        guard, grid = prep()
        d = 0
        grid[y][x] = 'O'

        visited = set()

        while 0 < guard[0] < len(grid[0]) - 1 and 0 < guard[1] < len(grid) - 1:
            res = guard[0] + directions[d][0], guard[1] + directions[d][1]
            if grid[res[1]][res[0]] in '#O':
                d = (d + 1) % 4
            else:
                guard = res
            if (*guard, d) in visited:
                total += 1
                break
            visited.add((*guard, d))

    return total


print(part1())
print(part2())
