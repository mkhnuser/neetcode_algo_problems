class MinStack:
    def __init__(self):
        self.items = []
        self.min_items = []

    def push(self, val: int) -> None:
        if not self.min_items:
            self.min_items.append(val)
        else:
            self.min_items.append(min(val, self.min_items[-1]))

        self.items.append(val)

    def pop(self) -> None:
        self.min_items.pop()
        self.items.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.min_items[-1]
