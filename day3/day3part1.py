import os
from parse import *


class ElfRectangle:
    def __init__(self, id, left, top, width, height):
        self.id = id
        self.left = left
        self.top = top
        self.width = width
        self.height = height


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.x * 3 + self.y * 5


class Grid:
    def __init__(self):
        self.positions = []

    def add_coord(self, coord: Coordinate):
        self.positions.append(coord)

    def is_overlap(self, coord: Coordinate):
        return coord in self.positions


# Format: #id @ left,top: widthxheight
def decode_rectangle(encoded: str) -> ElfRectangle:
    parsed = parse("#{rect_id:d} @ {left:d},{top:d}: {width:d}x{height:d}", encoded)
    rectangle = ElfRectangle(parsed["rect_id"], parsed["left"], parsed["top"],
                             parsed["width"], parsed["height"])
    return rectangle


def read_input(filename: str):
    rectangles = []
    with open(filename, 'r') as file:
        for line in file:
            rectangle = decode_rectangle(line.strip())
            rectangles.append(rectangle)

    return rectangles


def build_grid(rectangles):
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
