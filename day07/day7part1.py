import os
from parse import *


TIME = 60
WORKERS = 5


def read_input(filename: str):
    """
    Reads the input from the given file and returns a dictionary mapping steps to
    the steps which must be completed before them
    """
    steps = {}
    with open(filename, 'r') as file:
        for line in file:
            before, after = parse_step(line)
            if after not in steps:
                steps[after] = []
            if before not in steps:
                steps[before] = []
            steps[after].append(before)

    return steps


def parse_step(line):
    """
    Returns two strings representing the given line
    """
    parsed = parse("Step {before} must be finished before step {after} can begin.", line.strip())
    return parsed["before"], parsed["after"]


def get_starters(steps):
    """
    Returns the steps which do not currently rely on any other steps (i.e. can be
    started now)
    """
    starters = []
    for node in steps:
        if not steps[node]:
            starters.append(node)

    return starters


def remove_mappings(to_remove, steps):
    """
    Removes all instances of the given step (to_remove) from the steps list
    """
    for node in steps:
        if to_remove in steps[node]:
            steps[node].remove(to_remove)


def main():
    input_file = os.path.join(os.getcwd(), "input")
    steps = read_input(input_file)

    # a topological sort of all the given steps
    topo = []
    starters = sorted(get_starters(steps))

    while starters:
        node = starters[0]
        steps.pop(node)
        topo.append(node)
        remove_mappings(node, steps)
        starters = sorted(get_starters(steps))

    ordered = "".join(topo)

    print("Correct order of steps is {}".format(ordered))


if __name__ == '__main__':
    main()
