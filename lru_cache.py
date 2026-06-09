from typing import MutableMapping


class Node:
    def __init__(
        self,
        val: int,
        next: "Node | None" = None,
        prev: "Node | None" = None,
    ) -> None:
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node_mapping: MutableMapping[int, Node] = {}
        self.node_to_key_mapping: MutableMapping[Node, int] = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.key_to_node_mapping:
            node = self.key_to_node_mapping[key]
            # NOTE: Touch the node so that it does not get evicted.
            ##
            self.remove_from_the_list(node)
            self.move_to_the_head(node)
            ##
            #
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node_mapping:
            node = self.key_to_node_mapping[key]
            node.val = value
            self.remove_from_the_list(node)
            self.move_to_the_head(node)
            return

        node = Node(val=value)

        if len(self.key_to_node_mapping) >= self.capacity:
            assert self.tail is not None  # NOTE: Capacity is at least 1.

            lru_node = self.tail
            self.remove_from_the_list(lru_node)
            lru_node_key = self.node_to_key_mapping[lru_node]
            del self.key_to_node_mapping[lru_node_key]
            del self.node_to_key_mapping[lru_node]

        self.move_to_the_head(node)
        self.key_to_node_mapping[key] = node
        self.node_to_key_mapping[node] = key

    def remove_from_the_list(self, node: Node) -> None:
        if node is self.head:
            self.head = node.next
        if node is self.tail:
            self.tail = node.prev

        if node.next is not None:
            node.next.prev = node.prev
        if node.prev is not None:
            node.prev.next = node.next

        node.next = None
        node.prev = None

    def move_to_the_head(self, node) -> None:
        if self.head is None:
            self.tail = node
        else:
            prev_head = self.head
            node.next = prev_head
            prev_head.prev = node

        self.head = node
