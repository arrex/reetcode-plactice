class Solution1:
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


class Solution2:
    """
    Intuition:
        Use same greedy approach, optimize the sorting step. We bucket
        by cost, and iterate over each cost from lowest to highest.

    Runtime:
        O(n) to bucket costs.

        O(k) to iterate through all costs where k is the highest cost.
        Constraint specifies it to be 10^5, but we will keep general
        form 'k'.

        Overall, O(n + k) runtime.

    Memory:
        O(k) for the count array.
    """

    def maxIceCream(self, costs, coins):
        max_cost = max(costs)

        count = [0] * (max_cost + 1)
        for cost in costs:
            count[cost] += 1

        res = 0
        for cost in range(1, max_cost + 1):
            if count[cost] == 0:
                continue

            can_buy = min(count[cost], coins // cost)

            res += can_buy
            coins -= can_buy * cost

            if coins < cost:
                break

        return res
