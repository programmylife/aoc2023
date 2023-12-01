# template for aoc day

import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [line for line in puzzle_input.split()]


def part1(data):
    """Solve part 1"""
    sum = 0
    for line in data:
        digits = []
        for character in line:
            # get all digits
            if character.isdigit():
                digits.append(character)

        # if there is only one digit, repeat it. Otherwise, choose the first and last digit
        if len(digits) > 1:
            num = int(digits[0] + digits[-1])
        elif len(digits) == 1:
            num = int(digits[0] + digits[0])
        elif len(digits) == 0:
            raise ValueError("Why?!")

        sum += num

    return sum


def part2(data):
    """Solve part 2"""
    sum = 0
    for line in data:
        digits = []
        letters = []
        for character in line:
            # get digits
            if character.isdigit():
                digits.append(character)
                letters = []
            # append digit if it is a number spelled out like 'six'
            # start with the final letter as a hack because the input has overlap.
            else:
                letters.append(character)
                word = "".join(letters)
                if "one" in word:
                    digits.append("1")
                    letters = ["e"]
                if "two" in word:
                    digits.append("2")
                    letters = ["o"]
                if "three" in word:
                    digits.append("3")
                    letters = ["e"]
                if "four" in word:
                    digits.append("4")
                    letters = ["r"]
                if "five" in word:
                    digits.append("5")
                    letters = ["e"]
                if "six" in word:
                    digits.append("6")
                    letters = ["x"]
                if "seven" in word:
                    digits.append("7")
                    letters = ["n"]
                if "eight" in word:
                    digits.append("8")
                    letters = ["t"]
                if "nine" in word:
                    digits.append("9")
                    letters = ["e"]

        # if there is only one digit, repeat it. Otherwise, choose the first and last digit
        if len(digits) > 1:
            num = int(digits[0] + digits[-1])
        elif len(digits) == 1:
            num = int(digits[0] + digits[0])
        elif len(digits) == 0:
            raise ValueError("Why?!")

        sum += num

    return sum


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = pathlib.Path("data/day1.txt").read_text().strip()
    solution1, solution2 = solve(puzzle_input)
    solutions = (solution1, solution2)
    print("\n".join(str(solution) for solution in solutions))
    # submit_solutions(solution1=solution1, solution2=solution2)
