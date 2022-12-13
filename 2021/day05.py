from collections import defaultdict


with open("addenda/input05.txt", 'r') as file:
    lines = file.readlines()


def sign(n):
    if n < 0:
        return -1
    elif n > 0:
        return 1
    return 0


def part1():
    vents = defaultdict(lambda: 0)

    for line in lines:
        (x1, y1), (x2, y2) = ((int(n) for n in ln.split(',')) for ln in line.strip().split(' -> '))

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                vents[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                vents[(x, y1)] += 1

    return len([c for c in vents.items() if c[1] >= 2])


def part2():
    vents = defaultdict(lambda: 0)

    for line in lines:
        (x1, y1), (x2, y2) = ((int(n) for n in ln.split(',')) for ln in line.strip().split(' -> '))

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                vents[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                vents[(x, y1)] += 1
        elif abs(x1 - x2) == abs(y1 - y2):
            if sign(x1 - x2) == sign(y1 - y2):
                for x, y in zip(range(min(x1, x2), max(x1, x2) + 1), range(min(y1, y2), max(y1, y2) + 1)):
                    vents[(x, y)] += 1
            else:
                if sign(x1 - x2) == -1:
                    for x, y in zip(range(min(x1, x2), max(x1, x2) + 1), range(max(y1, y2), min(y1, y2) - 1, -1)):
                        vents[(x, y)] += 1
                else:
                    for x, y in zip(range(max(x1, x2), min(x1, x2) - 1, -1), range(min(y1, y2), max(y1, y2) + 1)):
                        vents[(x, y)] += 1

    return len([c for c in vents.items() if c[1] >= 2])


print(part1())
print(part2())
