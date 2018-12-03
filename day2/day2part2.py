import os
from day2.day2part1 import read_input


def remove_differing_character(word1: str, word2: str) -> str:
    result = ""
    for index, char in enumerate(word1):
        if char == word2[index]:
            result += char

    return result


def differ_count(word1: str, word2: str) -> int:
    # assumes words are of equal length
    difference = 0
    for index, char in enumerate(word1):
        if char != word2[index]:
            difference += 1

    return difference


def get_close_words(words):
    # words = sorted(words)
    # for index in range(len(words) - 1):
    #     if differ_count(words[index], words[index + 1]) <= 1:
    #         return words[index], words[index + 1]
    #
    # return None

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
