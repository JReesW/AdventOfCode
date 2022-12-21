with open("addenda/input21.txt", 'r') as file:
    lines = file.readlines()


ops = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}


def part1():
    monkeys_left = {}
    monkeys_known = {}

    for line in lines:
        match line.replace(':', '').split():
            case [name, val]:
                monkeys_known[name] = int(val)
            case [name, *rest]:
                monkeys_left[name] = ' '.join(rest)

    while monkeys_left:
        rem = []
        for monkey in monkeys_left:
            a, op, b = monkeys_left[monkey].split()
            if a in monkeys_known and b in monkeys_known:
                monkeys_known[monkey] = ops[op](monkeys_known[a], monkeys_known[b])
                rem.append(monkey)
        for r in rem:
            del monkeys_left[r]

    return monkeys_known['root']


def part2():
    monkeys_left = {}
    monkeys_known = {}
    root = (0, 1)

    for line in lines:
        match line.replace(':', '').split():
            case ["humn", *_]:
                pass
            case ["root", a, _, b]:
                root = (a, b)
            case [name, val]:
                monkeys_known[name] = int(val)
            case [name, *rest]:
                monkeys_left[name] = ' '.join(rest)

    while monkeys_left:
        rem = []
        for m in monkeys_left:
            a, op, b = monkeys_left[m].split()
            if a in monkeys_known and b in monkeys_known:
                monkeys_known[m] = ops[op](monkeys_known[a], monkeys_known[b])
                rem.append(m)
        if rem:
            for r in rem:
                del monkeys_left[r]
        else:
            break

    goal = monkeys_known[root[0]] if root[0] in monkeys_known else monkeys_known[root[1]]
    unknown = root[1] if root[0] in monkeys_known else root[0]

    def dive(monkey, expected):
        if monkey == "humn":
            return expected

        match monkeys_left[monkey].split():
            case [left, '+', right] if right in monkeys_known:
                return dive(left, expected - monkeys_known[right])
            case [left, '+', right] if left in monkeys_known:
                return dive(right, expected - monkeys_known[left])
            case [left, '-', right] if right in monkeys_known:
                return dive(left, expected + monkeys_known[right])
            case [left, '-', right] if left in monkeys_known:
                return dive(right, monkeys_known[left] - expected)
            case [left, '*', right] if right in monkeys_known:
                return dive(left, expected / monkeys_known[right])
            case [left, '*', right] if left in monkeys_known:
                return dive(right, expected / monkeys_known[left])
            case [left, '/', right] if right in monkeys_known:
                return dive(left, expected * monkeys_known[right])
            case [left, '/', right] if left in monkeys_known:
                return dive(right, monkeys_known[left] / expected)

    return dive(unknown, goal)


print(part1())
print(part2())
