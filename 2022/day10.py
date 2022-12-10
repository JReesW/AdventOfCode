with open("addenda/input10.txt", 'r') as file:
    lines = file.readlines()


def part1():
    special = (20, 60, 100, 140, 180, 220)
    interesting = []
    cycle = 1
    x = 1

    for line in lines:
        match line.strip().split():
            case ['noop']:
                if cycle in special:
                    interesting.append(cycle * x)
                cycle += 1
            case ['addx', n]:
                for _ in range(2):
                    if cycle in special:
                        interesting.append(cycle * x)
                    cycle += 1
                x += int(n)

    return sum(interesting)


def part2():
    # special = (20, 60, 100, 140, 180, 220)
    cycle = 1
    x = 1
    CRT = ""

    for line in lines:
        match line.strip().split():
            case ['noop']:
                if (cycle % 40) - 1 in (x-1, x, x+1):
                    CRT += '#'
                else:
                    CRT += '.'
                cycle += 1
            case ['addx', n]:
                for _ in range(2):
                    if (cycle % 40) - 1 in (x - 1, x, x + 1):
                        CRT += '#'
                    else:
                        CRT += '.'
                    cycle += 1
                x += int(n)

    print(cycle)
    for n in range(0, 240, 40):
        print(CRT[n:n+40])


print(len(lines), 'll')
print(part1())
print(part2())
