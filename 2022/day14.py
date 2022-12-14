with open("addenda/input14.txt", 'r') as file:
    lines = file.readlines()


def part1():
    paths = []
    for line in lines:
        paths.append([[int(c) for c in coords.split(',')] for coords in line.split(' -> ')])
    xmax, xmin, ymax, ymin = -99999, 99999, -99999, 99999
    for path in paths + [[[500, 0]]]:
        for coord in path:
            x, y = coord
            xmax = x if x > xmax else xmax
            xmin = x if x < xmin else xmin
            ymax = y if y > ymax else ymax
            ymin = y if y < ymin else ymin
    offsetx, offsety = xmin - 1, ymin - 1
    grid = [['.' for _ in range(xmax - xmin + 3)] for _ in range(ymax - ymin + 3)]

    for path in paths:
        for (x1, y1), (x2, y2) in zip(path, path[1:]):
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    grid[y - offsety][x1 - offsetx] = '#'
            else:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    grid[y1 - offsety][x - offsetx] = '#'

    try:
        while True:
            sand = [500, 0]

            while True:
                if grid[sand[1] - offsety + 1][sand[0] - offsetx] == '.':
                    sand[1] += 1
                elif grid[sand[1] - offsety + 1][sand[0] - offsetx - 1] == '.':
                    sand[0] -= 1
                    sand[1] += 1
                elif grid[sand[1] - offsety + 1][sand[0] - offsetx + 1] == '.':
                    sand[0] += 1
                    sand[1] += 1
                else:
                    grid[sand[1] - offsety][sand[0] - offsetx] = 'o'
                    break
    except IndexError:
        total = 0
        for row in grid:
            total += row.count('o')
        return total


def part2():
    paths = []
    for line in lines:
        paths.append([[int(c) for c in coords.split(',')] for coords in line.split(' -> ')])
    xmax, xmin, ymax, ymin = -99999, 99999, -99999, 99999
    for path in paths + [[[500, 0]]]:
        for coord in path:
            x, y = coord
            xmax = x if x > xmax else xmax
            xmin = x if x < xmin else xmin
            ymax = y if y > ymax else ymax
            ymin = y if y < ymin else ymin
    offsetx, offsety = xmin - 300, ymin - 1
    grid = [['.' if y < ymax+3 else '#' for _ in range(xmax - xmin + 610)] for y in range(ymax - ymin + 4)]

    for path in paths:
        for (x1, y1), (x2, y2) in zip(path, path[1:]):
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    grid[y - offsety][x1 - offsetx] = '#'
            else:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    grid[y1 - offsety][x - offsetx] = '#'

    try:
        while True:
            sand = [500, 0]

            while True:
                if grid[sand[1] - offsety + 1][sand[0] - offsetx] == '.':
                    sand[1] += 1
                elif grid[sand[1] - offsety + 1][sand[0] - offsetx - 1] == '.':
                    sand[0] -= 1
                    sand[1] += 1
                elif grid[sand[1] - offsety + 1][sand[0] - offsetx + 1] == '.':
                    sand[0] += 1
                    sand[1] += 1
                else:
                    grid[sand[1] - offsety][sand[0] - offsetx] = 'o'
                    if sand[1] == 0 and sand[0] == 500:
                        raise IndexError
                    break
    except IndexError:
        total = 0
        for row in grid:
            total += row.count('o')
        return total


print(part1())
print(part2())
