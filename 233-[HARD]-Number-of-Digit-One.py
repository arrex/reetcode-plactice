class Solution:
    """
    Intuition:
        Brute force solution is trivial (iterate 0...n and count num of 1's
        in each number).

        Use digit DP approach. We track the position of the current prefix,
        the tightness relative to the input, and the number of 1's in the
        current prefix as pieces of state we pass on.

    Runtime:
        Let D be the number of digits. Here, D is at most 10 due to n <= 10^9,
        but we will use general form notation.

        We have D * 2 * D = 2 * D^2 possible states. At each step, we iterate
        through up to 10 digits. This makes the total amount of work equal to
        O(2 * D^2 * 10) ~ O(D^2) overall.

    Memory:
        We have 4 * D^2 possible states, which equates to a memo table of size
        O(4 * D^2) ~ O(D^2).
    """

    def countDigitOne(self, n: int) -> int:
        # states:
        # - position
        #     - range(10) since n <= 10^9 from constraint
        # - tightness (limits next digit choice)
        #     - range(2) since either tight or not
        # - number of 1's in current prefix
        #     - range(10) since n <= 10^9 from constraint
        memo = [[[-1 for _ in range(10)] for _ in range(2)] for _ in range(10)]
        digits = str(n)

        def dp(pos, tight, num_ones):
            # base case
            if pos == len(digits):
                return num_ones

            # serve from memo table if we can
            if memo[pos][tight][num_ones] != -1:
                return memo[pos][tight][num_ones]

            # recursive next steps
            limit = int(digits[pos]) if tight else 9
            res = 0
            for d in range(limit + 1):
                res += dp(
                    pos + 1,
                    1 if tight and d == int(digits[pos]) else 0,
                    num_ones + 1 if d == 1 else num_ones,
                )

            # populate memo table
            memo[pos][tight][num_ones] = res
            return res

        # start with constraining tightness to n
        return dp(0, 1, 0)
