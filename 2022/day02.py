with open("addenda/input02.txt", 'r') as file:
    lines = file.readlines()


def part1():
    score = 0

    for line in lines:
        enemy, player = "ABC".index(line[0]), "XYZ".index(line[2])

        if enemy == player:
            score += 3
        elif ((enemy + 1) % 3) == player:
            score += 6
        score += player + 1

    return score


def part2():
    score = 0

    for line in lines:
        enemy, result = "ABC".index(line[0]), line[2]

        if result == 'Y':
            score += 3 + (enemy + 1)
        elif result == 'X':
            score += (enemy - 1) % 3 + 1
        else:
            score += 6 + ((enemy + 1) % 3) + 1

    return score


print(part1())
print(part2())
