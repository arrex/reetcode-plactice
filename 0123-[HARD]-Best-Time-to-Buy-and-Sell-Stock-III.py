class Solution:
    """
    Intuition:
        We can model this problem intuitively using a top-down recursive approach (top-down
        because we start with the largest subproblem).

        Our set of actions we can apply are buy/sell/skip. Buying requires us to not be
        holding any stock given we can't hold multiple shares at once. Selling requires
        us to be holding stock since we can't sell what we do not own. Skipping doesn't
        require any prerequisites.

        From a recursive standpoint, the 2 base cases to identify are: when we finished
        processing all the trading days and when we have no transactions left to make.
        Beyond that, the recursion is split by if we are holding a stock or not. If we
        are, then we can either sell or skip. If we are not, then we can either buy or
        skip. We then return the profits of the best option.

        We decrement remaining transactions upon a sell instead of a buy. This makes our
        base case of having no more transactions safe to return 0. If we decremented on
        buy, we would return 0 even if we were still potentially holding a stock.

        To make this recursive approach pass runtime constraints, we simply slap a cache
        to memoize visited states.

    Runtime:
        The worst case runtime can be define as the number of possible states multiplied
        by the work incurred for each state.

        The work for each state is constant, so O(1).

        Given we have n days, 2 values for holding (we can either be holding a stock or
        not holding one), and 3 values for remaining transactions (2, 1, 0), this gives
        us a total number of O(6 * n) possible states which simplifies to O(n).

        Overall, the runtime complexity is O(n).

    Memory:
        The dp cache takes O(6 * n) ~ O(n) space.

        The recursion stack can extend to O(n) depth.

        Overall, O(n) memory complexity.
    """

    def maxProfit(self, prices: list[int]) -> int:
        # dp[i][j][k] = max profits at day = i with holding = j and remaining tx = k
        dp = [[[-1] * 3 for _ in range(2)] for _ in range(len(prices))]

        # how much more profit can i make from this day onward
        def dfs(day, holding, remainingTx):
            # cannot make profits past last day
            if day == len(prices):
                return 0

            # cannot make profits with no more tx left
            if remainingTx == 0:
                return 0

            if dp[day][holding][remainingTx] != -1:
                return dp[day][holding][remainingTx]

            if holding:
                sell = prices[day] + dfs(day + 1, False, remainingTx - 1)
                skip = dfs(day + 1, True, remainingTx)

                best = max(sell, skip)
                dp[day][holding][remainingTx] = best

                return best
            else:
                buy = -1 * prices[day] + dfs(day + 1, True, remainingTx)
                skip = dfs(day + 1, False, remainingTx)

                best = max(buy, skip)
                dp[day][holding][remainingTx] = best

                return best

        return dfs(0, False, 2)
