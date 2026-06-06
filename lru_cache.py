from typing import MutableMapping


class Node:
    def __init__(
        self,
        value: int,
        next_node: "Node | None" = None,
        prev_node: "Node | None" = None,
    ) -> None:
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.key_to_node_mapping: MutableMapping[int, Node] = {}
        self.node_to_key_mapping: MutableMapping[Node, int] = {}
        self.head: Node | None = None
        self.tail: Node | None = None
        self.list_length: int = 0

    def get(self, key: int) -> int:
        node_to_return = self.key_to_node_mapping.get(key)

        if node_to_return is None:
            return -1

        self.detach(node_to_return)
        self.insert_at_head(node_to_return)
        return node_to_return.value

    def put(self, key: int, value: int) -> None:
        # NOTE: Case 1, the node is present.
        if key in self.key_to_node_mapping:
            node_to_update = self.key_to_node_mapping[key]
            node_to_update.value = value
            self.detach(node_to_update)
            self.insert_at_head(node_to_update)
            return

        # NOTE: Case 2, the node is not present.
        node = Node(value=value)
        self.key_to_node_mapping[key] = node
        self.node_to_key_mapping[node] = key

        if self.list_length >= self.capacity:
            assert self.tail is not None  # NOTE: capacity is at least one.
            tail = self.tail
            self.detach(tail)
            key_to_delete = self.node_to_key_mapping[tail]
            del self.key_to_node_mapping[key_to_delete]
            del self.node_to_key_mapping[tail]
            self.list_length -= 1

        self.insert_at_head(node)
        self.list_length += 1

    def insert_at_head(self, node):
        node.prev_node = None
        node.next_node = self.head

        if self.head:
            self.head.prev_node = node
        else:
            self.tail = node

        self.head = node

    def detach(self, node):
        if node.prev_node:
            node.prev_node.next_node = node.next_node
        else:
            self.head = node.next_node

        if node.next_node:
            node.next_node.prev_node = node.prev_node
        else:
            self.tail = node.prev_node

        node.prev_node = None
        node.next_node = None


def test_one():
    lru_cache = LRUCache(2)
    lru_cache.put(1, 10)  # ;  // cache: {1=10}
    print(lru_cache.get(1))  # ;      // return 10
    lru_cache.put(2, 20)  # ;  // cache: {1=10, 2=20}
    lru_cache.put(3, 30)  # ;  // cache: {2=20, 3=30}, key=1 was evicted
    print(lru_cache.get(2))  # ;      // returns 20
    print(lru_cache.get(1))  # ;      // return -1 (not found)


def test_two():
    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    print(lru_cache.get(1))
    lru_cache.put(3, 3)
    print(lru_cache.get(2))


if __name__ == "__main__":
    test_one()
    test_two()
