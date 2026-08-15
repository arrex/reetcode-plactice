class Solution:
    """
    Intuition:
        Dynamic sliding window problem with a frequency counter to track the
        condition.

    Runtime:
        O(n) as each index in the string is processed at most twice (once by
        right, once by left ptrs).

    Memory:
        O(1) for pointers and bounded array.
    """

    def maximumLengthSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        freq = [0] * 26

        while r < len(s):
            # update freq counter w curr char
            ix = ord(s[r]) - ord('a')
            freq[ix] += 1

            # check window validity and resize window if needed
            while freq[ix] > 2:
                jx = ord(s[l]) - ord('a')
                freq[jx] -= 1
                l += 1

            # store res
            res = max(res, r - l + 1)

            # increment r
            r += 1

        return res
