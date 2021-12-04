#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
import numpy as np
from timeit import timeit

# sys.path.append("/Users/rblount/Scripts/AdventOfCode/tools")

from AOC import AOC

testing = False
fabric_size = 1000


class Claim:
    def __init__(self, claim_input) -> None:
        self.claim_input = claim_input
        claim_split = claim_input.split()
        self.claim_number = claim_split[0][1:]
        self.x_pos, self.y_pos = claim_split[2].strip(":").split(",")
        self.x_pos = int(self.x_pos)
        self.y_pos = int(self.y_pos)
        self.width, self.height = claim_split[3].split("x")
        self.height = int(self.height)
        self.width = int(self.width)


def print_fabric(fabric):
    y_size, x_size = fabric.shape
    for y in range(y_size):
        for x in range(x_size):
            if fabric[y][x] == 0:
                print(".", end="")
            elif fabric[y][x] == 1:
                print("#", end="")
            else:
                print(fabric[y][x], end="")
        print()


def part1():
    fabric = np.zeros((fabric_size, fabric_size), dtype=int)
    for claim in claims:

        fabric[
            claim.y_pos : claim.y_pos + claim.height,
            claim.x_pos : claim.x_pos + claim.width,
        ] += 1

        # print_fabric(fabric)
    overlaps = fabric > 1
    print(overlaps.sum())


def part2():
    base_fabric = np.zeros((fabric_size, fabric_size), dtype=int)
    for claim in claims:

        base_fabric[
            claim.y_pos : claim.y_pos + claim.height,
            claim.x_pos : claim.x_pos + claim.width,
        ] += 1

    for claim in claims:
        overlay = np.zeros((fabric_size, fabric_size), dtype=int)
        overlay[
            claim.y_pos : claim.y_pos + claim.height,
            claim.x_pos : claim.x_pos + claim.width,
        ] += 1

        result = overlay & base_fabric

        if overlay.sum() == result.sum():
            print(claim.claim_number)
            return


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    global data
    data = AOC(codeDate, codeYear, test=testing)

    global claims
    claims = list()
    for claim in data.read_lines():
        x = Claim(claim)
        claims.append(x)

    global fabric
    fabric = np.zeros((1, 1))

    print(f"Time for Part One: {timeit(part1, number=1)}")
    print(f"Time for Part Two: {timeit(part2, number=1)}")


if __name__ == "__main__":
    main()
