class Monkey:
    def __init__(self, items, operation, test, dest):
        self.items = items
        self.operation = operation
        self.test = test
        self.dest = dest
        self.inspected = 0


input_monkeys = [
    Monkey([73, 77], lambda o: o * 5, 11, (6, 5)),
    Monkey([57, 88, 80], lambda o: o + 5, 19, (6, 0)),
    Monkey([61, 81, 84, 69, 77, 88], lambda o: o * 19, 5, (3, 1)),
    Monkey([78, 89, 71, 60, 81, 84, 87, 75], lambda o: o + 7, 3, (1, 0)),
    Monkey([60, 76, 90, 63, 86, 87, 89], lambda o: o + 2, 13, (2, 7)),
    Monkey([88], lambda o: o + 1, 17, (4, 7)),
    Monkey([84, 98, 78, 85], lambda o: o * o, 7, (5, 4)),
    Monkey([98, 89, 78, 73, 71], lambda o: o + 4, 2, (3, 2))
]


test_monkeys = [
    Monkey([79, 98], lambda o: o * 19, 23, (2, 3)),
    Monkey([54, 65, 75, 74], lambda o: o + 6, 19, (2, 0)),
    Monkey([79, 60, 97], lambda o: o * o, 13, (1, 3)),
    Monkey([74], lambda o: o + 3, 17, (0, 1))
]
