"""Day 07"""

import re
import pprint

global_counter = 0
global_directory_depth = 0
logs = []


def pp(x):
    pprint.pprint(x)


def readlines(path):
    with open(path, "r") as file:
        return [line.strip() for line in file]


def classify_line(line):
    cd_pattern = r"^\$ cd"
    file_pattern = r"^\d+ [a-z]+"
    directory_pattern = r"^dir [a-z]+"
    ls_pattern = r"^\$ ls"

    if re.match(cd_pattern, line):
        return "cd_command"

    if re.match(file_pattern, line):
        return "file"

    if re.match(directory_pattern, line):
        return "directory"

    if re.match(ls_pattern, line):
        return "ls_command"

    raise ValueError(f"Not classified: {line}")


def root_directory():
    return {
        "type": "directory",
        "name": "/",
        "parents": [],
        "size": None,
        "depth": 0,
        "position": 0,
    }


class FileSystem:
    def __init__(self):
        self.fs = [root_directory()]
        self.current_dir = {}
        self.parent_dir_names = []
        self.current_dir_depth = 0
        self.current_dir_position = 0

    def find_file_or_directory(self, name, parents):
        print(f"name: {name}")
        print(f"parents: {parents}")
        print(f"fs: {self.fs}")
        if name == "a":
            __import__("pdb").set_trace()
        parents = [self.parent_dir_names].append(dir_name)
        return [
            hsh for hsh in self.fs if hsh["name"] == name and hsh["parents"] == parents
        ]

    def go_up_fs_tree(self, dir_name):
        parents = self.parent_dir_names[0:-2]
        previous_dir = self.find_file_or_directory(dir_name, parents)

        if previous_dir:
            current_dir = previous_dir
        else:
            print(f"Directory {dir_name} not found")

        self.parent_dir_names = previous_dir["parents"]
        self.current_dir_depth = previous_dir["depth"]
        self.current_dir_position = previous_dir["position"]

    def go_down_fs_tree(self, dir_name):
        parents = list(self.current_dir["parents"])
        parents.append(self.current_dir["name"])
        next_dir = self.find_file_or_directory(dir_name, parents)
        __import__("pdb").set_trace()

        if next_dir:
            self.current_dir = next_dir
        else:
            raise TypeError(f"Directory {dir_name} not found")

        print(f"next_dir: {next_dir}")
        self.parent_dir_names = next_dir["parents"]
        self.current_dir_depth = next_dir["depth"]
        self.current_dir_position = next_dir["position"]

    def find_or_create_directory(self, line):
        if line.strip() == "$ cd /" and len(self.fs) == 1:
            self.fs.append(root_directory())
            self.current_dir = root_directory()
            return

        dir_name = line.split(" ")[1]

        if self.find_file_or_directory(dir_name, self.parent_dir_names):
            return

        hsh = self.new_directory(dir_name)
        self.fs.append(hsh)

    def change_directory(self, line):
        dir_name = line.split(" ")[2]

        if dir_name == "..":
            self.go_up_fs_tree(dir_name)
        if dir_name == "/":
            self.find_or_create_directory(line)
        if re.match(r"[a-z]+", dir_name):
            self.go_down_fs_tree(dir_name)

    def new_directory(self, dir_name):
        parents = list(self.current_dir["parents"])
        parents.append(self.current_dir["name"])
        hsh = {
            "type": "directory",
            "name": dir_name,
            "parents": parents,
            "size": None,
            "depth": self.current_dir["depth"] + 1,
            "position": self.current_dir["position"] + 1,
        }
        return hsh

    def new_file(self, name, size, parents):
        hsh = {
            "type": "file",
            "name": name,
            "parents": parents,
            "size": size,
            "depth": self.current_dir["depth"] + 1,
            "position": self.current_dir["position"] + 1,
        }
        return hsh

    def create_file(self, line):
        split = line.strip().split(" ")
        file_name = split[1]
        size = split[0]
        parents = [self.current_dir["parents"]]
        parents.append(self.current_dir["name"])

        existing_file = self.find_file_or_directory(file_name, parents)
        if existing_file:
            return existing_file

        hsh = self.new_file(file_name, size, parents)
        self.fs.append(hsh)

    def generate_filesystem(self, path):
        lines = readlines(path)

        for line in lines:
            print(line)
            classification = classify_line(line)

            if classification == "cd_command":
                self.change_directory(line)
            elif classification == "directory":
                self.find_or_create_directory(line)
            elif classification == "file":
                self.create_file(line)
            else:
                continue

        return self.fs


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


def go_to_parent_dir(fs, ary):
    cwd = fs
    for dirname in ary[0:-1]:
        cwd = cwd[dirname]
    return cwd


def change_directory_update_parents(
    line, current_dir, parent_dir_names, fs, directory_depth
):
    print(line)

    def find_dir(fs, previous_dir_name, directory_depth, parents):
        return next(
            (
                hsh
                for hsh in fs
                if (
                    hsh["name"] == dir_name
                    and hsh["directory_depth"] == directory_depth
                    and hsh["parents"] == parents
                )
            ),
            None,
        )

    def set_current_directory(fs, dir_name, directory_depth, parents):
        root = dir_name == "/"
        if root:
            return root_directory()
        else:
            current_dir = find_dir(fs, dir_name, directory_depth, parents)
            if not current_dir:
                print("No current dir")
            return current_dir

    def set_parent_directories(current_dir, parent_dir_names):
        root = dir_name == "/"

        if root:
            parent_dir_names = []
        else:
            if not current_dir:
                self.parent_dir_names.append(self.current_dir["name"])

        return parent_dir_names

    split = line.split(" ")
    dir_name = split[2]

    if re.match(r"/", dir_name):
        directory_depth = 0
        current_dir = root_directory()
        parent_dir_names = []
    elif re.match(r"[a-z]+", dir_name):
        directory_depth += 1
        current_dir = set_current_directory(
            fs, dir_name, directory_depth, parent_dir_names
        )

        parent_dir_names = set_parent_directories(
            current_dir, parent_dir_names)

    elif re.match(r"\.\.", dir_name):
        directory_depth -= 1
        previous_dir_name = current_dir["parents"][-1]
        previous_parent_dir_names = parent_dir_names[0:-1]

        current_dir = find_dir(
            fs, previous_dir_name, directory_depth, previous_parent_dir_names
        )
        parent_dir_names = previous_parent_dir_names

    return [current_dir, parent_dir_names, directory_depth]


def is_root(dir_name):
    return dir_name == "/"


# def change_directory(fs, dir_name, current_dir, parent_dir_names, dir_depth):
#     if is_root:
#         current_dir = root_directory()
#         parent_dir_names = []
#         dir_depth = 0
#     else:
#         current_dir = find_dir(fs, dir_name, dir_depth)
#         parent_dir_names = current_dir["parents"]
#         dir_depth = current_dir[""]


# def generate_filesystem(path):
#     def find_or_create_directory(line, current_dir, parent_dir_names, directory_depth):
#         name = line.split(" ")[1]
#         if name == "/":
#             return root_directory()
#         else:
#             parent = current_dir["name"]
#             if not parent in parent_dir_names:
#                 parent_dir_names.append(parent)

#         parents = list(parent_dir_names)

#         hsh = {
#             "type": "directory",
#             "name": name,
#             "parents": parents,
#             "size": None,
#             "directory_depth": directory_depth,
#         }

#         return hsh

#     def create_file(line, parent_dir_names):
#         split = line.split(" ")
#         name = split[1]
#         size = int(split[0])
#         parents = list(parent_dir_names)
#         return {"type": "file", "name": name, "parents": parents, "size": size}

#     current_dir = None
#     parent_dir_names = []
#     directory_depth = 0

#     fs = [find_or_create_directory("dir /", current_dir,
#                            parent_dir_names, directory_depth)]

#     lines = readlines(path)

#     for line in lines:
#         line_type = classify_line(line)

#         if line_type == "command":
#             if line.split(" ")[1] == "ls":
#                 continue
#             elif line.split(" ")[1] == "cd":
#                 (
#                     current_dir,
#                     parent_dir_names,
#                     directory_depth,
#                 ) = change_directory_update_parents(
#                     line, current_dir, parent_dir_names, fs, directory_depth
#                 )
#                 print(f"parents: {current_dir['parents']}")
#                 print(f"parents count: { len(current_dir['parents']) }")
#                 print(f"directory_depth: {directory_depth}\n")

#         elif line_type == "directory":
#             hsh = create_directory(
#                 line, current_dir, parent_dir_names, directory_depth)
#             if hsh["name"] == "zfl":
#                 my_list = [hsh for hsh in fs if hsh["name"] == "zfl"]
#             fs.append(hsh)

#         elif line_type == "file":
#             hsh = create_file(line, parent_dir_names)
#             fs.append(hsh)

#     return fs


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
    all_files = [
        hsh for hsh in fs if hsh["type"] == "file" and dirname in hsh["parents"]
    ]

    sizes = list(map(lambda hsh: hsh["size"], all_files))

    return sum(sizes)


# def directory_size(fs, dirname):
#     clone_fs = copy.copy(fs)
#
#     all_dirs = [hsh for hsh in clone_fs if hsh["type"] == "directory"]
#     dirnames = [dirname]

#     for i in range(len(all_dirs)):
#         for hsh in all_dirs:
#
#             if hsh["parent"] in dirnames:
#                 dirnames.append(hsh["parent"])
#                 all_dirs.remove(hsh)

#     for hsh in fs:
#         if hsh["type"] == "directory" and hsh["parent"] in dirnames:
#             dirnames.append(hsh["name"])

#     files = [hsh for hsh in fs if (
#         hsh["parent"] in dirnames and hsh["type"] == "file")]

#     file_sizes = list(map(lambda hsh: hsh["size"], files))

#     return sum(file_sizes)


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
