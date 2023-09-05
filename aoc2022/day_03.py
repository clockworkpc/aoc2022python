"""Day 03"""
# 1. Split a given string into substrings of equal length
# 2. Find the character(s) shared by the substrings
# 3. For each shared character return its numeric value
# 4. For the list of strings, return the sum-total
#       of the numeric values of the shared characters
#       from each pair of equal-length substrings

# For a given list of strings:
#   return the sum-total of the numeric values
#   of the characters
#   that are shared
#   by the equal-length substrings

# To achieve this:
# 1. Return a numeric value for a given alphabetic character
# 2. Find the shared character in pair of substrings
# 3. Split a string into equal-length substrings


import json
from itertools import chain

PRIORITIES_PATH = "aoc2022/day_03_priorities.json"

"""Part 01"""

# 1. Return a numeric value for a given alphabetic character
with open(PRIORITIES_PATH, "r") as file:
    PRIORITY = json.load(file)


def split_strip(path):
    with open(path, "r") as file:
        return [line.strip() for line in file]


def all_share_item_scores(path):
    lines = split_strip(path)
    score_ary = []

    for line in lines:
        # 3. Split a string into equal-length substrings
        half_len = int(len(line) / 2)
        string1, string2 = [line[:half_len], line[half_len:]]
        # 2. Find the shared character in pair of substrings
        shared_chars = [char for char in string1 if char in string2]
        line_scores = list(set([PRIORITY[char] for char in shared_chars]))
        score_ary.append(sum(line_scores))

    return score_ary


def all_share_item_scores_sum(path):
    scores = all_share_item_scores(path)
    return sum(scores)


def group_lines(path):
    group_ary = [[]]
    lines = split_strip(path)
    for index, line in enumerate(lines, 1):
        group_ary[-1].append(line)

        if index % 3 == 0 and index != len(lines):
            new_group = []
            group_ary.append(new_group)

    return group_ary


def common_group_items(grouped_lines):
    def extract_common_items(str_ary):
        collection = []
        for index, string in enumerate(str_ary, 1):
            if index == len(str_ary):
                break

            common_items = [item for item in string if item in str_ary[index]]
            collection.append(common_items)
            collection = [list(set(x)) for x in collection]

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

    common_scores = [PRIORITY[x] for x in common_items]
    return common_scores


def sum_common_item_scores(path):
    scores = collect_common_group_item_scores(path)
    return sum(scores)
