from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return None

        new_head, old_node_to_new_node_mapping = self.create_first_copy(head)
        self.update_random_pointers(new_head, old_node_to_new_node_mapping)
        return new_head

    def create_first_copy(self, head):
        old_node_to_new_node_mapping = {}
        # NOTE: 1 -> 44 -> 52.
        # dummy_node -> new 1 -> new 44 -> new 52.
        dummy_node = Node(-1)
        h = dummy_node

        while head is not None:
            val = head.val
            n = head.next
            r = head.random

            new_node = Node(val, n, r)
            old_node_to_new_node_mapping[head] = new_node

            h.next = new_node
            h = h.next
            head = head.next

        return dummy_node.next, old_node_to_new_node_mapping

    def update_random_pointers(self, head, old_node_to_new_node_mapping):
        while head:
            r_value = head.random
            if r_value is not None:
                head.random = old_node_to_new_node_mapping[r_value]
            head = head.next


def test():
    zero = Node(0)
    one = Node(1)
    two = Node(2)

    zero.next = one
    one.next = two

    sol = Solution()
    first_new_head = sol.copyRandomList(zero)


if __name__ == "__main__":
    test()
