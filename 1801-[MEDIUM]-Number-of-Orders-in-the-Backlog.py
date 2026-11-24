import heapq
from typing import List


class Solution:
    """
    Intuition:
        We maintain 2 backlogs: one for buy orders and one for sell orders.

        For each type of order, we try to consume as many orders from the
        backlog as we can. To fulfill orders, we only care about lowest/highest
        price. This hints heavily towards using min/max heap data structures.

    Runtime:
        We have O(n) orders to process. Each order is pushed and popped onto
        the heap at most once, so the total work is O(n log n).

    Memory:
        O(n) for both heaps.
    """

    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        MOD = 10**9 + 7

        buyHeap = []  # max-heap, priciest at root
        sellHeap = []  # min-heap, cheapest at root

        for price, amt, otype in orders:
            if otype == 0:  # case: buy
                while amt > 0 and sellHeap and sellHeap[0][0] <= price:
                    sellAmt = sellHeap[0][1]

                    matched = min(sellAmt, amt)
                    amt -= matched
                    sellHeap[0][1] -= matched

                    if sellAmt == 0:
                        heapq.heappop(sellHeap)

                if amt > 0:
                    heapq.heappush_max(buyHeap, [price, amt])
            else:  # case: sell
                while amt > 0 and buyHeap and buyHeap[0][0] >= price:
                    buyAmt = buyHeap[0][1]

                    matched = min(buyAmt, amt)
                    amt -= matched
                    buyHeap[0][1] -= matched

                    if buyAmt == 0:
                        heapq.heappop_max(buyHeap)

                if amt > 0:
                    heapq.heappush(sellHeap, [price, amt])

        res = 0
        for _, amt in buyHeap:
            res += amt
        for _, amt in sellHeap:
            res += amt
        return res % MOD
