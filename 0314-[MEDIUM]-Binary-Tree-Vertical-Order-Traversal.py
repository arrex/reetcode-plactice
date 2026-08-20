from collections import defaultdict, deque
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
        We need to keep track of the column number of each node. Thus, we store in each
        element of the queue the node and its appropriate column value while performing
        a BFS.

        We guarantee left to right order by processing left children first.

        For the return value, we need to return the traversal in order of leftmost column
        to rightmost column. For that, we keep track of the leftmost column in minCol and
        the rightmost in maxCol. Since the column number is the key in our colMap, we
        simply iterate and append.
    """

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([(root, 0)])
        colMap = defaultdict(list)
        minCol, maxCol = 0, 0

        while q:
            node, col = q.popleft()
            colMap[col].append(node.val)

            if node.left:
                q.append((node.left, col - 1))

                minCol = min(minCol, col - 1)

            if node.right:
                q.append((node.right, col + 1))

                maxCol = max(maxCol, col + 1)

        res = []
        for i in range(minCol, maxCol + 1):
            res.append(colMap[i])

        return res
