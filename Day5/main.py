#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC

testing = False


def change_case(char: str):
    if char.isupper():
        return char.lower()
    else:
        return char.upper()


def parse_polymer(polymer):
    polymer_length = len(polymer)
    new_polymer = ""
    i = 0
    while i < polymer_length:

        if i == polymer_length - 1:
            new_polymer += polymer[i]
            i += 1
        elif polymer[i] == change_case(polymer[i + 1]):
            i += 2
        else:
            new_polymer += polymer[i]
            i += 1
    return new_polymer


def remove_unit(polymer, unit):

    units_to_remove = [unit.lower(), unit.upper()]
    new_polymer = [char for char in polymer if char not in units_to_remove]
    return "".join(new_polymer)


def split_polymer(polymer):
    char_list = [x.lower() for x in polymer]
    return sorted(list(set(char_list)))


def react_polymer(polymer):

    new_polymer_length = 1
    polymer_length = len(polymer)
    while polymer_length != new_polymer_length and new_polymer_length != 0:
        polymer_length = len(polymer)
        new_polymer = parse_polymer(polymer)
        new_polymer_length = len(new_polymer)
        polymer = new_polymer

    return new_polymer


def part1(polymer):

    new_polymer = react_polymer(polymer)
    print(len(new_polymer))


def part2(polymer):
    shortest_polymer = len(polymer)
    units_to_check = split_polymer(polymer)
    for unit in units_to_check:
        print(f"Checking Unit: {unit}", end="")
        polymer_to_check = remove_unit(polymer, unit)
        new_polymer = react_polymer(polymer_to_check)
        print(f" - {len(new_polymer)}")
        if len(new_polymer) < shortest_polymer:
            shortest_polymer = len(new_polymer)
            shortest_unit = unit
    print(f"Unit {shortest_unit} - Polymer length {shortest_polymer}")


def main():
    # Get the path name and strip to the last 1 or 2 characters
    codePath = os.path.dirname(sys.argv[0])
    codeDate = int(codePath.split("/")[-1][3:])
    codeYear = int(codePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {codeYear} - Day {codeDate}")

    global data
    data = AOC(codeDate, codeYear, test=testing)
    input = data._read_file().strip()

    # part1(input)
    part2(input)


if __name__ == "__main__":
    main()
