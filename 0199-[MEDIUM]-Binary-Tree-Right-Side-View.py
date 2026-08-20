from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Intuition:
        We perform a traversal layer by layer. At each layer,
        we append the rightmost element i.e. the last element
        in the queue.

    Runtime:
        Each node is processed at most once, so O(n) runtime.

    Memory:
        deque data structure takes at most O(n) memory.
    """

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        view = []

        while q:
            # Append rightmost elmt
            view.append(q[-1].val)

            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return view
