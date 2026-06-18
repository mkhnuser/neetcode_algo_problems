from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # NOTE: Handle the initial root.
        if root is None:
            return False

        return self.has_path_sum(root, targetSum, 0)

    def has_path_sum(
        self,
        root: TreeNode | None,
        targetSum: int,
        current_summation: int,
    ) -> bool:
        if root is None:
            return False

        current_summation = root.val + current_summation
        if root.left is None and root.right is None and current_summation == targetSum:
            return True

        return self.has_path_sum(
            root.left,
            targetSum,
            current_summation,
        ) or self.has_path_sum(
            root.right,
            targetSum,
            current_summation,
        )
