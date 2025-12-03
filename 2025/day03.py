with open("addenda/input03.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def part1():
    total = 0
    for line in lines:
        top = 0
        for i, a in enumerate(line[:-1]):
            for b in line[i+1:]:
                if int(a+b) > top:
                    top = int(a+b)
        total += top
    return total


def part2():
    total = 0
    for line in lines:
        top = ""
        idx = -1
        for i in range(12):
            segment = line[idx+1 : -11 + i or None]
            idx = 1 + idx + segment.index(max(segment, key=int))
            top += line[idx]
        total += int(top)
    return total


print(part1())
print(part2())
