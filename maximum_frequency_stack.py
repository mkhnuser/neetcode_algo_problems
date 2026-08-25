class FreqStack:
    def __init__(self) -> None:
        self.counts = {}
        self.max_count = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        val_count = 1 + self.counts.get(val, 0)
        self.counts[val] = val_count

        if val_count > self.max_count:
            self.max_count = val_count
            self.stacks[val_count] = []

        self.stacks[val_count].append(val)

    def pop(self) -> int:
        output = self.stacks[self.max_count].pop()
        self.counts[output] -= 1

        if not self.stacks[self.max_count]:
            self.max_count -= 1

        return output
