with open("addenda/input04.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def part1():
    total = 0
    _lines = lines[::-1]

    for i in range(4):
        for y, line in enumerate(_lines):
            for x, char in enumerate(line):
                if char == 'X':
                    try:
                        if _lines[y][x+1] == 'M' and _lines[y][x+2] == 'A' and _lines[y][x+3] == 'S':
                            total += 1
                        if _lines[y+1][x+1] == 'M' and _lines[y+2][x+2] == 'A' and _lines[y+3][x+3] == 'S':
                            total += 1
                    except IndexError:
                        continue
        _lines = list(zip(*_lines[::-1]))

    return total


def part2():
    total = 0
    _lines = lines[::-1]

    for i in range(4):
        for y, line in enumerate(_lines):
            for x, char in enumerate(line):
                if char == 'A' and y > 0 and x > 0:
                    try:
                        if _lines[y-1][x-1] == 'M' and _lines[y+1][x+1] == 'S' and _lines[y-1][x+1] == 'M' and _lines[y+1][x-1] == 'S':
                            total += 1
                    except IndexError:
                        continue
        _lines = list(zip(*_lines[::-1]))

    return total


print(part1())
print(part2())
