with open("addenda/input06.txt", 'r') as file:
    line = file.readline()


def part1():
    fish = [int(n) for n in line.strip().split(',')]

    for _ in range(80):
        add = []
        for i, f in enumerate(fish):
            if f == 0:
                add.append(8)
            fish[i] = f - 1 if f - 1 >= 0 else 6
        fish += add

    return len(fish)


def part2():
    fish = [int(n) for n in line.strip().split(',')]
    fish = [fish.count(f) for f in range(9)]

    for d in range(256):
        f, *fish = fish
        fish[6] += f
        fish.append(f)

    return sum(fish)


print(part1())
print(part2())
