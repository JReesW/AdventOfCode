with open("addenda/input01.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def part1():
    total = 0

    left, right = [], []
    for line in lines:
        l, r = line.split('   ')
        left.append(int(l))
        right.append(int(r))

    for l, r in zip(sorted(left), sorted(right)):
        total += abs(l - r)

    return total


def part2():
    total = 0

    left, right = [], []
    for line in lines:
        l, r = line.split('   ')
        left.append(int(l))
        right.append(int(r))

    for l in left:
        total += l * right.count(l)

    return total


print(part1())
print(part2())
