with open("addenda/input25.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def part1():
    locks = []
    keys = []
    for i in range(0, len(lines), 8):
        if lines[i] == '#####':
            lock = []
            for col in range(5):
                for row in range(6):
                    if lines[i+row+1][col] == '.':
                        lock.append(row)
                        break
            locks.append(lock)
        if lines[i] == '.....':
            key = []
            for col in range(5):
                for row in range(6):
                    if lines[i+5-row][col] == '.':
                        key.append(row)
                        break
            keys.append(key)

    total = 0
    for lock in locks:
        for key in keys:
            if all([lock[col] + key[col] < 6 for col in range(5)]):
                total += 1

    return total


def part2():
    return "Merry Christmas!"


print(part1())
print(part2())
