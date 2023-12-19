import re


with open("addenda/input19.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def create_rule(rule):
    if '<' in rule:
        var, n = rule.split('<')
        return lambda part: part[var] < int(n)
    if '>' in rule:
        var, n = rule.split('>')
        return lambda part: part[var] > int(n)


def part1():
    rules = {}
    inputs = []

    doing_rules = True
    for line in lines:
        if doing_rules:
            if not line:
                doing_rules = False
                continue
            rule, body = line[:-1].split('{')
            conditions = body.split(',')
            rules[rule] = [(create_rule(cond.split(':')[0]), cond.split(':')[1]) for cond in conditions[:-1]]
            rules[rule].append((lambda _: True, conditions[-1]))
        else:
            x, m, a, s = [int(n) for n in re.findall(r'\d+', line)]
            inputs.append({'x': x, 'm': m, 'a': a, 's': s})

    total = 0
    for inp in inputs:
        current_rule = 'in'
        while current_rule not in ('A', 'R'):
            for rule_func, dest in rules[current_rule]:
                if rule_func(inp):
                    current_rule = dest
                    break
        if current_rule == 'A':
            total += sum(inp.values())

    return total


class Rule:
    def __init__(self, rule):
        op = '>' if '>' in rule else '<'
        var, val = rule.split(op)

        self.var = var
        self.op = op
        self.val = int(val)

    def parse(self, part):
        # part looks like {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}
        # returns: [parts that fail], [parts that succeed]
        mn, mx = part[self.var]

        if self.op == '>':
            if mn > self.val:
                return None, part
            elif mx <= self.val:
                return part, None
            else:
                rej, acc = part.copy(), part.copy()
                rej[self.var] = (mn, self.val)
                acc[self.var] = (self.val + 1, mx)
                return rej, acc
        else:
            if mx < self.val:
                return None, part
            elif mn >= self.val:
                return part, None
            else:
                rej, acc = part.copy(), part.copy()
                rej[self.var] = (self.val, mx)
                acc[self.var] = (mn, self.val - 1)
                return rej, acc


def part2():
    rules = {}

    for line in lines:
        if not line:
            break
        rule, body = line[:-1].split('{')
        conditions = body.split(',')
        rules[rule] = [(Rule(cond.split(':')[0]), cond.split(':')[1]) for cond in conditions[:-1]]
        rules[rule].append((None, conditions[-1]))

    parts = [
        ({'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}, 'in', 0)
    ]

    total = 0
    for part, r_id, r_nr in parts:
        if r_id in ('A', 'R'):
            if r_id == 'A':
                t = 1
                for mn, mx in part.values():
                    t *= (mx - mn) + 1
                total += t
        else:
            rule, dest = rules[r_id][r_nr]
            if rule is None:
                parts.append((part, dest, 0))
            else:
                rej, acc = rule.parse(part)
                if rej is not None:
                    parts.append((rej, r_id, r_nr + 1))
                if acc is not None:
                    parts.append((acc, dest, 0))

    return total


print(part1())
print(part2())
