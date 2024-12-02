with open("addenda/input02.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def part1():
    safe = 0

    for line in lines:
        nums = [int(n) for n in line.split(' ')]
        diffs = [a - b for a, b in zip(nums, nums[1:])]
        if all([1 <= abs(d) <= 3 for d in diffs]):
            if all([d < 0 for d in diffs]) or all([d > 0 for d in diffs]):
                safe += 1

    return safe


def part2():
    safe = 0

    for line in lines:
        nums = [int(n) for n in line.split(' ')]

        for i in range(len(nums)):
            _nums = [n for j, n in enumerate(nums) if i != j]
            diffs = [a - b for a, b in zip(_nums, _nums[1:])]
            if all([1 <= abs(d) <= 3 for d in diffs]):
                if all([d < 0 for d in diffs]) or all([d > 0 for d in diffs]):
                    safe += 1
                    break

    return safe


print(part1())
print(part2())
