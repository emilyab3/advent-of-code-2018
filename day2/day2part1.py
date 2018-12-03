import os


def read_input(filename):
    """
    Reads input from a file
    :param filename: the file to read from
    :return: a list of box IDs
    """
    frequencies = []
    with open(filename, 'r') as file:
        for line in file:
            frequencies.append(line.strip())

    return frequencies


def get_letter_frequencies(box_id: str) -> dict:
    """
    Gets the frequency of each character present in the given box ID
    :param box_id: the box ID to check
    :return: the characters in the box ID mapped to their frequencies
    """
    frequencies = {}
    for char in box_id:
        if char not in frequencies:
            frequencies[char] = 1
        else:
            frequencies[char] += 1

    return frequencies


def exactly_x_occurrences(box_id: str, x: int) -> bool:
    """
    Checks to see whether there are any characters in the given box ID which are
    repeated exactly x times
    :param box_id: the box ID to check
    :param x: the number of times the character should occur
    :return: True if there is a character in box_id which appears exactly x times,
    False otherwise
    """
    frequencies = get_letter_frequencies(box_id)
    for char in frequencies:
        if frequencies[char] == x:
            return True

    return False


def get_checksum(box_ids):
    """
    Returns the checksum of a given list of box IDs
    :param box_ids: the box IDs to calculate the checkum for
    :return: the checksum for the box IDs
    """
    exactly_two = 0
    exactly_three = 0
    for box_id in box_ids:
        if exactly_x_occurrences(box_id, 2):
            exactly_two += 1

        if exactly_x_occurrences(box_id, 3):
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
