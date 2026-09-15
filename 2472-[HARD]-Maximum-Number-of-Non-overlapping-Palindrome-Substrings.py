class Solution1:
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


class Solution2:
    """
    Intuition:
        We can use a bottom-up dp approach. Our dp cache stores solns to
        smaller subproblems. In other words, dp[i] stores the opt soln for
        s[:i].

        Our base case dp[0] is 0 because s[:0] contains 0 palindromes. Then,
        we iterate over each possible end index of our palindrome. We start
        at position k since the palindrome must have len at least k and any
        substring smaller than k will automatically contain 0 valid palindromes.

        Then, we use the greedy observation to find candidates. A valid
        palindrome in our case can either be of len k or k + 1 to account for
        even/odd cases. If we find a match, the soln is simply the max between
        the soln from the previous state `i - 1` and the soln from the start pos
        `r - k` + 1.

    Runtime:
        O(n * k) since the outer loop has roughly n iterations and checking
        each candidate requires O(k) time.

    Memory:
        O(n) for the dp cache.

        O(k) auxiliary memory to check each candidate.

        Overall, O(n + k) space.
    """

    def maxPalindromes(self, s: str, k: int) -> int:
        N = len(s)
        # dp[i] contains opt soln for s[:i]
        # base case: dp[0] = 0
        dp = [0] * (N + 1)

        for r in range(k, N + 1):
            dp[r] = dp[r - 1]

            if r >= k:
                candidate = s[r - k : r]
                if candidate == candidate[::-1]:
                    dp[r] = max(dp[r], dp[r - k] + 1)

            if r >= k + 1:
                candidate = s[r - k - 1 : r]
                if candidate == candidate[::-1]:
                    dp[r] = max(dp[r], dp[r - k - 1] + 1)

        return dp[N]
