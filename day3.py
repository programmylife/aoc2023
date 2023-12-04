import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""

    data_in_lines = [line for line in puzzle_input.splitlines()]
    data = []
    for line in data_in_lines:
        new = []
        for character in line:
            new.append(character)
        data.append(new)

    return data


def part1(data):
    """Solve part 1
    The engine schematic (your puzzle input) consists of a visual representation of the engine.
    There are lots of numbers and symbols you don't really understand, but apparently any number
    adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum.
    (Periods (.) do not count as a symbol.)

    Here is an example engine schematic:

    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..

    In this schematic, two numbers are not part numbers because they are not adjacent to a symbol:
    114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is
    a part number; their sum is 4361.

    Of course, the actual engine schematic is much larger.
    What is the sum of all of the part numbers in the engine schematic?
    """
    sum = 0

    for line_index, line in enumerate(data, start=0):
        is_adjacent_to_symbol = False
        current_number = []
        for character_index, character in enumerate(line, start=0):
            if character.isdigit() and not is_adjacent_to_symbol:
                is_adjacent_to_symbol = check_adjacency(
                    data, character_index, line_index
                )
                current_number.append(character)
            elif is_adjacent_to_symbol:
                if character.isdigit():
                    current_number.append(character)
                    if character_index == 139:
                        sum += int("".join(current_number))
                        current_number = []
                        is_adjacent_to_symbol = False
                else:
                    sum += int("".join(current_number))
                    current_number = []
                    is_adjacent_to_symbol = False
            else:
                current_number = []

    return sum


def check_adjacency(data, x, y):
    if y == 139:
        adjacent_squares = [
            data[y - 1][x - 1],
            data[y - 1][x],
            data[y - 1][x + 1],
            data[y][x - 1],
            data[y][x + 1],
        ]
    elif x == 139:
        adjacent_squares = [
            data[y - 1][x - 1],
            data[y - 1][x],
            data[y][x - 1],
            data[y + 1][x - 1],
            data[y + 1][x],
        ]
    else:
        adjacent_squares = [
            data[y - 1][x - 1],
            data[y - 1][x],
            data[y - 1][x + 1],
            data[y][x - 1],
            data[y][x + 1],
            data[y + 1][x - 1],
            data[y + 1][x],
            data[y + 1][x + 1],
        ]
    for character in adjacent_squares:
        if character != "." and not character.isdigit():
            return True

    return False


def part2(data):
    """Solve part 2
    A gear is any * symbol that is adjacent to exactly two part numbers.
    Its gear ratio is the result of multiplying those two numbers together.

    What is the sum of all of the gear ratios in your engine schematic?
    """

    sum = 0

    for line_index, line in enumerate(data, start=0):
        is_adjacent_to_symbol = False
        current_number = []
        # for character_index, character in enumerate(line,start=0):
        #     if character == "*":


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = pathlib.Path("data/day3.txt").read_text().strip()
    solution1, solution2 = solve(puzzle_input)
    solutions = (solution1, solution2)
    print("\n".join(str(solution) for solution in solutions))
