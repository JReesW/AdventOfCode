from collections import defaultdict

with open("addenda/input23.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def part1():
    connections = defaultdict(set)
    for line in lines:
        a, b = line.split('-')
        connections[a].add(b)
        connections[b].add(a)

    triples = set()
    for a in connections:
        for b in connections[a]:
            for c in connections[a]:
                if b in connections[c]:
                    triples.add(tuple(sorted((a, b, c))))

    return len([t for t in triples if any(x[0] == 't' for x in t)])


def part2():
    connections = defaultdict(set)
    for line in lines:
        a, b = line.split('-')
        connections[a].add(b)
        connections[b].add(a)

    groups = set()
    for conn in connections:
        for sub in connections[conn]:
            group = {conn, sub}
            for sub2 in connections[conn]:
                if all([g in connections[sub2] for g in group]):
                    group.add(sub2)
            groups.add(tuple(sorted(group)))

    return ','.join(max(groups, key=len))


print(part1())
print(part2())
