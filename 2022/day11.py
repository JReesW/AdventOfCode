from addenda.input11 import *
from functools import reduce


monkeys = input_monkeys


def part1():
    for _ in range(20):
        for monkey in monkeys:
            for _ in range(len(monkey.items)):
                item, *monkey.items = monkey.items
                monkey.inspected += 1
                new = monkey.operation(item) // 3

                monkeys[monkey.dest[0 if new % monkey.test == 0 else 1]].items.append(new)

    top = sorted([m.inspected for m in monkeys], reverse=True)
    return top[0] * top[1]


def part2():
    mul = reduce(lambda a, b: a*b, [m.test for m in monkeys])
    for _ in range(10_000):
        for monkey in monkeys:
            for _ in range(len(monkey.items)):
                item, *monkey.items = monkey.items
                monkey.inspected += 1
                new = monkey.operation(item) % mul

                receiver = monkeys[monkey.dest[0 if new % monkey.test == 0 else 1]]
                receiver.items.append(new)

    top = sorted([m.inspected for m in monkeys], reverse=True)
    return top[0] * top[1]


# print(part1())
print(part2())
