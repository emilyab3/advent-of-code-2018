import os
from day5.day5part1 import read_input, process_polymer


def get_components(polymer: str):
    """
    Returns a list of all the distinct characters which make up the given polymer
    (all lowercase)
    """
    components = []
    for unit in polymer:
        unit = unit.lower()
        if unit not in components:
            components.append(unit)

    return components


def experiment(polymer):
    """
    Determines the resulting lengths of polymers produced by removing all instances
    (both upper and lowercase) of a single character, and then processing the resulting
    polymer.

    Returns a mapping from character removed to resulting length.
    """
    components = get_components(polymer)
    lengths = {}
    for unit in components:
        check_polymer = polymer.replace(unit, "")
        check_polymer = check_polymer.replace(unit.upper(), "")
        length = len(process_polymer(check_polymer))
        lengths[unit] = length

    return lengths


def best_to_remove(polymer, lengths):
    """
    Determines which character in the given polymer, if removed, will result in
    the shortest length after processing
    """
    shortest = len(polymer)
    best = ""
    for unit, length in lengths.items():
        if length < shortest:
            shortest = length
            best = unit

    return best


def main():
    input_file = os.path.join(os.getcwd(), "input")
    polymer = read_input(input_file)

    lengths = experiment(polymer)
    best = best_to_remove(polymer, lengths)

    print("The best type to remove is {0}, resulting in a polymer of "
          "length {1}".format(best, lengths[best]))


if __name__ == '__main__':
    main()
