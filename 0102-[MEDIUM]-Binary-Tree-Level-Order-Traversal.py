from collections import defaultdict, deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    """
    Intuition:
        Build a dictionary where the key is the level and the value
        is an array contaning all nodes at that level. This solution
        illustrates a recursive approach.

    Runtime:
        Each node is processed at most once -> O(n) runtime.

    Memory:
        Call stack is O(h) memory where h is the height of the tree.
        In the worst case, the height is 'n' if we have an unbalanced
        tree.

        Dictionary is also O(n) since we store information about all
        nodes in it.

       Thus, overall memory complexity is O(n).
    """

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)

        def dfs(node, lvl):
            if not node:
                return

            levels[lvl].append(node.val)

            dfs(node.left, lvl + 1)
            dfs(node.right, lvl + 1)

        dfs(root, 0)
        return list(levels.values())


class Solution2:
    """
    Intuition:
        Same intuition as Solutin1, except iterative approach.

    Runtime:
        Each node processed once. O(n) runtime like Solution1.

    Memory:
        Queue takes up at most O(n) space.

        Dictionary takes up at most O(n) space.

        Overall O(n) memory complexity.

    """

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = defaultdict(list)
        q = deque([(root, 0)])

        while q:
            node, lvl = q.popleft()
            levels[lvl].append(node.val)

            if node.left:
                q.append((node.left, lvl + 1))

            if node.right:
                q.append((node.right, lvl + 1))

        return list(levels.values())
