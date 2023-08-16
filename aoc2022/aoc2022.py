"""Main module."""


def strip_split_text(path):
    with open(path, "r") as file:
        lines = [line.strip().split(" ") for line in file]
        return lines
