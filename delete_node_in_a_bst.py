from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        return self.recurse_deletion(root, key)

    def recurse_deletion(self, root: TreeNode | None, key: int) -> Optional[TreeNode]:
        if root is None:
            return root

        if key > root.val:
            root.right = self.recurse_deletion(root.right, key)
            return root
        elif key < root.val:
            root.left = self.recurse_deletion(root.left, key)
            return root
        else:
            # NOTE: root.val == key.
            if root.left is None and root.right is None:
                return None

            # NOTE: At least one child is present.
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            # NOTE: Precisely two children are present.
            # So, let's find a successor of root.
            c = root.right

            while c.left:
                c = c.left

            root.val = c.val
            root.right = self.recurse_deletion(root.right, c.val)
            return root
