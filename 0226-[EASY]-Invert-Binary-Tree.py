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
        Use a recursive approach. We process each node and
        recursively call the function on its children.

    Runtime:
        Need to process each node to invert children, so
        runtime of O(n).

    Memory:
        O(1) auxiliary space, so constant memory solution.

        Although note that call stack is O(log n) in the
        best case for a balanced binary tree (root to leaf
        path is log n) and O(n) in the worst case for an
        unbalanced tree.
    """

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


class Solution2:
    """
    Intuition:
        Iterative approach. Use a deque with DFS approach.

    Runtime:
        O(n) since each node is added to the queue and
        processed exactly once.

    Memory:
        We removed the need for a call stack since the
        solution is not recursive anymore.

        Need O(n) auxiliary space for the deque data struct.
        Thus, overall O(n) space.
    """

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        q = deque([root])

        while q:
            node = q.pop()
            node.left, node.right = node.right, node.left

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return root
