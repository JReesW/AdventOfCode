with open("addenda/input07.txt", 'r') as file:
    line = file.readline().strip()


def part1():
    pos = [int(n) for n in line.split(',')]
    best = 9999999999999

    for align in range(max(pos) + 1):
        total = 0

        for p in pos:
            total += abs(align - p)

        best = total if total < best else best

    return best


def part2():
    pos = [int(n) for n in line.split(',')]
    best = 9999999999999

    for align in range(max(pos) + 1):
        total = 0

        for p in pos:
            dist = abs(align - p)
            total += (dist * (dist + 1)) // 2

        best = total if total < best else best

    return best


print(part1())
print(part2())
