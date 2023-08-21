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

        if value == target_value:
            return current_path
        elif isinstance(value, dict):
            nested_result = find_parent(value, target_value, current_path)
            if nested_result:
                return nested_result

    return None


def readlines(path):
    with open(path, "r") as file:
        return [line.strip() for line in file]


def generate_filesystem(path):
    fs = {"/": {}}
    cwd = fs["/"]

    lines = readlines(path)
    print(lines)

    for line in lines:
        line_type = classify_line(line)
        print(line_type)

        if line_type == "directory":
            key = list(line)[1]
            cwd[key] = {}
        elif line_type == "file":
            split = line.split(" ")
            print(line)
            print(split)
            name = split[1]
            size = split[0]
            cwd.append({"name": name, "size": size})
        elif line_type == "command":
            split = line.split(" ")
            verb = split[1]
            if verb == "ls":
                continue
            elif verb == "cd":
                destination = split[2]

                if destination == "/":
                    continue

                if destination != "..":
                    print(f"destination for not cd.. => {destination}")
                    cwd = cwd[destination]
                elif destination == "..":
                    parent = find_parent(fs, list(cwd)[0])

    print(fs)
    return fs
    # change cwd to parent

    # def get_nested_value(dictionary, keys):
    #     if len(keys) == 0:
    #         return dictionary
    #     else:
    #         return get_nested_value(dictionary[keys[0]], keys[1:])

    # nested_keys = ['first_level', 'second_level', 'third_level']
    # result = get_nested_value(nested_dict, nested_keys)


def find_directories(fs, parent_key="/"):
    nested_keys = []
    items = fs.items()
    print(items)
    for key, value in fs.items():
        if isinstance(value, dict):
            nested_keys.append(key)
            print(f"KEY: {key}, VALUE: {value}")
            nested_keys.extend(find_directories(value, parent_key))
        # else:
        #     nested_keys.append(parent_key)
    return nested_keys


def create_fs_dictionary(terminal_output):
    def directory_name(line):
        return line.split(" ")[1]

    file_system = {}
    lines = terminal_output.split("\n")

    cwd = file_system

    for line in lines:
        line_type = classify_line(line)
        if line_type == "directory":
            dirname = directory_name(line)

    return file_system
