import os
from parse import *


class ElfRectangle:
    """ A class to represent a rectangle on a piece of fabric chosen by an elf"""

    def __init__(self, rect_id, left, top, width, height):
        """Creates a new ElfRectangle object with the given properties"""
        self.rect_id = rect_id
        self.left = left
        self.top = top
        self.width = width
        self.height = height


def decode_rectangle(encoded: str) -> ElfRectangle:
    """
    Decodes a string representing an ElfRectangle
    The string should be of the format: #id @ left,top: widthxheight
    :param encoded: the string to be decoded
    :return: the ElfRectangle decoded from the string
    """
    parsed = parse("#{rect_id:d} @ {left:d},{top:d}: {width:d}x{height:d}", encoded)
    rectangle = ElfRectangle(parsed["rect_id"], parsed["left"], parsed["top"],
                             parsed["width"], parsed["height"])
    return rectangle


def read_input(filename: str):
    """
    Reads input from the given file
    :param filename: the file to read from
    :return: a list of the ElfRectangles contained in the file
    """
    rectangles = []
    with open(filename, 'r') as file:
        for line in file:
            rectangle = decode_rectangle(line.strip())
            rectangles.append(rectangle)

    return rectangles


def build_grid(rectangles):
    """
    Builds a representation of all the ElfRectangles mapped out on a large piece
    of fabric. Each square inch is represented by a coordinate.
    :param rectangles: the rectangles to map out
    :return: a mapping from each coordinate (x, y) on the fabric to the number of
    ElfRectangles that coordinate is present in
    """
    all_coords = {}
    for rect in rectangles:
        for x in range(rect.left, rect.left + rect.width):
            for y in range(rect.top, rect.top + rect.height):
                coord = (x, y)
                if coord in all_coords:
                    all_coords[coord] += 1
                else:
                    all_coords[coord] = 1

    return all_coords


def get_overlap(rectangles):
    """
    Gets the number of coordinates on the piece of fabric which are overlapped by
    multiple ElfRectangles
    :param rectangles: the rectangles to check for overlap
    :return: the number of coordinated which are overlapped
    """
    all_coords = build_grid(rectangles)

    overlapping_coords = 0
    for coord, count in all_coords.items():
        if count > 1:
            overlapping_coords += 1

    return overlapping_coords


def main():
    input_file = os.path.join(os.getcwd(), "input")
    rectangles = read_input(input_file)
    num_overlapping = get_overlap(rectangles)
    print("{} square inches of fabric are within two or more claims".format(num_overlapping))


if __name__ == '__main__':
    main()
