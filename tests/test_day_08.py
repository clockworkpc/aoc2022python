#!/usr/bin/env python

import json
from aoc2022 import day_08 as d8

INPUT_TEST_PATH = "tests/input_files/day_08_input_sample.txt"
INPUT_FULL_PATH = "tests/input_files/day_08_input.txt"


def sample_map():
    with open("tests/fixtures/day_08_map.json", "r") as json_file:
        return json.load(json_file)


def test_map_trees():
    grid = ["30373", "25512", "65332", "33549", "35390"]
    res = d8.map_trees(INPUT_TEST_PATH)
    assert res == grid


def test_outer_trees():
    grid = d8.map_trees(INPUT_TEST_PATH)
    assert d8.outer_trees(grid) == 16


def test_visibility_left():
    row = "25512"
    res = d8.visible_from_left(row, 1)
    assert res is True
    res = d8.visible_from_left(row, 2)
    assert res is False
    res = d8.visible_from_left(row, 3)
    assert res is False

    row = "65332"
    res = d8.visible_from_left(row, 1)
    assert res is False
    res = d8.visible_from_left(row, 2)
    assert res is False
    res = d8.visible_from_left(row, 3)
    assert res is False

    row = "33549"
    res = d8.visible_from_left(row, 1)
    assert res is False
    res = d8.visible_from_left(row, 2)
    assert res is True
    res = d8.visible_from_left(row, 3)
    assert res is False

    row = "35390"
    res = d8.visible_from_left(row, 1)
    assert res is True
    res = d8.visible_from_left(row, 2)
    assert res is False
    res = d8.visible_from_left(row, 3)
    assert res is True


def test_visibility_right():
    row = "25512"
    res = d8.visible_from_right(row, 1)
    assert res is False
    res = d8.visible_from_right(row, 2)
    assert res is True
    res = d8.visible_from_right(row, 3)
    assert res is False

    row = "65332"
    res = d8.visible_from_right(row, 1)
    assert res is True
    res = d8.visible_from_right(row, 2)
    assert res is False
    res = d8.visible_from_right(row, 3)
    assert res is True

    row = "33549"
    res = d8.visible_from_right(row, 1)
    assert res is False
    res = d8.visible_from_right(row, 2)
    assert res is False
    res = d8.visible_from_right(row, 3)
    assert res is False

    row = "35390"
    res = d8.visible_from_right(row, 1)
    assert res is False
    res = d8.visible_from_right(row, 2)
    assert res is False
    res = d8.visible_from_right(row, 3)
    assert res is True


def test_column():
    grid = d8.map_trees(INPUT_TEST_PATH)
    res = d8.tree_column(grid, 0)
    assert res == list("32633")

    res = d8.tree_column(grid, 1)
    assert res == list("05535")

    res = d8.tree_column(grid, 2)
    assert res == list("35353")

    res = d8.tree_column(grid, 3)
    assert res == list("71349")

    res = d8.tree_column(grid, 4)
    assert res == list("32290")


def test_visibility_top():
    grid = d8.map_trees(INPUT_TEST_PATH)
    res = d8.visible_from_top(grid, 1, 1)
    assert res is True

    res = d8.visible_from_top(grid, 1, 2)
    assert res is False

    res = d8.visible_from_top(grid, 1, 3)
    assert res is False

    res = d8.visible_from_top(grid, 2, 1)
    assert res is True

    res = d8.visible_from_top(grid, 2, 2)
    assert res is False

    res = d8.visible_from_top(grid, 2, 3)
    assert res is False

    res = d8.visible_from_top(grid, 3, 1)
    assert res is False

    res = d8.visible_from_top(grid, 3, 2)
    assert res is False

    res = d8.visible_from_top(grid, 3, 3)
    assert res is False


def test_visibility_bottom():
    grid = d8.map_trees(INPUT_TEST_PATH)
    res = d8.visible_from_bottom(grid, 1, 1)
    assert res is False

    res = d8.visible_from_bottom(grid, 1, 2)
    assert res is False

    res = d8.visible_from_bottom(grid, 1, 3)
    assert res is False

    res = d8.visible_from_bottom(grid, 2, 1)
    assert res is False

    res = d8.visible_from_bottom(grid, 2, 2)
    assert res is False

    res = d8.visible_from_bottom(grid, 2, 3)
    assert res is True

    res = d8.visible_from_bottom(grid, 3, 1)
    assert res is False

    res = d8.visible_from_bottom(grid, 3, 2)
    assert res is False

    res = d8.visible_from_bottom(grid, 3, 3)
    assert res is False


def test_tree_visibility():
    grid = d8.map_trees(INPUT_TEST_PATH)
    res = d8.is_visible(grid, 0, 0)
    assert res is True

    res = d8.is_visible(grid, 0, 1)
    assert res is True

    res = d8.is_visible(grid, 0, 2)
    assert res is True

    res = d8.is_visible(grid, 0, 3)
    assert res is True

    res = d8.is_visible(grid, 0, 4)
    assert res is True

    res = d8.is_visible(grid, 4, 0)
    assert res is True

    res = d8.is_visible(grid, 4, 1)
    assert res is True

    res = d8.is_visible(grid, 4, 2)
    assert res is True

    res = d8.is_visible(grid, 4, 3)
    assert res is True

    res = d8.is_visible(grid, 4, 4)
    assert res is True

    res = d8.is_visible(grid, 1, 0)
    assert res is True

    res = d8.is_visible(grid, 2, 0)
    assert res is True

    res = d8.is_visible(grid, 3, 0)
    assert res is True

    res = d8.is_visible(grid, 1, 4)
    assert res is True

    res = d8.is_visible(grid, 2, 4)
    assert res is True

    res = d8.is_visible(grid, 3, 4)
    assert res is True

    res = d8.is_visible(grid, 1, 1)
    assert res is True

    res = d8.is_visible(grid, 1, 2)
    assert res is True

    res = d8.is_visible(grid, 1, 3)
    assert res is False

    res = d8.is_visible(grid, 2, 1)
    assert res is True

    res = d8.is_visible(grid, 2, 2)
    assert res is False

    res = d8.is_visible(grid, 2, 3)
    assert res is True

    res = d8.is_visible(grid, 3, 1)
    assert res is False

    res = d8.is_visible(grid, 3, 2)
    assert res is True

    res = d8.is_visible(grid, 3, 3)
    assert res is False


def test_visibility_map():
    grid = d8.map_trees(INPUT_TEST_PATH)
    res = d8.visibility_map(grid)
    assert res == sample_map()


def test_visibility_count():
    grid = d8.map_trees(INPUT_TEST_PATH)
    v_map = d8.visibility_map(grid)
    v_count = d8.visibility_count(v_map)
    assert v_count["visible"] == 21
    assert v_count["invisible"] == 4

    grid = d8.map_trees(INPUT_FULL_PATH)
    v_map = d8.visibility_map(grid)
    v_count = d8.visibility_count(v_map)
    assert v_count["visible"] == 1713
    assert v_count["invisible"] == 8088


def test_scenic_left():
    row = "30373"
    res = d8.visible_to_left(row, 0)
    assert res == 0
    res = d8.visible_to_left(row, 1)
    assert res == 1
    res = d8.visible_to_left(row, 2)
    assert res == 2
    res = d8.visible_to_left(row, 3)
    assert res == 3
    res = d8.visible_to_left(row, 4)
    assert res == 1

    row = "25512"
    res = d8.visible_to_left(row, 0)
    assert res == 0
    res = d8.visible_to_left(row, 1)
    assert res == 1
    res = d8.visible_to_left(row, 2)
    assert res == 1
    res = d8.visible_to_left(row, 3)
    assert res == 1
    res = d8.visible_to_left(row, 4)
    assert res == 2

    row = "65332"
    res = d8.visible_to_left(row, 0)
    assert res == 0
    res = d8.visible_to_left(row, 1)
    assert res == 1
    res = d8.visible_to_left(row, 2)
    assert res == 1
    res = d8.visible_to_left(row, 3)
    assert res == 1
    res = d8.visible_to_left(row, 4)
    assert res == 1

    row = "33549"
    res = d8.visible_to_left(row, 0)
    assert res == 0
    res = d8.visible_to_left(row, 1)
    assert res == 1
    res = d8.visible_to_left(row, 2)
    assert res == 2
    res = d8.visible_to_left(row, 3)
    assert res == 1
    res = d8.visible_to_left(row, 4)
    assert res == 4

    row = "35390"
    res = d8.visible_to_left(row, 0)
    assert res == 0
    res = d8.visible_to_left(row, 1)
    assert res == 1
    res = d8.visible_to_left(row, 2)
    assert res == 1
    res = d8.visible_to_left(row, 3)
    assert res == 3
    res = d8.visible_to_left(row, 4)
    assert res == 1


def test_scenic_right():
    row = "30373"
    res = d8.visible_to_right(row, 0)
    assert res == 2
    res = d8.visible_to_right(row, 1)
    assert res == 1
    res = d8.visible_to_right(row, 2)
    assert res == 1
    res = d8.visible_to_right(row, 3)
    assert res == 1
    res = d8.visible_to_right(row, 4)
    assert res == 0

    row = "25512"
    res = d8.visible_to_right(row, 0)
    assert res == 1
    res = d8.visible_to_right(row, 1)
    assert res == 1
    res = d8.visible_to_right(row, 2)
    assert res == 2
    res = d8.visible_to_right(row, 3)
    assert res == 1
    res = d8.visible_to_right(row, 4)
    assert res == 0

    row = "65332"
    res = d8.visible_to_right(row, 0)
    assert res == 4
    res = d8.visible_to_right(row, 1)
    assert res == 3
    res = d8.visible_to_right(row, 2)
    assert res == 1
    res = d8.visible_to_right(row, 3)
    assert res == 1
    res = d8.visible_to_right(row, 4)
    assert res == 0

    row = "33549"
    res = d8.visible_to_right(row, 0)
    assert res == 1
    res = d8.visible_to_right(row, 1)
    assert res == 1
    res = d8.visible_to_right(row, 2)
    assert res == 2
    res = d8.visible_to_right(row, 3)
    assert res == 1
    res = d8.visible_to_right(row, 4)
    assert res == 0

    row = "35390"
    res = d8.visible_to_right(row, 0)
    assert res == 1
    res = d8.visible_to_right(row, 1)
    assert res == 2
    res = d8.visible_to_right(row, 2)
    assert res == 1
    res = d8.visible_to_right(row, 3)
    assert res == 1
    res = d8.visible_to_right(row, 4)
    assert res == 0


def test_scenic_top():
    grid = ["30373", "25512", "65332", "33549", "35390"]

    res = d8.visible_to_top(grid, 0, 0)
    assert res == 0
    res = d8.visible_to_top(grid, 1, 0)
    assert res == 0
    res = d8.visible_to_top(grid, 2, 0)
    assert res == 0
    res = d8.visible_to_top(grid, 3, 0)
    assert res == 0
    res = d8.visible_to_top(grid, 4, 0)
    assert res == 0

    res = d8.visible_to_top(grid, 0, 1)
    assert res == 1
    res = d8.visible_to_top(grid, 1, 1)
    assert res == 1
    res = d8.visible_to_top(grid, 2, 1)
    assert res == 1
    res = d8.visible_to_top(grid, 3, 1)
    assert res == 1
    res = d8.visible_to_top(grid, 4, 1)
    assert res == 1

    res = d8.visible_to_top(grid, 0, 2)
    assert res == 2
    res = d8.visible_to_top(grid, 0, 3)
    assert res == 1
    res = d8.visible_to_top(grid, 0, 4)
    assert res == 1

    res = d8.visible_to_top(grid, 1, 2)
    assert res == 1
    res = d8.visible_to_top(grid, 1, 3)
    assert res == 1
    res = d8.visible_to_top(grid, 1, 4)
    assert res == 2

    res = d8.visible_to_top(grid, 2, 2)
    assert res == 1
    res = d8.visible_to_top(grid, 2, 3)
    assert res == 2
    res = d8.visible_to_top(grid, 2, 4)
    assert res == 1

    res = d8.visible_to_top(grid, 3, 2)
    assert res == 2
    res = d8.visible_to_top(grid, 3, 3)
    assert res == 3
    res = d8.visible_to_top(grid, 3, 4)
    assert res == 4

    res = d8.visible_to_top(grid, 4, 2)
    assert res == 1
    res = d8.visible_to_top(grid, 4, 3)
    assert res == 3
    res = d8.visible_to_top(grid, 4, 4)
    assert res == 1


def test_scenic_bottom():
    grid = ["30373", "25512", "65332", "33549", "35390"]

    res = d8.visible_to_bottom(grid, 0, 4)
    assert res == 0
    res = d8.visible_to_bottom(grid, 1, 4)
    assert res == 0
    res = d8.visible_to_bottom(grid, 2, 4)
    assert res == 0
    res = d8.visible_to_bottom(grid, 3, 4)
    assert res == 0
    res = d8.visible_to_bottom(grid, 4, 4)
    assert res == 0

    res = d8.visible_to_bottom(grid, 0, 3)
    assert res == 1
    res = d8.visible_to_bottom(grid, 1, 3)
    assert res == 1
    res = d8.visible_to_bottom(grid, 2, 3)
    assert res == 1
    res = d8.visible_to_bottom(grid, 3, 3)
    assert res == 1
    res = d8.visible_to_bottom(grid, 4, 3)
    assert res == 1

    res = d8.visible_to_bottom(grid, 0, 0)
    assert res == 2
    res = d8.visible_to_bottom(grid, 0, 1)
    assert res == 1
    res = d8.visible_to_bottom(grid, 0, 2)
    assert res == 2

    res = d8.visible_to_bottom(grid, 1, 0)
    assert res == 1
    res = d8.visible_to_bottom(grid, 1, 1)
    assert res == 1
    res = d8.visible_to_bottom(grid, 1, 2)
    assert res == 2

    res = d8.visible_to_bottom(grid, 2, 0)
    assert res == 1
    res = d8.visible_to_bottom(grid, 2, 1)
    assert res == 2
    res = d8.visible_to_bottom(grid, 2, 2)
    assert res == 1

    res = d8.visible_to_bottom(grid, 3, 0)
    assert res == 4
    res = d8.visible_to_bottom(grid, 3, 1)
    assert res == 1
    res = d8.visible_to_bottom(grid, 3, 2)
    assert res == 1

    res = d8.visible_to_bottom(grid, 4, 0)
    assert res == 3
    res = d8.visible_to_bottom(grid, 4, 1)
    assert res == 1
    res = d8.visible_to_bottom(grid, 4, 2)
    assert res == 1


def test_scenic_score():
    grid = ["30373", "25512", "65332", "33549", "35390"]

    res = d8.scenic_score(grid, 0, 0)
    assert res == 0
    res = d8.scenic_score(grid, 0, 1)
    assert res == 0
    res = d8.scenic_score(grid, 0, 2)
    assert res == 0
    res = d8.scenic_score(grid, 0, 3)
    assert res == 0
    res = d8.scenic_score(grid, 0, 4)
    assert res == 0
    res = d8.scenic_score(grid, 4, 0)
    assert res == 0
    res = d8.scenic_score(grid, 4, 1)
    assert res == 0
    res = d8.scenic_score(grid, 4, 2)
    assert res == 0
    res = d8.scenic_score(grid, 4, 3)
    assert res == 0
    res = d8.scenic_score(grid, 4, 4)
    assert res == 0
    res = d8.scenic_score(grid, 1, 0)
    assert res == 0
    res = d8.scenic_score(grid, 2, 0)
    assert res == 0
    res = d8.scenic_score(grid, 3, 0)
    assert res == 0
    res = d8.scenic_score(grid, 4, 0)
    assert res == 0
    res = d8.scenic_score(grid, 1, 4)
    assert res == 0
    res = d8.scenic_score(grid, 2, 4)
    assert res == 0
    res = d8.scenic_score(grid, 3, 4)
    assert res == 0
    res = d8.scenic_score(grid, 4, 4)
    assert res == 0

    res = d8.scenic_score(grid, 1, 1)
    assert res == 1
    res = d8.scenic_score(grid, 1, 2)
    assert res == 4
    res = d8.scenic_score(grid, 1, 3)
    assert res == 1

    res = d8.scenic_score(grid, 2, 1)
    assert res == 6
    res = d8.scenic_score(grid, 2, 2)
    assert res == 1
    res = d8.scenic_score(grid, 2, 3)
    assert res == 2

    res = d8.scenic_score(grid, 3, 1)
    assert res == 1
    res = d8.scenic_score(grid, 3, 2)
    assert res == 8
    res = d8.scenic_score(grid, 3, 3)
    assert res == 3
