"""Day 07"""

import re


def classify_line(line):
    first_cha
    if line[0] == "$":
        return "command"

    if re.match(r"^\d+", line):
        return "file"

    if re.match(r"^\dir", line):
        return "directory"


def create_fs_dictionary(terminal_output):
    file_system = {}
    lines = terminal_output.split("\n")

    for line in lines:
        line_type = classify_line(line)
    return file_system
