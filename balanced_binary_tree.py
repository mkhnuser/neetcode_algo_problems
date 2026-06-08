from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.recurse_solution(root)[0]

    def recurse_solution(self, root: Optional[TreeNode]) -> tuple[bool, int]:
        if root is None:
            # NOTE: (is_balanced, height).
            return (True, -1)
        if root.left is None and root.right is None:
            return (True, 0)

        is_left_balanced, left_height = self.recurse_solution(root.left)
        is_right_balanced, right_height = self.recurse_solution(root.right)
        is_currently_balanced = abs(left_height - right_height) <= 1

        return (
            is_left_balanced and is_right_balanced and is_currently_balanced,
            max(left_height, right_height) + 1,
        )
