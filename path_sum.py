from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        return self.has_path_sum(root, 0, targetSum)

    def has_path_sum(
        self,
        node: Optional[TreeNode],
        s: int,
        target_sum: int,
    ) -> bool:
        if node is None:
            return False

        new_s = s + node.val

        if node.left is None and node.right is None:
            # NOTE: A leaf node has been reached.
            return s + node.val == target_sum

        return self.has_path_sum(
            node.left,
            new_s,
            target_sum,
        ) or self.has_path_sum(
            node.right,
            new_s,
            target_sum,
        )
