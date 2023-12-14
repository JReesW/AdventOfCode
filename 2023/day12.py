from functools import cache


with open("addenda/input12.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def parse():
    rows = []

    for line in lines:
        pattern, nums = line.split(' ')
        nums = tuple(int(n) for n in nums.split(','))
        rows.append((pattern, nums))

    return rows


@cache
def dive(pattern, nums, n=0):
    if not pattern:
        return not nums and not n

    count = 0

    if pattern[0] in "#?":
        count += dive(pattern[1:], nums, n + 1)
    if pattern[0] in ".?" and (nums and nums[0] == n or not n):
        count += dive(pattern[1:], nums[1:] if n else nums)
    return count


def part1():
    rows = parse()

    total = 0
    for pattern, nums in rows:
        total += dive(pattern + '.', nums)

    return total


def part2():
    rows = parse()

    total = 0
    for pattern, nums in rows:
        total += dive('?'.join([pattern] * 5) + '.', nums * 5)

    return total


print(part1())
print(part2())
