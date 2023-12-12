# template for aoc day

import pathlib
import sys
import re
from contextlib import suppress

def parse(puzzle_input):
    """Parse input"""
    puzzle_by_line = [line for line in puzzle_input.splitlines()]
    for count, line in enumerate(puzzle_by_line):
        if "S" in line:
            start_y = count
            start_x = puzzle_by_line[start_y].index("S")

    return puzzle_by_line, start_y, start_x


def part1(data):
    """Solve part 1"""
    puzzle, start_y, start_x = data

    height = len(puzzle)
    width = len(puzzle[0])
    visited = set()
    best_distance = 0
    stack = [(start_y, start_x, 0)]

    # initialize this so it doesn't reset when checking for S right at the beginning
    loop = None
    path_length = 0
    while len(stack) > 0:
        y, x, current_distance = stack.pop(0)

        if y > height - 1 or y < 0 or x > width - 1 or x < 0:
            continue

        if (x, y) in visited:
            continue
        visited.add((x, y))

        best_distance = max(best_distance, current_distance)

        next_positions = get_next_positions(puzzle, stack, x, y)
        if next_positions == None:
            continue
        for x, y in next_positions:
            stack.append((x, y, current_distance + 1))

    return (best_distance + 1) // 2


def get_next_positions(puzzle, stack, x, y):
    value = puzzle[y][x]
    if value == "|":
        return (
            (y - 1, x),  # North
            (y + 1, x),  # South
        )
    elif value == "-":
        return (
            (y, x - 1),  # West
            (y, x + 1),  # East
        )
    elif value == "L":
        return (
            (y - 1, x),  # North
            (y, x + 1),  # East
        )
    elif value == "J":
        return (
            (y - 1, x),  # North
            (y, x - 1),  # West
        )
    elif value == "7":
        return (
            (y, x - 1),  # West
            (y + 1, x),  # South
        )
    elif value == "F":
        return (
            (y, x + 1),  # East
            (y + 1, x),  # South
        )
    elif value == "S":
        return (
            (y - 1, x),  # North
            # (y + 1, x),  # South
            # (y, x + 1),  # East
            # (y, x - 1),  # West
        )


def part2(data):
    """Solve part 2"""


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = pathlib.Path("data/day10.txt").read_text().strip()
    solution1, solution2 = solve(puzzle_input)
    solutions = (solution1, solution2)
    print("\n".join(str(solution) for solution in solutions))

