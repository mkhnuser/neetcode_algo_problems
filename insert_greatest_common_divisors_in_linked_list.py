import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(
        self,
        head: Optional[ListNode],
    ) -> Optional[ListNode]:
        if head is None:
            return None

        current = head.next
        prev = head

        while current:
            gcd_val = math.gcd(prev.val, current.val)
            new_node = ListNode(gcd_val, next=current)
            prev.next = new_node
            prev = current
            current = current.next

        return head
