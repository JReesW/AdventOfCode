with open("addenda/input02.txt", 'r') as file:
    lines = file.readlines()


def part1():
    pos = 0
    depth = 0

    for line in lines:
        match line.strip().split(' '):
            case ["forward", n]:
                pos += int(n)
            case ["down", n]:
                depth += int(n)
            case ["up", n]:
                depth -= int(n)

    return pos * depth


def part2():
    pos = 0
    depth = 0
    aim = 0

    for line in lines:
        match line.strip().split(' '):
            case ["forward", n]:
                pos += int(n)
                depth += aim * int(n)
            case ["down", n]:
                aim += int(n)
            case ["up", n]:
                aim -= int(n)

    return pos * depth


print(part1())
print(part2())
