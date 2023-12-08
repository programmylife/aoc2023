# template for aoc day

import pathlib
import sys
import re
from math import lcm


def parse(puzzle_input):
    """Parse input"""
    left_right_instructions, _, *data_in_lines = [
        line for line in puzzle_input.splitlines()
    ]
    data = {"left_right_instructions": left_right_instructions}
    for line in data_in_lines:
        line = line.split()
        data[line[0]] = {
            "L": re.sub(r"\W+", "", line[2].strip()),
            "R": re.sub(r"\W+", "", line[3].strip()),
        }
    return data


def part1(data):
    """Solve part 1"""
    left_right_instructions = data["left_right_instructions"]
    current_element = "AAA"
    step_count = 0
    while current_element != "ZZZ":
        # use step_count to index into lr instructions to find the next direction
        # wrapping if you go past the end
        current_direction = left_right_instructions[
            step_count % len(left_right_instructions)
        ]

        # use next LR instruction to set next element.
        current_element = data[current_element][current_direction]

        step_count += 1

    return step_count


def part2(data):
    """Solve part 2"""
    left_right_instructions = data["left_right_instructions"]
    step_count = 0

    steps_to_finish = []
    for key in data.keys():
        if key[2] == "A":
            current_element = key
            while current_element[2] != "Z":
                # use step_count to index into lr instructions to find the next direction
                # wrapping if you go past the end
                current_direction = left_right_instructions[
                    step_count % len(left_right_instructions)
                ]

                # use next LR instruction to set next element.
                current_element = data[current_element][current_direction]

                step_count += 1
            steps_to_finish.append(step_count)
            step_count = 0

    return lcm(*steps_to_finish)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = pathlib.Path("data/day8.txt").read_text().strip()
    solution1, solution2 = solve(puzzle_input)
    solutions = (solution1, solution2)
    print("\n".join(str(solution) for solution in solutions))
