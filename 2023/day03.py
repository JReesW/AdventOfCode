import re


class BreakOut(Exception):
    pass


with open("addenda/input03.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def part1():
    num_pos = {}

    for y, line in enumerate(lines):
        for x, m in zip(re.finditer("\d+", line), re.findall("\d+", line)):
            num_pos[(x.start(0), y)] = m

    parts = 0

    for (x, y), num in num_pos.items():
        try:
            for i, _ in enumerate(num):
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        yy = max(min(y + dy, len(lines) - 1), 0)
                        xx = max(min(x + dx + i, len(lines[0]) - 1), 0)
                        if lines[yy][xx] not in "0123456789.":
                            raise BreakOut
        except BreakOut:
            parts += int(num)

    return parts


def prod(ls):
    res = 1
    for n in ls:
        res *= n
    return res


def part2():
    num_pos = {}

    for y, line in enumerate(lines):
        for x, m in zip(re.finditer("\d+", line), re.findall("\d+", line)):
            num_pos[(x.start(0), y)] = m

    gears = {}

    for (x, y), num in num_pos.items():
        try:
            for i, _ in enumerate(num):
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        yy = max(min(y + dy, len(lines) - 1), 0)
                        xx = max(min(x + dx + i, len(lines[0]) - 1), 0)
                        if lines[yy][xx] == '*':
                            if (xx, yy) not in gears:
                                gears[(xx, yy)] = [int(num)]
                            else:
                                gears[(xx, yy)].append(int(num))

                            raise BreakOut
        except BreakOut:
            continue

    return sum([prod(g) for g in gears.values() if len(g) >= 2])


print(part1())
print(part2())
