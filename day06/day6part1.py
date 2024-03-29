import os


def read_input(filename: str):
    """
    Reads input from the given file and returns a list of tuples of the coordinates
    contained therein, as well as two tuples containing the min and max x and y values
    """
    coords = []
    with open(filename, 'r') as file:
        for line in file:
            x, _, y = line.strip().partition(", ")
            x = int(x)
            y = int(y)
            coords.append((x, y))

        min_x = min(coord[0] for coord in coords)
        min_y = min(coord[1] for coord in coords)
        max_x = max(coord[0] for coord in coords)
        max_y = max(coord[1] for coord in coords)

    return coords, (min_x, min_y), (max_x, max_y)


def manhattan(coord1, coord2):
    """
    Returns the manhattan distance between the given two coordinates
    """
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


def bounded(coord, coords):
    """
    Determines whether the given coordinate is bounded by the list of coordinates
    """
    xmax_bound = False
    ymax_bound = False
    xmin_bound = False
    ymin_bound = False

    for other in coords:
        if other[0] > coord[0]:
            xmax_bound = True
        elif other [0] < coord[0]:
            xmin_bound = True

        if other[1] > coord[1]:
            ymax_bound = True
        elif other[1] < coord[1]:
            ymin_bound = True

    return xmax_bound and ymax_bound and xmin_bound and ymin_bound


def are_equal(coord1, coord2):
    """
    Returns True if the two given coordinates have equal x and y coordinates, False
    otherwise
    """
    return coord1[0] == coord2[0] and coord1[1] == coord2[1]


def get_closest(start, coords):
    """
    Determines the coordinate in coords which is closest to the start coordinate.
    Returns None if two coordinates are equally close.
    """
    distances = {}
    for coord in coords:
        distances[coord] = manhattan(start, coord)

    lowest = min(distances.values())
    lowest_count = 0
    closest_coord = None
    for coord, distance in distances.items():
        if distance == lowest:
            lowest_count += 1
            closest_coord = coord

    if lowest_count > 1:
        closest_coord = None

    return closest_coord


def main():
    input_file = os.path.join(os.getcwd(), "input")
    coords, mins, maxes = read_input(input_file)

    closests = {}
    infinites = []
    for x in range(mins[0], maxes[0] + 1):
        for y in range(mins[1], maxes[1] + 1):
            closest = get_closest((x, y), coords)
            if not closest:
                continue

            if bounded((x, y), coords):
                if closest not in closests:
                    closests[closest] = 0
                closests[closest] += 1
            else:
                if closest not in infinites:
                    infinites.append(closest)

    current_max = 0
    for coord, count in closests.items():
        if count > current_max and coord not in infinites:
            current_max = count

    print("Biggest area is {}".format(current_max))


if __name__ == '__main__':
    main()
