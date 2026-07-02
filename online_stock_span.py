class StockSpanner:
    def __init__(self):
        self.s = []

    def next(self, price: int) -> int:
        counter = 1

        temp_stack = []

        while self.s and self.s[-1] <= price:
            temp_stack.append(self.s.pop())
            counter += 1

        while temp_stack:
            self.s.append(temp_stack.pop())

        self.s.append(price)
        return counter


class StockSpanner:
    def __init__(self):
        self.s = []  # NOTE: We store (price, span) pairs.

    def next(self, price: int) -> int:
        span = 1

        while self.s and self.s[-1][0] <= price:
            span += self.s[-1][1]
            self.s.pop()

        self.s.append((price, span))
        return span
