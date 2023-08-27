"""Day 09"""


class RopeGame:
    def __init__(self, knots=2):
        self.rope = [{"x": 0, "y": 0} for _ in range(knots)]
        self.tail_visited = [{"x": 0, "y": 0}]
        self.line_counter = 0
        self.move_counter = 0

    def head(self):
        return self.rope[0]

    def tail(self):
        return self.rope[-1]

    def main(self, path):
        with open(path, "r") as file:
            lines = file.readlines()

        for line in lines:
            self.move_rope(line)

    def working_knots(self, index):
        previous_knot = self.rope[index - 1]
        current_knot = self.rope[index]
        return [previous_knot, current_knot]

    def distance(self, index, axis):
        previous_knot, current_knot = self.working_knots(index)
        return previous_knot[axis] - current_knot[axis]

    def horizontal_distance(self, index):
        return self.distance(index, "x")

    def vertical_distance(self, index):
        return self.distance(index, "y")

    def same_axis(self, index, axis):
        previous_knot, current_knot = self.working_knots(index)
        return previous_knot[axis] == current_knot[axis]

    def same_row(self, index):
        return self.same_axis(index, "y")

    def same_column(self, index):
        return self.same_axis(index, "x")

    def is_adjacent(self, index):
        def in_range(axis_distance):
            return abs(axis_distance) in [0, 1]

        horizontal_in_range = in_range(self.horizontal_distance(index))
        vertical_in_range = in_range(self.vertical_distance(index))

        return horizontal_in_range and vertical_in_range

    def is_inline(self, index):
        horizontally_inline = abs(
            self.horizontal_distance(index)
        ) == 2 and self.same_row(index)

        vertically_inline = abs(
            self.vertical_distance(index)
        ) == 2 and self.same_column(index)

        return horizontally_inline or vertically_inline

    def is_diagonal(self, index):
        return (
            abs(self.horizontal_distance(index)) == 2
            or abs(self.vertical_distance(index)) == 2
        )

    def too_far(self, index):
        return (
            abs(self.horizontal_distance(index)) > 2
            or abs(self.vertical_distance(index)) > 2
        )

    def move_knot_straight(self, index):
        previous_knot = self.rope[index - 1]
        current_knot = self.rope[index]
        if self.same_row(index) and previous_knot["x"] > current_knot["x"]:
            current_knot["x"] += 1
        elif self.same_row(index) and previous_knot["x"] < current_knot["x"]:
            current_knot["x"] -= 1
        elif self.same_column(index) and previous_knot["y"] > current_knot["y"]:
            current_knot["y"] += 1
        elif self.same_column(index) and previous_knot["y"] < current_knot["y"]:
            current_knot["y"] -= 1
        else:
            raise ValueError(
                f"Unexpected position for head {previous_knot} or tail {current_knot}"
            )

    def move_knot_diagonally(self, index):
        def in_range(horizontal_range, vertical_range):
            return (
                self.horizontal_distance(index) in horizontal_range
                and self.vertical_distance(index) in vertical_range
            )

        north_east = in_range([1, 2], [1, 2])
        south_east = in_range([1, 2], [-2, -1])
        north_west = in_range([-2, -1], [1, 2])
        south_west = in_range([-2, -1], [-2, -1])

        current_knot = self.rope[index]

        if north_east:
            current_knot["x"] += 1
            current_knot["y"] += 1
        elif south_east:
            current_knot["x"] += 1
            current_knot["y"] -= 1
        elif north_west:
            current_knot["x"] -= 1
            current_knot["y"] += 1
        elif south_west:
            current_knot["x"] -= 1
            current_knot["y"] -= 1

    def update_tail_visited(self):
        hsh = {"x": self.tail()["x"], "y": self.tail()["y"]}

        if hsh in self.tail_visited:
            return

        self.tail_visited.append(hsh)

    def move_rope(self, line):
        self.line_counter += 1
        self.move_counter = 0
        direction = line.split()[0]
        steps = int(line.split()[1])

        def move_head(direction):
            if direction == "U":
                self.head()["y"] += 1
            elif direction == "D":
                self.head()["y"] -= 1
            elif direction == "R":
                self.head()["x"] += 1
            elif direction == "L":
                self.head()["x"] -= 1

        for _ in range(steps):
            self.move_counter += 1
            move_head(direction)

            index = 1
            while index < len(self.rope):
                if self.is_adjacent(index):
                    index += 1
                    continue

                if self.is_inline(index):
                    self.move_knot_straight(index)
                elif self.is_diagonal(index):
                    self.move_knot_diagonally(index)
                elif self.too_far(index):
                    raise ValueError(
                        f"{self.rope[index - 1]} has got away from {self.rope[index]}"
                    )
                else:
                    raise ValueError("Unrecognised error")

                if index + 1 == len(self.rope):
                    self.update_tail_visited()
                else:
                    index += 1
