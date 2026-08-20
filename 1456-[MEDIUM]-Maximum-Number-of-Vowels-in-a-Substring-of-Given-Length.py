class Solution1:
    """
    Intuition:
        This problem fits the requirements of a fixed sliding window problem.
        We use k as the size of our window and slide it along the string to
        verify all substrings.

    Notes:
        This solution isn't super elegantly written. Later solutions will
        improve on this. It's a good starting point though.

    Runtime: O(n)

    Memory: O(1)
    """

    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        l, r = 0, 0
        curr, res = 0, 0

        while r < len(s):
            # Reached max window size
            if r - l + 1 > k:
                if s[l] in vowels:
                    curr -= 1
                    res = max(res, curr)

                l += 1
            # Can still increment window
            else:
                if s[r] in vowels:
                    curr += 1
                    res = max(res, curr)

                r += 1

        return res


class Solution2:
    """
    Intuition:
        Since we are dealing with a fixed window size here, we can
        separate our approach into 2 parts. The first part will be
        counting the number of vowels in the first available window.
        Then, we slide the window across the remainder of the string
        to go through the remaining substrings.

    Notes:
        Runtime and memory still on the same scale, but majorly
        improved on Leetcode.
    """

    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        curr = 0

        # Since k might be greater than len of s
        for i in range(min(k, len(s))):
            if s[i] in vowels:
                curr += 1

        # Init res to same val as curr (we know res at least
        # equal to num of vowels in current window)
        res = curr

        # Slide window
        for i in range(k, len(s)):
            # Increment right ptr
            if s[i] in vowels:
                curr += 1

            # Increment left ptr
            if s[i - k] in vowels:
                curr -= 1

            # Adjust result
            res = max(res, curr)

        return res
