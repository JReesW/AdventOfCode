with open("addenda/input02.txt", 'r') as file:
    lines = file.readlines()


def part1():
    impossible = set()

    for line in lines:
        game, cubes = line.split(':')

        for rnd in cubes.strip().split(';'):
            for col in rnd.split(','):
                match col.strip().split(' '):
                    case [n, 'green']:
                        if int(n) > 13:
                            impossible.add(int(game.split(' ')[1]))
                    case [n, 'red']:
                        if int(n) > 12:
                            impossible.add(int(game.split(' ')[1]))
                    case [n, 'blue']:
                        if int(n) > 14:
                            impossible.add(int(game.split(' ')[1]))

    return sum({l for l in range(1, len(lines) + 1)} - impossible)


# Only works if your input has one of each color in every game, which I got
# If you have an input with a game that is missing a color, tough shit
def part2():
    powers = 0

    for line in lines:
        game, cubes = line.split(':')

        colors = {'red': 0, 'green': 0, 'blue': 0}

        for rnd in cubes.strip().split(';'):
            for col in rnd.split(','):
                n, color = col.strip().split()
                colors[color] = max(int(n), colors[color])

        powers += colors['red'] * colors['green'] * colors['blue']

    return powers


print(part1())
print(part2())
