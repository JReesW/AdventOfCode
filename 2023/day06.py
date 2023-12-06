import re


with open("addenda/input06.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def part1():
    times = [int(m) for m in re.findall("\d+", lines[0])]
    dists = [int(m) for m in re.findall("\d+", lines[1])]

    wins = 1
    for time, dist in zip(times, dists):
        w = 0
        for t in range(time):
            d = t * (time - t)
            if d > dist:
                w += 1
        wins *= w

    return wins


def part2():
    time = [int(m) for m in re.findall("\d+", lines[0].replace(' ', ''))][0]
    dist = [int(m) for m in re.findall("\d+", lines[1].replace(' ', ''))][0]

    wins = 0
    for t in range(time):
        d = t * (time - t)
        if d > dist:
            wins += 1

    return wins


print(part1())
print(part2())
