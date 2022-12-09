import re


with open("addenda/input04.txt", 'r') as file:
    lines = file.readlines()


class Board:
    def __init__(self, rows):
        self.rows = rows

    @property
    def cols(self):
        return list(map(list, zip(*self.rows)))

    def bingo(self):
        for row in self.rows:
            if all([isinstance(i, bool) for i in row]):
                return True

        for col in self.cols:
            if all([isinstance(i, bool) for i in col]):
                return True

        return False

    def mark(self, n):
        for y in range(5):
            for x in range(5):
                if self.rows[y][x] == n:
                    self.rows[y][x] = True

    def unmarked(self):
        unmarked = []

        for row in self.rows:
            unmarked += [int(i) for i in row if isinstance(i, str)]

        return unmarked


def part1():
    nums = lines[0].strip().split(',')
    boards = []

    cur = []
    for line in lines[1:]:
        if len(line) > 3:
            cur.append(re.findall(r'\d+', line))
        if len(cur) == 5:
            boards.append(Board(cur))
            cur = []

    for num in nums:
        for board in boards:
            board.mark(num)

            if board.bingo():
                return sum(board.unmarked()) * int(num)


def part2():
    nums = lines[0].strip().split(',')
    boards = []

    cur = []
    for line in lines[1:]:
        if len(line) > 3:
            cur.append(re.findall(r'\d+', line))
        if len(cur) == 5:
            boards.append(Board(cur))
            cur = []

    for num in nums:
        if len(boards) == 1:
            boards[0].mark(num)
            if boards[0].bingo():
                return sum(boards[0].unmarked()) * int(num)

        left = []
        for board in boards:
            board.mark(num)

            if not board.bingo():
                left.append(board)
        boards = left


print(part1())
print(part2())
