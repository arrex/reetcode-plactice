class Solution1:
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


class Solution2:
    """
    Intuition:
        We can translate our top-down recursive approach into a bottom-up tabular
        approach by looking at the structure of the recursive dfs helper in
        Solution 1. When going about top-down to bottom up translations, the key
        is in observing how the recursive function expressese the recurrence
        relation.

        Let us denote the function F(d, h, r) as the function outputting the max
        profits from day d onward with h representing if we are currently holding
        stock and r representing the remaining number of transactions we can make.

        From this, we can see that our recurrence relations are:
        - F(d, 1, r) = max(-prices[d] + F(d + 1, 0, r - 1), F(d + 1, 1, r))
          i.e. best of sell or skip
        - F(d, 0, r) = max(prices[d] + F(d + 1, 1, r), F(d + 1, 0, r))
          i.e. best of buy or skip

        Notice that our base cases are at d == len(prices). As such, this means that
        we will have to process days in reverse order (right to left) to build off
        the base case in a bottom-up manner. We can also embed the base cases into
        our dp cache by zero initializing it.

    Runtime:
        O(3 * 2 * n) ~ O(n) to process each state once.

    Memory:
        O(3 * 2 * n) ~ O(n) for the dp cache.
    """

    def maxProfit(self, prices: list[int]) -> int:
        # dp[i][j][k] = max profits at day = i with holding = j and remaining tx = k
        # 0-init to cover base cases
        dp = [[[0] * 3 for _ in range(2)] for _ in range(len(prices) + 1)]

        # process days in reverse order based on recurrence relation
        for day in range(len(prices) - 1, -1, -1):
            for holding in range(2):
                for remTx in [
                    1,
                    2,
                ]:  # don't care about 0 remaining tx since profit is 0 by base case
                    if holding:  # sell or skip
                        dp[day][True][remTx] = max(
                            prices[day] + dp[day + 1][False][remTx - 1], dp[day + 1][True][remTx]
                        )
                    else:  # buy or skip
                        dp[day][holding][remTx] = max(
                            -prices[day] + dp[day + 1][True][remTx], dp[day + 1][False][remTx]
                        )

        # max profits if we start at day 0 onward, currenly not holding anything,
        # and have 2 txs left to make
        return dp[0][False][2]


class Solution3:
    """
    Intuition:
        We can build off Solution 2 by realizing that the recurrence relation only
        depends on the current day and the next day. Thus, we only need to store
        the buffers for 2 days rather than all of them.

    Runtime:
        Still O(n).

    Memory:
        O(6) for each buffer which simplifies to O(1).
    """

    def maxProfit(self, prices: list[int]) -> int:
        tmrw = [[0] * 3 for _ in range(2)]
        today = [[0] * 3 for _ in range(2)]

        for day in range(len(prices) - 1, -1, -1):
            for holding in range(2):
                for remTx in [1, 2]:
                    if holding:  # sell or skip
                        today[True][remTx] = max(
                            prices[day] + tmrw[False][remTx - 1], tmrw[True][remTx]
                        )
                    else:  # buy or skip
                        today[False][remTx] = max(
                            -prices[day] + tmrw[True][remTx], tmrw[False][remTx]
                        )

            today, tmrw = tmrw, today

        return tmrw[False][2]


class Solution4:
    """
    Intuition:
        We build off of Solution 3. Observe that only 4 values ever change.

        For a given day, we only care about:
        - holding=True, remTx=1
        - holding=True, remTx=2
        - holding=False, remTx=1
        - holding=False, remTx=2

        As per base cases, we do not care about remTx=0 since we cannot make
        profits if we have no transactions left.

        As such, we can collapse the nested array buffers into 4 variables
        to make computations more efficient.

        Beware of ordering since we mutate variables. We need to order
        assignments in a way that an updated value is not used in subsequent
        calculations.

    Runtime:
        Still O(n).

    Memory:
        Still O(1).
    """

    def maxProfit(self, prices: list[int]) -> int:
        # flat = shorthand in trading to mean not holding anything
        #
        # holding1: holding=True, remTx=1
        # holding2: holding=True, remTx=2
        # flat1: holding=False, remTx=1
        # flat2: holding=False, remTx=2
        holding1 = holding2 = 0
        flat1 = flat2 = 0

        for day in range(len(prices) - 1, -1, -1):
            flat2 = max(-prices[day] + holding2, flat2)
            holding2 = max(prices[day] + flat1, holding2)
            flat1 = max(-prices[day] + holding1, flat1)
            holding1 = max(prices[day], holding1)

        return flat2
