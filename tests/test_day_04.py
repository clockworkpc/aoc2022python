#!/usr/bin/env python

from aoc2022 import day_04 as d4

import json

INPUT_TEST_PATH = "tests/input_files/day_04_input_sample.txt"
INPUT_FULL_PATH = "tests/input_files/day_04_input.txt"

"""PART 01"""


def test_assign_sections():
    line = "2-4,6-8"
    res = d4.assign_sections(line)
    assert res == [[2, 3, 4], [6, 7, 8]]


def test_common_sections():
    line = "2-4,6-8"
    assigned_sections = d4.assign_sections(line)
    res = d4.common_sections(assigned_sections)
    assert res == []

    line = "5-7,7-9"
    assigned_sections = d4.assign_sections(line)
    res = d4.common_sections(assigned_sections)
    assert res == [7]

    line = "2-8,3-7"
    assigned_sections = d4.assign_sections(line)
    res = d4.common_sections(assigned_sections)
    assert res == [3, 4, 5, 6, 7]

    line = "6-6,4-6"
    assigned_sections = d4.assign_sections(line)
    res = d4.common_sections(assigned_sections)
    assert res == [6]

    line = "2-6,4-8"
    assigned_sections = d4.assign_sections(line)
    res = d4.common_sections(assigned_sections)
    assert res == [4, 5, 6]


def test_arrangement_label():
    line = "2-4,6-8"
    assigned_sections = d4.assign_sections(line)
    res = d4.arrangement_label(assigned_sections)
    assert res == "distinct"

    line = "2-3,4-5"
    assigned_sections = d4.assign_sections(line)
    res = d4.arrangement_label(assigned_sections)
    assert res == "distinct"

    line = "5-7,7-9"
    assigned_sections = d4.assign_sections(line)
    res = d4.arrangement_label(assigned_sections)
    assert res == "overlap"

    line = "2-8,3-7"
    assigned_sections = d4.assign_sections(line)
    res = d4.arrangement_label(assigned_sections)
    assert res == "subset"

    line = "6-6,4-6"
    assigned_sections = d4.assign_sections(line)
    res = d4.arrangement_label(assigned_sections)
    assert res == "subset"

    line = "2-6,4-8"
    assigned_sections = d4.assign_sections(line)
    res = d4.arrangement_label(assigned_sections)
    assert res == "overlap"

    line = "36-38,37-96"
    assigned_sections = d4.assign_sections(line)
    res = d4.arrangement_label(assigned_sections)
    assert res == "overlap"


def test_count_arrangements():
    res = d4.count_arrangements(INPUT_TEST_PATH)
    assert res == {"distinct": 2, "overlap": 2, "subset": 2}
    assert res["subset"] == 2

    res = d4.count_arrangements(INPUT_FULL_PATH)
    assert res == {"distinct": 221, "overlap": 320, "subset": 459}
    assert res["subset"] == 459
    assert res["overlap"] + res["subset"] == 459 + 320
