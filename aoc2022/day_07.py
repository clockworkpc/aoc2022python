"""Day 07"""

import re
import pprint


def pp(x):
    pprint.pprint(x)


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
    def directory_hash(name, parent):
        return {"type": "directory", "name": name, "parent": parent, "size": None}

    def file_hash(name, parent, size):
        return {"type": "file", "name": name, "parent": parent, "size": size}

    root_dir_hash = directory_hash("/", None)
    fs = [root_dir_hash]
    parent_dirs = []
    working_dirs = ["/"]

    def cpd():
        return parent_dirs[-1]

    def cwd():
        return working_dirs[-1]

    lines = readlines(path)

    for line in lines:
        pp(fs)
        line_type = classify_line(line)

        if line_type == "directory":
            name = line.split(" ")[1]
            print(f"DIRECTORY NAME: {name}")
            hsh = directory_hash(name, cpd())
            fs.append(hsh)
        elif line_type == "file":
            split = line.split(" ")
            name = split[1]
            print(f"FILE NAME: {name}")
            size = int(split[0])
            hsh = file_hash(name, cpd(), size)
            fs.append(hsh)
        elif line_type == "command":
            print(line)
            split = line.split(" ")
            verb = split[1]
            if verb == "ls":
                continue
            elif verb == "cd":
                destination = split[2]

                if destination != "..":
                    new_parent_dir = cwd()
                    new_working_dir = destination

                    parent_dirs.append(new_parent_dir)
                    working_dirs.append(new_working_dir)
                elif destination == "..":
                    last_file_or_directory = fs[-1]
                    new_working_dir_name = last_file_or_directory["parent"]
                    working_dirs.append(new_working_dir_name)

                    new_working_dir = [
                        hsh for hsh in fs if hsh["name"] == new_working_dir_name
                    ][0]
                    new_parent_dir = new_working_dir["parent"]
                    parent_dirs.append(new_parent_dir)
    return fs


def get_all_dirs(fs, dirname):
    # TODO: Need to eliminate subdirectory at the same level
    keys = []
    print(fs.items())
    __import__("pdb").set_trace()
    for key, value in fs.items():
        # keys.append(key)
        if isinstance(value, dict):
            print(f"keys: {keys}")
            print(f"dirname: {dirname}, key: {key}, value: {value}")
            keys.append(key)
            keys.extend(get_all_dirs(value, dirname))
    return keys


def dir_size(fs, dirname):
    cwd = fs
    file_sizes = []

    dirnames = get_all_dirs(fs, dirname)
    print(f"dirnames: {dirnames}\n")
    index = dirnames.index(dirname)
    if index + 1 == len(dirnames):
        for directory in dirnames:
            cwd = cwd[directory]
    else:
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
