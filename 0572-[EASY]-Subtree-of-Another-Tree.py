from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Inuition:
        Traverse the tree from the root. At each node, check if the subtree
        starting at the current node is equivalent to the tree provided in
        subRoot.

    Runtime:
        Let the tree rooted at 'root' be t and the tree rooted at subRoot be
        s.

        We process each node in t once. Thus, the runtime would be O(m) where
        m is the number of nodes in t.

        For each node in t, we check if it is an equivalent tree as s. The
        runtime of isSameTree is O(n) where n is the number of nodes in s.

        Overall, the total runtime is O(m * n).

    Memory:
        The recursion depth is O(h) on avg where h is the height of the tree
        and O(n) in the worst case with a skewed tree.

        Here, if tree rooted at 'root' has m nodes and tree rooted at 'subRoot'
        has n nodes, the worst case recursion depth is O(m + n).
    """

    res = False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base cases
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        elif (not root and subRoot) or (root and not subRoot) or root.val != subRoot.val:
            return False

        return self.isSameTree(root.left, subRoot.left) and self.isSameTree(
            root.right, subRoot.right
        )
