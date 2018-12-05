import os


def read_input(filename: str):
    polymer = ""
    with open(filename, 'r') as file:
        for line in file:
            polymer = line

    return polymer


def opposite_polarity(unit1: str, unit2: str):
    return (unit1.isupper() and unit2.islower()) or \
           (unit1.islower() and unit2.isupper())


def same_type(unit1: str, unit2: str):
    return unit1.lower() == unit2.lower()


def will_react(unit1: str, unit2: str):
    return opposite_polarity(unit1, unit2) and same_type(unit1, unit2)


def process_polymer(polymer: str):
    remaining = polymer
    current = 0
    while current < len(remaining) - 1:
        first = remaining[current]
        second = remaining[current + 1]
        if will_react(first, second):
            if current != 0:
                remaining = remaining[0:current] + remaining[current + 2:]
                current -= 1
            else:
                remaining = remaining[current + 2:]
        else:
            current += 1

    return remaining


def main():
    input_file = os.path.join(os.getcwd(), "input")
    polymer = read_input(input_file)

    remaining = process_polymer(polymer)
    print("The remaining polymer is {} long".format(len(remaining)))


if __name__ == '__main__':
    main()
