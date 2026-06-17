from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(
        self,
        root: Optional[TreeNode],
        target: int,
    ) -> Optional[TreeNode]:
        if root is None:
            return None

        return self.recurse_deletion(root, target)

    def recurse_deletion(self, root: TreeNode | None, target: int) -> TreeNode | None:
        if root is None:
            return None

        root.left = self.recurse_deletion(root.left, target)
        root.right = self.recurse_deletion(root.right, target)

        if root.left is None and root.right is None and root.val == target:
            return None

        return root
