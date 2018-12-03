import os
from day3.day3part1 import read_input, build_grid


def one_true_elf(rectangles):
    """
    Returns the ID of the ElfRectangle which does not overlap with any other ElfRectangle
    :param rectangles: the rectangles to be checked
    :return: the ID of the non-overlapping rectangle, or 0 if none exists
    """
    all_coords = build_grid(rectangles)
    for rect in rectangles:
        is_overlap = False
        for x in range(rect.left, rect.left + rect.width):
            for y in range(rect.top, rect.top + rect.height):
                coord = (x, y)
                if all_coords[coord] > 1:
                    is_overlap = True

        if not is_overlap:
            return rect.rect_id

    return 0


def main():
    input_file = os.path.join(os.getcwd(), "input")
    rectangles = read_input(input_file)
    winning_elf = one_true_elf(rectangles)
    print("The ID of the only non-overlapping claim is {}".format(winning_elf))


if __name__ == '__main__':
    main()
