from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.recurse(root, output)
        return output

    def recurse(self, root: Optional[TreeNode], output: list[int]) -> None:
        if not root:
            return

        self.recurse(root.left, output)
        self.recurse(root.right, output)
        output.append(root.val)
