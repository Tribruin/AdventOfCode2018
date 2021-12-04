#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from timeit import timeit
from collections import Counter

# sys.path.append("/Users/rblount/Scripts/AdventOfCode/tools")

from AOC import AOC

testing = False


def part1():
    ids = data.read_lines()
    doubles = 0
    triples = 0
    for id in ids:
        counts = Counter(id)
        values = counts.values()
        if 2 in values:
            doubles += 1
        if 3 in values:
            triples += 1
    print(doubles * triples)


def part2():
    ids = data.read_lines()
    for i in range(len(ids) - 1):
        for k in range(i + 1, len(ids)):
            non_matches = 0
            for x in range(len(ids[i])):
                if ids[i][x] != ids[k][x]:
                    non_matches += 1
            if non_matches == 1:
                for x in range(len(ids[i])):
                    if ids[i][x] == ids[k][x]:
                        print(ids[i][x], end="")

                print()
                return


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    global data
    data = AOC(codeDate, codeYear, test=testing)

    print(f"Time for Part One: {timeit(part1, number=1)}")
    print(f"Time for Part Two: {timeit(part2, number=1)}")


if __name__ == "__main__":
    main()
