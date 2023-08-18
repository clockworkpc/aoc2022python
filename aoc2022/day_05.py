"""Day 05"""

import re
import pprint
from collections import Counter

pp = pprint.PrettyPrinter(indent=4)
# Part 01


def readlines(path, split=True):
    with open(path, "r") as file:
        if split:
            return [line.split(" ") for line in file]
        else:
            return [line for line in file]


def filter_by_pattern(pattern, lines):
    return list(filter(lambda line: re.match(pattern, line), lines))


def new_map_sans_crates(lines):
    def is_header(line):
        return line[0] == "" and line[1] == "1"

    header_ary = list(filter(lambda line: is_header(line), lines))[0]
    key_ary = [item.strip() for item in header_ary if re.match(r"\d", item)]

    map_dict = {}
    for key in key_ary:
        map_dict[key] = []

    return map_dict


def extract_distinct_elements(line):
    distinct_elements = []
    seen_elements = set()

    for element in line:
        stripped_element = element.strip()
        if stripped_element and stripped_element not in seen_elements:
            seen_elements.add(stripped_element)
            distinct_elements.append(element)

    return distinct_elements


def find_crate_lines(path):
    with open(path, "r") as file:
        lines = []
        pattern = r"\[[A-Z]\]"
        for line in file:
            if re.search(pattern, line):
                clean_line = line.replace("\n", "")
                joined = "".join(clean_line)
                corrected = joined.replace("    ", "#")
                chars = [c for c in corrected if re.match(r"[A-Z#]", c)]
                lines.append(chars)

        return lines


def new_map_with_crates(path, empty_map):
    crate_ary_ary = find_crate_lines(path)

    for crate_ary in crate_ary_ary:
        for index, char in enumerate(crate_ary, 1):
            key = str(index)

            if char == "#":
                continue

            empty_map[key].append(char)

    return empty_map


def import_map(path):
    lines = readlines(path)
    empty_map = new_map_sans_crates(lines)
    return new_map_with_crates(path, empty_map)


def move_crate(my_map, cmd, cratemover_old=True):
    def extract_substring(word, integer=True):
        string = re.search(r"\b{}\b \d+".format(word), cmd).group()
        number = re.search(r"\d+", string).group()
        return int(number) if integer else number

    move = extract_substring("move")
    origin_str = extract_substring("from", False)
    destination_str = extract_substring("to", False)

    origin = my_map[origin_str]
    destination = my_map[destination_str]

    if cratemover_old:
        for _ in range(move):
            crate = origin.pop(0)
            destination.insert(0, crate)
    else:
        crates = origin[:move]
        del origin[:move]
        destination[:0] = crates

    return my_map


def import_instructions(path):
    lines = readlines(path, split=False)
    instructions = []
    for line in lines:
        if re.findall("move", line):
            instructions.append(line.strip())
    return instructions


def top_crates_from_instructions(path, cratemover_old=True):
    my_map = import_map(path)
    instructions = import_instructions(path)

    for i in instructions:
        move_crate(my_map, i, cratemover_old)

    return top_crates(my_map)


def top_crates(my_map):
    crates = list(map(lambda ary: ary[0], my_map.values()))
    joined = "".join(crates)
    return joined
