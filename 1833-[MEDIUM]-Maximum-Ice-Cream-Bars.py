class Solution:
    """
    Intuition:
        Use greedy approach to solve this problem. Sort the inputs
        and choose as many as possible.

    Runtime:
        O(n * log n) to sort.

        O(n) or linear pass.

        O(n * log n) overall.

    Memory:
        O(1) since sort in place.
    """

    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()

        res = 0
        for cost in costs:
            if cost > coins:
                break

            res += 1
            coins -= cost

        return res
