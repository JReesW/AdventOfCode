import re
import itertools
import math


with open("addenda/input08.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def part1():
    instructions = lines[0]

    nodes = {}
    for line in lines[2:]:
        node, left, right = re.findall("\w+", line)
        nodes[node] = left, right

    steps = 0
    loc = 'AAA'
    for c in itertools.cycle(instructions):
        steps += 1
        if c == 'L':
            loc = nodes[loc][0]
        else:
            loc = nodes[loc][1]
        if loc == 'ZZZ':
            return steps

def part2():
    instructions = lines[0]

    nodes = {}
    for line in lines[2:]:
        node, left, right = re.findall("\w+", line)
        nodes[node] = left, right

    locs = [node for node in nodes if node[2] == 'A']
    steps = {loc: 0 for loc in range(len(locs))}
    step = 0
    for c in itertools.cycle(instructions):
        step += 1
        if c == 'L':
            locs = [nodes[loc][0] for loc in locs]
        else:
            locs = [nodes[loc][1] for loc in locs]
        for i, loc in enumerate(locs):
            if loc[2] == 'Z' and steps[i] == 0:
                steps[i] = step
        if all([steps[loc] != 0 for loc in range(len(locs))]):
            break

    lcm = 1
    for n in steps.values():
        lcm = lcm * n // math.gcd(lcm, n)

    return lcm


print(part1())
print(part2())
