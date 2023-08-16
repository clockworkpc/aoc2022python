#!/usr/bin/env python

import pytest

from aoc2022 import day_01 as d1

input_test_path = "tests/input_files/day_01_input_sample.txt"
input_full_path = "tests/input_files/day_01_input.txt"


grouped_lines = [[1000, 2000, 3000], [4000], [
    5000, 6000], [7000, 8000, 9000], [10000]]


def test_calorie_counter():
    res = d1.group_integers(input_test_path)
    print(res)
    assert res == grouped_lines


def test_sum_calories():
    grouped_integers = d1.group_integers(input_test_path)
    res = d1.sum_calories(grouped_integers)
    assert res == [6000, 4000, 11000, 24000, 10000]


def test_max_calories():
    grouped_integers = d1.group_integers(input_test_path)
    calorie_sums = d1.sum_calories(grouped_integers)
    res = d1.max_calories(calorie_sums)
    assert res == 24000


def test_max_calories_d1a():
    grouped_integers = d1.group_integers(input_full_path)
    calorie_sums = d1.sum_calories(grouped_integers)
    res = d1.max_calories(calorie_sums)
    assert res == 68292


def test_max_calories_d1b():
    grouped_integers = d1.group_integers(input_full_path)
    calorie_sums = d1.sum_calories(grouped_integers)
    res = d1.max_calories(calorie_sums, end_index=3)
    assert res == 203203
