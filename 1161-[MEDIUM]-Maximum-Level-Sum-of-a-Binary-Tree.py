from collections import defaultdict, deque
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
        Use BFS to process all nodes. For each element in the queue, also store
        the level. To track sums, we store the level as the key in a hashmap and
        the sum value as the value.

    Notes:
        Need extra loop overhead to fetch level with max sum.

        Constraints specify that root will never be empty. Guarantee at least 1
        node in tree.
    """

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Key = level, value = sum
        map = defaultdict(int)
        q = deque([(root, 1)])

        while q:
            node, lvl = q.popleft()
            map[lvl] += node.val

            if node.left:
                q.append((node.left, lvl + 1))

            if node.right:
                q.append((node.right, lvl + 1))

        res, maxSum = 0, -inf
        for key, val in map.items():
            if val > maxSum:
                res, maxSum = key, val

        return res


class Solution2:
    """
    Intuition:
        We can keep track of the result through a variable. Still, we use BFS, but
        since we know we are going level by level we can just process the entire
        level and then compare its sum to the current largest sum.

    Notes:
        Removed the extra memory needed for the hashmap.
    """

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res, currLvl, maxSum = 0, 0, -inf
        q = deque([(root)])

        while q:
            currSum = 0
            currLvl += 1

            for i in range(len(q)):
                node = q.popleft()
                currSum += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            if currSum > maxSum:
                res, maxSum = currLvl, currSum

        return res


class Solution3:
    """
    Intuition:
        Same intuition as previous solutions.

    Notes:
        Removed overhead of deque. Just use primitive arrays.
    """

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # Don't need this, but keep to prevent type checker from yelling
        if not root:
            return 0

        currLevel, resLevel, maxSum = 0, 0, -inf
        q = [root]

        while q:
            currLevel += 1
            currSum = 0
            nextQ = []

            for node in q:
                currSum += node.val

                if node.left:
                    nextQ.append(node.left)

                if node.right:
                    nextQ.append(node.right)

            if currSum > maxSum:
                resLevel, maxSum = currLevel, currSum

            q = nextQ

        return resLevel
