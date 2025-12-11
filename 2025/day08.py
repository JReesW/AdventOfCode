from itertools import combinations
from math import dist
from collections import defaultdict
from functools import reduce

with open("addenda/input08.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def part1():
    connections = {}
    junctions = []
    for line in lines:
        junctions.append(tuple(map(int, line.split(','))))
    
    uid = 0
    order = sorted(combinations(junctions, 2), key=lambda x: dist(x[0], x[1]))
    for i in range(1000):
        a, b = order[i]
        if a in connections and b in connections:
            if connections[a] != connections[b]:
                replace = connections[b]
                for k, v in connections.items():
                    if v == replace:
                        connections[k] = connections[a]
        elif a in connections and b not in connections:
            connections[b] = connections[a]
        elif b in connections and a not in connections:
            connections[a] = connections[b]
        else:
            connections[a] = uid
            connections[b] = uid
            uid += 1
    
    occs = defaultdict(lambda: 0)
    for v in connections.values():
        occs[v] += 1
    three_largest = list(sorted(occs.values(), reverse=True))[:3]
    
    return reduce(lambda a, b: a * b, three_largest)


def part2():
    connections = {}
    junctions = []
    for line in lines:
        junctions.append(tuple(map(int, line.split(','))))
    
    uid = 0
    order = sorted(combinations(junctions, 2), key=lambda x: dist(x[0], x[1]))
    i = 0
    while not all(c == 0 for c in connections.values()) or not all(j in connections for j in junctions):
        a, b = order[i]
        if a in connections and b in connections:
            if connections[a] != connections[b]:
                new, old = sorted((connections[a], connections[b]))
                for k, v in connections.items():
                    if v == old:
                        connections[k] = new
        elif a in connections and b not in connections:
            connections[b] = connections[a]
        elif b in connections and a not in connections:
            connections[a] = connections[b]
        else:
            connections[a] = uid
            connections[b] = uid
            uid += 1
        i += 1
    
    a, b = order[i-1]
    return a[0] * b[0]


print(part1())
print(part2())
