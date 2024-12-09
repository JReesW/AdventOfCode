with open("addenda/input09.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def part1():
    files = []
    for i, c in enumerate(lines[0]):
        if i % 2 == 0:
            for j in range(int(c)):
                files.append(int(i) // 2)
        else:
            for j in range(int(c)):
                files.append(None)

    try:
        for i, c in enumerate(files):
            if c is None:
                while files[-1] is None:
                    files.pop(-1)
                files[i] = files.pop(-1)
    except IndexError:
        pass

    return sum([i * c for i, c in enumerate(files)])


def part2():
    files = []
    for i, c in enumerate(lines[0]):
        if i % 2 == 0:
            files.append((int(i) // 2, int(c)))
        else:
            files.append((-1, int(c)))

    for i, file in enumerate(reversed([f for f in files if f[0] != -1])):
        f_i = files.index(file)
        for j, empty in [(k, f) for k, f in enumerate(files) if f[0] == -1 and k < f_i]:
            if empty[1] >= file[1]:
                files[j] = (empty[0], empty[1] - file[1])
                files[f_i] = (-1, files[f_i][1])
                files.insert(j, file)
                break

    res = []
    for f, l in files:
        res += list((max(f, 0), ) * l)

    return sum([i * c for i, c in enumerate(res)])


print(part1())
print(part2())
