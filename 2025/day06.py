import re
from functools import reduce

with open("addenda/input06.txt", 'r') as file:
    lines = [line for line in file.readlines()]


def part1():
    slines = [l.strip() for l in lines]
    cols = [[] for _ in range(len(re.split(r' +', slines[0])))]
    for line in slines:
        for c, v in enumerate(re.split(r' +', line)):
            cols[c].append(v)
    
    total = 0
    for col in cols:
        *nums, op = col
        func = (lambda a, b: a * b) if op == '*' else (lambda a, b: a + b)
        total += reduce(func, map(int, nums))
    
    return total


def part2():
    cols = ["" for _ in range(len(lines[0]))]
    for line in lines[:-1]:
        for x, c in enumerate(line):
            cols[x] += c
    
    nums = []
    for col in cols:
        if not re.fullmatch('^[ \n]+$', col): nums.append(int(col))
        else: nums.append(None)

    total, curr = 0, None
    for i in range(len(nums)):
        if curr is None:
            op = lines[-1][i]
            func = (lambda a, b: a * b) if op == '*' else (lambda a, b: a + b)
            curr = 1 if op == '*' else 0
        if nums[i] is None:
            total += curr
            curr = None
        else:
            curr = func(curr, nums[i])
    
    return total


print(part1())
print(part2())
