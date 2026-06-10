from typing import List, Optional
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if root is None:
            return output

        q = Queue()
        q.put(root)

        while q.qsize():
            last_value = None

            for _ in range(q.qsize()):
                current = q.get()
                last_value = current.val
                if current.left:
                    q.put(current.left)
                if current.right:
                    q.put(current.right)

            output.append(last_value)
            last_value = None

        return output
