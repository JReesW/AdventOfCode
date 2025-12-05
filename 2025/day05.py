from bisect import insort_left


with open("addenda/input05.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def part1():
    total = 0
    ranges = []

    for line in [l for l in lines if '-' in l]:
        begin, end = line.split('-')
        begin, end = int(begin), int(end)
        ranges.append((begin, end))
    
    for line in [l for l in lines if '-' not in l and l]:
        n = int(line)
        for b, e in ranges:
            if b <= n <= e:
                total += 1
                break
    
    return total


def part2():
    ranges = []
    for line in [l for l in lines if '-' in l]:
        begin, end = line.split('-')
        r = int(begin), int(end)
        insort_left(ranges, r)
    
    i = 0
    while i < len(ranges) - 1:
        (bx, ex), (by, ey) = ranges[i:i+2]
        if bx <= by <= ex or bx <= ey <= ex:
            ranges[i] = min(bx, by), max(ex, ey)
            ranges.pop(i+1)
        else: i+= 1
    
    return sum(e - b + 1 for b, e in ranges)


print(part1())
print(part2())
