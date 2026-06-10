from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.traverse_in_order(root, output)
        return output

    def traverse_in_order(self, root, output):
        if not root:
            return None
        self.traverse_in_order(root.left, output)
        output.append(root.val)
        self.traverse_in_order(root.right, output)


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        output = []

        current = root
        stack = []

        while current or stack:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                output.append(current.val)
                current = current.right

        return output
