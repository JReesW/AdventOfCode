import re


with open("addenda/input16.txt", 'r') as file:
    lines = file.readlines()


class Valve:
    def __init__(self, name, flow, conns):
        self.name = name
        self.flow = flow
        self.conns = conns
        self.valves = None
        self.dists = {}

    def __repr__(self):
        return f"{self.name}, {self.flow}f/m, conn: {[(k.name, d) for k, d in self.dists.items()]}"

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def set_valves(self, valves):
        self.valves = valves

    def search(self, visited, time, score):
        results = [0]
        for v, d in self.dists.items():
            if v not in visited and (t := time + d + 1) < 30:
                results.append(v.search(visited + [self], t, score + ((30 - t) * v.flow)))
        return max([*results, score])


def part1():
    valves = {}

    for line in lines:
        name, flow, *conns = re.findall(r"([A-Z]{2}|\d+)+", line)
        valves[name] = Valve(name, int(flow), conns)

    while not all([all([w in v.dists for w in valves.values() if v != w]) for v in valves.values()]):
        for v in valves.values():
            for c in v.conns:
                if valves[c] not in v.dists:
                    v.dists[valves[c]] = 1
                else:
                    for cc, d in valves[c].dists.items():
                        if cc != v:
                            if cc in v.dists:
                                v.dists[cc] = min(d + 1, v.dists[cc])
                            else:
                                v.dists[cc] = d + 1

    rem = []
    for v in valves.values():
        if v.flow == 0 and v.name != 'AA':
            rem.append(v)
    for r in rem:
        del valves[r.name]
    for v in valves.values():
        for r in rem:
            del v.dists[r]
        v.set_valves(valves)

    return valves['AA'].search([], 0, 0)


def part2():
    pass


print(part1())
print(part2())
