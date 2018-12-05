import os
from day5.day5part1 import read_input, process_polymer


def get_components(polymer: str):
    components = []
    for unit in polymer:
        unit = unit.lower()
        if unit not in components:
            components.append(unit)

    return components


def main():
    input_file = os.path.join(os.getcwd(), "input")
    polymer = read_input(input_file)

    components = get_components(polymer)
    lengths = {}
    for unit in components:
        check_polymer = polymer.replace(unit, "")
        check_polymer = check_polymer.replace(unit.upper(), "")
        length = len(process_polymer(check_polymer))
        lengths[unit] = length

    shortest = len(polymer)
    best_to_remove = ""
    for unit, length in lengths.items():
        if length < shortest:
            shortest = length
            best_to_remove = unit

    print("The best type to remove is {0}, resulting in a polymer of length {1}".format(best_to_remove, shortest))


if __name__ == '__main__':
    main()
