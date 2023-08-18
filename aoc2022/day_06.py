"""Day 06"""


def uniq_check(substring):
    ary = list(set(list(substring)))
    return len(ary) == len(substring)


def uniq_start(string, substr_len):
    counter = substr_len

    running = True
    while running:
        substring = string[:substr_len]
        if uniq_check(substring):
            return counter

        str_list = list(string)
        del str_list[0]
        string = "".join(str_list)
        counter += 1


def uniq_start_from_input(path, substr_len):
    with open(path, "r") as file:
        results = []
        strings = [line.strip() for line in file]
        for string in strings:
            result = uniq_start(string, substr_len)
            results.append(result)
        return results
