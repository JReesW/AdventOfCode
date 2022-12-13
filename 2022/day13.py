from functools import cmp_to_key
from ast import literal_eval
from itertools import zip_longest


with open("addenda/input13.txt", 'r') as file:
    lines = [line.split() for line in file.read().split('\n\n')]


class Empty:
    """"""


def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


def comp(left, right):
    for a, b in zip_longest(left, right, fillvalue=Empty()):
        res = 0
        if isinstance(a, Empty):
            return 1
        if isinstance(b, Empty):
            return -1
        if isinstance(a, list) and isinstance(b, list):
            if len(a) > 0 and len(b) == 0:
                return -1
            elif len(a) == 0 and len(b) > 0:
                return 1
            res = comp(a, b)
        elif isinstance(a, list):
            res = comp(a, [b])
        elif isinstance(b, list):
            res = comp([a], b)
        elif a != b:
            res = 1 if a < b else -1
        if res != 0:
            return res
    return 0


def part1():
    total = 0
    for i, (left, right) in enumerate(lines):
        left = literal_eval(left)
        right = literal_eval(right)

        if comp(left, right) == 1:
            total += i + 1
    return total


def part2():
    all_lines = []
    for left, right in lines:
        all_lines.append(literal_eval(left))
        all_lines.append(literal_eval(right))

    first = None
    second = None
    all_lines += [[2]]
    all_lines += [[6]]
    for i, row in enumerate(sorted(all_lines, key=cmp_to_key(comp), reverse=True)):
        if row == [2]:
            first = i + 1
        if row == [6]:
            second = i + 1
    return first * second


print(part1())
print(part2())
