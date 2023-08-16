"""Day 03"""

import string
import json

PRIORITIES_PATH = "aoc2022/day_03_priorities.json"


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
