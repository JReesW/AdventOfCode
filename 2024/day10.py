with open("addenda/input10.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def part1(p2=False):
    total = 0
    grid = []
    trailheads = []
    for y, line in enumerate(lines):
        grid.append([])
        for x, c in enumerate(line):
            grid[y].append(int(c))
            if c == '0':
                trailheads.append((x, y))

    for trailhead in trailheads:
        trails = [trailhead]
        for i in range(1, 10):
            _trails = []
            for trail in trails:
                for d in directions:
                    t = trail[0] + d[0], trail[1] + d[1]
                    if 0 <= t[0] < len(grid[0]) and 0 <= t[1] < len(grid) and grid[t[1]][t[0]] == i:
                        _trails.append(t)
            trails = _trails
        trails = trails if p2 else set(trails)
        total += len(trails)

    return total


def part2():
    return part1(True)


print(part1())
print(part2())
