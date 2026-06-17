from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        if root is None:
            return node

        # return self.recurse_insertion(root, node)
        return self.insert_iteratively(root, node)

    def recurse_insertion(self, root: TreeNode | None, node: TreeNode) -> TreeNode:
        if root is None:
            return node

        if root.val < node.val:
            root.right = self.recurse_insertion(root.right, node)
        else:
            root.left = self.recurse_insertion(root.left, node)

        return root

    def insert_iteratively(self, root: TreeNode, node: TreeNode) -> TreeNode:
        c = root

        while True:
            if node.val > c.val:
                if c.right is None:
                    c.right = node
                    return root
                c = c.right
            else:
                if c.left is None:
                    c.left = node
                    return root
                c = c.left
