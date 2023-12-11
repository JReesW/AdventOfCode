with open("addenda/input11.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def parse():
    empty_hor = []
    empty_ver = []

    for y, line in enumerate(lines):
        if '#' not in line:
            empty_hor.append(y)

    for x in range(len(lines[0])):
        if '#' not in [line[x] for line in lines]:
            empty_ver.append(x)

    galaxies = []
    for y, row in enumerate(lines):
        for x, col in enumerate(row):
            if col == '#':
                galaxies.append((x, y))

    return empty_hor, empty_ver, galaxies


def part1():
    empty_hor, empty_ver, galaxies = parse()

    total_dist = 0
    for i, gal in enumerate(galaxies):
        for gal2 in galaxies[i + 1:]:
            hor_d = abs(gal[0] - gal2[0]) + len([e for e in empty_ver if min(gal[0], gal2[0]) < e < max(gal[0], gal2[0])])
            ver_d = abs(gal[1] - gal2[1]) + len([e for e in empty_hor if min(gal[1], gal2[1]) < e < max(gal[1], gal2[1])])
            total_dist += hor_d + ver_d

    return total_dist


def part2():
    empty_hor, empty_ver, galaxies = parse()

    total_dist = 0
    expansion = 1_000_000
    for i, gal in enumerate(galaxies):
        for gal2 in galaxies[i + 1:]:
            hor_d = abs(gal[0] - gal2[0]) + (expansion - 1) * len(
                [e for e in empty_ver if min(gal[0], gal2[0]) < e < max(gal[0], gal2[0])])
            ver_d = abs(gal[1] - gal2[1]) + (expansion - 1) * len(
                [e for e in empty_hor if min(gal[1], gal2[1]) < e < max(gal[1], gal2[1])])
            total_dist += hor_d + ver_d

    return total_dist


print(part1())
print(part2())
