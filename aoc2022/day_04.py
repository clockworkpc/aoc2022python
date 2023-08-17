"""Day 04"""


# Part 01


def split_strip(path):
    with open(path, "r") as file:
        return [line.strip() for line in file]


def assign_sections(line):
    sections = []
    start_end_ary = list(map(lambda x: x.split("-"), line.split(",")))

    for start_end in start_end_ary:
        start = int(start_end[0])
        end = int(start_end[1])
        ary = list(range(start, end + 1))
        sections.append(ary)

    return sections


def common_sections(assigned_sections):
    s0 = assigned_sections[0]
    s1 = assigned_sections[1]
    return [item for item in s0 if item in s1]


def arrangement_label(assigned_sections):
    cs = common_sections(assigned_sections)
    s0 = assigned_sections[0]
    s1 = assigned_sections[1]

    # No common sections
    if not cs:
        return "distinct"

    # Identical sections
    if s0 == s1:
        return "subset"

    # Same length, some common sections
    if len(s0) == len(s1):
        return "overlap"

    max_set = set(max(assigned_sections, key=len))
    min_set = set(min(assigned_sections, key=len))

    # Smaller set is a subset of the larger set
    if min_set <= max_set:
        return "subset"
    else:
        return "overlap"


def count_arrangements(path):
    arrangements = {"distinct": 0, "overlap": 0, "subset": 0}
    lines = split_strip(path)
    for line in lines:
        assigned_sections = assign_sections(line)
        label = arrangement_label(assigned_sections)
        arrangements[label] += 1
    return arrangements
