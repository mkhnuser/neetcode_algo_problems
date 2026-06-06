from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
    ) -> Optional[ListNode]:
        new_l1 = self.reverse_linked_list(l1)
        new_l2 = self.reverse_linked_list(l2)
        l1_num_string_repr = self.get_list_string_repr(new_l1)
        l2_num_string_repr = self.get_list_string_repr(new_l2)
        l1_num = int(l1_num_string_repr)
        l2_num = int(l2_num_string_repr)
        res = l1_num + l2_num
        res_str = str(res)
        dummy_head = ListNode(val=None)
        head = dummy_head

        for char in res_str:
            head.next = ListNode(val=int(char))
            head = head.next

        output_head = self.reverse_linked_list(dummy_head.next)
        return output_head

    def reverse_linked_list(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None
        if head.next is None:
            # NOTE: This is the new head.
            return head

        new_head = self.reverse_linked_list(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def get_list_string_repr(self, head: ListNode) -> str:
        string_repr = ""

        while head:
            string_repr += str(head.val)
            head = head.next

        return string_repr
