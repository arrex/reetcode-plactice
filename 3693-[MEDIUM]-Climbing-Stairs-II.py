from math import inf
from typing import List


class Solution:
    """
    Intuition:
        Use a bottom-up dp approach.

        Our base case is at step 0 where cost is 0.

        Then, we iterate through each step `i` from 1 to n inclusive
        and look backwards at `i - 1`, `i - 2`, and `i - 3`, which are
        the jumps we are allowed to make, to find the minimal cost to
        reach step `i`.

    Runtime:
        We have n steps to iterate over and each step requires us to
        look back 3 paths. This gives O(3 * n) ~ O(n) runtime.

    Memory:
        O(n) for the dp cache.
    """

    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [inf] * (n + 1)

        # base case
        dp[0] = 0

        for i in range(n + 1):
            for j in [i - 1, i - 2, i - 3]:
                if j < 0:
                    continue

                dp[i] = min(dp[i], dp[j] + costs[i - 1] + (i - j) ** 2)

        return dp[n]
