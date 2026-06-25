from queue import Queue
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        q = Queue()
        q.put(node)
        old_to_new = {}
        old_to_new[node] = Node(val=node.val)

        while q.qsize() > 0:
            n = q.get()
            for g in n.neighbors:
                if g not in old_to_new:
                    old_to_new[g] = Node(val=g.val)
                    q.put(g)
                old_to_new[n].neighbors.append(old_to_new[g])

        return old_to_new[node]
