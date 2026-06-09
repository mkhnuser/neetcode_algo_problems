class BrowserHistory:
    def __init__(self, homepage: str):
        self.main_history = [homepage]
        self.forward_history = []

    def visit(self, url: str) -> None:
        self.main_history.append(url)
        self.forward_history.clear()

    def back(self, steps: int) -> str:
        # NOTE: We should always keep the homepage on history.
        while len(self.main_history) > 1 and steps > 0:
            self.forward_history.append(self.main_history.pop())
            steps -= 1
        return self.main_history[-1]

    def forward(self, steps: int) -> str:
        while self.forward_history and steps > 0:
            self.main_history.append(self.forward_history.pop())
            steps -= 1
        return self.main_history[-1]


class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.pointer = 0

    def visit(self, url: str) -> None:
        self.pointer += 1
        self.history = self.history[: self.pointer]
        self.history.append(url)

    def back(self, steps: int) -> str:
        self.pointer = max(0, self.pointer - steps)
        return self.history[self.pointer]

    def forward(self, steps: int) -> str:
        self.pointer = min(len(self.history) - 1, self.pointer + steps)
        return self.history[self.pointer]


class Node:
    def __init__(
        self,
        val: str,
        next: "Node | None" = None,
        prev: "Node | None" = None,
    ) -> None:
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory:
    def __init__(self, homepage: str) -> None:
        homepage_node = Node(homepage)
        self.pointer = homepage_node

    def visit(self, url: str) -> None:
        node = Node(url)
        node.prev = self.pointer
        self.pointer.next = node
        self.pointer = self.pointer.next

    def back(self, steps: int) -> str:
        while steps > 0 and self.pointer.prev:
            self.pointer = self.pointer.prev
            steps -= 1

        return self.pointer.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.pointer.next:
            self.pointer = self.pointer.next
            steps -= 1

        return self.pointer.val
