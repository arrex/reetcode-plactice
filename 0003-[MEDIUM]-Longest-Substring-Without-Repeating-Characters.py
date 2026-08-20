class Solution:
    """
    Intuition:
        We use a dynamic sliding window technique. The keywords here are longest
        which implies optimization and substring which implies a contiguous
        substructure in the provided input string.

        We keep a hashset to track the current characters in a substring. As
        soon as we encounter a duplicate, we increment the left pointer until
        the duplicate character is removed.

    Runtime:
        O(n) -> one pass

    Memory:
        O(n) -> hashset contains at most all chars in input string
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        chars = set()
        longest = 0

        while r < len(s):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1

            chars.add(s[r])

            longest = max(longest, r - l + 1)

            r += 1

        return longest
