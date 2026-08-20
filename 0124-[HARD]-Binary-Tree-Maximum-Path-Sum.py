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
        The maximum path sum can be found by considering all possible combinations
        of paths. Each node can either be the start of the path, somewhere in the
        middle of the path or the end of the path.

        We can use a depth-first search (DFS) approach to traverse the tree and
        calculate the maximum path sum at each node.

        At each node, we calculate the maximum path sum that includes the node as
        the start, middle or end of the path. We then update the maximum path sum
        seen so far.

        Note: this solution was written without consulting the solution... it can
        be polished further.

    Runtime:
        Each node is processed once in a bottom-up manner. Therefore, we have
        a linear runtime of O(n).

    Memory:
        Call stack requires O(h) where h is the height of the tree. In the
        best case, h is log(n). In the worst case h is n with an unbalanced
        tree.

        Overall O(n) memory.
    """

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = -inf

        def dfs(node):
            if not node:
                return -inf

            left = dfs(node.left)
            right = dfs(node.right)

            combinations = [
                left,
                right,
                node.val,
                left + node.val,
                right + node.val,
                left + node.val + right,
            ]
            highest = max(combinations)

            self.maxSum = max(self.maxSum, highest)

            return max([left + node.val, right + node.val, node.val])

        dfs(root)
        return int(self.maxSum)


class Solution2:
    """
    Intuition:
        Same intuition as Solution1, but with a more concise & polished implementation.

    Runtime:
        Same as Solution1.

    Memory:
        Same as Solution1.
    """

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = root.val

        def dfs(node):
            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            path = left + node.val + right

            self.maxSum = max(self.maxSum, path)
            return node.val + max(left, right)

        dfs(root)
        return self.maxSum


class Solution3:
    """
    Intuition:
        Same as Solution1. Iterative DFS approach.

    Runtime:
        Same as Solution1. O(n) time.

    Memory:
        Same as Solution1. O(n) space. Only difference is we mimic
        call stack with an array stack.
    """

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        maxPaths = {}

        node = root
        last = None
        stack = []

        while stack or node:
            # go left
            if node:
                stack.append(node)
                node = node.left
            # hit bottom
            else:
                node = stack[-1]

                if not node.right or node.right == last:
                    stack.pop()

                    left = max(maxPaths.get(node.left, 0), 0)
                    right = max(maxPaths.get(node.right, 0), 0)
                    path = left + node.val + right

                    res = max(res, path)

                    maxPaths[node] = node.val + max(left, right)

                    last = node
                    node = None
                else:
                    node = node.right

        return res
