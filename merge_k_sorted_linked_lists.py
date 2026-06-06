from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        # WARNING: Some heads might be Nones at this point.
        mapping = {}
        for i, list_head in enumerate(lists):
            if list_head is not None:
                mapping[i] = list_head

        # NOTE: No heads are Nones at this point.
        dummy_head = ListNode(val=-1)
        pointer = dummy_head

        while mapping:
            index_to_node = list(mapping.items())
            min_index, min_node = min(index_to_node, key=lambda item: item[1].val)

            pointer.next = min_node
            pointer = pointer.next

            if min_node.next is not None:
                mapping[min_index] = min_node.next
            else:
                del mapping[min_index]

        return dummy_head.next
