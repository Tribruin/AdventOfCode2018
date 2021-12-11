#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
import numpy as np
from AOC import AOC

testing = True


class Location:
    def __init__(self, coords) -> None:
        self.x, self.y = coords

    def generate_map(
        self,
        size: tuple,
    ):
        x_size, y_size = size
        map = np.zeros((y_size, x_size), dtype=int)
        for y in range(y_size):
            for x in range(x_size):
                map[y][x] = compute_distance((self.x, self.y), (x, y))
        self.map = map

    def compute_area(self, coords_to_check):
        area = np.full(np.shape(self.map), True)
        for coord in coords_to_check:
            # print(area)
            # print(self.map)
            # print()
            # print(coord.map)
            # print()
            # print(self.map < coord.map)
            if not coord == self:
                new_map = self.map < coord.map
                area = area & new_map
            # print(area)
        print(sum(sum(area)))
        return sum(sum(area))


def compute_distance(a: tuple, b: tuple):
    x1, y1 = a
    x2, y2 = b
    return abs(x2 - x1) + abs(y2 - y1)


def parse_input(input: AOC):
    coords = list()
    lines = input.read_lines()
    for line in lines:
        x, y = line.split(",")
        coords.append(Location((int(x), int(y))))
    return coords


def part1(coords):

    # Parse out all the infinate coords
    finite_coords = list()
    coords_to_remote = list()

    all_x_coords = [coord.x for coord in coords]
    lowest_x = min(all_x_coords)
    highest_x = max(all_x_coords)

    all_y_coords = [coord.y for coord in coords]
    lowest_y = min(all_y_coords)
    highest_y = max(all_y_coords)

    for coord in coords:
        coord.generate_map((highest_x + 2, highest_y + 2))

        if (lowest_x < coord.x < highest_x) and (lowest_y < coord.y < highest_y):
            finite_coords.append(coord)

    # Now that we have maped each coordinate, we only need to check the coordinates
    # That are not on the edge
    max_area = 0
    for coord in finite_coords:
        area = coord.compute_area(coords)
        if area > max_area:
            max_area = area
            max_coord = coord

    print(coord.map)
    print(max_area)

    return


def part2():
    pass


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    data = AOC(codeDate, codeYear, test=testing)
    coordinates = parse_input(data)

    part1(coordinates)


if __name__ == "__main__":
    main()
