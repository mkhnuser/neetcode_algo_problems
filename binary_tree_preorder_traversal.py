from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # output = []
        # self.recurse(root, output)
        # return output
        if root is None:
            return []

        output = []
        current = root
        stack = []

        while stack or current:
            if current:
                output.append(current.val)
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right

        return output

    def recurse(self, root: Optional[TreeNode], output: list[int]) -> None:
        if not root:
            return

        output.append(root.val)
        self.recurse(root.left, output)
        self.recurse(root.right, output)
