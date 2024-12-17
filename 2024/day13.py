import re
import numpy as np

with open("addenda/input13.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def prep():
    machines = []

    for i, line in enumerate(lines[::4]):
        ax, ay = re.findall(r'Button .: X\+(\d+), Y\+(\d+)', line)[0]
        bx, by = re.findall(r'Button .: X\+(\d+), Y\+(\d+)', lines[i * 4 + 1])[0]
        px, py = re.findall(r'Prize: X=(\d+), Y=(\d+)', lines[i * 4 + 2])[0]
        machines.append([int(x) for x in (ax, ay, bx, by, px, py)])

    return machines


def part1():
    machines = prep()

    total = 0
    for ax, ay, bx, by, px, py in machines:
        cheapest = 9999999
        for a in range(101):
            for b in range(101):
                if a * ax + b * bx == px and a * ay + b * by == py:
                    cheapest = min(cheapest, a * 3 + b)
        if cheapest < 9999999:
            total += cheapest

    return total


def part2():
    machines = prep()

    total = 0
    for ax, ay, bx, by, px, py in machines:
        Ma = np.asarray([[ax, bx], [ay, by]])
        Mb = np.asarray([px + 10000000000000, py + 10000000000000])
        a, b = np.linalg.solve(Ma, Mb)
        if (a % 1 <= 0.001 or a % 1 >= 0.999) and (b % 1 <= 0.001 or b % 1 >= 0.999):
            total += a * 3 + b

    return int(total)


print(part1())
print(part2())
