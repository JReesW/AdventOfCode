with open("addenda/input12.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


alphabet = "abcdefghijklmnopqrstuvwxyz"


def walkable(src, dst):
    if src == 'S':
        src = 'a'
    if dst == 'E':
        dst = 'z'
    if alphabet.index(dst) - alphabet.index(src) <= 1:
        return True
    return False


def fill(start):
    grid = [[None for _ in range(len(lines[0]))] for _ in range(len(lines))]
    goal = None
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] in start:
                grid[y][x] = 0
            if lines[y][x] == "E":
                goal = (y, x)

    cur = 0
    while any([None in row for row in grid]):
        for y in range(len(lines)):
            for x in range(len(lines[0])):
                if (y, x) == goal and grid[y][x] is not None:
                    return grid[y][x]
                if grid[y][x] == cur:
                    if y-1 >= 0 and grid[y-1][x] is None and walkable(lines[y][x], lines[y-1][x]):
                        grid[y-1][x] = cur + 1
                    if y+1 < len(lines) and grid[y+1][x] is None and walkable(lines[y][x], lines[y+1][x]):
                        grid[y+1][x] = cur + 1
                    if x-1 >= 0 and grid[y][x-1] is None and walkable(lines[y][x], lines[y][x-1]):
                        grid[y][x-1] = cur + 1
                    if x+1 < len(lines[0]) and grid[y][x+1] is None and walkable(lines[y][x], lines[y][x+1]):
                        grid[y][x+1] = cur + 1
        cur += 1


def part1():
    return fill("S")


def part2():
    return fill("aS")


print(part1())
print(part2())
