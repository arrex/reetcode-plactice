from math import inf
from typing import List


class Solution1:
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


class Solution2:
    """
    Intuition:
        We build on our dp approach. Notice how a given state only ever
        depends on the 3 last states

        As such, we don't need the full dp cache since we only ever care
        about step `i` and steps `i - 1`, `i - 2`, and `i - 3`.

        The increase in cost from jumping from step `i` to step `j` is
        defined as:
            cost[j] + (j - i)^2

        The `(j - i)^2` can be evaluated to a constant once we realize that
        `j - i` represents the gap which can be either 1, 2 or 3. So the
        square of the gap is either 1, 4 or 9. From the oldest state `s1`,
        the gap is 3, so that term for the cost is 9. For s2, it is 4. For s3,
        it is 1.

        Thus, we can find the minimum on the current cost + the gap and then
        add the cost (the cost is added to every path anyways, so we don't
        need to include it in the min call).

    Runtime:
        O(n) for a single linear scan on costs.

    Memory:
        O(1).
    """

    def climbStairs(self, n: int, costs: List[int]) -> int:
        s1 = s2 = s3 = 0

        for c in costs:
            s1, s2, s3 = s2, s3, min(s1 + 9, s2 + 4, s3 + 1) + c

        return s3
