import re

with open("addenda/input14.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]

width = 101
height = 103


def part1():
    robots = []
    for line in lines:
        px, py, vx, vy = [int(m) for m in re.findall(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line)[0]]
        robots.append(((px + vx * 100) % width, (py + vy * 100) % height))

    x_mid = width // 2
    y_mid = height // 2
    totals = [0, 0, 0, 0]
    for x in range(x_mid):
        for y in range(y_mid):
            if (c := (x, y)) in robots:
                totals[0] += robots.count(c)
            if (c := (x + x_mid + 1, y)) in robots:
                totals[1] += robots.count(c)
            if (c := (x, y + y_mid + 1)) in robots:
                totals[2] += robots.count(c)
            if (c := (x + x_mid + 1, y + y_mid + 1)) in robots:
                totals[3] += robots.count(c)

    return totals[0] * totals[1] * totals[2] * totals[3]


def part2():
    robots = []
    for line in lines:
        px, py, vx, vy = [int(m) for m in re.findall(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line)[0]]
        robots.append((px, py, vx, vy))

    second = 0
    while True:
        second += 1
        new_robots = []

        for px, py, vx, vy in robots:
            new_robots.append(((px + vx) % width, (py + vy) % height, vx, vy))
        robots = new_robots

        count = {}
        for x, y, _, _ in robots:
            if (x, y) not in count:
                count[(x, y)] = 0
            count[(x, y)] += 1

        if all([n == 1 for n in count.values()]):
            grid = [['.' for _ in range(width)] for _ in range(height)]
            for x, y, _, _ in robots:
                grid[y][x] = '#'

            for line in grid:
                print(''.join(line))
            return second




print(part1())
print(part2())
