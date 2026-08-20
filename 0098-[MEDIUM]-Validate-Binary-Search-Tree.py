from collections import deque
from math import inf
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
        We can reason each node as having a left and right bound. The
        node's value has to fall within that specific bound.

        Initial condition: at the root, there are no bound constraints
        yet (we will build them as we go), so the left and right bounds
        are respectively -inf and inf.

        As we traverse the tree, we can enforce new constraints on the
        child nodes.

        The child composing the left subtree will need to enforce an
        upper bound equal to the current node's value sin it and all
        of its children must have values less than the current node.

        The child composing the right subtree will need to enforce a
        lower bound equal to the current node's value since it and all
        of its children must have values greater than the current node.

        This solution takes a recursive approach in solving the problem
        with the outlined ideas.

    Runtime:
        Each node has to be processed once to validate the BST, so O(n)
        runtime.

    Memory:
        The call stack of the helper dfs function has size O(h) where h
        is the height of the tree. Thus, we have O(log n) in the best case
        and O(n) in the worst case with an unbalanced tree.
    """

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode, l: int, r: int):
            if not node:
                return True

            # violates BST property
            if node.val <= l or node.val >= r:
                return False

            return dfs(node.left, l, node.val) and dfs(node.right, node.val, r)

        return dfs(root, -inf, inf)


class Solution2:
    """
    Intuition:
        Same idea as Solution1, but with an iterative approach.

    Runtime:
        Same as Solution1.

    Memory:
        Same as Solution1. deque 'simulates' call stack.
    """

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        q = deque([(root, -inf, inf)])

        while q:
            node, l, r = q.pop()

            if node.val <= l or node.val >= r:
                return False

            if node.left:
                q.append((node.left, l, node.val))

            if node.right:
                q.append((node.right, node.val, r))

        return True
