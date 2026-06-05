from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return

        list_length = self.find_list_length(head)

        if list_length == 1:
            return

        left_pointer = head
        right_pointer = self.locate_last_node(head)
        self.create_prev_refs(head)

        head_pointer = ListNode()
        num_of_iterations = list_length
        current_pointer = left_pointer
        c = 1

        while c <= num_of_iterations:
            head_pointer.next = current_pointer

            if current_pointer is left_pointer:
                left_pointer = left_pointer.next
                current_pointer = right_pointer
            else:
                right_pointer = right_pointer.prev
                current_pointer = left_pointer

            head_pointer = head_pointer.next
            c += 1

        head_pointer.next = None

    def create_prev_refs(self, head: ListNode) -> None:
        h = head

        while h.next is not None:
            h.next.prev = h
            h = h.next

    def find_list_length(self, head: ListNode) -> int:
        c = 0
        h = head
        while h:
            c += 1
            h = h.next
        return c

    def locate_last_node(self, head: ListNode) -> ListNode:
        h = head
        while h.next is not None:
            h = h.next
        return h


def print_list(node):
    while node is not None:
        print(node.val)
        node = node.next


def test():
    zero = ListNode(val=0)

    sol = Solution()
    print("0")
    sol.reorderList(zero)

    print_list(zero)

    ###

    zero = ListNode(val=0)
    one = ListNode(val=1)

    zero.next = one

    sol = Solution()
    print("0 1")
    sol.reorderList(zero)

    print_list(zero)

    ###

    zero = ListNode(val=0)
    one = ListNode(val=1)
    two = ListNode(val=2)

    zero.next = one
    one.next = two

    sol = Solution()
    print("0 1 2")
    sol.reorderList(zero)

    print_list(zero)


if __name__ == "__main__":
    test()
