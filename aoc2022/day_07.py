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
