with open("addenda/test.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def str_diff(a, b):
    return len([0 for x, y in zip(a, b) if x != y])


def find_mirror(grid, flip=False, p2=False):
    if flip:
        grid = ["".join([row[x] for row in grid]) for x in range(len(grid[0]))]

    for i, (a, b) in enumerate(zip(grid, grid[1:])):
        if p2:
            total_diff = 0
            if str_diff(a, b) <= 1:
                total_diff += str_diff(a, b)
                for x, y in zip(grid[:i+1][::-1], grid[i+1:]):
                    d = str_diff(x, y)
                    total_diff += d
                    if d >= 2:
                        break
                else:
                    res = (i + 1) * (1 if flip else 100)
                    if total_diff <= 1 and res != p2:
                        return res
        else:
            if a == b:
                for x, y in zip(grid[:i+1][::-1], grid[i+1:]):
                    if x != y:
                        break
                else:
                    return (i + 1) * (1 if flip else 100)

    if not flip:
        return find_mirror(grid, True, p2)
    raise Exception


def part1(p2=False):
    grids = []

    grid = []
    for line in lines:
        if len(line) == 0:
            grids.append(grid[::])
            grid = []
        else:
            grid.append(line)
    grids.append(grid[::])

    res = [find_mirror(grid) for grid in grids]

    return res if p2 else sum(res)


def part2():
    grids = []

    grid = []
    for line in lines:
        if len(line) == 0:
            grids.append(grid[::])
            grid = []
        else:
            grid.append(line)
    grids.append(grid[::])

    # for grid in grids:
    #     print(find_mirror(grid))
    p1 = part1(True)

    return sum([find_mirror(grid, p2=p1[i]) for i, grid in enumerate(grids)])


print(part1())
print(part2())
