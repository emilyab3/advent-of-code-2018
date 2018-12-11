import os
from day06.day6part1 import read_input, manhattan


MAX_TOTAL_DISTANCE = 10000


def main():
    input_file = os.path.join(os.getcwd(), "input")
    coords, mins, maxes = read_input(input_file)

    goldilocks_zone = 0
    for x in range(mins[0], maxes[0] + 1):
        for y in range(mins[1], maxes[1] + 1):
            total_distance = 0
            for coord in coords:
                total_distance += manhattan((x, y), coord)

            if total_distance < MAX_TOTAL_DISTANCE:
                goldilocks_zone += 1

    print("Size of the region is {}".format(goldilocks_zone))


if __name__ == '__main__':
    main()
