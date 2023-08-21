#!/usr/bin/env python

from aoc2022 import day_07 as d7
import json

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
    res = d7.generate_filesystem(INPUT_TEST_PATH)
    assert res == sample_fs()


# def test_find_directories():
#     fs = sample_fs()

#     res = d7.find_directories(fs)
#     assert res == ["/", "a", "d"]


# def test_create_fs_dictionary():
#     terminal_output = """$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d"""
#     fs_dictionary = {
#         "/": {"a": {"b.txt": {"size": 14848514}, "c.dat": {"size": 8504156}}, "d": {}}
#     }
#     res = d7.create_fs_dictionary(terminal_output)
#     assert res == fs_dictionary
