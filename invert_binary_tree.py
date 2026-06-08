from typing import Optional
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        self.invert_in_bfs_manner(root)
        return root

    def invert_in_bfs_manner(self, root: TreeNode) -> None:
        q = Queue()
        q.put(root)

        while q.qsize():
            node = q.get()
            left_child = node.left
            right_child = node.right

            node.left = right_child
            node.right = left_child

            if left_child:
                q.put(left_child)
            if right_child:
                q.put(right_child)

    def invert_in_dfs_manner(self, root: TreeNode) -> None:
        left_child = root.left
        right_child = root.right

        root.left = right_child
        root.right = left_child

        if left_child:
            self.invert_in_dfs_manner(left_child)
        if right_child:
            self.invert_in_dfs_manner(right_child)
