from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    """
    Intuition:
    We want to hire k workers with the lowest total cost, but we can only choose from
    the first 'candidates' and last 'candidates' workers at any given time. To efficiently
    retrieve the lowest-cost worker among these options, we use two min-heaps: one for
    the left end and one for the right end of the list.

    Initially, we fill the two heaps with up to 'candidates' elements from each end of
    the costs list. At each step, we compare the smallest element from both heaps and
    hire the cheaper one, adding its cost to the total. After hiring, we refill the heap
    from the unprocessed middle segment to maintain the pool size (if possible).

    This approach ensures that we always consider the lowest available costs from both
    ends and update the heaps efficiently using priority queues (heaps), giving us a
    greedy and optimal solution for minimizing total hiring cost.

    Runtime:
        O((n * log n) + k * log n) where n = candidates. Each heap contains 'candidates'
        number of elements. Building the 'left' and 'right' heaps takes n * log n time.
        For each iteration up to k, we also remove and add elements to the heap which
        takes log n time. We have k iterations, so this gives us k * log n.

    Memory:
        We need 2 heaps with 'candidates' number of elements in each. In the worst case,
        candidates is equal to or greater than the number of elements in the costs input
        array. Therefore, the overall space complexity would be O(N) where N scales
        linearly with the size of 'costs'.
    """

    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        totalCost = 0
        l, r = candidates, len(costs) - candidates - 1
        left = costs[:candidates]
        right = costs[max(candidates, len(costs) - candidates) :]
        heapify(left)
        heapify(right)

        for _ in range(k):
            if not right or left and left[0] <= right[0]:
                totalCost += heappop(left)

                if l <= r:
                    heappush(left, costs[l])
                    l += 1
            else:
                totalCost += heappop(right)

                if l <= r:
                    heappush(right, costs[r])
                    r -= 1

        return totalCost
