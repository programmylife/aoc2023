# template for aoc day

import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    data_in_lines = [line for line in puzzle_input.splitlines()]
    data = {}
    for num, line in enumerate(data_in_lines, start=1):
        data[num] = {"winning_numbers": [], "your_numbers": []}
        line_tokens = line.split()
        key = None
        for token in line_tokens:
            if ":" in token:
                key = "winning_numbers"
                data[num][key] = []
                continue
            if "|" in token:
                key = "your_numbers"
                data[num][key] = []
                continue
            if key:
                data[num][key].append(token)
    return data
def part1(data):
    """Solve part 1
     you have to figure out which of the numbers you have appear in the list of winning numbers.
     The first match makes the card worth one point and each match after the first
     doubles the point value of that card.
     """
    sum = 0
    for _, card in data.items():
        count = 0
        for winning_number in card['winning_numbers']:
                if winning_number in card['your_numbers']:
                    count += 1
        if count != 0:
            sum += pow(2,count-1)

    return sum


def part2(data):
    """Solve part 2
    There's no such thing as "points". Instead, scratchcards only cause you to win
    more scratchcards equal to the number of winning numbers you have.

    Specifically, you win copies of the scratchcards below the winning card equal
    to the number of matches. So, if card 10 were to have 5 matching numbers, you
    would win one copy each of cards 11, 12, 13, 14, and 15.
    Process all of the original and copied scratchcards until no more scratchcards are won.
    Including the original set of scratchcards, how many total scratchcards do you end up with?
    """
    count = 0
    for index, card in data.items():
        data[index]['total_copies'] = data[index].get('total_copies', 1)
        winners = 0
        for winning_number in card['winning_numbers']:
                if winning_number in card['your_numbers']:
                    winners += 1
        if winners != 0:
            # increase copies of subsequent cards by one for each winner * number of copies of current card
            for subsequent_index in range(index+1,index+winners+1):
                data[subsequent_index]['total_copies'] = data[subsequent_index].get('total_copies', 1) + 1*data[index]['total_copies']

    for index, card in data.items():
        count += data[index].get('total_copies', 1)

    return count

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = pathlib.Path("data/day4.txt").read_text().strip()
    solution1, solution2 = solve(puzzle_input)
    solutions = (solution1, solution2)
    print("\n".join(str(solution) for solution in solutions))
