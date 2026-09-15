class Solution:
    """
    Intuition:
        The intuition is that we can be greedy in searching for palindromes.
        Selecting a palindrome longer than k does not help us find the optimal
        result.

        As such, we can traverse the string and, at each position, search for
        the next palindrome that satisfies the minimum length of k. Our search
        should favour the palindrome with the smallest end position rather than
        smallest start position. This is because if we force a palindrome at
        the current position, then we might get stuck with an overly long
        palindrome when skipping it would have been more optimal.

    Runtime:
        The helper function runs in O(n^3). It checks up to n^2 substrings with
        each palindrome check costing O(n).

        The while loop processes disjoint sections of the input string. We update
        our position to the subsequent index of the last palindrome found. The O(n^3)
        cost of the helper can be thought of as being "split" across each iteration
        of the while loop, so it does not add a linear term to our runtime.

        Thus, our overall runtime is O(n^3).

    Memory:
        O(n) needed for palindrome check.
    """

    def maxPalindromes(self, s: str, k: int) -> int:
        if k == 1:
            return len(s)

        res = 0
        ix = 0
        while True:
            ix = self.find_next_pal(ix, s, k)

            if ix == -1:
                break

            res += 1

        return res

    def find_next_pal(self, pos, s, k):
        # greedily find nearest palindrome of size at least k
        # so search by nearest end ix
        for r in range(pos + k - 1, len(s)):
            for l in range(pos, r - k + 2):
                substr = s[l : r + 1]

                if substr == substr[::-1]:
                    # return next ix to start search at
                    return r + 1

        # no next pal
        return -1
