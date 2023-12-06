with open("addenda/input04.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def part1():
    total = 0

    for line in lines:
        _, nums = line.split(': ')
        winning, yours = nums.split(' | ')
        winning = {int(n) for n in winning.split(' ') if n.strip().isnumeric()}
        yours = {int(n) for n in yours.split(' ') if n.strip().isnumeric()}

        points = 2 ** (len(winning & yours) - 1)
        total += points if points >= 1 else 0

    return total


def part2():
    cards = {n+1: 1 for n in range(len(lines))}

    for line in lines:
        card, nums = line.split(': ')
        card = int(card.split(' ')[-1])

        winning, yours = nums.split(' | ')
        winning = {int(n) for n in winning.split(' ') if n.strip().isnumeric()}
        yours = {int(n) for n in yours.split(' ') if n.strip().isnumeric()}

        matching = len(winning & yours)
        try:
            for i in range(1, matching+1):
                cards[card + i] += cards[card]
        except IndexError:
            pass

    return sum(cards.values())


print(part1())
print(part2())
