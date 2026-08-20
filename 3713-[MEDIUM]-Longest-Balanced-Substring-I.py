class Solution:
    """
    Intuition:
        Since the input size constraint is not too large (s.len <= 1000), we
        can deduce that this is an O(n^2) soln.

        Thus, one approach would be to take all possible starting indices and
        check them against all subarrays starting at that given index.

        We can use a frequency array with 26 elmts and increment the count of
        each letter. If we increment from 0, we know we encountered a distinct
        letter. If the current frequency we incremented is greater than all
        other frequencies, we change `maxFreq` accordingly. `maxFreq` allows
        us to check if our subarray is balanced or not.

    Runtime:
        O(n^2) to compute each subarray.

    Memory:
        O(1).
    """

    def longestBalanced(self, s: str) -> int:
        res = 0
        N = len(s)

        for l in range(N):
            freq = [0] * 26
            distinct = 0
            maxFreq = 0

            for r in range(l, N):
                ix = ord(s[r]) - ord("a")

                # check if curr char is a new distinct char
                if freq[ix] == 0:
                    distinct += 1

                freq[ix] += 1

                # check if curr char now has highest freq
                maxFreq = max(maxFreq, freq[ix])

                if r - l + 1 == maxFreq * distinct:
                    res = max(res, r - l + 1)

        return res
