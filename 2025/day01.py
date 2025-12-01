with open("addenda/input01.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def part1():
    at = 50
    total = 0

    for dir, *num in lines:
        num = int(''.join(num))
        if dir == 'L': at = (at - num) % 100
        if dir == 'R': at = (at + num) % 100
        if at == 0: total += 1
    
    return total


def part2():
    at = 50
    total = 0

    for dir, *num in lines:
        num = int(''.join(num))
        for _ in range(num):
            if dir == 'L': at = (at - 1) % 100
            if dir == 'R': at = (at + 1) % 100
            if at == 0: total += 1
    
    return total


print(part1())
print(part2())
