with open("addenda/test.txt", 'r') as file:
    lines = file.readlines()


def dist(a, b):
    return abs(a[0] - a[1]) + abs(b[0] - b[1])


def part1():
    beacons = []
    sensors = []
    y = 10

    for line in lines:
        match line.split():
            case [_, _, xs, ys, _, _, _, _, xb, yb]:
                xs = int(xs.split(',')[0].split('=')[1])
                ys = int(ys.split(':')[0].split('=')[1])
                xb = int(xb.split(',')[0].split('=')[1])
                yb = int(yb.split('=')[1])
                beacons.append((xb, yb))
                sensors.append((xs, ys))

    total = set()
    for x in range(-1000, 1000):
        try:
            for sensor, beacon in zip(sensors, beacons):
                if dist(sensor, (x, y)) > dist(sensor, beacon) and (x, y) not in (*sensors, *beacons):
                    raise Exception
        except Exception:
            total.add((x, y))
    return len(total)


def part2():
    pass


print(part1())
print(part2())
