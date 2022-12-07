with open("addenda/input01.txt", 'r') as file:
    lines = file.readlines()


def prep():
    total = []
    current = []

    for line in lines:
        if line.strip().isnumeric():
            current.append(int(line))
        else:
            total.append(current)
            current = []
    return total


def part1():
    total = prep()
    return sorted([sum(t) for t in total], reverse=True)[0]


def part2():
    total = prep()
    return sum(sorted([sum(t) for t in total], reverse=True)[:3])


print(part1())
print(part2())
