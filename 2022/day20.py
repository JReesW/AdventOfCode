with open("addenda/input20.txt", 'r') as file:
    lines = file.readlines()


class Node:
    def __init__(self, value, i=None):
        self.value = value
        self.moved = False
        self.i = i

    def __eq__(self, other):
        if self.i is not None:
            return (self.value == other.value) and (self.moved == other.moved) and self.i == other.i
        return (self.value == other.value) and (self.moved == other.moved)


def part1():
    array = [Node(int(line)) for line in lines]

    for line in lines:
        n = Node(int(line))
        i = [idx for idx, node in enumerate(array) if node == n][0]
        n.moved = True
        array.pop(i)
        i_at = (i + n.value) % len(array)
        if i_at == 0:
            array.append(n)
        else:
            array.insert((i + n.value) % len(array), n)

    zero = [i for i, n in enumerate(array) if n.value == 0][0]

    return sum([array[(zero + i) % len(array)].value for i in (1000, 2000, 3000)])


def part2():
    array = [Node(int(line) * 811589153, i) for i, line in enumerate(lines)]

    for lp in range(10):
        for ix, line in enumerate(lines):
            n = Node(int(line) * 811589153, ix)
            i = [idx for idx, node in enumerate(array) if node == n][0]
            n.moved = True
            array.pop(i)
            i_at = (i + n.value) % len(array)
            if i_at == 0:
                array.append(n)
            else:
                array.insert((i + n.value) % len(array), n)
        for node in array:
            node.moved = False

    zero = [i for i, n in enumerate(array) if n.value == 0][0]

    return sum([array[(zero + i) % len(array)].value for i in (1000, 2000, 3000)])


print(part1())
print(part2())
