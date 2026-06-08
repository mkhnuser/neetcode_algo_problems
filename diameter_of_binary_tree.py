from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # NOTE: Diameter = # of edges.
        return self.recurse_solution(root)[0]

    def recurse_solution(self, root: Optional[TreeNode]) -> tuple[int, int]:
        if root is None:
            # NOTE: (max_diameter, max_height).
            return (-1, -1)
        if root.left is None and root.right is None:
            # NOTE: The leaf node has been hit.
            return (0, 0)

        left_max_diameter, left_height = self.recurse_solution(root.left)
        right_max_diameter, right_height = self.recurse_solution(root.right)
        current_diameter = 2 + left_height + right_height
        max_diameter = max(current_diameter, left_max_diameter, right_max_diameter)
        return (max_diameter, max(left_height, right_height) + 1)
