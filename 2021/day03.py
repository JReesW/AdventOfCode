with open("addenda/input03.txt", 'r') as file:
    lines = file.readlines()


def part1():
    nums = [list(line.strip()) for line in lines]
    nums = list(map(list, zip(*nums)))

    gamma = int("".join(['1' if num.count('1') > len(num) // 2 else '0' for num in nums]), 2)
    epsilon = int("".join(['1' if num.count('1') < len(num) // 2 else '0' for num in nums]), 2)

    return gamma * epsilon


def part2():
    oxygen = [line.strip() for line in lines]
    co2 = [o for o in oxygen]

    for n in range(len(oxygen[0])):
        if len(oxygen) == 1:
            break

        zeros, ones = [], []

        for s in oxygen:
            (zeros, ones)[s[n] == '1'].append(s)

        if len(zeros) > len(ones):
            oxygen = zeros
        else:
            oxygen = ones

    for n in range(len(co2[0])):
        if len(co2) == 1:
            break

        zeros, ones = [], []

        for s in co2:
            (zeros, ones)[s[n] == '1'].append(s)

        if len(zeros) > len(ones):
            co2 = ones
        else:
            co2 = zeros

    return int(oxygen[0], 2) * int(co2[0], 2)


print(part1())
print(part2())
