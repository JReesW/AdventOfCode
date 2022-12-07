with open("addenda/input06.txt") as file:
    line = file.readline()


def part1():
    for i, v in enumerate(zip(line, line[1:], line[2:], line[3:])):
        if len(set(v)) == 4:
            return i + 4


def part2():
    for i, v in enumerate(zip(line, line[1:], line[2:], line[3:], line[4:], line[5:], line[6:], line[7:], line[8:], line[9:], line[10:], line[11:], line[12:], line[13:])):
        if len(set(v)) == 14:
            return i + 14


print(part1())
print(part2())
