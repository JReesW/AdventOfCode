with open("addenda/input15.txt", 'r') as file:
    line = [line.strip() for line in file.readlines()][0]


def hash_label(label):
    current = 0
    for c in label:
        current += ord(c)
        current *= 17
        current %= 256
    return current


def part1():
    hashes = line.split(',')
    total = 0

    for h in hashes:
        total += hash_label(h)

    return total


def part2():
    boxes = [{} for _ in range(256)]

    hashes = line.split(',')

    for h in hashes:
        match h.split('='):
            case [key, val]:
                box = hash_label(key)
                boxes[box][key] = int(val)
            case [key]:
                key = key[:-1]
                box = hash_label(key)

                if key in boxes[box]:
                    del boxes[box][key]

    power = 0

    for b, box in enumerate(boxes):
        for i, (k, v) in enumerate(box.items()):
            power += (b + 1) * (i + 1) * v

    return power


print(part1())
print(part2())
