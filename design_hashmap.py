class Node:
    def __init__(
        self,
        key: int,
        val: int,
        next: "Node | None" = None,
    ) -> None:
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:
    def __init__(self, bucket_size: int = 10**4) -> None:
        self.bucket_size = bucket_size
        self.mapping = [Node(-1, -1) for _ in range(self.bucket_size)]

    def put(self, key: int, value: int) -> None:
        c = self.mapping[key % len(self.mapping)]

        while c.next:
            if c.next.key == key:
                c.next.val = value
                return
            c = c.next

        c.next = Node(key, value)

    def get(self, key: int) -> int:
        c = self.mapping[key % len(self.mapping)]

        while c.next:
            if c.next.key == key:
                return c.next.val
            c = c.next

        return -1

    def remove(self, key: int) -> None:
        c = self.mapping[key % len(self.mapping)]

        while c.next:
            if c.next.key == key:
                c.next = c.next.next
                return
            c = c.next
