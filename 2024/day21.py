from random import random
from functools import cache

with open("addenda/input21.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


keypad = {
    '7': (0, 0), '8': (1, 0), '9': (2, 0),
    '4': (0, 1), '5': (1, 1), '6': (2, 1),
    '1': (0, 2), '2': (1, 2), '3': (2, 2),
    ' ': (0, 3), '0': (1, 3), 'A': (2, 3)
}
movepad = {
    ' ': (0, 0), '^': (1, 0), 'A': (2, 0),
    '<': (0, 1), 'v': (1, 1), '>': (2, 1)
}


@cache
def path(start, end):
    pad = keypad if (start in keypad and end in keypad) else movepad
    dx, dy = pad[end][0] - pad[start][0], pad[end][1] - pad[start][1]
    x_path = ('<' if dx < 0 else '>') * abs(dx)
    y_path = ('^' if dy < 0 else 'v') * abs(dy)

    if (pad[start][0], pad[start][1] + dy) == pad[' ']:
        return x_path + y_path + 'A'
    if (pad[start][0] + dx, pad[start][1]) == pad[' ']:
        return y_path + x_path + 'A'
    return (x_path + y_path if random() < 0.5 else y_path + x_path) + 'A'


@cache
def length(code, depth):
    if depth == 0:
        return len(code)
    s = 0
    for i, c in enumerate(code):
        s += length(path(code[i-1], c), depth - 1)
    return s


def part1():
    total = 0
    for code in lines:
        min_total = 99999999999999
        for _ in range(1000):
            path.cache_clear()
            length.cache_clear()
            min_total = min(min_total, int(code[:-1]) * length(code, 3))
        total += min_total
    return total


def part2():
    total = 0
    for code in lines:
        min_total = 9999999999999999999999999
        for i in range(1000):
            path.cache_clear()
            length.cache_clear()
            min_total = min(min_total, int(code[:-1]) * length(code, 26))
        total += min_total
    return total


print(part1())
print(part2())
