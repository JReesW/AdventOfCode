with open("addenda/test.txt", 'r') as file:
    lines = file.readlines()


class Valve:
    def __init__(self, name, flow, conns, valves):
        self.name = name
        self.flow = flow
        self.conns = conns
        self.valves = valves

    def path_to(self, target, path=None):
        print(self.name, target, path)
        if path is None:
            path = []
        if target == self.name:
            return path + [self.name]
        conns = [self.valves[c].path_to(target, path + [self.name]) for c in self.conns if c not in path]
        return min(conns, key=lambda c: (len(c) - 1) % len(conns)) if conns else []

    def __repr__(self):
        return f"Valve {self.name} has flow rate={self.flow}; tunnels lead to valves {', '.join(self.conns)}"


def part1():
    valves = {}

    for line in lines:
        match line.strip().split():
            case [_, name, _, _, flow, _, _, _, _, *conns]:
                flow = int(flow.split(';')[0].split('=')[1])
                conns = [c.replace(',', '') for c in conns]
                valves[name] = Valve(name, flow, conns, valves)

    print(valves['AA'].path_to('CC'))


def part2():
    pass


print(part1())
print(part2())
