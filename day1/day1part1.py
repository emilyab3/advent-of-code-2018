import os


def read_input(filename):
    frequencies = []
    with open(filename, 'r') as file:
        for line in file:
            frequency = int(line)
            frequencies.append(frequency)

    return frequencies


def main():
    input_file = os.path.join(os.getcwd(), "input")
    frequencies = read_input(input_file)

    total_frequency = 0
    for frequency in frequencies:
        total_frequency += frequency

    print(total_frequency)


if __name__ == '__main__':
    main()
