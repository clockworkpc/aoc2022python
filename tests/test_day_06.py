#!/usr/bin/env python

from aoc2022 import day_06 as d6

import json

INPUT_TEST_PATH = "tests/input_files/day_06_input_sample.txt"
INPUT_FULL_PATH = "tests/input_files/day_06_input.txt"

"""PART 01"""


def test_uniq_check():
    substring = "mjqj"
    res = d6.uniq_check(substring)
    assert res == False

    substring = "jqjp"
    res = d6.uniq_check(substring)
    assert res == False

    substring = "qjpq"
    res = d6.uniq_check(substring)
    assert res == False

    substring = "jpqm"
    res = d6.uniq_check(substring)
    assert res == True


def test_uniq_start():
    string = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    substr_len = 4
    res = d6.uniq_start(string, substr_len)
    assert res == 7

    string = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    substr_len = 4
    res = d6.uniq_start(string, substr_len)
    assert res == 5

    string = "nppdvjthqldpwncqszvftbrmjlhg"
    substr_len = 4
    res = d6.uniq_start(string, substr_len)
    assert res == 6

    string = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    substr_len = 4
    res = d6.uniq_start(string, substr_len)
    assert res == 10

    string = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    substr_len = 4
    res = d6.uniq_start(string, substr_len)
    assert res == 11

    string = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    substr_len = 14
    res = d6.uniq_start(string, substr_len)
    assert res == 19

    string = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    substr_len = 14
    res = d6.uniq_start(string, substr_len)
    assert res == 23

    string = "nppdvjthqldpwncqszvftbrmjlhg"
    substr_len = 14
    res = d6.uniq_start(string, substr_len)
    assert res == 23

    string = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    substr_len = 14
    res = d6.uniq_start(string, substr_len)
    assert res == 29

    string = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    substr_len = 14
    res = d6.uniq_start(string, substr_len)
    assert res == 26


def test_uniq_start_from_input():
    path = INPUT_FULL_PATH
    substr_len = 4
    res = d6.uniq_start_from_input(path, substr_len)
    assert res[0] == 1848

    path = INPUT_FULL_PATH
    substr_len = 14
    res = d6.uniq_start_from_input(path, substr_len)
    assert res[0] == 2308
