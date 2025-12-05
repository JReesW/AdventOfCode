with open("addenda/input04.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def part1():
    total = 0
    mx, my = len(lines[0])-1, len(lines)-1
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '@':
                adjacent = 0
                if y > 0 and lines[y-1][x] == '@': adjacent += 1
                if y > 0 and x < mx and lines[y-1][x+1] == '@': adjacent += 1
                if x < mx and lines[y][x+1] == '@': adjacent += 1
                if y < my and x < mx and lines[y+1][x+1] == '@': adjacent += 1
                if y < my and lines[y+1][x] == '@': adjacent += 1
                if y < my and x > 0 and lines[y+1][x-1] == '@': adjacent += 1
                if x > 0 and lines[y][x-1] == '@': adjacent += 1
                if y > 0 and x > 0 and lines[y-1][x-1] == '@': adjacent += 1
                if adjacent < 4: total += 1
    return total


def part2():
    grid = [[c for c in line] for line in lines]
    total = 0
    while True:
        removed = 0
        mx, my = len(grid[0])-1, len(grid)-1
        for y, line in enumerate(grid):
            for x, c in enumerate(line):
                if c == '@':
                    adjacent = 0
                    if y > 0 and grid[y-1][x] == '@': adjacent += 1
                    if y > 0 and x < mx and grid[y-1][x+1] == '@': adjacent += 1
                    if x < mx and grid[y][x+1] == '@': adjacent += 1
                    if y < my and x < mx and grid[y+1][x+1] == '@': adjacent += 1
                    if y < my and grid[y+1][x] == '@': adjacent += 1
                    if y < my and x > 0 and grid[y+1][x-1] == '@': adjacent += 1
                    if x > 0 and grid[y][x-1] == '@': adjacent += 1
                    if y > 0 and x > 0 and grid[y-1][x-1] == '@': adjacent += 1
                    if adjacent < 4: 
                        removed += 1
                        grid[y][x] = '.'
        total += removed
        if removed == 0: 
            break
    return total


print(part1())
print(part2())
