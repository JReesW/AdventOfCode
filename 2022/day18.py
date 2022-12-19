with open("addenda/input18.txt", 'r') as file:
    lines = file.readlines()


def part1():
    droplets = {tuple(int(c) for c in line.strip().split(',')) for line in lines}
    area = 0

    for drop in droplets:
        for x in (-1, 1):
            if (drop[0] + x, drop[1], drop[2]) not in droplets:
                area += 1
            if (drop[0], drop[1] + x, drop[2]) not in droplets:
                area += 1
            if (drop[0], drop[1], drop[2] + x) not in droplets:
                area += 1

    return area


def part2():
    droplets = {tuple(int(c) for c in line.strip().split(',')) for line in lines}
    air = set()
    min_c, max_c = -2, 24

    queue = {(0, 0, 0)}

    while queue:
        new_queue = set()
        for q in queue:
            air.add(q)
            for x in (-1, 1):
                if (new_q := (q[0] + x, q[1], q[2])) not in air | droplets:
                    if all(min_c < c < max_c for c in new_q):
                        new_queue.add(new_q)
                if (new_q := (q[0], q[1] + x, q[2])) not in air | droplets:
                    if all(min_c < c < max_c for c in new_q):
                        new_queue.add(new_q)
                if (new_q := (q[0], q[1], q[2] + x)) not in air | droplets:
                    if all(min_c < c < max_c for c in new_q):
                        new_queue.add(new_q)
        queue = new_queue

    area = 0

    for drop in droplets:
        for x in (-1, 1):
            if (drop[0] + x, drop[1], drop[2]) in air:
                area += 1
            if (drop[0], drop[1] + x, drop[2]) in air:
                area += 1
            if (drop[0], drop[1], drop[2] + x) in air:
                area += 1

    return area


print(part1())
print(part2())
