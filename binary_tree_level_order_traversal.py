from typing import List, Optional
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []

        if root is None:
            return output

        q = Queue()
        q.put(root)
        level_array = []

        while q.qsize():
            for _ in range(q.qsize()):
                current = q.get()
                level_array.append(current.val)
                if current.left:
                    q.put(current.left)
                if current.right:
                    q.put(current.right)

            output.append(level_array)
            level_array = []

        return output


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []

        if root is None:
            return output

        def dfs(root, depth):
            if not root:
                return
            if len(output) == depth:
                output.append([])
            output[depth].append(root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 0)

        return output
