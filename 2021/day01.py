with open("addenda/input01.txt", 'r') as file:
    lines = file.readlines()


def part1():
    depths = [int(line) for line in lines]
    total = 0

    for a, b in zip(depths, depths[1:]):
        if b > a:
            total += 1

    return total


def part2():
    depths = [int(line) for line in lines]
    total = 0

    for a, b, c, d in zip(depths, depths[1:], depths[2:], depths[3:]):
        if b + c + d > a + b + c:
            total += 1

    return total


print(part1())
print(part2())
