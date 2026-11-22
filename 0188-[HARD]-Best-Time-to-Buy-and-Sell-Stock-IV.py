class Solution1:
    """
    Intuition:
        We base our solution off of Leetcode problem #123.

        In problem #123, we only have 2 transactions to make. Here, we need
        to generalize it to k transactions.

        As such, the shape of our buffers changes, but the recurrence relation
        still holds. We just port that relation over to obtain our solution.

    Runtime:
        Each day now requires us to process O(k) possible remaining transaction
        values, excluding 0 because no treansactiosn left means no way to create
        more profits. Thus, our runtime becomes O(n * 2 * k) ~ O(n * k).

    Memory:
        Each buffer has size O(2 * k) ~ O(k), so O(k) overall memory complexity.
    """

    def maxProfit(self, k: int, prices: list[int]) -> int:
        tmrw = [[0] * (k + 1) for _ in range(2)]
        today = [[0] * (k + 1) for _ in range(2)]

        for day in range(len(prices) - 1, -1, -1):
            # holding = true
            # actions: sell or skip
            for remTx in range(1, k + 1):
                today[1][remTx] = max(prices[day] + tmrw[0][remTx - 1], tmrw[1][remTx])

            # holding = false
            # actions: buy or skip
            for remTx in range(1, k + 1):
                today[0][remTx] = max(-prices[day] + tmrw[1][remTx], tmrw[0][remTx])

            # swap to save on allocation
            today, tmrw = tmrw, today

        return tmrw[0][k]


class Solution2:
    """
    Intuition:
        In problem #123, we went from buffers to the current day and the
        subsequent day to 4 stand-alone vars since we noticed that only
        4 values ever change.

        We can generalize that idea here to flatten the shape of our buffers.
        Instead of variables, though, we will use arrays since `k` can vary.

        Ordering matters as we don't want to update a value that will be
        used by later computations (inconsistent state transition). By
        looking at the ordering in problem #123's Solution 4, we see that
        the updates should happen in this order:
        - flat, k
        - holding, k
        - flat, k-1
        - holding, k-1
        ...
        - flat, 1
        - holding, 1

    Runtime:
        Still O(n * k).

    Memory:
        Still O(k).
    """

    def maxProfit(self, k: int, prices: list[int]) -> int:
        holding = [0] * (k + 1)
        flat = [0] * (k + 1)

        for day in range(len(prices) - 1, -1, -1):
            for remTx in range(k, 0, -1):
                # actions: buy or skip
                flat[remTx] = max(-prices[day] + holding[remTx], flat[remTx])
                # actions: sell or skip
                holding[remTx] = max(prices[day] + flat[remTx - 1], holding[remTx])

        return flat[k]
