# template for aoc day

import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    data_in_lines = [line for line in puzzle_input.splitlines()]
    data = {}

    times = data_in_lines[0].split()
    times.pop(0)
    distances = data_in_lines[1].split()
    distances.pop(0)
    return times, distances


def part1(data):
    """Solve part 1
    Time:      7  15   30
    Distance:  9  40  200

    This document describes three races:

    The first race lasts 7 milliseconds. The record distance in this race is 9 millimeters.
    The second race lasts 15 milliseconds. The record distance in this race is 40 millimeters.
    The third race lasts 30 milliseconds. The record distance in this race is 200 millimeters.
    Your toy boat has a starting speed of zero millimeters per millisecond. For each whole millisecond
    you spend at the beginning of the race holding down the button, the boat's speed increases by one
    millimeter per millisecond.

    Since the current record for this race is 9 millimeters, there are actually 4 different ways you could win:
    you could hold the button for 2, 3, 4, or 5 milliseconds at the start of the race.
    To see how much margin of error you have, determine the number of ways you can beat the record in each race;
    in this example, if you multiply these values together, you get 288 (4 * 8 * 9).
    """

    # calculate distances
    ways_to_win_list = []
    result = 1
    for race_end_time, race_final_distance in zip(data[0], data[1]):
        ways_to_win_count = 0
        for time in range(int(race_end_time) + 1):
            velocity = int(time)
            remaining_time = int(race_end_time) - int(time)
            distance = velocity * remaining_time
            if distance > int(race_final_distance):
                ways_to_win_count += 1

        result *= ways_to_win_count

    return result


def part2(data):
    """Solve part 2"""
    race_end_time = int("".join(time for time in data[0]))
    race_final_distance = int("".join(distance for distance in data[1]))
    ways_to_win_count = 0
    for time in range(int(race_end_time) + 1):
        velocity = int(time)
        remaining_time = int(race_end_time) - int(time)
        distance = velocity * remaining_time
        if distance > int(race_final_distance):
            ways_to_win_count += 1

    return ways_to_win_count


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = pathlib.Path("data/day6.txt").read_text().strip()
    solution1, solution2 = solve(puzzle_input)
    solutions = (solution1, solution2)
    print("\n".join(str(solution) for solution in solutions))
