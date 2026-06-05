from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:
        if list1 is None:
            # NOTE: list2 at this point is either None or a node.
            return list2
        if list2 is None:
            # NOTE: list1 at this point is either None or a node.
            return list1

        # NOTE: At this point, both list1 and list2 are not None and are actual nodes.
        pointer_one = list1
        pointer_two = list2

        if pointer_one.val <= pointer_two.val:
            head = pointer_one
            pointer_one = pointer_one.next
        else:
            head = pointer_two
            pointer_two = pointer_two.next

        first_node = head

        while pointer_one is not None and pointer_two is not None:
            if pointer_one.val <= pointer_two.val:
                c = pointer_one
                pointer_one = pointer_one.next
            else:
                c = pointer_two
                pointer_two = pointer_two.next

            head.next = c
            head = head.next

        while pointer_one is not None:
            head.next = pointer_one
            pointer_one = pointer_one.next
            head = head.next

        while pointer_two is not None:
            head.next = pointer_two
            pointer_two = pointer_two.next
            head = head.next

        return first_node
