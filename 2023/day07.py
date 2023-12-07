import functools


with open("addenda/input07.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def strength(card):
    occs = {c: card.count(c) for c in card}

    match sorted(occs.values(), reverse=True):
        case [5]:
            return 6
        case [4, 1]:
            return 5
        case [3, 2]:
            return 4
        case [3, 1, 1]:
            return 3
        case [2, 2, 1]:
            return 2
        case [2, 1, 1, 1]:
            return 1
        case [1, 1, 1, 1, 1]:
            return 0


def compare(a, b, p2=False):
    if p2:
        strength_a = max([strength(a.replace('J', c)) for c in "AKQT98765432"])
        strength_b = max([strength(b.replace('J', c)) for c in "AKQT98765432"])
        order = "AKQT98765432J"
    else:
        strength_a = strength(a)
        strength_b = strength(b)
        order = "AKQJT98765432"

    if strength_a == strength_b:
        for ca, cb in zip(a, b):
            ia = order.index(ca)
            ib = order.index(cb)
            if ia < ib:
                return 1
            elif ib < ia:
                return -1
    elif strength_a > strength_b:
        return 1
    else:
        return -1


def run(comp_func):
    hands = {}
    for line in lines:
        hand, bid = line.split(' ')
        hands[hand] = int(bid)

    ordered = sorted(hands.keys(), key=functools.cmp_to_key(comp_func))
    total = 0
    for pos, hand in enumerate(ordered):
        total += hands[hand] * (pos + 1)
    return total


def part1():
    return run(compare)


def part2():
    return run(functools.partial(compare, p2=True))


print(part1())
print(part2())
