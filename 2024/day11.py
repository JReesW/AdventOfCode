with open("addenda/input11.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def part1():
    stones = [int(s) for s in lines[0].split(' ')]

    for blink in range(25):
        _stones = []
        for i, stone in enumerate(stones):
            if stone == 0:
                _stones.append(1)
            elif len(s := str(stone)) % 2 == 0:
                _stones.append(int(s[:len(s) // 2]))
                _stones.append(int(s[len(s) // 2:]))
            else:
                _stones.append(stone * 2024)
        stones = _stones

    return len(stones)


def part2():
    start_stones = [int(s) for s in lines[0].split(' ')]
    stones = {}
    rules = {0: [1]}

    def add_rule(_stone):
        if len(s := str(_stone)) % 2 == 0:
            rules[_stone] = [int(s[:len(s) // 2]), int(s[len(s) // 2:])]
        else:
            rules[_stone] = [_stone * 2024]

    for stone in start_stones:
        if stone not in stones:
            stones[stone] = 0
        stones[stone] += 1

    for blink in range(75):
        new_stones = stones.copy()
        for k, v in stones.items():
            if k not in rules:
                add_rule(k)

            new_stones[k] -= v
            for res in rules[k]:
                if res not in new_stones:
                    new_stones[res] = 0
                new_stones[res] += v

        stones = new_stones

    return sum(stones.values())


print(part1())
print(part2())
