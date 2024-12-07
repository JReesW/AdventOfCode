with open("addenda/input07.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def both(p2=False):
    total = 0

    for line in lines:
        target, nums = line.split(': ')
        target, nums = int(target), iter([int(n) for n in nums.split(' ')])

        equations = [next(nums)]
        try:
            while True:
                n = next(nums)
                for i in range(len(equations)):
                    equations.append(equations[i] * n)
                    if p2:
                        equations.append(int(f"{equations[i]}{n}"))
                    equations[i] += n
        except StopIteration:
            pass

        if any([eq == target for eq in equations]):
            total += target

    return total


def part1():
    return both()


def part2():
    return both(True)


print(part1())
print(part2())
