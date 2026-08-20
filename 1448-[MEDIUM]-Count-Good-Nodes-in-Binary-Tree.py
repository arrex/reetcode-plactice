from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    """
    Intuition:
        We simply traverse the graph iteratively by storing the node as well as the
        maxVal encountered in the path as a tuple in the queue. This way,
        whenever we process the node's children, we can check if they are good or
        not by comparing their respective value to the maxVal in the path.
        We can also then compute the new maxVal in the path and continue
        until we have processed all nodes in the tree.

    Runtime:
        O(n) where n is the number of nodes in the tree.

    Memory:
        O(n) where n is the number of nodes in the tree in case of an
        unbalanced tree.
    """

    def goodNodes(self, root: TreeNode) -> int:
        numGood = 0
        # Encode as (node, maxVal) where
        # maxVal is the greatest val encountered so far
        q = deque([(root, root.val)])

        while q:
            node, maxVal = q.popleft()

            # Check if good
            if node.val >= maxVal:
                numGood += 1

            # Compute new maximum value in path
            maxVal = max(node.val, maxVal)

            if node.left:
                q.append((node.left, maxVal))

            if node.right:
                q.append((node.right, maxVal))

        return numGood


class Solution2:
    """
    Intuition:
        Same as Solution1, but with a recursive approach and a non-local
        instance variable.

    Runtime:
        O(n) -> each node processed once.

    Memory:
        Call stack of size O(h) which is O(log n) in best case and O(n)
        in worst case.
    """

    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0

        def dfs(node: TreeNode, maxVal: int) -> None:
            if not node:
                return

            if node.val >= maxVal:
                self.good += 1

            maxVal = max(maxVal, node.val)

            dfs(node.left, maxVal)
            dfs(node.right, maxVal)

        dfs(root, root.val)
        return self.good
