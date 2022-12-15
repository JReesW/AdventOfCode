import time


with open("addenda/input15.txt", 'r') as file:
    lines = file.readlines()


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def part1():
    pairs = {}
    y = 2000000

    for line in lines:
        match line.split():
            case [_, _, xs, ys, _, _, _, _, xb, yb]:
                xs = int(xs.split(',')[0].split('=')[1])
                ys = int(ys.split(':')[0].split('=')[1])
                xb = int(xb.split(',')[0].split('=')[1])
                yb = int(yb.split('=')[1])
                pairs[(xs, ys)] = (xb, yb)

    points = set()
    for s, b in pairs.items():
        d = dist(s, b)
        yd = dist(s, (s[0], y))
        if yd <= d:
            points |= {(s[0] + x, y) for x in range(-(d - yd), (d - yd) + 1)}
    points -= set(pairs.keys()) | set(pairs.values())
    return len(points)


# Abysmally slow
def part2():
    print("strap in, this gon' take a while")
    max_c = 4000000
    beacons = []
    sensors = []

    for line in lines:
        match line.split():
            case [_, _, xs, ys, _, _, _, _, xb, yb]:
                xs = int(xs.split(',')[0].split('=')[1])
                ys = int(ys.split(':')[0].split('=')[1])
                xb = int(xb.split(',')[0].split('=')[1])
                yb = int(yb.split('=')[1])
                beacons.append((xb, yb))
                sensors.append((xs, ys))

    points = set()
    for i, ((sx, sy), (bx, by)) in enumerate(zip(sensors, beacons)):
        print(f"{i} / {len(sensors) - 1}")

        p = sx, sy
        d = dist((sx, sy), (bx, by))

        for x, y in zip(range(0, d + 2), range(d + 1, -1, -1)):
            for xx, yy in ((p[0] + x, p[1] + y), (p[0] + x, p[1] - y), (p[0] - x, p[1] + y), (p[0] - x, p[1] - y)):
                if 0 <= xx <= max_c and 0 <= yy <= max_c:
                    if all([dist((xx, yy), s) > dist(s, b) for s, b in zip(sensors, beacons)]):
                        if (xx, yy) not in sensors and (xx, yy) not in beacons:
                            points.add((xx, yy))

    return points
    # keeping it for if the above doesn't work lol
    #     print(f"{i} / {len(sensors) - 1}")
    #
    #
    #     points |= {(p[0] + x, p[1] + y) for x, y in zip(range(0, d + 2), range(d + 1, -1, -1))}
    #     points |= {(p[0] + x, p[1] - y) for x, y in zip(range(0, d + 2), range(d + 1, -1, -1))}
    #     points |= {(p[0] - x, p[1] + y) for x, y in zip(range(0, d + 2), range(d + 1, -1, -1))}
    #     points |= {(p[0] - x, p[1] - y) for x, y in zip(range(0, d + 2), range(d + 1, -1, -1))}
    #
    # print(len(points))
    # answers = []
    # for i, p in enumerate(points):
    #     if i % 10000 == 0:
    #         print(f"{i} / 75428427 -> {i / 75428427:.3%}")
    #     if 0 <= p[0] <= max_c and 0 <= p[1] <= max_c:
    #         if all([dist(p, s) > dist(s, b) for s, b in zip(sensors, beacons)]):
    #             print(p)
    #             answers.append(p)
    # print(answers)


print(part1())
print(part2())
