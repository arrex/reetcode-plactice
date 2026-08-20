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
        Just iterate through each node and check if its value falls within
        defined range. Brute force approach.

    Notes:
        - Search space can be reduced since we are given a BST!
    """

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        q = deque([root])
        rangeSum = 0

        while q:
            node = q.popleft()

            if low <= node.val <= high:
                rangeSum += node.val

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return rangeSum


class Solution2:
    """
    Intuition:
        The key here is to notice that we are working with a BST. Therefore, rather
        than processing every node in the tree, we can be more selective on which
        nodes we add to the queue depending on their value.

        For example, if a node's value is less than the lower boundary, then we know
        that all elements in its left subtree will also be less than the lower boundary
        by default. Therefore, if the current node's value is less than the lower
        boundary, we only care about processing elements in its right subtree.

        A similar argument can be made about the right subtree. If an node's value is
        greater than the upper boundary, the forget about all the elements in its
        right subtree and only focus on elements in its left subtree.

    Notes:
        - More efficient since reduced search space
    """

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        q = deque([root])
        rangeSum = 0

        while q:
            node = q.popleft()

            if low <= node.val <= high:
                rangeSum += node.val

            if node.left and node.val >= low:
                q.append(node.left)

            if node.right and node.val <= high:
                q.append(node.right)

        return rangeSum
