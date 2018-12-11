import os
from parse import *


class Point:
    def __init__(self, x, y, x_vel, y_vel):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel


def read_input(filename: str):
    points = []
    with open(filename, 'r') as file:
        for line in file:
            point = parse_point(line.strip())
            points.append(point)

    return points


def parse_point(point):
    parsed = parse("position=<{x}, {y}> velocity=<{x_vel}, {y_vel}>", point)
    x = int(parsed["x"].strip())
    y = int(parsed["y"].strip())
    x_vel = int(parsed["x_vel"].strip())
    y_vel = int(parsed["y_vel"].strip())
    new_point = Point(x, y, x_vel, y_vel)
    return new_point


def progress_points(points):
    new_points = []
    for point in points:
        new_point = Point(point.x + point.x_vel, point.y + point.y_vel, point.x_vel, point.y_vel)
        new_points.append(new_point)
    return new_points


def draw_scatter(points, width, height, min_x, min_y):
    rows = []
    for y in range(height + 1):
        row = []
        for x in range(width + 1):
            row.append(".")
        rows.append(row)

    for point in points:
        rows[point.y - min_y][point.x - min_x] = "#"

    rows_to_print = ["".join(row) for row in rows]
    print("\n".join(rows_to_print))


def main():
    input_file = os.path.join(os.getcwd(), "input")
    points = read_input(input_file)

    last_area = 999999999
    seconds = 0
    while True:
        new_points = progress_points(points)

        min_x = min([point.x for point in new_points])
        min_y = min([point.y for point in new_points])
        max_x = max([point.x for point in new_points])
        max_y = max([point.y for point in new_points])

        width = max_x - min_x
        height = max_y - min_y
        area = width + height

        if area > last_area:
            draw_scatter(points, width, height, min_x, min_y)
            break

        last_area = area
        points = new_points
        seconds += 1

    print(seconds)  # part 2


if __name__ == '__main__':
    main()
