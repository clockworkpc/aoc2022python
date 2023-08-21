"""Day 07"""

import re


def classify_line(line):
    def regex_test(pattern, value):
        if re.match(pattern, line):
            return value

    return (
        regex_test(r"^\$", "command")
        or regex_test(r"^\d+", "file")
        or regex_test(r"^dir", "directory")
    )


def find_parent(dictionary, target_value, path=None):
    if path is None:
        path = []

    for key, value in dictionary.items():
        current_path = path + [key]

        if isinstance(value, dict) and next(iter(value)) == target_value:
            return current_path
        elif isinstance(value, dict):
            nested_result = find_parent(value, target_value, current_path)
            if nested_result:
                return nested_result

    return None


def readlines(path):
    with open(path, "r") as file:
        return [line.strip() for line in file]


def go_to_parent_dir(fs, ary):
    cwd = fs
    for dirname in ary[0:-1]:
        cwd = cwd[dirname]
    return cwd


def generate_filesystem(path):
    fs = {"/": {}}
    parent_location = fs
    cwd = fs["/"]

    lines = readlines(path)

    for line in lines:
        line_type = classify_line(line)

        if line_type == "directory":
            key = line.split(" ")[1]
            cwd[key] = {}
        elif line_type == "file":
            split = line.split(" ")
            name = split[1]
            size = int(split[0])
            cwd[name] = size
        elif line_type == "command":
            split = line.split(" ")
            verb = split[1]
            if verb == "ls":
                continue
            elif verb == "cd":
                destination = split[2]

                if destination == "/":
                    cwd = fs["/"]
                elif destination != "..":
                    cwd = cwd[destination]
                elif destination == "..":
                    parent = find_parent(fs, list(cwd)[0])
                    cwd = go_to_parent_dir(fs, parent)

    return fs


def get_all_dirs(fs):
    # TODO: Need to eliminate subdirectory at the same level
    keys = []
    for key, value in fs.items():
        print(f"key: {key}, value: {value}")
        # keys.append(key)
        if isinstance(value, dict):
            keys.append(key)
            keys.extend(get_all_dirs(value))
    return keys


def dir_size(fs, dirname):
    cwd = fs
    file_sizes = []

    dirnames = get_all_dirs(fs)
    print(f"dirnames: {dirnames}")
    index = dirnames.index(dirname)
    print(f"index: {index}")
    if index + 1 == len(dirnames):
        for directory in dirnames:
            cwd = cwd[directory]
            print(f"new cwd: {cwd}")
    else:
        print("I am here")
        dir_position = dirnames.index(dirname)
        for directory in dirnames[0: dir_position + 1]:
            cwd = cwd[directory]

    print(cwd)

    for key, value in cwd.items():
        if type(value) is int:
            file_sizes.append(value)

    return sum(file_sizes)


# def find_directories(fs, parent_key="/"):
#     nested_keys = []
#     items = fs.items()
#     print(items)
#     for key, value in fs.items():
#         if isinstance(value, dict):
#             nested_keys.append(key)
#             print(f"KEY: {key}, VALUE: {value}")
#             nested_keys.extend(find_directories(value, parent_key))
#         # else:
#         #     nested_keys.append(parent_key)
#     return nested_keys


# def create_fs_dictionary(terminal_output):
#     def directory_name(line):
#         return line.split(" ")[1]

#     file_system = {}
#     lines = terminal_output.split("\n")

#     cwd = file_system

#     for line in lines:
#         line_type = classify_line(line)
#         if line_type == "directory":
#             dirname = directory_name(line)

#     return file_system
