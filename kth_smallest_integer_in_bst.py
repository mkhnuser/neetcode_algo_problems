from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        in_order_traversal_array = []
        self.obtain_in_order_traversal(root, in_order_traversal_array)
        return in_order_traversal_array[k - 1].val

    def obtain_in_order_traversal(
        self,
        root: Optional[TreeNode],
        output: list[TreeNode],
    ) -> list[TreeNode] | None:
        if root is None:
            return None

        self.obtain_in_order_traversal(root.left, output)
        output.append(root)
        self.obtain_in_order_traversal(root.right, output)
