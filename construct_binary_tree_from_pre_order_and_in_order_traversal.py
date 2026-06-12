from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None

        # NOTE:
        # pre = current node first, in = left node first.
        root_val = preorder[0]
        root = TreeNode(root_val)
        root_val_index = inorder.index(root_val)
        root.left = self.buildTree(
            preorder[1 : root_val_index + 1],
            inorder[:root_val_index],
        )
        root.right = self.buildTree(
            preorder[root_val_index + 1 :],
            inorder[root_val_index + 1 :],
        )
        return root
