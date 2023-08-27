#!/usr/bin/env python

import json
from aoc2022 import day_09 as d9

INPUT_TEST_PATH = "tests/input_files/day_09_input_sample.txt"
INPUT_FULL_PATH = "tests/input_files/day_09_input.txt"


def sample_map():
    with open("tests/fixtures/day_09_map.json", "r") as json_file:
        return json.load(json_file)


# def test_adjacent():
#     obj = d9.RopeGame()

#     line = "R 4"
#     obj.move_rope(line)
#     assert len(obj.head["x"]) == 4
#     assert len(obj.head["y"]) == 0
#     assert len(obj.tail["x"]) == 3
#     assert len(obj.tail["y"]) == 0
#     assert obj.tail_visited == [
#         {"x": 0, "y": 0},
#         {"x": 1, "y": 0},
#         {"x": 2, "y": 0},
#         {"x": 3, "y": 0},
#     ]

#     line = "U 4"
#     obj.move_rope(line)
#     assert len(obj.head["x"]) == 4
#     assert len(obj.head["y"]) == 4
#     assert len(obj.tail["x"]) == 4
#     assert len(obj.tail["y"]) == 3

#     assert obj.tail_visited == [
#         {"x": 0, "y": 0},
#         {"x": 1, "y": 0},
#         {"x": 2, "y": 0},
#         {"x": 3, "y": 0},
#         {"x": 4, "y": 1},
#         {"x": 4, "y": 2},
#         {"x": 4, "y": 3},
#     ]
#     line = "L 3"
#     obj.move_rope(line)
#     assert len(obj.head["x"]) == 1
#     assert len(obj.head["y"]) == 4
#     assert len(obj.tail["x"]) == 2
#     assert len(obj.tail["y"]) == 4

#     assert obj.tail_visited == [
#         {"x": 0, "y": 0},
#         {"x": 1, "y": 0},
#         {"x": 2, "y": 0},
#         {"x": 3, "y": 0},
#         {"x": 4, "y": 1},
#         {"x": 4, "y": 2},
#         {"x": 4, "y": 3},
#         {"x": 3, "y": 4},
#         {"x": 2, "y": 4},
#     ]
#     line = "D 1"
#     obj.move_rope(line)
#     assert len(obj.head["x"]) == 1
#     assert len(obj.head["y"]) == 3
#     assert len(obj.tail["x"]) == 2
#     assert len(obj.tail["y"]) == 4

#     line = "R 4"
#     obj.move_rope(line)
#     assert len(obj.head["x"]) == 5
#     assert len(obj.head["y"]) == 3
#     assert len(obj.tail["x"]) == 4
#     assert len(obj.tail["y"]) == 3

#     line = "D 1"
#     obj.move_rope(line)
#     assert len(obj.head["x"]) == 5
#     assert len(obj.head["y"]) == 2
#     assert len(obj.tail["x"]) == 4
#     assert len(obj.tail["y"]) == 3

#     line = "L 5"
#     obj.move_rope(line)
#     assert len(obj.head["x"]) == 0
#     assert len(obj.head["y"]) == 2
#     assert len(obj.tail["x"]) == 1
#     assert len(obj.tail["y"]) == 2

#     line = "R 2"
#     obj.move_rope(line)
#     assert len(obj.head["x"]) == 2
#     assert len(obj.head["y"]) == 2
#     assert len(obj.tail["x"]) == 1
#     assert len(obj.tail["y"]) == 2
#     sorted_list = sorted(obj.tail_visited, key=lambda x: x["y"])

#     assert sorted_list == [
#         {"x": 0, "y": 0},
#         {"x": 1, "y": 0},
#         {"x": 2, "y": 0},
#         {"x": 3, "y": 0},
#         {"x": 4, "y": 1},
#         {"x": 4, "y": 2},
#         {"x": 3, "y": 2},
#         {"x": 2, "y": 2},
#         {"x": 1, "y": 2},
#         {"x": 4, "y": 3},
#         {"x": 3, "y": 3},
#         {"x": 3, "y": 4},
#         {"x": 2, "y": 4},
#     ]

#     assert len(obj.tail_visited) == 13


def test_main():
    obj = d9.RopeGame(2)
    obj.main(INPUT_TEST_PATH)
    assert len(obj.tail_visited) == 13

    obj = d9.RopeGame(2)
    obj.main(INPUT_FULL_PATH)
    assert len(obj.tail_visited) == 6098

    obj = d9.RopeGame(10)
    obj.main(INPUT_FULL_PATH)
    assert len(obj.tail_visited) == 2597
