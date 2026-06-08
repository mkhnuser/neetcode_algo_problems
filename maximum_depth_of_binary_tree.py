from typing import Optional
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # NOTE: Depth = number of nodes.
        return self.solve_using_bfs(root)

    def solve_using_recursive_dfs(self, root) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def solve_using_bfs(self, root) -> int:
        if root is None:
            return 0

        q = Queue()
        q.put(root)
        level = 0

        while q.qsize():
            for _ in range(q.qsize()):  # NOTE: Process the whole level.
                node = q.get()
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            level += 1

        return level

    def solve_using_iterative_dfs_without_coloring(self, root) -> int:
        if root is None:
            return 0

        stack = []
        global_depth = 0
        # NOTE: (node, depth).
        stack.append((root, 1))

        while stack:
            node, current_depth = stack.pop()
            global_depth = max(global_depth, current_depth)

            if node.left:
                stack.append((node.left, current_depth + 1))
            if node.right:
                stack.append((node.right, current_depth + 1))

        return global_depth

    def solve_using_iterative_dfs_with_coloring(self, root) -> int:
        if root is None:
            return 0

        self.set_colors(root)
        stack = []
        stack.append(root)
        global_depth = 0
        current_depth = 0

        while stack:
            node = stack.pop()
            if node.secret_color == "white":
                node.secret_color = "gray"
                stack.append(node)

                current_depth += 1
                global_depth = max(global_depth, current_depth)

                if node.left and node.left.secret_color == "white":
                    stack.append(node.left)
                if node.right and node.right.secret_color == "white":
                    stack.append(node.right)

            elif node.secret_color == "gray":
                node.secret_color = "black"
                current_depth -= 1

        return global_depth

    def set_colors(self, root) -> None:
        if root is None:
            return None

        root.secret_color = "white"
        self.set_colors(root.left)
        self.set_colors(root.right)
