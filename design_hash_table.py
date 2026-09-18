class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next: Node | None = None


class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_size = 0
        self.table: list[Node | None] = [None] * self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self._hash_function(key)
        node = self.table[index]

        if node is None:
            self.table[index] = Node(key, value)
            self.current_size += 1
        else:
            prev = None

            while node:
                if node.key == key:
                    node.value = value
                    return
                prev, node = node, node.next

            assert isinstance(prev, Node)
            prev.next = Node(key, value)
            self.current_size += 1

        if self.current_size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self._hash_function(key)
        node = self.table[index]

        while node:
            if node.key == key:
                return node.value
            node = node.next

        return -1

    def remove(self, key: int) -> bool:
        index = self._hash_function(key)
        node = self.table[index]
        prev = None

        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.table[index] = node.next
                self.current_size -= 1
                return True

            prev, node = node, node.next

        return False

    def getSize(self) -> int:
        return self.current_size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table: list[Node | None] = [None] * new_capacity

        for node in self.table:
            while node:
                index = node.key % new_capacity
                if new_table[index] is None:
                    new_table[index] = Node(node.key, node.value)
                else:
                    new_node = new_table[index]
                    assert new_node
                    while new_node.next:
                        new_node = new_node.next
                    new_node.next = Node(node.key, node.value)
                node = node.next

        self.capacity = new_capacity
        self.table = new_table

    def _hash_function(self, key: int) -> int:
        return key % self.capacity
