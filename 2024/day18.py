with open("addenda/input18.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
width = height = 71


def walk(grid):
    checks = [(0, 0)]
    grid[0][0] = 0
    while checks:
        check = checks.pop(0)
        for d in directions:
            new_check = check[0] + d[0], check[1] + d[1]
            if 0 <= new_check[0] < width and 0 <= new_check[1] < height:
                if grid[new_check[1]][new_check[0]] == '.':
                    checks.append(new_check)
                    grid[new_check[1]][new_check[0]] = grid[check[1]][check[0]] + 1

    return grid[height - 1][width - 1]


def part1():
    grid = [['.' for _ in range(width)] for _ in range(height)]
    for line in lines[:1024]:
        x, y = [int(n) for n in line.split(',')]
        grid[y][x] = '#'

    return walk(grid)


def part2():
    grid = [['.' for _ in range(width)] for _ in range(height)]
    for line in lines[:1024]:
        x, y = [int(n) for n in line.split(',')]
        grid[y][x] = '#'

    i = 1024
    while True:
        x, y = [int(n) for n in lines[i].split(',')]
        grid[y][x] = '#'
        if walk([row[:] for row in grid]) == '.':
            return lines[i]
        i += 1


print(part1())
print(part2())
