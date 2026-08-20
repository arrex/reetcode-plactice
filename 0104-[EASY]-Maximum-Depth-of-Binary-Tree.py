from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    """
    Intuition:
        Use a recursive approach with a base case and a recursive step.

    Runtime:
        O(n) since we need to process each node once.

    Memory:
        O(1) auxiliary space.

        Call stack is O(n) in the worst case for an unbalanced tree.

        So overall constant auxiliary memory, but noteworthy to look
        at how call stack scales.
    """

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class Solution2:
    """
    Intuition:
        This problem is fairly straightforward. He simply use either BFS or DFS to
        process each node in the binary tree and determine if its depth is the
        greatest.

    Runtime:
        O(n) where n is the number of nodes in the binary tree

    Memory:
        O(n) where n is the number of nodes in the binary tree
    """

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Encode as (node, depth)
        q = deque([(root, 1)])
        maxDepth = 0

        while q:
            node, depth = q.popleft()

            maxDepth = max(maxDepth, depth)

            if node.left:
                q.append((node.left, depth + 1))

            if node.right:
                q.append((node.right, depth + 1))

        return maxDepth
