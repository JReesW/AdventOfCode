with open("addenda/input03.txt", 'r') as file:
    lines = file.readlines()


alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def part1():
    total = 0

    for line in lines:
        left, right = set(line[:len(line) // 2]), set(line[len(line) // 2:].strip())

        total += sum(alphabet.index(c) for c in left & right)

    return total


def part2():
    total = 0

    for threes in zip(lines[::3], lines[1::3], lines[2::3]):
        one, two, three = (set(n.strip()) for n in threes)
        total += sum(alphabet.index(c) for c in one & two & three)

    return total


print(part1())
print(part2())
