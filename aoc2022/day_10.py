"""Day 10"""


class Device:
    def __init__(self):
        self.cycles = 0
        self.x = [{"index": 0, "value": 1}]

    def x_value_during(self, index):
        hsh = next((hsh for hsh in self.x if hsh["index"] == index - 1), None)
        return hsh["value"] if hsh else "No Value Found"

    def x_value_after(self, index):
        hsh = next((hsh for hsh in self.x if hsh["index"] == index), None)
        return hsh["value"] if hsh else "No Value Found"

    def signal_strength_during(self, index):
        return self.x[index - 1]["value"] * index

    def signal_strength_after(self, index):
        return self.x[index]["value"] * index

    def increment_cycles_only(self):
        new_cycle = self.cycles + 1
        current_value = self.x[-1]["value"]
        hsh = {"index": new_cycle, "value": current_value}
        self.x.append(hsh)
        self.cycles += 1

    def increment_cycles_update_x(self, line):
        new_cycle = self.cycles + 1
        current_value = self.x[-1]["value"]

        string = line.split()[1]
        new_value = int(string)

        hsh = {"index": new_cycle, "value": current_value + new_value}
        self.x.append(hsh)
        self.cycles += 1

    def execute(self, line):
        if line == "noop":
            self.increment_cycles_only()

            return

        for i in range(2):
            if i == 0:
                self.increment_cycles_only()
            elif i == 1:
                self.increment_cycles_update_x(line)

    def sum_signal_strengths(self, index_ary):
        values = [self.signal_strength_during(index) for index in index_ary]
        return sum(values)

    def main(self, path):
        with open(path, "r") as file:
            lines = file.readlines()

        for line in lines:
            self.execute(line.strip())
