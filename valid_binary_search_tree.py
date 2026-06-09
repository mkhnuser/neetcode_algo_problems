from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # NOTE: The comparison is strict in this problem.
        return self.recurse_solution(
            root, lower_bound=float("-inf"), upper_bound=float("+inf")
        )

    def recurse_solution(
        self,
        root: Optional[TreeNode],
        lower_bound: float,
        upper_bound: float,
    ) -> bool:
        if root is None:
            return True

        is_left_subtree_valid = self.recurse_solution(
            root.left,
            lower_bound=lower_bound,
            upper_bound=root.val,
        )
        is_right_subtree_valid = self.recurse_solution(
            root.right,
            lower_bound=root.val,
            upper_bound=upper_bound,
        )
        is_current_node_within_bounds = (
            lower_bound < root.val and root.val < upper_bound
        )

        return (
            is_left_subtree_valid
            and is_current_node_within_bounds
            and is_right_subtree_valid
        )
