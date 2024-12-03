import re

with open("addenda/input03.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def part1():
    total = 0
    for line in lines:
        for match in re.findall(r'mul\((\d+),(\d+)\)', line):
            a, b = match
            total += int(a) * int(b)
    return total


def part2():
    total = 0
    do = True
    for line in lines:
        for match in re.findall(r'mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))', line):
            a, b, c, d = match
            if c == 'do()':
                do = True
            elif d == "don't()":
                do = False
            elif do:
                total += int(a) * int(b)
    return total


print(part1())
print(part2())
