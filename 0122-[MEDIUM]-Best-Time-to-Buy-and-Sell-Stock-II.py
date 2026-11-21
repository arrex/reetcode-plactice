class Solution:
    """
    Intuition:
        We notice that the maximum profit we can realize is the sum of
        profits over all time windows where the stock price increases.

        The next thing we notice is that the total profits over a time
        window is the sum of the profits made day to day.

        This way, we can process each day with respect to the day before
        and check the gain. If the gain/profit is positive, then we add
        it to our total profits. Otherwise, we discard as we would not
        have bought or sold on that day.

    Runtime:
        O(n) for the linear pass on the input array.

    Memory:
        O(1) auxiliary space.
    """

    def maxProfit(self, prices: list[int]) -> int:
        tot = 0

        for i in range(1, len(prices)):
            profit = prices[i] - prices[i - 1]
            if profit > 0:
                tot += profit

        return tot
