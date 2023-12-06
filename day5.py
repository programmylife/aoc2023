# template for aoc day

import pathlib
import sys


def parse(puzzle_input):
    """Parse input
    parse seeds separately
    parse each map like:
    seed-to-soil map:
    50 98 2
    52 50 48
    {
    'seeds': 79 14 55 13
    'seed_to_soil': destination_starts: [50,52]
                    source_starts: [98,50]
                    ranges: [2,48]
    ...
    'humidity_to_location':
                    }
    """

    data_in_lines = [line for line in puzzle_input.splitlines()]
    data = {
        "seeds": [],
        "seed_to_soil": {"destination_starts": [], "source_starts": [], "ranges": []},
        "soil_to_fertilizer": {
            "destination_starts": [],
            "source_starts": [],
            "ranges": [],
        },
        "fertilizer_to_water": {
            "destination_starts": [],
            "source_starts": [],
            "ranges": [],
        },
        "water_to_light": {"destination_starts": [], "source_starts": [], "ranges": []},
        "light_to_temperature": {
            "destination_starts": [],
            "source_starts": [],
            "ranges": [],
        },
        "temperature_to_humidity": {
            "destination_starts": [],
            "source_starts": [],
            "ranges": [],
        },
        "humidity_to_location": {
            "destination_starts": [],
            "source_starts": [],
            "ranges": [],
        },
    }
    for line in data_in_lines:
        if "seeds" in line:
            seeds = line.split()
            for number in seeds:
                if number.isdigit():
                    data["seeds"].append(int(number))
        elif "seed-to-soil" in line:
            key = "seed_to_soil"
        elif "soil-to-fertilizer" in line:
            key = "soil_to_fertilizer"
        elif "fertilizer-to-water" in line:
            key = "fertilizer_to_water"
        elif "water-to-light" in line:
            key = "water_to_light"
        elif "light-to-temperature" in line:
            key = "light_to_temperature"
        elif "temperature-to-humidity" in line:
            key = "temperature_to_humidity"
        elif "humidity-to-location" in line:
            key = "humidity_to_location"
        # skip return lines
        elif len(line) < 1:
            continue
        else:
            # all numeric lines
            numbers = line.split()
            data[key]["destination_starts"].append(int(numbers[0]))
            data[key]["source_starts"].append(int(numbers[1]))
            data[key]["ranges"].append(int(numbers[2]))

    return data


def part1(data):
    """Solve part 1
    find the lowest location number that corresponds to any of the initial seeds.
    To do this, you'll need to convert each seed number through other categories
    until you can find its corresponding location number.

    What is the lowest location number that corresponds to any of the initial seed numbers?
    """
    result = []
    for seed_number in data["seeds"]:
        cur_index = seed_number
        for key, value in data.items():
            if key == "seeds":
                continue

            # check if the index is in any of the ranges.
            for list_index in range(len(data[key]["ranges"])):
                if (
                    cur_index >= data[key]["source_starts"][list_index]
                    and cur_index
                    < data[key]["source_starts"][list_index]
                    + data[key]["ranges"][list_index]
                ):
                    # do the math and set the index
                    cur_index += (
                        data[key]["destination_starts"][list_index]
                        - data[key]["source_starts"][list_index]
                    )
                    break
        result.append(cur_index)
    return min(result)


def part2(data):
    """Solve part 2"""
    result = []
    for count, seed_number in enumerate(data["seeds"]):
        if count > 1:
            break
        if count % 2:
            continue
        else:
            # print(seed_number, seed_number+data['seeds'][count+1])
            # print(range(seed_number, seed_number+data['seeds'][count+1]))
            for cur_index in range(seed_number, seed_number+data['seeds'][count+1]):
                for key, value in data.items():
                    if key == "seeds":
                        continue

                    # check if the index is in any of the ranges.
                    for list_index in range(len(data[key]["ranges"])):
                        if (
                            cur_index >= data[key]["source_starts"][list_index]
                            and cur_index
                            < data[key]["source_starts"][list_index]
                            + data[key]["ranges"][list_index]
                        ):
                            # do the math and set the index
                            cur_index += (
                                data[key]["destination_starts"][list_index]
                                - data[key]["source_starts"][list_index]
                            )
                            break
                result.append(cur_index)
    return min(result)



def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = pathlib.Path("data/day5.txt").read_text().strip()
    solution1, solution2 = solve(puzzle_input)
    solutions = (solution1, solution2)
    print("\n".join(str(solution) for solution in solutions))
