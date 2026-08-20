from collections import deque
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(
        self, val: int = 0, left: "Node" = None, right: "Node" = None, next: "Node" = None
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    """
    Intuition:
        We process the binary tree layer by layer. We go from right to left and use the 'prev' ptr
        to store the next pointer for the subsequent node.

    Runtime:
        O(n) -> We need to process each node once and set its next pointer.

    Memory:
        O(n) -> O(w) where w is the width of the largest layer. Here, it's the deepest layer since we
        are dealing with a perfect binary tree. Since the deepest layer contains roughly half the nodes
        of the tree, we can simplify O(n/2) to O(n).
    """

    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return None

        q = deque([root])

        while q:
            prev = None

            for _ in range(len(q)):
                node = q.pop()
                node.next = prev
                prev = node

                # order matters!
                if node.left and node.right:
                    q.appendleft(node.right)
                    q.appendleft(node.left)

        return root
