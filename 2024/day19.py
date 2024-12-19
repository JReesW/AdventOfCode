from functools import cache

with open("addenda/input19.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


@cache
def dive(towel, patterns):
    if towel == '':
        return 1
    _patterns = [pattern for pattern in patterns if towel.startswith(pattern)]
    return sum([dive(towel[len(pattern):], patterns) for pattern in _patterns])


def part1():
    patterns = tuple(lines[0].split(', '))
    requests = lines[2:]

    total = 0
    for towel in requests:
        if dive(towel, patterns):
            total += 1

    return total


def part2():
    patterns = tuple(lines[0].split(', '))
    requests = lines[2:]

    total = 0
    for towel in requests:
        total += dive(towel, patterns)

    return total


print(part1())
print(part2())
