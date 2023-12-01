with open("addenda/input01.txt", 'r') as file:
    lines = file.readlines()


def part1():
    total = 0

    for line in lines:
        digits = [c for c in line if c.isdigit()]
        total += int(f"{digits[0]}{digits[-1]}")

    return total


def part2():
    total = 0
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for line in lines:
        for word in words:
            if word in line:
                line = line.replace(word, f"{word}{words.index(word)+1}{word}")

        digits = [c for c in line if c.isdigit()]
        total += int(f"{digits[0]}{digits[-1]}")

    return total


print(part1())
print(part2())
