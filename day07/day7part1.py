import os
from parse import *


OFFSET = 64
TIME = 60
WORKERS = 5


class Node:
    def __init__(self, current):
        self.current = current
        self.incoming = []
        self.outgoing = []

    def add_incoming(self, incoming):
        self.incoming.append(incoming)

    def add_outgoing(self, outgoing):
        self.outgoing.append(outgoing)

    def __lt__(self, other):
        return self.current < other.current

    def __eq__(self, other):
        return self.current == other.current

    def __hash__(self):
        return ord(self.current)


def read_input(filename: str):
    # steps = []
    steps = {}
    with open(filename, 'r') as file:
        for line in file:
            before, after = parse_step(line)
            # current = Node(after)
            if after not in steps:
                steps[after] = []
            if before not in steps:
                steps[before] = []
            # if current not in steps:
            # current.add_incoming(before)
            steps[after].append(before)

    return steps


def get_starters(steps):
    starters = []
    for node in steps:
        if not steps[node]:
            starters.append(node)

    return starters


def parse_step(line):
    parsed = parse("Step {before} must be finished before step {after} can begin.", line.strip())
    return parsed["before"], parsed["after"]


def remove_mappings(to_remove, steps):
    for node in steps:
        if to_remove in steps[node]:
            steps[node].remove(to_remove)


def main():
    input_file = os.path.join(os.getcwd(), "input")
    steps = read_input(input_file)

    topo = []
    starters = sorted(get_starters(steps))

    while starters:
        node = starters[0]
        steps.pop(node)
        # starters.remove(node)
        topo.append(node)
        remove_mappings(node, steps)
        starters = sorted(get_starters(steps))

    ordered = "".join(topo)

    print("Correct order of steps is {}".format(ordered))


if __name__ == '__main__':
    main()
