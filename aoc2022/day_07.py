"""Day 07"""

from collections import defaultdict


def change_directory(c, stack):
    dest = c.split()[2]
    if dest == "..":
        stack.pop()
    else:
        path = f"{stack[-1]}_{dest}" if stack else dest
        stack.append(path)


def add_file(c, stack, sizes):
    size = c.split()[0]
    for path in stack:
        sizes[path] += int(size)


def readlines(path):
    with open(path, "r") as file:
        return file.readlines()


def import_commands(commands, stack, sizes):
    for c in commands:
        if c.startswith("$ ls") or c.startswith("dir"):
            continue
        if c.startswith("$ cd"):
            change_directory(c, stack)
        else:
            add_file(c, stack, sizes)


def generate_sizes(path):
    commands = readlines(path)
    stack = []
    sizes = defaultdict(int)
    import_commands(commands, stack, sizes)
    return sizes


def filter_directories_by_limit(sizes, limit):
    return list((n for n in sizes.values() if n <= limit))


def sum_filtered_directories_by_size(sizes, max_dir_size):
    filtered_dirs = (n for n in sizes.values() if n <= max_dir_size)
    return sum(filtered_dirs)


def find_smallest_directory(sizes, disk_space, space_needed):
    occupied_space = disk_space - sizes["/"]
    target = space_needed - occupied_space
    reverse_values = sorted(set(sizes.values()), reverse=True)
    result = min(size for size in reverse_values if size > target)
    return result
