class Solution:
    """
    Intuition:
        Used a fixed sliding window approach since we are trying to match
        a string `needle` within a longer string `haystack`.

        Rule out the base case where the needle is longer than the haystack.

    Runtime:
        We have n windows. Each window takes k time to check where k is the
        size of the window. This means our runtime is O(n * k).

    Memory:
        O(1) since we only deal with ptrs.
    """

    def strStr(self, haystack: str, needle: str) -> int:
        # base case
        if len(needle) > len(haystack):
            return -1

        l, r = 0, len(needle) - 1
        while r < len(haystack):
            if haystack[l : r + 1] == needle:
                return l

            l += 1
            r += 1

        return -1
