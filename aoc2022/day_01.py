"""Day 01"""

import re


def group_integers(path):
    with open(path, "r") as file:
        lines = [line.strip() for line in file]

    def strip_and_convert(str):
        return int(str.strip()) if str != "" else str

    nested_array = []
    current_array = []

    array = list(map(strip_and_convert, lines))

    for item in array:
        if item == "":
            nested_array.append(current_array)
            current_array = []
        else:
            current_array.append(item)

    if current_array:
        nested_array.append(current_array)
    return nested_array


def sum_calories(grouped_integers):
    def sum_calories(x):
        return sum(x)

    calorie_sums = list(map(sum_calories, grouped_integers))

    return calorie_sums


def max_calories(calorie_sums, end_index=1):
    sorted_calorie_sums = sorted(calorie_sums, reverse=True)
    start_index = 0
    return sum(sorted_calorie_sums[start_index:end_index])
