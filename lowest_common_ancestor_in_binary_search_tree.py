class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self,
        root: TreeNode,
        p: TreeNode,
        q: TreeNode,
    ) -> TreeNode:
        path_to_p = []
        self.find_path(root, p, path_to_p)
        path_to_q = []
        self.find_path(root, q, path_to_q)
        assert path_to_p
        assert path_to_q

        path_to_p_value_set = {node.val for node in path_to_p}
        for node in reversed(path_to_q):
            if node.val in path_to_p_value_set:
                return node

    def find_path(
        self,
        root: TreeNode | None,
        node: TreeNode,
        path: list[TreeNode],
    ) -> list[TreeNode]:
        if root is None:
            return []

        path.append(root)

        if root.val < node.val:
            return self.find_path(root.right, node, path)
        elif root.val > node.val:
            return self.find_path(root.left, node, path)
        else:
            return path


class Solution:
    def lowestCommonAncestor(
        self,
        root: TreeNode,
        p: TreeNode,
        q: TreeNode,
    ) -> TreeNode:
        current = root

        while current:
            if p.val > current.val and q.val > current.val:
                current = current.right
            elif p.val < current.val and q.val < current.val:
                current = current.left
            else:
                return current
