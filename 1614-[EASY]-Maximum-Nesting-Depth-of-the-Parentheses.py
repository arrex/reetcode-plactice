class Solution:
    """
    Intuition:
        Since the input string is valid, we only care
        about counting the nesting depth. Maintain a
        stack and track its largest size.

    Runtime:
        O(n) for the linear pass on the input string.

    Memory:
        O(n / 2) ~ O(n) for the stack since an input
        string of length n can form at most n / 2 pairs
        of parentheses.
    """

    def maxDepth(self, s: str) -> int:
        res = 0

        stack = []
        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")":
                res = max(res, len(stack))
                stack.pop()

        return res
