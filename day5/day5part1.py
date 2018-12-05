import os


def read_input(filename: str) -> str:
    """
    Reads a polymer from the given file and returns it as a string
    """
    polymer = ""
    with open(filename, 'r') as file:
        for line in file:
            polymer = line

    return polymer


def opposite_polarity(unit1: str, unit2: str):
    """
    Returns True if the given units have opposite polarities (i.e. are different
    cases), False otherwise
    """
    return (unit1.isupper() and unit2.islower()) or \
           (unit1.islower() and unit2.isupper())


def same_type(unit1: str, unit2: str):
    """
    Returns True if the given two units have the same type (i.e. are the same
    letter, regardless of case), False otherwise
    """
    return unit1.lower() == unit2.lower()


def will_react(unit1: str, unit2: str):
    """
    Returns True if the given two units will react with each other (i.e. have opposite
    polarities and the same type), False otherwise
    """
    return opposite_polarity(unit1, unit2) and same_type(unit1, unit2)


def process_polymer(polymer: str):
    """
    Processes the given polymer, removing any reacting pairs which are present
    """
    remaining = polymer
    current = 0
    while current < len(remaining) - 1:
        first = remaining[current]
        second = remaining[current + 1]

        if will_react(first, second):
            # cuts the reacting units out of the polymer
            if current != 0:
                remaining = remaining[0:current] + remaining[current + 2:]
                current -= 1
            else:
                remaining = remaining[current + 2:]
        else:
            # no reaction, progresses along the polymer
            current += 1

    return remaining


def main():
    input_file = os.path.join(os.getcwd(), "input")
    polymer = read_input(input_file)

    remaining = process_polymer(polymer)
    print("The remaining polymer is {} long".format(len(remaining)))


if __name__ == '__main__':
    main()
