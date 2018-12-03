import os


def read_input(filename):
    frequencies = []
    with open(filename, 'r') as file:
        for line in file:
            frequencies.append(line.strip())

    return frequencies


def get_letter_frequencies(word: str) -> dict:
    frequencies = {}
    for char in word:
        if char not in frequencies:
            frequencies[char] = 1
        else:
            frequencies[char] += 1

    return frequencies


def exactly_x_occurrences(word: str, x: int) -> bool:
    frequencies = get_letter_frequencies(word)
    for char in frequencies:
        if frequencies[char] == x:
            return True

    return False


def get_checksum(words):
    exactly_two = 0
    exactly_three = 0
    for word in words:
        if exactly_x_occurrences(word, 2):
            exactly_two += 1

        if exactly_x_occurences(word, 3):
            exactly_three += 1

    checksum = exactly_two * exactly_three
    return checksum


def main():
    input_file = os.path.join(os.getcwd(), "input")
    words = read_input(input_file)
    checksum = get_checksum(words)
    print("The checksum for this list is " + str(checksum))


if __name__ == "__main__":
    main()
