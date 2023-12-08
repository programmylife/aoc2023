# template for aoc day

import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    data_in_lines = [line for line in puzzle_input.splitlines()]
    data = []
    for item in data_in_lines:
        hand, bid = item.split()
        data.append((hand, int(bid)))
    return data


def part1(data):
    """Solve part 1"""

    five_of_a_kind_value = 7
    four_of_a_kind_value = 6
    full_house_value = 5
    three_of_a_kind_value = 4
    two_pair_value = 3
    one_pair_value = 2
    high_card_value = 1

    card_value_dict_part_1 = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }

    list_of_hands = []

    for hand, bid in data:
        card_values = {}
        for card in hand:
            card_values[card] = card_values.get(card, 0) + 1
        if set(card_values.values()) == set([5]):
            hand_value = five_of_a_kind_value
        elif set(card_values.values()) == set([4, 1]):
            hand_value = four_of_a_kind_value
        elif set(card_values.values()) == set([3, 2]):
            hand_value = full_house_value
        elif set(card_values.values()) == set([3, 1]):
            hand_value = three_of_a_kind_value
        elif sorted(card_values.values()) == [1, 2, 2]:
            hand_value = two_pair_value
        elif 2 in card_values.values():
            hand_value = one_pair_value
        else:
            hand_value = high_card_value

        list_of_hands = insert_hand_into_list(
            current_hand={"hand": hand, "hand_value": hand_value, "bid": bid},
            list_of_hands=list_of_hands,
            card_value_dict=card_value_dict_part_1,
        )

    result = 0
    # go through final list and multiple rank * bid
    for rank, hand in enumerate(list_of_hands, start=1):
        result += hand["bid"] * rank

    return result


def insert_hand_into_list(current_hand=None, list_of_hands=None, card_value_dict=None):
    if len(list_of_hands) == 0:
        list_of_hands.append(current_hand)
    else:
        for index, hand_in_list in enumerate(list_of_hands):
            if current_hand["hand_value"] > hand_in_list["hand_value"]:
                # move on because high hands go at the end
                continue
            elif current_hand["hand_value"] < hand_in_list["hand_value"]:
                # insert because we want lowest hands first
                list_of_hands.insert(index, current_hand)
                return list_of_hands
            elif current_hand["hand_value"] == hand_in_list["hand_value"]:
                for current_hand_card, hand_in_list_card in zip(
                    current_hand["hand"], hand_in_list["hand"]
                ):
                    # if this card is lower, we want to insert it.
                    if (
                        card_value_dict[current_hand_card]
                        < card_value_dict[hand_in_list_card]
                    ):
                        list_of_hands.insert(index, current_hand)
                        return list_of_hands
                    elif (
                        card_value_dict[current_hand_card]
                        == card_value_dict[hand_in_list_card]
                    ):
                        continue
                    # if this card is higher, move on to compare to next hand.
                    if (
                        card_value_dict[current_hand_card]
                        > card_value_dict[hand_in_list_card]
                    ):
                        break
            else:
                raise ValueError(
                    "hand_value should be greater than, less than, or equal to."
                )
        else:
            # if we haven't inserted yet, append at the end
            list_of_hands.append(current_hand)
    return list_of_hands


def part2(data):
    """Solve part 2"""

    five_of_a_kind_value = 7
    four_of_a_kind_value = 6
    full_house_value = 5
    three_of_a_kind_value = 4
    two_pair_value = 3
    one_pair_value = 2
    high_card_value = 1

    card_value_dict_part_2 = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 1,
        "Q": 12,
        "K": 13,
        "A": 14,
    }

    list_of_hands = []

    for hand, bid in data:
        card_values = {}
        for card in hand:
            card_values[card] = card_values.get(card, 0) + 1
        if set(card_values.values()) == set([5]):
            hand_value = five_of_a_kind_value
        elif set(card_values.values()) == set([4, 1]):
            if "J" in hand:
                hand_value = five_of_a_kind_value
            else:
                hand_value = four_of_a_kind_value
        elif set(card_values.values()) == set([3, 2]):
            if "J" in hand:
                hand_value = five_of_a_kind_value
            else:
                hand_value = full_house_value
        elif set(card_values.values()) == set([3, 1]):
            if "J" in hand:
                hand_value = four_of_a_kind_value
            else:
                hand_value = three_of_a_kind_value
        elif sorted(card_values.values()) == [1, 2, 2]:
            j_count = hand.count("J")
            if j_count == 1:
                hand_value = full_house_value
            elif j_count == 2:
                hand_value = four_of_a_kind_value
            else:
                hand_value = two_pair_value
        elif 2 in card_values.values():
            if "J" in hand:
                hand_value = three_of_a_kind_value
            else:
                hand_value = one_pair_value
        else:
            if "J" in hand:
                hand_value = one_pair_value
            else:
                hand_value = high_card_value

        list_of_hands = insert_hand_into_list(
            current_hand={"hand": hand, "hand_value": hand_value, "bid": bid},
            list_of_hands=list_of_hands,
            card_value_dict=card_value_dict_part_2,
        )

    result = 0
    # go through final list and multiply rank * bid
    for rank, hand in enumerate(list_of_hands, start=1):
        result += hand["bid"] * rank

    return result


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = pathlib.Path("data/day7.txt").read_text().strip()
    solution1, solution2 = solve(puzzle_input)
    solutions = (solution1, solution2)
    print("\n".join(str(solution) for solution in solutions))
