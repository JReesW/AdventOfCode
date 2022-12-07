with open("addenda/input07.txt", 'r') as file:
    lines = file.readlines()


class Dir:
    def __init__(self, name, parent, children):
        self.name = name
        self.parent = parent
        self.children = children

    def size(self):
        total = 0
        for child in self.children:
            if isinstance(child, Dir):
                total += child.size()
            else:
                total += child
        return total


root = Dir('/', None, [])
dirs = []


def prep():
    cur = root
    for line in lines:
        match line.strip().split(' '):
            case ['$', 'cd', '/']:
                cur = root
            case ['$', 'cd', '..']:
                cur = cur.parent
            case ['$', 'cd', dest]:
                for child in cur.children:
                    if isinstance(child, Dir) and child.name == dest:
                        cur = child
                        break
            case ['dir', name]:
                cur.children.append(new_dir := Dir(name, cur, []))
                dirs.append(new_dir)
            case [size, _] if size.isnumeric():
                cur.children.append(int(size))
            case _:
                pass


def part1():
    sizes = [d.size() for d in dirs]
    return sum(s for s in sizes if s <= 100000)


def part2():
    needed = 30_000_000 - (70_000_000 - root.size())
    sizes = (d.size() for d in dirs)
    return min(s for s in sizes if s >= needed)


prep()
print(part1())
print(part2())
