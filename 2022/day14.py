with open("addenda/test.txt", 'r') as file:
    lines = file.readlines()


def part1():
    paths = []
    for line in lines:
        paths.append([[int(c) for c in coords.split(',')] for coords in line.split(' -> ')])
    xmax, xmin, ymax, ymin = -99999, 99999, -99999, 99999
    for path in paths:
        for coord in path:
            x, y = coord
            xmax = x if x > xmax else xmax
            xmin = x if x < xmin else xmin
            ymax = y if y > ymax else ymax
            ymin = y if y < ymin else ymin
    offsetx, offsety = xmin - 1, ymin - 1
    grid = [['.' for _ in range(xmax - xmin + 3)] for _ in range(ymax - ymin + 3)]



def part2():
    pass


print(part1())
print(part2())
