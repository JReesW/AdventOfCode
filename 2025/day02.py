with open("addenda/input02.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def part1():
    total = 0
    for pair in lines[0].split(','):
        start, end = [max(10, int(p)) for p in pair.split('-')]
        for single in range(start, end+1):
            half = str(single)[:len(str(single))//2]
            if single == int(half+half):
                total += int(single)
            

    return total


def part2():
    total = 0
    for pair in lines[0].split(','):
        start, end = [max(10, int(p)) for p in pair.split('-')]
        for single in range(start, end+1):
            for d in range(1, len(str(single))):
                part = str(single)[:d]
                if single == int(part*(len(str(single)) // d)):
                    total += int(single)
                    break
    return total


print(part1())
print(part2())
