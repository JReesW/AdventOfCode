with open("addenda/input09.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def part1():
    total = 0

    for line in lines:
        seq = [int(n) for n in line.split(' ')]
        seqs = [seq[::]]

        while any([c != 0 for c in seq]):
            seq = [b - a for a, b in zip(seq, seq[1:])]
            seqs.append(seq[::])

        val = 0
        for history in seqs[::-1][1:]:
            val = history[-1] + val

        total += val

    return total


def part2():
    total = 0

    for line in lines:
        seq = [int(n) for n in line.split(' ')]
        seqs = [seq[::]]

        while any([c != 0 for c in seq]):
            seq = [b - a for a, b in zip(seq, seq[1:])]
            seqs.append(seq[::])

        val = 0
        for history in seqs[::-1][1:]:
            val = history[0] - val

        total += val

    return total


print(part1())
print(part2())
