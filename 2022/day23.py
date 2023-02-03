with open("addenda/input23.txt", 'r') as file:
    lines = file.readlines()


def print_grid(elves):
    grid = {elf.pos for elf in elves}
    xs, ys = list(map(list, zip(*grid)))
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)

    for y in range(ymin, ymax + 1):
        line = ""
        for x in range(xmin, xmax + 1):
            if (x, y) in grid:
                line += '#'
            else:
                line += '.'
        print(line)
    print('')


def unoccupied(elves):
    grid = {elf.pos for elf in elves}
    xs, ys = list(map(list, zip(*grid)))
    width = max(xs) - min(xs) + 1
    height = max(ys) - min(ys) + 1

    return (width * height) - len(elves)


directions = [
    ((-1, -1), (0, -1), (1, -1)),
    ((-1, 1), (0, 1), (1, 1)),
    ((-1, -1), (-1, 0), (-1, 1)),
    ((1, -1), (1, 0), (1, 1)),
]


class Elf:
    def __init__(self, pos):
        self.pos = pos
        self.proposition = None

    def offset(self, pos):
        return self.pos[0] + pos[0], self.pos[1] + pos[1]

    def __repr__(self):
        return f"<{self.pos} -> {self.proposition}>"


def part1():
    elves = []

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                elves.append(Elf((x, y)))

    for _ in range(10):
        positions = {elf.pos for elf in elves}
        for elf in elves:
            elf.proposition = None
            if any(occupied := [any([elf.offset(d) in positions for d in direction]) for direction in directions]):
                for d, b in zip(directions, occupied):
                    if not b:
                        elf.proposition = elf.offset(d[1])
                        break
        ps = [elf.proposition for elf in elves if elf.proposition is not None]
        p_counts = {p: ps.count(p) for p in ps}

        for elf in elves:
            if elf.proposition is not None and p_counts[elf.proposition] == 1:
                elf.pos = elf.proposition
        directions.append(directions.pop(0))

    return unoccupied(elves)


def part2():
    elves = []

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                elves.append(Elf((x, y)))

    rnd = 1
    while True:
        rnd += 1
        if rnd % 100 == 0:
            print(rnd)
        positions = {elf.pos for elf in elves}
        for elf in elves:
            elf.proposition = None
            if any(occupied := [any([elf.offset(d) in positions for d in direction]) for direction in directions]):
                for d, b in zip(directions, occupied):
                    if not b:
                        elf.proposition = elf.offset(d[1])
                        break
        ps = [elf.proposition for elf in elves if elf.proposition is not None]
        p_counts = {p: ps.count(p) for p in ps}

        for elf in elves:
            if elf.proposition is not None and p_counts[elf.proposition] == 1:
                elf.pos = elf.proposition

        new_positions = {elf.pos for elf in elves}
        if positions == new_positions:
            break
        directions.append(directions.pop(0))

    return rnd


print(part1())
print(part2())
