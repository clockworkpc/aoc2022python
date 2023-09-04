"""Day 01"""


def group_integers(path):
    with open(path, "r") as file:
        lines = [line.strip() for line in file]

    def strip_and_convert(string):
        return 0 if len(string) == 0 else int(string.strip())

    array = list(map(strip_and_convert, lines))

    nested_array = []
    current_array = []

    for integer in array:
        # add the current list to the nested list
        # replace the current list with an empty one
        if integer == 0:
            nested_array.append(current_array)
            current_array = []
        else:
            # add the integer to the current list
            current_array.append(integer)
        print(nested_array)

    # if the current list is not empty
    # i.e. the last integer was not 0
    # the current list needs to be added to the nested list
    if current_array:
        nested_array.append(current_array)
    return nested_array


def sum_grouped_integers(grouped_integers):
    return list(map(lambda x: sum(x), grouped_integers))


def max_calories(calorie_sums, end_index=1):
    sorted_calorie_sums = sorted(calorie_sums, reverse=True)
    return sum(sorted_calorie_sums[:end_index])
