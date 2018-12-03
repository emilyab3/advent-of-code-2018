import os
import sys
from day1.day1part1 import read_input


def main():
    input_file = os.path.join(os.getcwd(), "input")
    frequencies = read_input(input_file)
    # frequencies = [1, -1]
    resulting_frequencies = []
    current_total = 0
    resulting_frequencies.append(current_total)
    duplicate = False
    while not duplicate:
        for frequency in frequencies:
            current_total += frequency
            if current_total not in resulting_frequencies:
                resulting_frequencies.append(current_total)
            else:
                duplicate = True
                print("First recurring frequency is " + str(current_total))
                break


if __name__ == '__main__':
    main()
