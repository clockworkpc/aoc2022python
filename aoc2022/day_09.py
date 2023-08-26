"""Day 09"""


class RopeGame:
    def __init__(self):
        self.head = {"x": 0, "y": 0}
        self.tail = {"x": 0, "y": 0}
        self.tail_visited = [{"x": 0, "y": 0}]

    def main(self, path):
        with open(path, "r") as file:
            lines = file.readlines()

        for line in lines:
            self.move_pieces(line)

    def horizontal_distance(self):
        return self.head["x"] - self.tail["x"]

    def vertical_distance(self):
        return self.head["y"] - self.tail["y"]

    def same_row(self):
        return self.tail["y"] == self.head["y"]

    def same_column(self):
        return self.tail["x"] == self.head["x"]

    def is_adjacent(self):
        horizontally_adjacent = abs(
            self.horizontal_distance()) <= 1 and self.same_row()
        vertically_adjacent = abs(
            self.vertical_distance()) <= 1 and self.same_column()
        diagonally_adjacent = (
            abs(self.horizontal_distance()) == 1 and abs(
                self.vertical_distance()) == 1
        )

        return horizontally_adjacent or vertically_adjacent or diagonally_adjacent

    def is_inline(self):
        horizontally_inline = abs(
            self.horizontal_distance()) == 2 and self.same_row()
        vertically_inline = abs(self.vertical_distance()
                                ) == 2 and self.same_column()
        return horizontally_inline or vertically_inline

    def is_diagonal(self):
        return (
            abs(self.horizontal_distance()) == 2 or abs(
                self.vertical_distance()) == 2
        )

    def too_far(self):
        return abs(self.horizontal_distance()) > 2 or abs(self.vertical_distance()) > 2

    def move_tail_straight(self):
        if self.same_row() and self.head["x"] > self.tail["x"]:
            self.tail["x"] += 1
        elif self.same_row() and self.head["x"] < self.tail["x"]:
            self.tail["x"] -= 1
        elif self.same_column() and self.head["y"] > self.tail["y"]:
            self.tail["y"] += 1
        elif self.same_column() and self.head["y"] < self.tail["y"]:
            self.tail["y"] -= 1
        else:
            raise ValueError(
                f"Unexpected position for head {self.head} or tail {self.tail}"
            )

    def move_tail_diagonally(self):
        r2u1 = self.horizontal_distance() == 2 and self.vertical_distance() == 1
        r1u2 = self.horizontal_distance() == 1 and self.vertical_distance() == 2

        r2d1 = self.horizontal_distance() == 2 and self.vertical_distance() == -1
        r1d2 = self.horizontal_distance() == 1 and self.vertical_distance() == -2

        l2u1 = self.horizontal_distance() == -2 and self.vertical_distance() == 1
        l1u2 = self.horizontal_distance() == -1 and self.vertical_distance() == 2

        l2d1 = self.horizontal_distance() == -2 and self.vertical_distance() == -1
        l1d2 = self.horizontal_distance() == -1 and self.vertical_distance() == -2

        if r2u1 or r1u2:
            self.tail["x"] += 1
            self.tail["y"] += 1
        elif r2d1 or r1d2:
            self.tail["x"] += 1
            self.tail["y"] -= 1
        elif l2u1 or l1u2:
            self.tail["x"] -= 1
            self.tail["y"] += 1
        elif l2d1 or l1d2:
            self.tail["x"] -= 1
            self.tail["y"] -= 1

    def update_tail_visited(self):
        hsh = {"x": self.tail["x"], "y": self.tail["y"]}

        if hsh in self.tail_visited:
            return

        self.tail_visited.append(hsh)

    def move_pieces(self, line):
        direction = line.split()[0]
        steps = int(line.split()[1])

        def move_head(direction):
            if direction == "U":
                self.head["y"] += 1
            elif direction == "D":
                self.head["y"] -= 1
            elif direction == "R":
                self.head["x"] += 1
            elif direction == "L":
                self.head["x"] -= 1

        for _ in range(steps):
            move_head(direction)

            if self.is_adjacent():
                continue

            if self.is_inline():
                self.move_tail_straight()
            elif self.is_diagonal():
                self.move_tail_diagonally()
            elif self.too_far():
                raise ValueError(
                    f"Head {self.head} has got away from tail {self.tail}")
            else:
                raise ValueError("Unrecognised error")

            self.update_tail_visited()
