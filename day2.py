import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    data_in_lines = [line for line in puzzle_input.splitlines()]
    data = {}
    for num, line in enumerate(data_in_lines, start=1):
        data[num] = {"red": [], "green": [], "blue": []}
        line_tokens = line.split()
        for index, token in enumerate(line_tokens):
            if "red" in token:
                data[num]["red"].append(int(line_tokens[index - 1]))
            elif "green" in token:
                data[num]["green"].append(int(line_tokens[index - 1]))
            elif "blue" in token:
                data[num]["blue"].append(int(line_tokens[index - 1]))

    return data


def part1(data):
    """Solve part 1
    Determine which games would have been possible if the bag had been loaded with
    only 12 red cubes, 13 green cubes, and 14 blue cubes.
    What is the sum of the IDs of those games?
    """
    sum = 0
    for game_index, value in data.items():
        is_game_possible = True
        for color, list_of_occurrences in value.items():
            if color == "red":
                for num in list_of_occurrences:
                    if num > 12:
                        is_game_possible = False

            if color == "green":
                for num in list_of_occurrences:
                    if num > 13:
                        is_game_possible = False

            if color == "blue":
                for num in list_of_occurrences:
                    if num > 14:
                        is_game_possible = False

        if is_game_possible:
            sum += game_index

    return sum


def part2(data):
    """Solve part 2
    The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
    The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively.
    Adding up these five powers produces the sum 2286.

    For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
    """
    sum = 0
    power = 0
    for game_index, value in data.items():
        for color, list_of_occurrences in value.items():
            if color == "red":
                max_red = max(list_of_occurrences)

            if color == "green":
                max_green = max(list_of_occurrences)

            if color == "blue":
                max_blue = max(list_of_occurrences)

        power = max_red * max_green * max_blue
        sum += power

    return sum


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = pathlib.Path("data/day2.txt").read_text().strip()
    solution1, solution2 = solve(puzzle_input)
    solutions = (solution1, solution2)
    print("\n".join(str(solution) for solution in solutions))
