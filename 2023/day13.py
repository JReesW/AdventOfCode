with open("addenda/input13.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def parse_grid():
    grids = []

    grid = []
    for line in lines:
        if len(line) == 0:
            grids.append(grid[::])
            grid = []
        else:
            grid.append(line)
    grids.append(grid[::])

    return grids


def str_diff(a, b):
    return len([0 for x, y in zip(a, b) if x != y])


def find_reflecting_row(grid, diff):
    for i in range(1, len(grid)):
        if sum(str_diff(a, b) for a, b in zip(grid[:i][::-1], grid[i:])) == diff:
            return i
    return 0


def get_grid_value(grid, diff):
    if row := find_reflecting_row(grid, diff):
        return 100 * row
    if col := find_reflecting_row(list(zip(*grid)), diff):
        return col


def part1():
    grids = parse_grid()

    return sum(get_grid_value(grid, 0) for grid in grids)


def part2():
    grids = parse_grid()

    return sum(get_grid_value(grid, 1) for grid in grids)


print(part1())
print(part2())
