"""Day 03"""


import json
from itertools import chain

PRIORITIES_PATH = "aoc2022/day_03_priorities.json"

"""Part 01"""


def priority_dictionary():
    with open(PRIORITIES_PATH, "r") as file:
        return json.load(file)


def halve_line(line):
    half_len = int(len(line) / 2)
    before_half_len = half_len - 1
    half1 = line[0:half_len]
    half2 = line[half_len: len(line)]
    return [half1, half2]


def unique_sorted_characters(half_line):
    unique_characters = "".join(set(half_line))
    sorted_characters = "".join(sorted(unique_characters))
    return sorted_characters


def unique_lists(line_halves):
    usc_ary = []
    for half_line in line_halves:
        usc = unique_sorted_characters(half_line)
        usc_ary.append(usc)
    return usc_ary


def share_items(usc_ary):
    return [item for item in usc_ary[0] if item in usc_ary[1]]


def share_item_scores(usc_ary):
    chars = share_items(usc_ary)
    p_dict = priority_dictionary()
    scores = list(map(lambda x: p_dict[x], chars))
    return scores


def share_item_scores_sum(usc_ary):
    return sum(share_item_scores(usc_ary))


def split_strip(path):
    with open(path, "r") as file:
        return [line.strip() for line in file]


def all_share_item_scores(path):
    lines = split_strip(path)
    score_ary = []

    for line in lines:
        line_halves = halve_line(line)
        usc_ary = unique_lists(line_halves)
        score = share_item_scores_sum(usc_ary)
        score_ary.append(score)

    return score_ary


def all_share_item_scores_sum(path):
    scores = all_share_item_scores(path)
    return sum(scores)


"""PART 02"""


def group_lines(path, size=3):
    group_ary = [[]]
    lines = split_strip(path)
    for index, line in enumerate(lines, 1):
        group_ary[-1].append(line)

        if index % 3 == 0 and index != len(lines):
            new_group = []
            group_ary.append(new_group)

    return group_ary


def common_group_items(grouped_lines):
    def reduce_lists(nested_list):
        return list(map(lambda x: list(set(x)), nested_list))

    def extract_common_items(str_ary):
        collection = []
        for index, string in enumerate(str_ary, 1):
            if index == len(str_ary):
                break

            common_items = [item for item in string if item in str_ary[index]]
            collection.append(common_items)
            collection = reduce_lists(collection)

        return collection

    all_common_items = extract_common_items(grouped_lines)
    unique_common_items = extract_common_items(all_common_items)
    return list(chain.from_iterable(unique_common_items))


def collect_common_group_items(path):
    grouped_lines_ary = group_lines(path)

    collected_common_items = []
    for grouped_lines in grouped_lines_ary:
        common_items = common_group_items(grouped_lines)
        collected_common_items.append(common_items)

    return list(chain.from_iterable(collected_common_items))


def collect_common_group_item_scores(path):
    common_items = collect_common_group_items(path)
    pd = priority_dictionary()
    common_scores = list(map(lambda x: pd[x], common_items))

    return common_scores


def sum_common_item_scores(path):
    scores = collect_common_group_item_scores(path)
    return sum(scores)
