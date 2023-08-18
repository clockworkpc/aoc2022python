#!/usr/bin/env python

from aoc2022 import day_05 as d5

import json

INPUT_TEST_PATH = "tests/input_files/day_05_input_sample.txt"
INPUT_FULL_PATH = "tests/input_files/day_05_input.txt"

"""PART 01"""


def test_new_map_empty():
    lines = d5.readlines(INPUT_TEST_PATH)
    res = d5.new_map_sans_crates(lines)
    assert res == {"1": [], "2": [], "3": []}


def test_new_map_populated():
    lines = d5.readlines(INPUT_TEST_PATH)
    empty_map = d5.new_map_sans_crates(lines)
    res = d5.new_map_with_crates(INPUT_TEST_PATH, empty_map)
    assert res == {"1": ["N", "Z"], "2": ["D", "C", "M"], "3": ["P"]}


def test_import_map():
    res = d5.import_map(INPUT_TEST_PATH)
    assert res == {"1": ["N", "Z"], "2": ["D", "C", "M"], "3": ["P"]}


def test_move_crate_old():
    my_map = d5.import_map(INPUT_TEST_PATH)

    cmd = "move 1 from 2 to 1"
    res = d5.move_crate(my_map, cmd)
    assert res == {"1": ["D", "N", "Z"], "2": ["C", "M"], "3": ["P"]}

    cmd = "move 3 from 1 to 3"
    res = d5.move_crate(my_map, cmd)
    assert res == {"1": [], "2": ["C", "M"], "3": ["Z", "N", "D", "P"]}

    cmd = "move 2 from 2 to 1"
    res = d5.move_crate(my_map, cmd)
    assert res == {"1": ["M", "C"], "2": [], "3": ["Z", "N", "D", "P"]}

    cmd = "move 1 from 1 to 2"
    res = d5.move_crate(my_map, cmd)
    assert res == {"1": ["C"], "2": ["M"], "3": ["Z", "N", "D", "P"]}


def test_move_crate_new():
    my_map = d5.import_map(INPUT_TEST_PATH)
    cratemover_old = False

    cmd = "move 1 from 2 to 1"
    res = d5.move_crate(my_map, cmd, cratemover_old)
    assert res == {"1": ["D", "N", "Z"], "2": ["C", "M"], "3": ["P"]}

    cmd = "move 3 from 1 to 3"
    res = d5.move_crate(my_map, cmd, cratemover_old)
    assert res == {"1": [], "2": ["C", "M"], "3": ["D", "N", "Z", "P"]}

    cmd = "move 2 from 2 to 1"
    res = d5.move_crate(my_map, cmd, cratemover_old)
    assert res == {"1": ["C", "M"], "2": [], "3": ["D", "N", "Z", "P"]}

    cmd = "move 1 from 1 to 2"
    res = d5.move_crate(my_map, cmd, cratemover_old)
    assert res == {"1": ["M"], "2": ["C"], "3": ["D", "N", "Z", "P"]}


def test_top_crates():
    my_map = {"1": ["C"], "2": ["M"], "3": ["Z", "N", "D", "P"]}
    res = d5.top_crates(my_map)
    assert res == "CMZ"


def test_import_instructions():
    res = d5.import_instructions(INPUT_TEST_PATH)
    text = [
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]
    assert res == text


def test_top_crates_from_instructions():
    res = d5.top_crates_from_instructions(INPUT_TEST_PATH)
    assert res == "CMZ"

    path = INPUT_TEST_PATH
    cratemover_old = False
    res = d5.top_crates_from_instructions(INPUT_TEST_PATH, cratemover_old)
    assert res == "MCD"

    res = d5.top_crates_from_instructions(INPUT_FULL_PATH)
    assert res == "BSDMQFLSP"

    cratemover_old = False
    res = d5.top_crates_from_instructions(INPUT_FULL_PATH, cratemover_old)
    assert res == "PGSQBFLDP"
