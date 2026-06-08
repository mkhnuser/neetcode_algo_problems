from queue import Queue
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True

        if root is None:
            return False

        # NOTE: OK, you know two roots.
        # 1. Traverse.
        # 2. When subroot is found, do:
        # a. Traverse this subtree and check for its substructure.

        q = Queue()
        q.put(root)
        while q.qsize():
            node = q.get()
            if node.val == subRoot.val:
                if self.check_structure_and_values(node, subRoot):
                    return True
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)

        return False

    def check_structure_and_values(
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
