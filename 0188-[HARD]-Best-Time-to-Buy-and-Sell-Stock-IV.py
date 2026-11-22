class Solution:
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
