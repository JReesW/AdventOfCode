with open("addenda/test.txt", 'r') as file:
    line = file.readlines()[0].strip()


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


# (Y, X)  TODO change back?
rocks = [
    {(0, 0), (0, 1), (0, 2), (0, 3)},  # horizontal line
    {(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)},  # plus
    {(0, 2), (1, 2), (2, 2), (2, 1), (2, 0)},  # backwards L
    {(0, 0), (1, 0), (2, 0), (3, 0)},  # vertical line
    {(0, 0), (0, 1), (1, 1), (1, 0)}  # square
]


class Tower:
    def __init__(self):
        self.columns = [
            {0},
            {0},
            {0},
            {0},
            {0},
            {0},
            {0}
        ]

    def tops(self):
        return [max(col) for col in self.columns]

    def __contains__(self, item: tuple):
        y, x = item
        return y in self.columns[x]

    def __repr__(self):
        pass


def part1():
    tower = Tower()
    stone = 0




def part2():
    pass


print(part1())
print(part2())
