import os
from day1.day1part1 import read_input


def first_recurring_frequency(frequencies):
    """
    Finds the first frequency (found by adding together all the frequencies from
    the input) which is repeated
    :param frequencies: the frequencies being added
    :return: the first frequency which is repeated
    """
    resulting_frequencies = []
    current_total = 0
    resulting_frequencies.append(current_total)
    duplicate = False

    # the frequencies need to be looked at repeatedly until a duplicate is found
    while not duplicate:
        for frequency in frequencies:
            current_total += frequency
            if current_total not in resulting_frequencies:
                resulting_frequencies.append(current_total)
            else:
                duplicate = True
                break

    return current_total


def main():
    input_file = os.path.join(os.getcwd(), "input")
    frequencies = read_input(input_file)
    frequency = first_recurring_frequency(frequencies)
    print("First recurring frequency is " + str(frequency))


if __name__ == '__main__':
    main()
