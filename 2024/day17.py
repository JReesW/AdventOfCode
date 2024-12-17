with open("addenda/input17.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def part1(abc=None):
    a, b, c = [int(line.split(': ')[1]) for line in lines[:3]]
    a, b, c = (a, b, c) if abc is None else abc
    program = [int(c) for c in lines[4] if c.isdigit()]
    pointer = 0

    def combo(n):
        return n if n < 4 else [a, b, c][n-4]

    output = ""
    try:
        while True:
            operation, operand = program[pointer:pointer+2]
            if operation == 0:  # adv
                a = a // (2 ** combo(operand))
            elif operation == 1:  # bxl
                b ^= operand
            elif operation == 2:  # bst
                b = combo(operand) % 8
            elif operation == 3:  # jnz
                if a != 0:
                    pointer = operand
                    continue
            elif operation == 4:  # bxc
                b = b ^ c
            elif operation == 5:  # out
                output += str(combo(operand) % 8) + ','
            elif operation == 6:  # bdv
                b = a // (2 ** combo(operand))
            elif operation == 7:  # cdv
                c = a // (2 ** combo(operand))
            pointer += 2
    except (IndexError, ValueError):
        return output[:-1]


def part2():
    program = lines[4].split(': ')[1]

    outputs = 0
    a = 0
    while True:
        if part1((a, 0, 0)) == program[-(outputs * 2 + 1):]:
            if outputs == 15:
                return a
            a <<= 3
            outputs += 1
        else:
            a += 1


print(part1())
print(part2())
