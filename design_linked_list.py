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


# NOTE: OK, node indexes are zero-based: 0 -> 1 -> 2.


class MyLinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.list_length: int = 0

    def get(self, index: int) -> int:
        current = self.head
        current_index = -1

        while current is not None:
            current_index += 1
            if current_index == index:
                return current.val

            current = current.next

        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)

        prev_head = self.head

        if prev_head is None:
            self.head = node
            self.tail = node
        else:
            node.next = prev_head
            prev_head.prev = node
            self.head = node

        self.list_length += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)

        prev_tail = self.tail

        if prev_tail is None:
            self.head = node
            self.tail = node
        else:
            prev_tail.next = node
            node.prev = prev_tail
            self.tail = node

        self.list_length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        if index > self.list_length:
            # NOTE: Invalid index.
            return
        if index == self.list_length:
            self.addAtTail(val)
            return

        # NOTE: At this point, 0 < index < self.list_length.
        # So, we add before the node at the index `index`.

        current = self.head
        current_index = -1

        while current is not None:
            current_index += 1
            if current_index == index:
                break

            current = current.next
        else:
            raise RuntimeError("Bang!")

        assert current is not None
        assert current.prev is not None

        node = Node(val)
        node.next = current
        node.prev = current.prev
        current.prev.next = node
        current.prev = node

        self.list_length += 1

    def deleteAtIndex(self, index: int) -> None:
        current = self.head
        current_index = -1

        while current is not None:
            current_index += 1
            if current_index == index:
                break

            current = current.next
        else:
            return  # NOTE: No break has been hit, so the passed index is invalid.

        if current is self.head:
            self.head = current.next
        if current is self.tail:
            self.tail = current.prev

        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev

        current.next = None
        current.prev = None

        self.list_length -= 1
