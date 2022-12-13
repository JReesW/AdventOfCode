with open("addenda/input09.txt", 'r') as file:
    lines = file.readlines()


def c_dist(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))


mov = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0)
}


def part1():
    head = (0, 0)
    tail = (0, 0)
    visited = {tail}

    for line in lines:
        d, n = line.strip().split()
        for _ in range(int(n)):
            prev = head
            head = (head[0] + mov[d][0], head[1] + mov[d][1])
            if c_dist(head, tail) > 1:
                tail = prev
                visited.add(tail)

    return len(visited)


def sign(n):
    return 1 if n > 0 else -1 if n < 0 else 0


def relative(a, b):
    return sign(a[0] - b[0]), sign(a[1] - b[1])


def part2():
    head = (0, 0)
    tails = [(0, 0)] * 9
    visited = {tails[-1]}

    for line in lines:
        d, n = line.strip().split()
        for _ in range(int(n)):
            new = [(head[0] + mov[d][0], head[1] + mov[d][1])]
            head = new[0]
            for i, tail in enumerate(tails):
                if c_dist(new[i], tail) > 1:
                    rel = relative(new[i], tail)
                    new_t = tail[0] + rel[0], tail[1] + rel[1]
                    new.append(new_t)
                else:
                    new.append(tail)
            tails = new[1:]
            visited.add(tails[-1])

    return len(visited)


print(part1())
print(part2())
