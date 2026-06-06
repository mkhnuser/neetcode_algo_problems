from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_length = self.get_list_length(head)
        number_of_nodes_to_skip = list_length - n

        if number_of_nodes_to_skip == 0:
            return head.next

        c = 0
        h = head

        while h:
            c += 1
            if c == number_of_nodes_to_skip:
                if h.next is not None:
                    h.next = h.next.next
                else:
                    # NOTE: One node deletion case.
                    return None

            h = h.next

        return head

    def get_list_length(self, head) -> int:
        c = 0

        while head:
            c += 1
            head = head.next

        return c


def print_list(head):
    while head:
        print(head.val)
        head = head.next


def test():
    zero = ListNode(val=0)
    one = ListNode(val=1)
    two = ListNode(val=2)

    zero.next = one
    one.next = two

    sol = Solution()
    new_head = sol.removeNthFromEnd(zero, 1)
    print_list(new_head)

    ###

    zero = ListNode(val=0)
    one = ListNode(val=1)
    two = ListNode(val=2)

    zero.next = one
    one.next = two

    sol = Solution()
    new_head = sol.removeNthFromEnd(zero, 2)
    print_list(new_head)

    ###

    zero = ListNode(val=0)
    one = ListNode(val=1)
    two = ListNode(val=2)

    zero.next = one
    one.next = two

    sol = Solution()
    new_head = sol.removeNthFromEnd(zero, 3)
    print_list(new_head)


if __name__ == "__main__":
    test()
