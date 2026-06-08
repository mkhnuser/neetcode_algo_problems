from queue import Queue
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.solve_iteratively_with_bfs(p, q)

    def solve_recursively_with_dfs(
        self,
        p: Optional[TreeNode],
        q: Optional[TreeNode],
    ) -> bool:
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        assert p is not None
        assert q is not None

        # NOTE: At this point, both p and q are not None.
        if p.val != q.val:
            return False

        return self.solve_recursively_with_dfs(
            p.left,
            q.left,
        ) and self.solve_recursively_with_dfs(
            p.right,
            q.right,
        )

    def solve_iteratively_with_dfs(
        self,
        p: Optional[TreeNode],
        q: Optional[TreeNode],
    ) -> bool:
        stack = []
        stack.append((p, q))

        while stack:
            # NOTE: Consume the whole tree and check it at the same time.
            a, b = stack.pop()

            if not a and not b:
                continue

            if (not a or not b) or (a.val != b.val):
                return False

            stack.append((a.left, b.left))
            stack.append((a.right, b.right))

        return True

    def solve_iteratively_with_bfs(
        self,
        p: Optional[TreeNode],
        q: Optional[TreeNode],
    ) -> bool:
        p_queue = Queue()
        q_queue = Queue()
        p_queue.put(p)
        q_queue.put(q)

        while p_queue.qsize() > 0 and q_queue.qsize() > 0:
            a = p_queue.get()
            b = q_queue.get()

            if not a and not b:
                continue

            if (not a or not b) or (a.val != b.val):
                return False

            p_queue.put(a.left)
            q_queue.put(b.left)
            p_queue.put(a.right)
            q_queue.put(b.right)

        return p_queue.qsize() == 0 == q_queue.qsize()
