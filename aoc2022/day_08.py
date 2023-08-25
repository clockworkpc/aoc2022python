"""Day 08"""


def map_trees(path):
    with open(path, "r") as file:
        return file.read().splitlines()


def outer_trees(grid):
    return (len(grid) * 2) + ((len(grid[0]) - 2) * 2)


def visible_from_left(row, index):
    tree_height = int(row[index])
    return all(int(height) < tree_height for height in row[:index])


def visible_from_right(row, index):
    tree_height = int(row[index])
    return all(int(height) < tree_height for height in row[index + 1:])


def tree_column(grid, column_index):
    return [row[column_index] for row in grid]


def visible_from_top(grid, column_index, tree_index):
    column = tree_column(grid, column_index)
    tree_height = int(column[tree_index])
    collection = [int(height) < tree_height for height in column[:tree_index]]
    return all(collection)


def visible_from_bottom(grid, column_index, tree_index):
    column = tree_column(grid, column_index)
    tree_height = int(column[tree_index])
    collection = [
        int(height) < tree_height for height in column[tree_index + 1:]]
    return all(collection)


def is_visible(grid, row_number, position_in_row):
    first_row = row_number == 0
    last_row = row_number == len(grid) - 1
    first_column = position_in_row == 0
    last_column = position_in_row == len(grid[0]) - 1

    if first_row or last_row or first_column or last_column:
        return True

    row = grid[row_number]
    left = visible_from_left(row, position_in_row)
    right = visible_from_right(row, position_in_row)

    column_index = position_in_row
    tree_index = row_number

    top = visible_from_top(grid, column_index, tree_index)
    bottom = visible_from_bottom(grid, column_index, tree_index)

    result = any([left, right, top, bottom])
    return result


def visibility_map(grid):
    results = []
    for row_number, row in enumerate(grid, start=0):
        row_results = []
        for position_in_row, tree in enumerate(row, start=0):
            result = is_visible(grid, row_number, position_in_row)
            row_results.append(result)
        results.append(row_results)

    return results


def visibility_count(visibility_map):
    flat_list = [item for sublist in visibility_map for item in sublist]
    visible = [item for item in flat_list if item is True]
    invisible = [item for item in flat_list if item is False]

    return {"visible": len(visible), "invisible": len(invisible)}


def visible_to_left(row, position_in_row):
    if position_in_row == 0:
        return 0

    tree_height = int(row[position_in_row])
    tree_list = row[:position_in_row:][::-1]
    vision = 0
    index = 0
    while index != len(tree_list):
        vision += 1
        if int(tree_list[index]) >= tree_height:
            return vision
        index += 1
    return vision


def visible_to_right(row, position_in_row):
    if position_in_row == len(row) - 1:
        return 0

    tree_height = int(row[position_in_row])
    tree_list = row[position_in_row + 1:]
    vision = 0
    index = 0
    while index != len(tree_list):
        vision += 1
        if int(tree_list[index]) >= tree_height:
            return vision
        index += 1
    return vision


def visible_to_top(grid, column_index, tree_index):
    if tree_index == 0:
        return 0

    column = tree_column(grid, column_index)
    tree_height = int(column[tree_index])
    tree_list = column[:tree_index:][::-1]
    vision = 0
    index = 0
    while index != len(tree_list):
        vision += 1
        if int(tree_list[index]) >= tree_height:
            return vision
        index += 1
    return vision


def visible_to_bottom(grid, column_index, tree_index):
    if tree_index == 4:
        return 0

    column = tree_column(grid, column_index)
    tree_height = int(column[tree_index])
    tree_list = column[tree_index + 1:]
    vision = 0
    index = 0
    while index != len(tree_list):
        vision += 1
        if int(tree_list[index]) >= tree_height:
            return vision
        index += 1
    return vision


def scenic_score(grid, row_number, position_in_row):
    is_top_row = row_number == 0
    is_bottom_row = row_number == len(grid) - 1
    is_left_column = position_in_row == 0
    is_right_column = position_in_row == len(grid) - 1

    if is_top_row or is_bottom_row or is_left_column or is_right_column:
        return 0

    row = grid[row_number]
    left = visible_to_left(row, position_in_row)
    right = visible_to_right(row, position_in_row)

    column_index = position_in_row
    tree_index = row_number
    top = visible_to_top(grid, column_index, tree_index)
    bottom = visible_to_bottom(grid, column_index, tree_index)

    scores = left * right * top * bottom

    print(f"row: {row_number}, tree: {position_in_row}")
    print(f"left: {left}")
    print(f"right: {right}")
    print(f"top: {top}")
    print(f"bottom: {bottom}")
    return scores
