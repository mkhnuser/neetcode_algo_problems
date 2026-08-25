from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int,
    ) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        left_prev, cur = dummy_node, head

        for _ in range(left - 1):
            left_prev, cur = cur, cur.next

        prev = None

        for _ in range(right - left + 1):
            tmp_next = cur.next
            cur.next = prev
            prev, cur = cur, tmp_next

        left_prev.next.next = cur
        left_prev.next = prev

        return dummy_node.next
