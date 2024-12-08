from collections import defaultdict
from itertools import permutations

with open("addenda/input08.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


in_bounds = lambda c: 0 <= c[0] < len(lines[0]) and 0 <= c[1] < len(lines)


def part1():
    antennae = defaultdict(list)
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != '.':
                antennae[char].append((x, y))

    antinodes = set()
    for _, locations in antennae.items():
        for a, b in permutations(locations, 2):
            d = (a[0] - b[0], a[1] - b[1])
            antinodes.add((a[0] + d[0], a[1] + d[1]))

    return len([a for a in antinodes if in_bounds(a)])


def part2():
    antennae = defaultdict(list)
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != '.':
                antennae[char].append((x, y))

    antinodes = set()
    for _, locations in antennae.items():
        for a, b in permutations(locations, 2):
            d = (a[0] - b[0], a[1] - b[1])
            antinodes.add(a)
            pos, neg = (a[0] + d[0], a[1] + d[1]), (a[0] - d[0], a[1] - d[1])
            while in_bounds(pos):
                antinodes |= {pos, neg}
                pos, neg = (pos[0] + d[0], pos[1] + d[1]), (neg[0] - d[0], neg[1] - d[1])

    return len([a for a in antinodes if in_bounds(a)])


print(part1())
print(part2())
