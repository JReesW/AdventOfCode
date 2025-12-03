from enum import Enum
from math import lcm
from functools import reduce


class Pulse(Enum):
    LOW = 0
    HIGH = 1


class Module:  # Broadcast
    def __init__(self, name: str, targets: list[str]):
        self.name = name
        self.targets = targets
    
    def pulse(self, source: str, p: Pulse):
        for target in self.targets:
            pulse_queue.append((self.name, target, p))


class FlipFlop(Module):
    def __init__(self, name: str, targets: list[str]):
        super().__init__(name, targets)

        self.on = False
    
    def pulse(self, source:str, p: Pulse):
        if p == Pulse.LOW:
            self.on = not self.on
            output = Pulse.HIGH if self.on else Pulse.LOW
            for target in self.targets:
                pulse_queue.append((self.name, target, output))


class Conjunction(Module):
    def __init__(self, name: str, targets: list[str]):
        super().__init__(name, targets)

        self.memory: dict[str: Pulse] = {}
    
    def pulse(self, source: str, p: Pulse):
        self.memory[source] = p
        output = Pulse.LOW if all(m == Pulse.HIGH for m in self.memory.values()) else Pulse.HIGH
        for target in self.targets:
            pulse_queue.append((self.name, target, output))


registry: dict[str, Module] = {}
pulse_queue: list[tuple[str, str, Pulse]] = []


with open("addenda/input20.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def register():
    registry.clear()
    pulse_queue.clear()

    for line in lines:
        source, targets = line.split(' -> ')
        if source[0] == '%':
            registry[source[1:]] = FlipFlop(source[1:], targets.split(', '))
        elif source[0] == '&':
            registry[source[1:]] = Conjunction(source[1:], targets.split(', '))
        else:
            registry['broadcast'] = Module('broadcast', targets.split(', '))
    
    # Register modules that target conjunctions, for the conjunction memory
    for name, module in registry.items():
        for target in module.targets:
            if target in registry and isinstance(registry[target], Conjunction):
                registry[target].memory[name] = Pulse.LOW


def part1():
    register()

    low, high = 0, 0
    for _ in range(1000):
        pulse_queue.append(('button', 'broadcast', Pulse.LOW))
        while pulse_queue:
            (source, target, pulse) = pulse_queue.pop(0)
            if pulse == Pulse.LOW: low += 1
            if pulse == Pulse.HIGH: high += 1
            if target in registry:
                registry[target].pulse(source, pulse)
    
    return low * high


def part2():
    register()

    # Find all conjunctions eventually leading to rx that are triggered by flipflops
    triggered_by_flipflops = {}
    conjunction_queue = [name for name, module in registry.items() if 'rx' in module.targets]

    while conjunction_queue:
        module = conjunction_queue.pop()
        for source in registry[module].memory:
            if isinstance(registry[source], Conjunction):
                conjunction_queue.append(source)
            else:
                triggered_by_flipflops[module] = 0
                break
    
    presses = 0
    while not all(triggered_by_flipflops.values()):
        pulse_queue.append(('button', 'broadcast', Pulse.LOW))
        presses += 1
        while pulse_queue:
            (source, target, pulse) = pulse_queue.pop(0)
            if source in triggered_by_flipflops and pulse == Pulse.LOW and triggered_by_flipflops[source] == 0:
                triggered_by_flipflops[source] = presses
            if target in registry:
                registry[target].pulse(source, pulse)
    
    return reduce(lcm, triggered_by_flipflops.values())


print(part1())
print(part2())
