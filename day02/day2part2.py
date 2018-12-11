import os
from day02.day2part1 import read_input


def remove_differing_character(word1: str, word2: str) -> str:
    """
    Removes any characters which are at the same index of word1 and word2, but which
    are different
    :param word1: the first word to check
    :param word2: the second word to check
    :return: a string with any differing characters absent
    """
    result = ""
    for index, char in enumerate(word1):
        if char == word2[index]:
            result += char

    return result


def differ_count(word1: str, word2: str) -> int:
    """
    The number of characters which are different at the same indices of word1 and
    word2. Assumes words are of equal length.
    :param word1: the first word to check
    :param word2: the second word to check
    :return: the number  of differing indices in these two words
    """
    difference = 0
    for index, char in enumerate(word1):
        if char != word2[index]:
            difference += 1

    return difference


def get_close_words(words):
    """
    Gets the words in the given list which differ by exactly one character
    :param words: the words to compare
    :return: a tuple of the two close words
    """
    for word1 in words:
        for word2 in words:
            if differ_count(word1, word2) == 1:
                return word1, word2


def main():
    input_file = os.path.join(os.getcwd(), "input")
    words = read_input(input_file)
    close_words = get_close_words(words)

    if close_words:
        final = remove_differing_character(close_words[0], close_words[1])
        print("The two words differ at character " + final)


if __name__ == "__main__":
    main()
