from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.recurse(root))

    def recurse(
        self,
        root: TreeNode | None,
    ) -> tuple[int, int]:
        if not root:
            return (0, 0)

        L = self.recurse(root.left)
        R = self.recurse(root.right)

        # NOTE: Compute the profit with the root.
        profit_with_root = root.val
        profit_with_root += L[1]
        profit_with_root += R[1]

        # NOTE: Computer the profit without the root.
        profit_without_root = 0
        profit_without_root += max(L)
        profit_without_root += max(R)

        return (profit_with_root, profit_without_root)
