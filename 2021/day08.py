with open("addenda/input08.txt", 'r') as file:
    lines = file.readlines()


def part1():
    total = 0

    for line in lines:
        output = line.split('|')[1].strip()

        total += len([s for s in output.split() if len(s) in (2, 4, 3, 7)])

    return total


def part2():
    total = 0

    for line in lines:
        example, output = [ln.strip().split() for ln in line.split('|')]
        one, seven, four, eight = sorted(
            {"".join(sorted(s)) for s in set(example + output) if len(s) in (2, 3, 4, 7)},
            key=len
        )
        one, seven, four, eight = (set(n) for n in (one, seven, four, eight))

        s = ""
        for o in (set(o) for o in output):
            if o == one:
                s += '1'
            elif o == seven:
                s += '7'
            elif o == four:
                s += '4'
            elif o == eight:
                s += '8'
            elif len(o - one) == 5:
                s += '6'
            elif len(o - one) == 3:
                s += '3'
            elif len(o - four) == 2:
                if len(o & four) == 4:
                    s += '9'
                else:
                    s += '5'
            elif len(o & eight) == 5:
                s += '2'
            else:
                s += '0'
        total += int(s)

    return total


print(part1())
print(part2())
