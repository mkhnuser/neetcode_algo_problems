from typing import NamedTuple, List


class Node:
    def __init__(
        self,
        pair: "KeyValuePair",
        left: "Node | None" = None,
        right: "Node | None" = None,
    ) -> None:
        self.pair = pair
        self.left = left
        self.right = right


class KeyValuePair(NamedTuple):
    key: int
    val: int


class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        # NOTE: Override a key, value pair if it's already present.

        pair = KeyValuePair(key, val)
        node = Node(pair)

        if self.root is None:
            self.root = node
            return

        self._recurse_insertion(self.root, node)
        return

    def get(self, key: int) -> int:
        if self.root is None:
            return -1
        return self._recurse_get(self.root, key)

    def getMin(self) -> int:
        if self.root is None:
            return -1

        current = self.root
        while current.left is not None:
            current = current.left

        return current.pair.val

    def getMax(self) -> int:
        if self.root is None:
            return -1

        current = self.root
        while current.right is not None:
            current = current.right

        return current.pair.val

    def remove(self, key: int) -> None:
        if self.root is None:
            return

        self.root = self._recurse_removal(self.root, key)
        return

    def getInorderKeys(self) -> List[int]:
        # output = []
        # if self.root is None:
        #     return output
        #
        # self._recurse_get_in_order_keys(self.root, output)
        # return output
        if self.root is None:
            return []
        return self._get_in_order_keys_iteratively(self.root)

    def _recurse_insertion(self, root: Node | None, node: Node) -> Node | None:
        if root is None:
            return node

        if root.pair.key < node.pair.key:
            root.right = self._recurse_insertion(root.right, node)
        elif root.pair.key > node.pair.key:
            root.left = self._recurse_insertion(root.left, node)
        else:
            new_key_value_pair = KeyValuePair(key=node.pair.key, val=node.pair.val)
            root.pair = new_key_value_pair

        return root

    def _recurse_removal(self, root: Node | None, key: int) -> Node | None:
        if root is None:
            return None

        if root.pair.key < key:
            root.right = self._recurse_removal(root.right, key)
        elif root.pair.key > key:
            root.left = self._recurse_removal(root.left, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            successor = root.right
            while successor.left is not None:
                successor = successor.left

            new_key_value_pair = KeyValuePair(
                key=successor.pair.key,
                val=successor.pair.val,
            )
            root.pair = new_key_value_pair
            root.right = self._recurse_removal(
                root.right,
                successor.pair.key,
            )

        return root

    def _recurse_get(self, root: Node | None, key: int) -> int:
        if root is None:
            return -1

        if root.pair.key < key:
            return self._recurse_get(root.right, key)
        elif root.pair.key > key:
            return self._recurse_get(root.left, key)
        else:
            return root.pair.val

    def _recurse_get_in_order_keys(self, node: Node | None, output: list[int]) -> None:
        if node is None:
            return

        self._recurse_get_in_order_keys(node.left, output)
        output.append(node.pair.key)
        self._recurse_get_in_order_keys(node.right, output)

    def _get_in_order_keys_iteratively(self, root: Node) -> list[int]:
        c = root
        stack: list[Node] = []
        in_order_keys: list[int] = []

        while c or stack:
            if c:
                stack.append(c)
                c = c.left
            else:
                c = stack.pop()
                in_order_keys.append(c.pair.key)
                c = c.right

        return in_order_keys


class MyHashSet:
    def __init__(self):
        self.bst = TreeMap()

    def add(self, key: int) -> None:
        self.bst.insert(key, key)

    def remove(self, key: int) -> None:
        self.bst.remove(key)

    def contains(self, key: int) -> bool:
        return self.bst.get(key) != -1
