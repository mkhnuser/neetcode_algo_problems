from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # return self.recurse(root, float("-inf"))
        return self.bfs(root, float("-inf"))

    def recurse(
        self,
        node: TreeNode | None,
        path_maximum: float | int,
    ) -> int:
        if node is None:
            return 0

        res = 1 if node.val >= path_maximum else 0
        path_maximum = max(path_maximum, node.val)
        res += self.recurse(node.left, path_maximum)
        res += self.recurse(node.right, path_maximum)
        return res

    def bfs(
        self,
        node: TreeNode,
        path_maximum: float | int,
    ) -> int:
        res = 0
        q = Queue()
        path_maximum = float("-inf")
        q.put((node, path_maximum))

        while q.qsize():
            node, path_maximum = q.get()

            if node.val >= path_maximum:
                res += 1
            if node.left:
                q.put((node.left, max(node.val, path_maximum)))
            if node.right:
                q.put((node.right, max(node.val, path_maximum)))

        return res
