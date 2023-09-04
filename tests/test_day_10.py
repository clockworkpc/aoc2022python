#!/usr/bin/env python

import json
from aoc2022 import day_10 as d10

INPUT_TEST_PATH = "tests/input_files/day_10_input_sample.txt"
INPUT_FULL_PATH = "tests/input_files/day_10_input.txt"


def tiny_x():
    with open("tests/fixtures/day_10_tiny_logs.json", "r") as json_file:
        return json.load(json_file)


def sample_input():
    with open("tests/input_files/day_10_input.txt", "r") as file:
        return file.readlines()


def test_run_noop():
    o = d10.Device()
    line = "noop"
    o.execute(line)
    assert o.cycles == 1
    assert o.x_value_during(1) == 1
    assert o.x_value_after(1) == 1
    assert o.signal_strength_during(1) == 1
    assert o.signal_strength_after(1) == 1

    line = "addx 3"
    o.execute(line)
    assert o.cycles == 3
    assert o.x_value_during(2) == 1
    assert o.x_value_during(3) == 1
    assert o.x_value_after(2) == 1
    assert o.x_value_after(3) == 4
    assert o.signal_strength_during(2) == 2 * 1
    assert o.signal_strength_during(3) == 3 * 1
    assert o.signal_strength_after(2) == 2 * 1
    assert o.signal_strength_after(3) == 3 * 4

    line = "addx -5"
    o.execute(line)
    assert o.cycles == 5
    assert o.x_value_during(4) == 4
    assert o.x_value_during(5) == 4
    assert o.signal_strength_during(4) == 4 * 4
    assert o.signal_strength_during(5) == 5 * 4
    assert o.x_value_after(4) == 4
    assert o.x_value_after(5) == -1
    assert o.signal_strength_after(4) == 4 * 4
    assert o.signal_strength_after(5) == 5 * -1


def test_main():
    path = "tests/input_files/day_10_input_sample_tiny.txt"
    o = d10.Device()
    o.main(path)
    assert o.x == tiny_x()

    o = d10.Device()
    o.main(INPUT_TEST_PATH)
    assert o.x_value_during(20) == 21
    assert o.signal_strength_during(20) == 420
    assert o.x_value_during(60) == 19
    assert o.signal_strength_during(60) == 60 * 19
    assert o.x_value_during(100) == 18
    assert o.signal_strength_during(100) == 100 * 18
    assert o.x_value_during(140) == 21
    assert o.signal_strength_during(140) == 140 * 21
    assert o.x_value_during(180) == 16
    assert o.signal_strength_during(180) == 180 * 16
    assert o.x_value_during(220) == 18
    assert o.signal_strength_during(220) == 220 * 18

    index_ary = [20, 60, 100, 140, 180, 220]
    assert o.sum_signal_strengths(index_ary) == 13140

    o = d10.Device()
    o.main(INPUT_FULL_PATH)
    index_ary = [20, 60, 100, 140, 180, 220]
    assert o.sum_signal_strengths(index_ary) == 12460
