class Solution:
    """
    Intuition:
        We can use a greedy approach.

        We try to fill items of both types first, then deal with remainders for each type.

        The important thing to notice is that when dealing with the remaining items of type
        `need1`, if we opt to pay `costBoth`, we also need to update the remaining items of
        type `need2`.

    Runtime:
        O(1).

    Memory:
        O(1).
    """

    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        res = 0

        # fill both greedily
        cnt = min(need1, need2)
        res += cnt * min(cost1 + cost2, costBoth)

        need1 -= cnt
        need2 -= cnt

        # fill remaining qty of need1 items
        if need1 > 0:
            cost = min(cost1, costBoth)

            if cost == cost1:
                res += need1 * cost1
            else:  # cost is costBoth
                res += need1 * costBoth
                # also decr need2 items since we take both
                need2 -= need1

            need1 = 0

        # fill remaining qty of need2 items
        if need2 > 0:
            price = min(cost2, costBoth)
            res += need2 * price

        return res
