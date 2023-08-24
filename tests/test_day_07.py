#!/usr/bin/env python

from aoc2022 import day_07 as d7
import json
import pprint

INPUT_TEST_PATH = "tests/input_files/day_07_input_sample.txt"
INPUT_FULL_PATH = "tests/input_files/day_07_input.txt"


def pp(x):
    pprint.pprint(x)


def sample_lines():
    with open(INPUT_TEST_PATH, "r") as file:
        return [line for line in file]


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


# def test_log():
#     lines = sample_lines()
#     for line in lines:
#         log = d7.update_logs(line)
#         print(log)

#     res = d7.logs
#     assert res == "hello"


def test_generate_filesystem():
    def sort_nested_dicts(fs):
        return sorted(fs, key=lambda x: x["name"])

    obj = d7.FileSystem()
    res = obj.generate_filesystem(INPUT_TEST_PATH)
    for index, hsh in enumerate(sort_nested_dicts(res), start=0):
        test_hsh = sort_nested_dicts(sample_fs())[index]
        print(hsh)
        print(test_hsh)
        assert hsh == test_hsh


# def test_directory_size():
#     fs = d7.generate_filesystem(INPUT_TEST_PATH)

#     res = d7.directory_size(fs, "e")
#     assert res == 584

#     res = d7.directory_size(fs, "d")
#     assert res == 4060174 + 8033020 + 5626152 + 7214296
#     assert res == 24933642

#     res = d7.directory_size(fs, "a")
#     assert res == 94853

#     res = d7.directory_size(fs, "/")
#     assert res == 48381165


# def test_collect_dir_sizes():
#     fs = d7.generate_filesystem(INPUT_TEST_PATH)
#     res = d7.collect_dir_sizes(fs, limit=None)
#     test = {"/": 48381165, "a": 94853, "d": 24933642, "e": 584}
#     assert res == test

#     res = d7.collect_dir_sizes(fs, limit=100000)
#     test = {"a": 94853, "e": 584}
#     assert res == test

# def test_generate_filesystem_full():


# def test_sum_collect_dir_sizes():
# fs = d7.generate_filesystem(INPUT_TEST_PATH)
# res = d7.sum_collect_dir_sizes(fs, limit=100000)
# assert res == 94853 + 584

# fs = d7.generate_filesystem(INPUT_FULL_PATH)
# res = d7.sum_collect_dir_sizes(fs, limit=100000)
# assert res == 95437
