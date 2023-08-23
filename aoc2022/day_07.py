"""Day 07"""

import re
import pprint
import copy


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
        line_type = classify_line(line)

        if line_type == "directory":
            name = line.split(" ")[1]
            hsh = directory_hash(name, cwd())
            fs.append(hsh)
        elif line_type == "file":
            split = line.split(" ")
            name = split[1]
            size = int(split[0])
            hsh = file_hash(name, cwd(), size)
            fs.append(hsh)
        elif line_type == "command":
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


# def get_all_dirs(fs, dirname):
#     # TODO: Need to eliminate subdirectory at the same level
#     keys = []
#     for key, value in fs.items():
#         # keys.append(key)
#         if isinstance(value, dict):
#             keys.append(key)
#             keys.extend(get_all_dirs(value, dirname))
#     return keys


def directory_size(fs, dirname):
    clone_fs = copy.copy(fs)
    print(f"LEN FS: {len(clone_fs)}")
    all_dirs = [hsh for hsh in clone_fs if hsh["type"] == "directory"]
    dirnames = [dirname]

    for i in range(len(all_dirs)):
        for hsh in all_dirs:
            print(hsh)
            if hsh["parent"] in dirnames:
                dirnames.append(hsh["parent"])
                all_dirs.remove(hsh)

    for hsh in fs:
        if hsh["type"] == "directory" and hsh["parent"] in dirnames:
            dirnames.append(hsh["name"])

    files = [hsh for hsh in fs if (
        hsh["parent"] in dirnames and hsh["type"] == "file")]

    file_sizes = list(map(lambda hsh: hsh["size"], files))

    return sum(file_sizes)


def collect_dir_sizes(fs, limit=None):
    dirnames = [hsh["name"] for hsh in fs if hsh["type"] == "directory"]
    dir_hsh = {}
    for dirname in dirnames:
        dir_size = directory_size(fs, dirname)
        if limit and dir_size >= limit:
            continue
        else:
            dir_hsh[dirname] = dir_size
    return dir_hsh


def sum_collect_dir_sizes(fs, limit=None):
    pp(fs)
    hsh = collect_dir_sizes(fs, limit)
    sizes = list(hsh.values())
    return sum(sizes)
