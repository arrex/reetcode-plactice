class Solution:
    """
    Intuition:
        Just do what the problem says.

    Runtime:
        O(n).

    Memory:
        O(1).
    """

    def reverseDegree(self, s: str) -> int:
        res = 0
        for i, c in enumerate(s):
            res += (26 - ord(c) + ord("a")) * (i + 1)
        return res
