#!/usr/bin/env python

import json
from aoc2022 import day_09 as d9

INPUT_TEST_PATH = "tests/input_files/day_09_input_sample.txt"
INPUT_FULL_PATH = "tests/input_files/day_09_input.txt"


def sample_map():
    with open("tests/fixtures/day_09_map.json", "r") as json_file:
        return json.load(json_file)


def test_adjacent():
    obj = d9
    line = "R 4"
    head, tail = obj.move_pieces(line)
    print(head)
    print(tail)
    assert len(head["x"]) == 4
    assert len(head["y"]) == 0
    assert len(tail["x"]) == 3
    assert len(head["y"]) == 0

    line = "U 4"
    head, tail = obj.move_pieces(line)
    print(head)
    print(tail)
    assert len(head["x"]) == 4
    assert len(head["y"]) == 0
    assert len(tail["x"]) == 3
    assert len(head["y"]) == 0
