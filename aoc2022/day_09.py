"""Day 09"""

head = {"x": [], "y": []}
tail = {"x": [], "y": []}


def horizontal_distance():
    return len(tail["x"]) - len(head["x"])


def vertical_distance():
    return len(tail["y"]) - len(head["y"])


def same_row():
    return len(tail["y"]) == len(head["y"])


def same_column():
    return len(tail["x"]) == len(head["x"])


def is_adjacent():
    horizontally_adjacent = abs(horizontal_distance()) <= 1 and same_row()
    vertically_adjacent = abs(vertical_distance()) <= 1 and same_column()
    diagonally_adjacent = (
        abs(horizontal_distance()) == 1 and abs(vertical_distance()) == 1
    )

    return horizontally_adjacent or vertically_adjacent or diagonally_adjacent


def is_inline():
    horizontally_inline = abs(horizontal_distance()) == 2 and same_row()
    vertically_inline = abs(vertical_distance()) == 2 and same_column()
    return horizontally_inline or vertically_inline


def is_diagonal():
    return abs(horizontal_distance()) == 2 and abs(vertical_distance()) == 2


def too_far():
    return abs(horizontal_distance()) > 2 or abs(vertical_distance()) > 2


def move_tail_straight():
    if same_row() and len(head["x"]) > len(tail["x"]):
        tail["x"].append(1)
    elif same_row() and len(head["x"]) < len(tail["x"]):
        tail["x"].pop()
    elif same_column() and len(head["y"]) > len(tail["y"]):
        tail["y"].append(1)
    elif same_column() and len(head["y"]) < len(tail["y"]):
        tail["y"].pop()
    else:
        raise ValueError(f"Unexpected position for head {head} or tail {tail}")


def move_tail_diagonally():
    r2u1 = horizontal_distance() == 2 and vertical_distance() == 1
    r1u2 = horizontal_distance() == 1 and vertical_distance() == 2

    r2d1 = horizontal_distance() == 2 and vertical_distance() == -1
    r1d2 = horizontal_distance() == 1 and vertical_distance() == -2

    l2u1 = horizontal_distance() == -2 and vertical_distance() == 1
    l1u2 = horizontal_distance() == -1 and vertical_distance() == 2

    l2d1 = horizontal_distance() == -2 and vertical_distance() == -1
    l1d2 = horizontal_distance() == -1 and vertical_distance() == -2

    if r2u1 or r1u2:
        tail["x"].append(1)
        tail["y"].append(1)
    elif r2d1 or r1d2:
        tail["x"].append(1)
        tail["y"].pop()
    elif l2u1 or l1u2:
        tail["x"].pop()
        tail["y"].append(1)
    elif l2d1 or l1d2:
        tail["x"].pop()
        tail["y"].pop()


def move_pieces(line):
    direction = line.split()[0]
    steps = int(line.split()[1])

    moves = {
        "U": lambda player: player["y"].append(1),
        "D": lambda player: player["y"].pop(),
        "R": lambda player: player["x"].append(1),
        "L": lambda player: player["x"].pop(),
    }

    for _ in range(steps):
        print(f"Step {_} of {steps}")
        moves[direction](head)

        if is_adjacent():
            continue

        if is_inline():
            move_tail_straight()
        elif is_diagonal():
            move_tail_diagonally()
        elif too_far():
            raise ValueError(f"Head {head} has got away from tail {tail}")
        else:
            raise ValueError("Unrecognised error")

    return [head, tail]
