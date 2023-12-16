with open("addenda/input16.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


LEFT = (-1, 0)
UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)


def get_energized(grid, start):
    visited = set()
    active = [start]

    while active:
        new_active = []

        for x, y, d in active:
            new_pos = x + d[0], y + d[1]

            if 0 <= new_pos[0] < len(grid[0]) and 0 <= new_pos[1] < len(grid):
                match grid[new_pos[1]][new_pos[0]]:
                    case '.':
                        new_active.append((*new_pos, d))
                    case '-' if d in (LEFT, RIGHT):
                        new_active.append((*new_pos, d))
                    case '-':
                        new_active.append((*new_pos, LEFT))
                        new_active.append((*new_pos, RIGHT))
                    case '|' if d in (UP, DOWN):
                        new_active.append((*new_pos, d))
                    case '|':
                        new_active.append((*new_pos, UP))
                        new_active.append((*new_pos, DOWN))
                    case '/':
                        new_d = RIGHT
                        if d == LEFT:
                            new_d = DOWN
                        elif d == DOWN:
                            new_d = LEFT
                        elif d == RIGHT:
                            new_d = UP
                        new_active.append((*new_pos, new_d))
                    case '\\':
                        new_d = LEFT
                        if d == LEFT:
                            new_d = UP
                        elif d == DOWN:
                            new_d = RIGHT
                        elif d == RIGHT:
                            new_d = DOWN
                        new_active.append((*new_pos, new_d))

        new_active = [n for n in new_active if n not in visited]
        visited |= set(new_active)
        active = new_active[::]

    unique_pos = set()
    for x, y, d in visited:
        unique_pos.add((x, y))

    return len(unique_pos)


def part1():
    grid = [list(line) for line in lines]

    return get_energized(grid, (-1, 0, RIGHT))


def part2():
    grid = [list(line) for line in lines]
    best = 0

    for y in range(len(grid)):
        best = max(best, get_energized(grid, (-1, y, RIGHT)))
        best = max(best, get_energized(grid, (len(grid[0]), y, LEFT)))
    for x in range(len(grid[0])):
        best = max(best, get_energized(grid, (x, -1, DOWN)))
        best = max(best, get_energized(grid, (x, len(grid), UP)))

    return best


print(part1())
print(part2())
