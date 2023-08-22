#!/usr/bin/env python

from aoc2022 import day_07 as d7
import json
import pprint

INPUT_TEST_PATH = "tests/input_files/day_07_input_sample.txt"
INPUT_FULL_PATH = "tests/input_files/day_07_input.txt"


def sample_fs():
    with open("tests/fixtures/day_07_fs.json", "r") as json_file:
        return json.load(json_file)


def test_classify_line():
    line = "$ ls"
    res = d7.classify_line(line)
    assert res == "command"

    line = "dir a"
    res = d7.classify_line(line)
    assert res == "directory"

    line = "dir d"
    res = d7.classify_line(line)
    assert res == "directory"

    line = "14848514 b.txt"
    res = d7.classify_line(line)
    assert res == "file"

    line = "8504156 c.dat"
    res = d7.classify_line(line)
    assert res == "file"


def test_generate_filesystem():
    def sort_nested_dicts(fs):
        return sorted(fs, key=lambda x: x["name"])

    res = d7.generate_filesystem(INPUT_TEST_PATH)
    res_keys = list(map(lambda x: x["name"], res))
    sample_keys = list(map(lambda x: x["name"], sample_fs()))
    print(sorted(res_keys))
    print(sorted(sample_keys))
    assert len(res) == len(sample_fs())
    pprint.pprint(sort_nested_dicts(sample_fs()))
    print("\n")
    pprint.pprint(sort_nested_dicts(res))
    assert sort_nested_dicts(res) == sort_nested_dicts(sample_fs())


# def test_dir_size():
#     fs = d7.generate_filesystem(INPUT_TEST_PATH)

#     res = d7.dir_size(fs, "e")
#     assert res == 584

#     res = d7.dir_size(fs, "d")
#     assert res == 4060174 + 8033020 + 5626152 + 7214296
