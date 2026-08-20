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
        We essentially need to find the longest path between any 2 nodes
        in the tree. To do this, we can define a function to compute the
        maximum path of its right and left child recursively.

        Note that the diameter does not necessarily include the root.

    Runtime:
        Each node processed once, so O(n) runtime.

    Memory:
        O(1) auxiliary memory.

        O(n) memory for call stack in worst case if tree is unbalanced.

        Overall O(n) memory.
    """

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def findDepth(node):
            if not node:
                return 0

            left = findDepth(node.left)
            right = findDepth(node.right)

            self.diameter = max(self.diameter, left + right)

            return max(left, right) + 1

        findDepth(root)

        return self.diameter


class Solution2:
    """
    Intuition:
        Iterative approach. We simulate the call stack
        using the stack data structure.

    Runtime:
        Same runtime as recursive soln, overall O(n).

    Memory:
        Call stack simulated by stack array. Overall O(n).
    """

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        node = root  # curr node
        last = None  # last fully processed node
        stack = []  # simulate call stack
        depths = {}  # {node: depth}
        maxDiam = 0  # result

        while node or stack:
            # traverse down left subtree
            if node:
                stack.append(node)
                node = node.left
            # hit end of left subtree
            else:
                # peek top of stack
                node = stack[-1]

                # if peeked node has no right subtree or right subtree already processed
                if not node.right or last == node.right:
                    # remove node
                    stack.pop()

                    # compute diameter
                    dL = depths.get(node.left, 0)
                    dR = depths.get(node.right, 0)
                    currDiam = dL + dR

                    # update max diameter
                    maxDiam = max(maxDiam, currDiam)

                    # update depth mapping of current node
                    depths[node] = max(dL, dR) + 1
                    # last processed node is now curr node
                    last = node
                    # set curr node to None to force stack pop on next iter
                    node = None
                else:
                    # traverse down right subtree
                    node = node.right

        return maxDiam
