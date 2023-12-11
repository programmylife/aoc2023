# template for aoc day

import pathlib
import sys
import re
from math import lcm


def parse(puzzle_input):
    """Parse input"""
    data = [line for line in puzzle_input.splitlines()]
    return data


def part1(data):
    """Solve part 1"""
    result = 0
    for line in data:
        current_difference_list = line.split()
        current_difference_list = [int(num) for num in current_difference_list]
        difference_lists = []
        difference_lists.append(current_difference_list)
        while any(current_difference_list):
            current_difference_list = generate_difference_list(current_difference_list)
            difference_lists.append(current_difference_list)

        extrapolated_value = 0
        for current_list in difference_lists:
            extrapolated_value += current_list[-1]

        result += extrapolated_value

    return result


def generate_difference_list(line):
    difference_list = []
    prev_num = "a"
    for num in line:
        if prev_num == "a":
            prev_num = num
            continue
        difference_list.append(num - prev_num)
        prev_num = num
    return difference_list


def part2(data):
    """Solve part 2"""
    result = 0
    for line in data:
        current_difference_list = line.split()
        current_difference_list = [int(num) for num in current_difference_list]
        difference_lists = []
        difference_lists.append(current_difference_list)
        while any(current_difference_list):
            current_difference_list = generate_difference_list(current_difference_list)
            difference_lists.append(current_difference_list)

        extrapolated_value = 0
        # reverse the lists, then loop over them
        for current_list in reversed(difference_lists):
            # skip list of 0s
            if not any(current_list):
                continue
            extrapolated_value = current_list[0] - extrapolated_value

        result += extrapolated_value

    return result


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = pathlib.Path("data/day9.txt").read_text().strip()
    solution1, solution2 = solve(puzzle_input)
    solutions = (solution1, solution2)
    print("\n".join(str(solution) for solution in solutions))
