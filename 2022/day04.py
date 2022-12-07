with open("addenda/input04.txt") as file:
    lines = file.readlines()


def part1():
    total = 0

    for line in lines:
        a, b = ([int(l) for l in ln.split('-')] for ln in line.strip().split(','))
        a, b = set(range(a[0], a[1] + 1)), set(range(b[0], b[1] + 1))

        if a <= b or b <= a:
            total += 1

    return total


def part2():
    total = 0

    for line in lines:
        a, b = ([int(l) for l in ln.split('-')] for ln in line.strip().split(','))
        a, b = set(range(a[0], a[1] + 1)), set(range(b[0], b[1] + 1))

        if len(a & b):
            total += 1

    return total


print(part1())
print(part2())
