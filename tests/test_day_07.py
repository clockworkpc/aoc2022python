#!/usr/bin/env python

import json
from aoc2022 import day_07 as d7

INPUT_TEST_PATH = "tests/input_files/day_07_input_sample.txt"
INPUT_FULL_PATH = "tests/input_files/day_07_input.txt"


def sample_fs():
    with open("tests/fixtures/day_07_fs.json", "r") as json_file:
        return json.load(json_file)


def test_generate_sizes():
    res = d7.generate_sizes(INPUT_TEST_PATH)
    assert res == sample_fs()


def test_sum_filtered_directories():
    sizes = d7.generate_sizes(INPUT_TEST_PATH)
    limit = 100000
    res = d7.filter_directories_by_limit(sizes, limit)
    assert res == [94853, 584]
    assert sum(res) == 95437

    sizes = d7.generate_sizes(INPUT_FULL_PATH)
    limit = 100000
    res = d7.filter_directories_by_limit(sizes, limit)
    assert sum(res) == 1783610


def test_find_smallest_directory():
    sizes = d7.generate_sizes(INPUT_TEST_PATH)
    disk_space = 70000000
    space_needed = 30000000
    res = d7.find_smallest_directory(sizes, disk_space, space_needed)
    assert res == 24933642

    sizes = d7.generate_sizes(INPUT_FULL_PATH)
    disk_space = 70000000
    space_needed = 30000000
    res = d7.find_smallest_directory(sizes, disk_space, space_needed)
    assert res == 4370655
