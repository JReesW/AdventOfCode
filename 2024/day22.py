from functools import reduce

with open("addenda/input22.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def part1():
    nums = [int(n) for n in lines]
    for i, n in enumerate(nums):
        for _ in range(2000):
            n = (n ^ (n * 64)) % 16777216
            n = (n ^ (n // 32)) % 16777216
            n = (n ^ (n * 2048)) % 16777216
        nums[i] = n

    return sum(nums)


def part2():
    patterns = []
    nums = [int(n) for n in lines]
    for i, n in enumerate(nums):
        patterns.append({})
        pattern = (None, None, None, None)
        for _ in range(2000):
            m = n
            n = (n ^ (n * 64)) % 16777216
            n = (n ^ (n // 32)) % 16777216
            n = (n ^ (n * 2048)) % 16777216
            a, b, c, d = pattern
            pattern = b, c, d, (m % 10) - (n % 10)
            if pattern not in patterns[i]:
                patterns[i][pattern] = n % 10
        nums[i] = n

    all_patterns = reduce(lambda x, y: x | y, patterns)

    best = None, 0
    for pattern in all_patterns:
        subtotal = 0
        for _patterns in patterns:
            if pattern in _patterns:
                subtotal += _patterns[pattern]
        if subtotal > best[1]:
            best = pattern, subtotal

    return best[1]


print(part1())
print(part2())
