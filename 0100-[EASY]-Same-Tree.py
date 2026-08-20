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
        Recursive approach taken here. Comparisons are intuitive. Traverse the tree
        until we reach the leaf nodes.

    Runtime:
        O(n) -> Need to process each pair of nodes once.

    Memory:
        O(n) -> Stack trace will take O(h) memory where h is the height of the tree.
        In the best case, h = log(n) since the tree is balanced. In the worst case,
        h = n if the tree is unbalanced.
    """

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (p and not q) or (not p and q) or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class Solution2:
    """
    Intuition:
        Iterative approach. Same intuition as Solution1, but use a queue to store
        nodes.

    Runtime:
        O(n) -> One pass over each node for comparisons.

    Memory:
        O(n) -> In the worst case, the largest layer of the tree will be the deepest
        one. This layer will contain at most around half the nodes of the tree,
        meaning the width we obtain is O(w) where w = n / 2 which simplifies to O(n).
    """

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p, q)])

        while queue:
            for _ in range(len(queue)):
                n1, n2 = queue.popleft()

                if not n1 and not n2:
                    continue
                elif (n1 and not n2) or (not n1 and n2) or n1.val != n2.val:
                    return False

                queue.append((n1.left, n2.left))
                queue.append((n1.right, n2.right))

        return True
