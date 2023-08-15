#!/usr/bin/env python

import pytest

from advent_of_code_2022 import day_02 as d2

input_test_path = "tests/input_files/day_02_input_sample.txt"
input_full_path = "tests/input_files/day_02_input.txt"


def test_strip_split_text():
    res = d2.strip_split_text(input_test_path)
    assert res == [["A", "Y"], ["B", "X"], ["C", "Z"]]


def test_item_and_round_scores():
    str_ary_ary = d2.strip_split_text(input_test_path)
    print(str_ary_ary)
    res = d2.item_and_round_scores(str_ary_ary)
    assert res["p2"] == [[2, 6], [1, 0], [3, 3]]
    assert res["p1"] == [[1, 0], [2, 6], [3, 3]]


def test_score_sums():
    str_ary_ary = d2.strip_split_text(input_test_path)
    item_and_round_scores = d2.item_and_round_scores(str_ary_ary)
    res = d2.score_sums(item_and_round_scores)
    assert res["p2"] == [8, 1, 6]
    assert res["p1"] == [1, 8, 6]


def test_final_score_sample():
    res = d2.final_scores(input_test_path)
    assert res["p2"] == 15
    assert res["p1"] == 15


def test_final_score():
    res = d2.final_scores(input_full_path)
    assert res["p2"] == 13924


def test_final_score_sample_new_score():
    res = d2.final_scores(input_test_path, True)
    assert res["p2"] == 12
