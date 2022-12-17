import re
import multiprocessing as mp


with open("addenda/input16.txt", 'r') as file:
    lines = file.readlines()


class Valve:
    def __init__(self, name, flow, conns, max_time):
        self.name = name
        self.flow = flow
        self.conns = conns
        self.valves = None
        self.dists = {}
        self.max_time = max_time

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
            if v not in visited and (t := time + d + 1) < self.max_time:
                results.append(v.search(visited + [self], t, score + ((self.max_time - t) * v.flow)))
        return max([*results, score])


def get_valves(max_time):
    valves = {}

    for line in lines:
        name, flow, *conns = re.findall(r"([A-Z]{2}|\d+)+", line)
        valves[name] = Valve(name, int(flow), conns, max_time)

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

    return valves


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))


def calculate_segment(rnge):
    valves = get_valves(26)

    scores = []
    for n in range(rnge[0], rnge[-1] + 1):
        if n % 50 == 0:
            print(f"{(n - rnge[0]) / (rnge[-1] - rnge[0]):.2%}")
        if n in [2 ** x for x in range(17)]:
            continue
        pattern = f"{n:0{15}b}"

        h, e = [], []
        for i, (v, _) in enumerate(valves['AA'].dists.items()):
            (h, e)[pattern[i] == '0'].append(v)

        human_score = valves['AA'].search(h, 0, 0)
        elephant_score = valves['AA'].search(e, 0, 0)
        scores.append(human_score + elephant_score)

    return max(scores)


def part1():
    valves = get_valves(30)

    return valves['AA'].search([], 0, 0)


def part2():
    valves = get_valves(26)
    pw = len(valves) - 1

    ranges = split(range(1, (2 ** pw) - 1), 12)

    with mp.Pool(12) as p:
        scores = p.map(calculate_segment, ranges)

    return max(scores)


if __name__ == '__main__':
    print(part1())
    print(part2())
