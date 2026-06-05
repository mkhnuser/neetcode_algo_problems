class TimeMap:
    def __init__(self):
        self.data = []

    def set(self, key: str, value: str, timestamp: int) -> None:
        # NOTE: alice, happy, 1. becomes (alice, 1, happy).
        self.data.append((key, timestamp, value))
        self.data.sort()

    def get(self, key: str, timestamp: int) -> str:
        first_key_index = self.find_first_key_index(key)
        last_key_index = self.find_last_key_index(key)

        if first_key_index is None or last_key_index is None:
            return ""

        # NOTE: Find the last timestamp_prev <= timestamp and return its associated value.
        return self.find_value(
            self.data[first_key_index : last_key_index + 1],
            timestamp,
        )

    def find_value(self, slice, timestamp) -> str:
        lower_bound = 0
        upper_bound = len(slice) - 1
        output = ""

        while lower_bound <= upper_bound:
            middle_index = (lower_bound + upper_bound) // 2
            tuple_ = slice[middle_index]
            key, t, value = tuple_

            if t > timestamp:
                # NOTE: Search to the left.
                upper_bound = middle_index - 1
            else:
                # NOTE: t <= timestamp.
                output = value
                lower_bound = middle_index + 1

        return output

    def find_first_key_index(self, key: str) -> int | None:
        lower_bound = 0
        upper_bound = len(self.data) - 1
        output = None

        while lower_bound <= upper_bound:
            middle_index = (lower_bound + upper_bound) // 2
            tuple_ = self.data[middle_index]
            k, t, value = tuple_

            if k == key:
                output = middle_index
                upper_bound = middle_index - 1
            elif k < key:
                # NOTE: Search the key to the right.
                lower_bound = middle_index + 1
            else:
                # NOTE: Search the key to the left.
                upper_bound = middle_index - 1

        return output

    def find_last_key_index(self, key: str) -> int | None:
        lower_bound = 0
        upper_bound = len(self.data) - 1
        output = None

        while lower_bound <= upper_bound:
            middle_index = (lower_bound + upper_bound) // 2
            tuple_ = self.data[middle_index]
            k, t, value = tuple_

            if k == key:
                output = middle_index
                lower_bound = middle_index + 1
            elif k < key:
                # NOTE: Search the key to the right.
                lower_bound = middle_index + 1
            else:
                # NOTE: Search the key to the left.
                upper_bound = middle_index - 1

        return output
