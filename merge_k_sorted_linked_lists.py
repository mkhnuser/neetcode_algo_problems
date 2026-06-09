import heapq
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class NodeWrapper:
    def __init__(self, node: ListNode) -> None:
        self.node = node

    def __le__(self, other) -> None:
        return self.node.val <= other.node.val

    def __lt__(self, other) -> None:
        return self.node.val < other.node.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # return self.solve_using_min_heap(lists)
        return self.solve_using_mapping(lists)

    def solve_using_mapping(
        self,
        lists: List[Optional[ListNode]],
    ) -> Optional[ListNode]:
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

    def solve_using_min_heap(
        self,
        lists: List[Optional[ListNode]],
    ) -> Optional[ListNode]:
        if not lists:
            return None

        heap = []
        dummy_node = ListNode(-1)

        for node in lists:
            if node is not None:
                wrapper = NodeWrapper(node)
                heapq.heappush(heap, wrapper)

        h = dummy_node

        while heap:
            min_wrapper = heapq.heappop(heap)
            min_node = min_wrapper.node
            next_node = min_node.next

            if next_node is not None:
                wrapper = NodeWrapper(next_node)
                heapq.heappush(heap, wrapper)

            h.next = min_node
            h = h.next

        return dummy_node.next
