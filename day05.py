stacks = [
    ['F', 'D', 'B', 'Z', 'T', 'J', 'R', 'N'],
    ['R', 'S', 'N', 'J', 'H'],
    ['C', 'R', 'N', 'J', 'G', 'Z', 'F', 'Q'],
    ['F', 'V', 'N', 'G', 'R', 'T', 'Q'],
    ['L', 'T', 'Q', 'F'],
    ['Q', 'C', 'W', 'Z', 'B', 'R', 'G', 'N'],
    ['F', 'C', 'L', 'S', 'N', 'H', 'M'],
    ['D', 'N', 'Q', 'M', 'T', 'J'],
    ['P', 'G', 'S']
]


with open("addenda/input05.txt", 'r') as file:
    lines = file.readlines()


def part1():
    for line in lines:
        line, dest = line.strip().split(" to ")
        num, src = line.split("move ")[1].split(" from ")
        num, src, dest = int(num), int(src), int(dest)




print(part1())
