from collections import defaultdict

with open("addenda/input05.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def separate_ordered():
    order = defaultdict(set)
    last = 0

    for i, line in enumerate(lines):
        if line == '':
            last = i + 1
            break
        a, b = [int(l) for l in line.split('|')]
        order[a].add(b)

    ordered = []
    unordered = []

    for line in lines[last:]:
        update = [int(u) for u in line.split(',')]
        for u in update:
            if u in order:
                for _u in order[u]:
                    if _u in update:
                        if update.index(u) > update.index(_u):
                            break
                else:
                    continue
                break
        else:
            ordered.append(update)
            continue
        unordered.append(update)

    return order, ordered, unordered


def part1():
    _, ordered, _ = separate_ordered()

    return sum([o[len(o) // 2] for o in ordered])


def part2():
    total = 0

    order, _, unordered = separate_ordered()

    for update in unordered:
        ordered = []
        while update:
            page = update.pop(0)
            for p in update:
                if page in order[p]:
                    update.append(page)
                    break
            else:
                ordered.append(page)
        total += ordered[len(ordered) // 2]

    return total


print(part1())
print(part2())
