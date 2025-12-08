from collections import defaultdict

with open("addenda/input07.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def part1():
    tachyons = set()
    splitters = set()
    max_depth = len(lines)
    for y, line in enumerate(lines):
        for x, col in enumerate(line):
            if col == 'S': tachyons.add((x, y))
            if col == '^': splitters.add((x, y))
    
    splits = 0
    for _ in range(max_depth):
        new_tachyons = set()
        for x, y in tachyons:
            if (x, y+1) in splitters:
                new_tachyons.add((x-1, y+1))
                new_tachyons.add((x+1, y+1))
                splits += 1
            else: new_tachyons.add((x, y+1))
        tachyons = new_tachyons
    return splits


def part2():
    tachyons = {}
    splitters = set()
    max_depth = len(lines)
    for y, line in enumerate(lines):
        for x, col in enumerate(line):
            if col == 'S': tachyons[(x, y)] = 1
            if col == '^': splitters.add((x, y))
    
    for _ in range(max_depth):
        new_tachyons = defaultdict(lambda: 0)
        for (x, y), v in tachyons.items():
            if (x, y+1) in splitters:
                new_tachyons[(x-1, y+1)] += v
                new_tachyons[(x+1, y+1)] += v
            else: new_tachyons[(x, y+1)] += v
        tachyons = new_tachyons
    return sum(tachyons.values())


print(part1())
print(part2())
