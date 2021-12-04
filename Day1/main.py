#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from itertools import cycle
from timeit import timeit

# sys.path.append("/Users/rblount/Scripts/AdventOfCode/tools")

from AOC import AOC

testing = False


def part1():
    print(sum(data.read_int()))


def part2():
    freq_changes = cycle(data.read_int())
    found_freqs = list()
    current_freq = 0
    for freq in freq_changes:
        current_freq += freq
        if current_freq in found_freqs:
            print(current_freq)
            break
        else:
            found_freqs.append(current_freq)
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
