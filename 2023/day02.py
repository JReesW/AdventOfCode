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


def part2():
#     lines = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".splitlines()
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
