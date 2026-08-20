from typing import List


class Solution:
    """
    Intuition:
        This problem can be solved using a greedy approach
        intuitively (min cost + the fact that it's an easy...).

        The first idea is to sort the prices and process them in
        triplets. However, this idea fails against cases like
        [1, 3, 3, 3] where we are better selecting the triplet
        of candies costing 3$.

        This is where greedy comes in. Instead of processing
        from left to right, we go from right to left. From
        highest to lowest. In such a way, the triplets we
        form will always have the candies with the highest
        price, so the one we get for free saves us the most
        amount of money.

    Runtime:
        O(n * log n) to sort.

        O(n) to process.

        Overall, O(n * log n) runtime.

    Memory:
        O(1) to sort since in-place.
    """

    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        res = 0

        for i in range(len(cost) - 1, -1, -3):
            if i - 2 < 0:
                res += sum(cost[: i + 1])
            else:
                j = i - 1
                res += cost[i] + cost[j]

        return res
