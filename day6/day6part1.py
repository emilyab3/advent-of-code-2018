import os


def read_input(filename: str):
    """
    Reads input from the given file and returns a mapping from the datetimes in the
    file to their corresponding messages
    :param filename: the file to read
    :return: the mapping from datetimes to messages
    """
    coords = []
    min_x = 1000
    min_y = 1000
    max_x = -1000
    max_y = -1000
    with open(filename, 'r') as file:
        for line in file:
            x, _, y = line.strip().partition(", ")
            x = int(x)
            y = int(y)
            coords.append((x, y))

            min_x = x if x < min_x else min_x
            min_y = y if y < min_y else min_y
            max_x = x if x > max_x else max_x
            max_y = y if y > max_y else max_y

    return coords, (min_x, min_y), (max_x, max_y)


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def bounded(coord, coords):
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


def are_equal(x, y):
    return x[0] == y[0] and x[1] == y[1]


def get_closest(x, coords):
    distances = {}
    for coord in coords:
        distances[coord] = manhattan(x, coord)

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
