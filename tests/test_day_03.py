#!/usr/bin/env python

from aoc2022 import day_03 as d3

INPUT_TEST_PATH = "tests/input_files/day_03_input_sample.txt"
INPUT_FULL_PATH = "tests/input_files/day_03_input.txt"
PRIORITIES_PATH = "aoc2022/day_03_priorities.json"

"""PART 01"""


def test_all_share_item_scores():
    res_sample = d3.all_share_item_scores(INPUT_TEST_PATH)
    assert res_sample == [16, 38, 42, 22, 20, 19]


def test_all_share_item_scores_sum():
    res_sample = d3.all_share_item_scores_sum(INPUT_TEST_PATH)
    assert res_sample == sum([16, 38, 42, 22, 20, 19])

    res = d3.all_share_item_scores_sum(INPUT_FULL_PATH)
    assert res == 7872


# PART 02


def test_group_lines():
    test_lines = [
        [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
        ],
        [
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw",
        ],
    ]
    res = d3.group_lines(INPUT_TEST_PATH)
    assert res == test_lines


def test_common_group_items():
    gl0 = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
    ]

    res0 = d3.common_group_items(gl0)
    assert res0 == ["r"]

    gl1 = [
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]

    res1 = d3.common_group_items(gl1)
    assert res1 == ["Z"]


def test_collect_common_group_items():
    cgi = ["r", "Z"]
    res = d3.collect_common_group_items(INPUT_TEST_PATH)
    assert res == cgi


def test_collect_common_group_item_scores():
    cgi = [18, 52]
    res0 = d3.collect_common_group_item_scores(INPUT_TEST_PATH)
    assert res0 == cgi
    res1 = d3.sum_common_item_scores(INPUT_TEST_PATH)
    assert res1 == 70
    res2 = d3.sum_common_item_scores(INPUT_FULL_PATH)
    assert res2 == 2497
